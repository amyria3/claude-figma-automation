#!/usr/bin/env python3
"""Abgleich Figma ↔ app.tcss.

Aufruf:
    python3 token_check.py dump.txt ../app.tcss            # Abgleich, Exit-Code 1 bei Fehlern
    python3 token_check.py dump.txt ../app.tcss --emit-type # §6 Textstile als @utility ausgeben

dump.txt ist die Ausgabe von figma-dump.js (use_figma, nur lesend).

Geprüft wird:
  1. Jede Code-Syntax var(--x) aus Figma existiert in app.tcss.
  2. Der Wert stimmt in jedem Modus (Farben als Hex, Maße in px).
  3. Eine CSS-Variable bekommt aus Figma nur einen Wert (keine Konflikte).
  4. Jede Theme-Achse deklariert in jedem Modus dieselben Tokens.
  5. Jede Farbe außer den Primitiven hat eine Utility (@theme inline).
  6. Jeder Textstil hat eine @utility type-* mit denselben Werten.
Hinweise (kein Fehler): Variablen ohne Code-Syntax, CSS-Variablen ohne Figma-Gegenstück,
Leading-/Tracking-Tokens, die kein Textstil nutzt.
"""
import re
import sys

ROOT = ('root',)
WEIGHTS = {'thin': 100, 'extralight': 200, 'light': 300, 'regular': 400, 'medium': 500,
           'semibold': 600, 'bold': 700, 'extrabold': 800, 'black': 900}
CASE = {'UPPER': 'uppercase', 'LOWER': 'lowercase', 'TITLE': 'capitalize'}
DECO = {'UNDERLINE': 'underline', 'STRIKETHROUGH': 'line-through'}


# ---------------------------------------------------------------- CSS lesen
def parse_css(css):
    """Liefert scopes {scope: {--name: wert}}, utilities {name: {prop: wert}}, registrations."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    scopes, utilities, registrations = {}, {}, {}
    scopes['?unknown'] = set()
    stack, buf = [], ''
    for ch in css:
        if ch == '{':
            stack.append(buf.strip()); buf = ''
        elif ch == '}':
            if buf.strip():
                _decl(buf, stack, scopes, utilities, registrations)
            buf = ''
            if stack: stack.pop()
        elif ch == ';':
            _decl(buf, stack, scopes, utilities, registrations); buf = ''
        else:
            buf += ch
    return scopes, utilities, registrations


def _decl(text, stack, scopes, utilities, registrations):
    text = text.strip()
    if ':' not in text or text.startswith('@'):
        return
    prop, val = [x.strip() for x in text.split(':', 1)]
    util = next((p.split()[1] for p in stack if p.startswith('@utility')), None)
    if util:
        nested = [p for p in stack[stack.index(next(p for p in stack if p.startswith('@utility'))) + 1:]]
        key = ('::'.join(nested) + '::' if nested else '') + prop
        utilities.setdefault(util, {})[key] = ' '.join(val.split())
        return
    if not prop.startswith('--'):
        return
    inline = any(p.startswith('@theme') and 'inline' in p for p in stack)
    if inline and prop.startswith('--color-'):
        registrations[prop] = val
        return
    bp = next((re.match(r'@variant\s+([\w-]+)', p).group(1) for p in stack
               if re.match(r'@variant\s+', p)), None)
    sel = next((p for p in reversed(stack) if not p.startswith('@')), ':root')
    for s in [x.strip() for x in sel.split(',')]:
        m = re.fullmatch(r'\[(data-[\w-]+)="([^"]+)"\]', s)
        if bp:
            scope = ('bp', bp)
        elif m:
            scope = (m.group(1), m.group(2))
        elif s == ':root':
            scope = ROOT
        else:
            scopes['?unknown'].add(' '.join(sel.split())[-100:])
            continue
        scopes.setdefault(scope, {})[prop] = val


def chain(scope):
    if scope[0] == 'bp':
        order = ['base', 'md', 'lg']
        i = order.index(scope[1])
        return [('bp', b) for b in reversed(order[1:i + 1])] + [ROOT]
    return [scope, ROOT] if scope != ROOT else [ROOT]


def resolve(scopes, name, scope, depth=0):
    if depth > 20:
        return None
    for s in chain(scope):
        if name in scopes.get(s, {}):
            v = scopes[s][name].strip()
            m = re.fullmatch(r'var\(\s*(--[\w-]+)\s*(?:,[^)]*)?\)', v)
            return resolve(scopes, m.group(1), scope, depth + 1) if m else v
    return None


def norm(v):
    if v is None:
        return None
    v = v.strip().lower()
    if v.startswith('#'):
        h = v[1:]
        if len(h) in (3, 4): h = ''.join(c * 2 for c in h)
        if len(h) == 8 and h.endswith('ff'): h = h[:6]
        return '#' + h
    m = re.fullmatch(r'(-?[\d.]+)(rem|px|em|%)?', v)
    if m:
        n = float(m.group(1))
        return round(n * 16, 3) if m.group(2) == 'rem' else round(n, 4)
    return v


# ---------------------------------------------------------------- Dump lesen
def parse_dump(text):
    cols, values, nocs, form, styles = [], [], [], [], []
    col = None
    for line in text.splitlines():
        line = line.rstrip()
        if not line:
            continue
        f = line.split('|')
        if f[0] == '#C':
            col = {'name': f[1], 'axis': f[2], 'modes': f[3].split(',')}; cols.append(col)
        elif f[0] == 'V':
            values.append({'css': f[1], 'figma': f[2], 'col': col, 'vals': f[3].split(',')})
        elif f[0] == '!NOCS':
            nocs.append((col['name'] if col else '?', f[1]))
        elif f[0] == '!FORM':
            form.append((col['name'] if col else '?', f[1], f[2]))
        elif f[0] == 'T':
            styles.append(dict(zip(['name', 'family', 'style', 'size', 'sizecs', 'lh', 'ls',
                                    'case', 'deco', 'para'], f[1:])))
    return cols, values, nocs, form, styles


def scope_for(col, i):
    axis, mode = col['axis'], col['modes'][i]
    if axis == 'root':
        return ROOT
    if axis == 'bp':
        return ROOT if mode == 'base' else ('bp', mode)
    return (axis, mode)


# ---------------------------------------------------------------- Textstile
def slug(name):
    s = name.replace('&', ' ').replace('<', '').replace('>', '')
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s)
    return 'type-' + re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()


def token_by_value(scopes, prefix, value):
    for name in scopes.get(ROOT, {}):
        if name.startswith(prefix) and '*' not in name:
            n = norm(resolve(scopes, name, ROOT))
            if isinstance(n, float) and abs(n - value) < 0.0005:
                return name
    return None


def expected_type(style, scopes):
    errs, d = [], {}
    fam = None
    for name, v in scopes.get(ROOT, {}).items():
        if name.startswith('--font-') and '*' not in name:
            m = re.match(r'\s*["\']?([^"\',]+)', v)
            if m and m.group(1).strip().lower() == style['family'].lower():
                fam = name
    if fam: d['font-family'] = f'var({fam})'
    else: errs.append(f"kein --font-* für Familie „{style['family']}“")
    if style['sizecs'] in ('-', '?'):
        errs.append('Schriftgröße nicht an eine Typografy-Variable gebunden')
    else:
        d['font-size'] = style['sizecs']
    d['font-weight'] = str(WEIGHTS.get(style['style'].replace(' ', '').lower(), 400))
    if style['lh'].endswith('%'):
        lh = float(style['lh'][:-1]) / 100
        t = token_by_value(scopes, '--leading-', round(lh, 4))
        if t: d['line-height'] = f'var({t})'
        else: errs.append(f"kein --leading-* für {style['lh']}")
    else:
        errs.append(f"Zeilenhöhe {style['lh']} ist nicht relativ")
    if style['ls'].endswith('%'):
        ls = float(style['ls'][:-1]) / 100
        t = token_by_value(scopes, '--tracking-', round(ls, 4))
        if t: d['letter-spacing'] = f'var({t})'
        else: errs.append(f"kein --tracking-* für {style['ls']}")
    else:
        errs.append(f"Laufweite {style['ls']} ist nicht relativ")
    if style['case'] in CASE: d['text-transform'] = CASE[style['case']]
    if style['deco'] in DECO: d['text-decoration-line'] = DECO[style['deco']]
    para = float(style['para'] or 0)
    if para > 0:
        t = token_by_value(scopes, '--spacing-', para)
        d['& + &::margin-top'] = f'var({t})' if t else f'{para / 16:g}rem'
    return d, errs


def emit_type(styles, scopes):
    out = []
    for s in styles:
        d, errs = expected_type(s, scopes)
        out.append(f"@utility {slug(s['name'])} {{ /* {s['name']} */")
        nested = {}
        for k, v in d.items():
            if '::' in k:
                sel, prop = k.split('::'); nested.setdefault(sel, []).append((prop, v))
            else:
                out.append(f'  {k}: {v};')
        for sel, decls in nested.items():
            out.append(f'  {sel} {{ ' + ' '.join(f'{p}: {v};' for p, v in decls) + ' }')
        for e in errs:
            out.append(f'  /* FEHLT: {e} */')
        out.append('}')
    return '\n'.join(out)


# ---------------------------------------------------------------- Abgleich
def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    dump = open(sys.argv[1], encoding='utf-8').read()
    css = open(sys.argv[2], encoding='utf-8').read()
    scopes, utilities, regs = parse_css(css)
    unknown = scopes.pop('?unknown')
    cols, values, nocs, form, styles = parse_dump(dump)

    if '--emit-type' in sys.argv:
        print(emit_type(styles, scopes)); return

    err, info = [], []
    figma_names = set()
    for s in sorted(unknown):
        err.append(f"SELEKTOR  Custom Properties unter unbekanntem Selektor: „{s}“ "
                   f"(oft ein vorzeitig beendeter Kommentar)")

    # 1–3 Namen, Werte, Konflikte
    seen = {}
    for v in values:
        name, col = v['css'], v['col']
        figma_names.add(name)
        if col['axis'] == 'root':
            prev = seen.get(name)
            if prev and prev[0] != v['vals'][0]:
                err.append(f"KONFLIKT  {name}: {prev[1]} = {prev[0]}, {v['figma']} = {v['vals'][0]}")
            seen.setdefault(name, (v['vals'][0], v['figma']))
        if not any(name in d for d in scopes.values()):
            err.append(f"FEHLT     {name}  ({col['name']} › {v['figma']})"); continue
        for i, fv in enumerate(v['vals']):
            if fv.startswith(('s:', 'b:')):
                continue
            cv = resolve(scopes, name, scope_for(col, i))
            if norm(cv) != norm(fv):
                err.append(f"WERT      {name} [{col['modes'][i]}]  Figma {fv} · CSS {cv}  ({v['figma']})")

    # 4 Vollständigkeit je Achse
    for col in cols:
        if not col['axis'].startswith('data-'):
            continue
        sets = {m: set(scopes.get((col['axis'], m), {})) for m in col['modes']}
        union = set().union(*sets.values())
        for m, s in sets.items():
            if s != union:
                err.append(f"LÜCKE     [{col['axis']}=\"{m}\"] fehlt: {', '.join(sorted(union - s))}")
        extra = {k[1] for k in scopes if k[0] == col['axis']} - set(col['modes'])
        for m in sorted(extra):
            err.append(f"MODUS     [{col['axis']}=\"{m}\"] gibt es in Figma nicht ({col['name']})")

    # 5 Registrierungen
    reg_targets = {}
    for r, val in regs.items():
        m = re.fullmatch(r'var\((--[\w-]+)\)', val.strip())
        if not m or not any(m.group(1) in d for d in scopes.values()):
            err.append(f"REG       {r}: {val} zeigt auf keine Variable")
        elif m:
            reg_targets[m.group(1)] = r
    for v in values:
        if v['col']['name'] == 'Clrs / Primitives' or not v['vals'][0].startswith('#'):
            continue
        if v['css'] not in reg_targets:
            err.append(f"REG       {v['css']} hat keine Utility (--color-* in @theme inline)")

    # 6 Textstile
    expected = {}
    for s in styles:
        u = slug(s['name'])
        if u in expected:
            err.append(f"TEXT      Name doppelt: {u} ({s['name']})")
        d, errs = expected_type(s, scopes)
        expected[u] = (s['name'], d)
        for e in errs:
            err.append(f"TEXT      {s['name']}: {e}")
        if u not in utilities:
            err.append(f"TEXT      @utility {u} fehlt ({s['name']})"); continue
        have = utilities[u]
        for k in sorted(set(d) | set(have)):
            if d.get(k) != have.get(k):
                err.append(f"TEXT      {u} › {k}: Figma {d.get(k)} · CSS {have.get(k)}")
    for u in sorted(k for k in utilities if k.startswith('type-') and k not in expected):
        err.append(f"TEXT      @utility {u} hat keinen Textstil in Figma")

    # Hinweise
    for c, n in nocs:
        info.append(f"OHNE CODE-SYNTAX  {c} › {n}")
    for c, n, cs in form:
        info.append(f"CODE-SYNTAX-FORM  {c} › {n}: {cs}")
    used = ' '.join(' '.join(d.values()) for _, d in expected.values())
    declared = set()
    for s, d in scopes.items():
        declared |= set(d)
    for n in sorted(declared - figma_names):
        if '*' in n or n.startswith('--font-'):
            continue
        if n.startswith(('--leading-', '--tracking-')):
            if f'var({n})' not in used:
                info.append(f"UNGENUTZT         {n} (kein Textstil)")
            continue
        info.append(f"NUR IM CSS        {n}")

    print(f"Figma: {len(values)} Variablen mit Code-Syntax, {len(styles)} Textstile · "
          f"CSS: {len(declared)} Variablen, {len(regs)} Farb-Utilities, {len(utilities)} @utility")
    print(f"\nFehler: {len(err)}")
    for e in err: print('  ' + e)
    print(f"\nHinweise: {len(info)}")
    for i in info: print('  ' + i)
    sys.exit(1 if err else 0)


if __name__ == '__main__':
    main()
