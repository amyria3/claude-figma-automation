// Figma → Abgleich-Dump für token_check.py
// In use_figma ausführen (Datei rLwATluwV4CSS5rXceLptH). Nur lesend.
// Ausgabe als dump.txt speichern und `python3 token_check.py dump.txt ../app.tcss` starten.
// Passt die Ausgabe nicht in eine Antwort (≈ 20 kB), PART = 1 und PART = 2 nacheinander
// ausführen und beide Ausgaben untereinander in dump.txt speichern.

const PART = 0;            // 0 = alles, 1 = nur Variablen, 2 = nur Textstile
const SKIP = [/^__/, /Tailwind-utility-units/];   // Inhaltsdaten, eingebaute Tailwind-Skala
// Collection → CSS-Achse. Alles andere: ein Modus in :root.
const AXES = {
  'Clrs / Color Modes': 'data-theme',
  'Clrs / Mega Cards': 'data-lively-theme',
  'Clrs / Special': 'data-special-theme',
  'Lyt scl / Width': 'bp',          // Modusname beginnt mit base / md / lg
};

const cols = await figma.variables.getLocalVariableCollectionsAsync();
const vars = await figma.variables.getLocalVariablesAsync();
const byId = new Map(vars.map(v => [v.id, v]));
const colById = new Map(cols.map(c => [c.id, c]));
const h2 = x => Math.round(x * 255).toString(16).padStart(2, '0');
const hex = c => '#' + h2(c.r) + h2(c.g) + h2(c.b) + (c.a !== undefined && c.a < 1 ? h2(c.a) : '');

// Alias rekursiv auflösen: gleiche Collection → gleicher Modus, fremde → deren Standardmodus
function resolve(v, modeId, depth = 0) {
  if (depth > 12) return '?loop';
  let val = v.valuesByMode[modeId];
  if (val === undefined) val = v.valuesByMode[colById.get(v.variableCollectionId).defaultModeId];
  if (val && typeof val === 'object' && val.type === 'VARIABLE_ALIAS') {
    const t = byId.get(val.id);
    if (!t) return '?missing';
    const tc = colById.get(t.variableCollectionId);
    const m = t.variableCollectionId === v.variableCollectionId ? modeId : tc.defaultModeId;
    return resolve(t, m, depth + 1);
  }
  if (val && typeof val === 'object' && 'r' in val) return hex(val);
  if (typeof val === 'number') return String(Math.round(val * 1000) / 1000);
  if (typeof val === 'boolean') return 'b:' + val;
  return 's:' + String(val);
}

const out = [];
if (PART !== 2) {
  for (const c of cols) {
    if (SKIP.some(r => r.test(c.name))) continue;
    const axis = AXES[c.name] || 'root';
    const modes = axis === 'bp' ? c.modes.map(m => m.name.split(' ')[0]) : c.modes.map(m => m.name);
    out.push(`#C|${c.name}|${axis}|${modes.join(',')}`);
    for (const id of c.variableIds) {
      const v = byId.get(id);
      const cs = (v.codeSyntax && v.codeSyntax.WEB) || '';
      const m = cs.match(/^var\((--[\w-]+)\)$/);
      if (!cs) {
        if (!/Nur Figma/i.test(v.description || '')) out.push(`!NOCS|${v.name}`);
        continue;
      }
      if (!m) { out.push(`!FORM|${v.name}|${cs}`); continue; }
      out.push(`V|${m[1]}|${v.name}|${c.modes.map(md => resolve(v, md.modeId)).join(',')}`);
    }
  }
}
if (PART !== 1) {
  out.push('#T');
  for (const s of await figma.getLocalTextStylesAsync()) {
    let sizeCs = '-';
    const b = s.boundVariables && s.boundVariables.fontSize;
    if (b) { const v = byId.get(b.id); sizeCs = (v && v.codeSyntax && v.codeSyntax.WEB) || '?'; }
    const lh = s.lineHeight.unit === 'AUTO' ? 'auto'
      : Math.round(s.lineHeight.value * 100) / 100 + (s.lineHeight.unit === 'PERCENT' ? '%' : 'px');
    const ls = Math.round(s.letterSpacing.value * 100) / 100 + (s.letterSpacing.unit === 'PERCENT' ? '%' : 'px');
    out.push(['T', s.name, s.fontName.family, s.fontName.style, s.fontSize, sizeCs, lh, ls,
      s.textCase, s.textDecoration, s.paragraphSpacing].join('|'));
  }
}
return out.join('\n');
