# 2.7 Layout: So bauen sich Page, Section und Komponenten auf

Stand: 25.09.2026 · Figma-Datei „B2C und CI“, Seite COMPONENTS & SCREENS · Vorlagen `Templates / Page` (Set 8358:53818) und `Templates / Section` (Set 8308:40715)

![So setzen sich Page, Section und Komponenten zusammen](img/layout-ebenen.png)

Die Seite besteht aus drei Ebenen. Komponenten wie `Primitives / Headline / H1` oder `Templates / Cards Order` gehen in die Slots der Section. Sections gehen in den Section-Slot der Page. Nur der Bildschirm scrollt, die Seite selbst hat keinen eigenen Scroll-Bereich.

---

## So baut die Designerin die Seite in Figma

```
Templates / Page   (Hug, Min-Höhe = Bildschirm)
├─ Header          (Sticky)
├─ main            (Hug, Fill-Breite)
│   └─ Sections    → Section-Slot
└─ Footer          (Fill-Breite)
```

1. **Die Seite wächst mit dem Inhalt.** Die Höhe steht auf Hug, die Min-Höhe auf der Bildschirmhöhe (792). Eine feste Höhe gibt es nicht, damit die ganze Seite auf dem Canvas sichtbar bleibt.
2. **Nur der Bildschirm scrollt.** An `Page`, `main` und den Sections stehen Overflow und „Clip content“ auf aus. Einen eigenen Scroll-Bereich bekommen nur Teile, die unabhängig scrollen: ein Modal, ein Filter-Panel oder ein horizontales Karussell.
3. **Header, main und Footer sind Geschwister.** Der Footer liegt nicht in `main`.
4. **Der Header ist sticky.** Unter Position steht „Sticky“.
5. **Die Breite kommt über Fill.** Sections und Footer füllen die Breite, und `Wrapper [max-w-content]` begrenzt den Inhalt.
6. **Inhalte kommen in Slots.** Eine Komponente liegt immer in einem Slot der Section (Breadcrumps, ContentSlot 01 … 05), eine Section immer im Section-Slot der Page. Leere Slots blendest Du aus, die Breadcrumb der Section über die Property „Display Breadcrumps“.
7. **Den Bildschirm legt das Device fest.** Die Bildschirmgröße wählst Du im Prototyp-Panel. Ist die Seite höher als das Device, scrollt der Prototyp von selbst.
8. **Nach Änderungen prüfst Du die Höhe.** Springt eine Seite oder ein Slot auf eine feste Höhe, stellst Du ihn wieder auf Hug.

---

## So setzt der Webentwickler die Seite mit Dev Mode und Code um

### So liest Du die Seite in Dev Mode

1. Der KI-Agent / der Entwickler übernimmt die Höhe der Seite aus Figma nicht. Sie wird dynamisch über die Klasse `min-h-dvh` berechnet.
2. **Die Seite scrollt als Ganzes.** Der KI-Agent / der Entwickler baut keinen inneren Scroll-Container, also kein `overflow-y: auto` mit fester Höhe an `main` oder den Sections.
3. **Slots bekommen kein Element.** Die Inhalte eines Slots folgen direkt im Wrapper. Min-Höhe und Fläche eines leeren Slots sind Platzhalter in Figma.
4. **Die Werte liest Du aus den Variablen.** Die Code-Syntax WEB zeigt `var(--…)`. Da `app.tcss` diese Variablen in `@theme` anlegt, gibt es passende Utilities: `--spacing-xl` → `py-xl`, `--content-max` → `max-w-content` (über `@utility`).
5. **Der Name `Wrapper [klasse]` nennt die Klasse**, die diese Ebene braucht.
6. **`main.flex-1` ergänzt Du selbst.** So bleibt der Footer bei kurzem Inhalt unten. Figma bildet das nicht ab.

### So sieht `Templates / Page` in Tailwind aus

```html
<body class="flex min-h-dvh min-w-content flex-col items-center bg-surface">
  <header class="sticky top-0 z-50 flex w-full flex-col items-center bg-surface">…</header>

  <main class="flex w-full flex-1 flex-col items-center">
    <nav aria-label="Breadcrumb" class="flex h-5 w-full items-center justify-center gap-3 px-md-l">…</nav>
    <!-- Section-Slot: Sections folgen direkt, ohne eigenes Element -->
  </main>

  <footer class="flex w-full flex-col items-center justify-center bg-surface py-md-l">…</footer>
</body>
```

| Figma | Variable (WEB) | Tailwind |
|---|---|---|
| Page min-w | `var(--content-min)` | `min-w-content` |
| Page min-h 792 | keine Variable (Viewport) | `min-h-dvh` |
| Fill Page, Header, Footer | `var(--surface-color)` | `bg-surface` |
| Footer padding oben/unten | `var(--spacing-md-l)` | `py-md-l` |
| Breadcrumb px | `var(--spacing-md-l)` | `px-md-l` |
| Breadcrumb gap / Höhe | `calc(var(--spacing) * 3)` / `* 5` | `gap-3` / `h-5` |
| max-w-screen | nur Figma | – |
| gap / padding `…-zero` | `var(--spacing-zero)` | keine Klasse nötig |

### So sieht `Templates / Section` in Tailwind aus

```html
<section class="flex w-full flex-col items-center bg-surface py-xl">
  <div class="flex w-full max-w-content flex-col gap-md-l px-md-l">
    <!-- Breadcrumps-Slot (optional) -->
    <!-- ContentSlot 01 … 05: Inhalte folgen direkt, ohne Wrapper-Element -->
  </div>
</section>
```

| Figma | Variable (WEB) | Tailwind |
|---|---|---|
| Section padding oben/unten | `var(--spacing-xl)` | `py-xl` |
| Section Fill | `var(--surface-color)` | `bg-surface` |
| Wrapper max-w | `var(--content-max)` | `max-w-content` |
| Wrapper px und gap | `var(--spacing-md-l)` | `px-md-l`, `gap-md-l` |
| Slot min-h | `calc(var(--spacing) * 3)` | nur Figma (Platzhalter) |

In Figma steht an der Section „Clip content“ an. Im Code fehlt `overflow-hidden` bewusst, damit Dropdowns und Sticky-Elemente in einer Section nicht abgeschnitten werden.

---

Verwandt: [2.5 Breakpoints und Width](../2.5-breakpoints-und-width.md) · [2.3 Design-Tokens Tailwind v4](../2.3-design-tokens-tailwind-v4.md)
