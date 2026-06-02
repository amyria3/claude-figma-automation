# Figma Design-Prinzipien by Arkadieff

> **Ausnahmen:** Jedes Prinzip erlaubt Ausnahmen, sofern das UI-Pattern es erfordert. Beispiel: Ein Karussell erfordert, dass alle Kind-Frames `hug` haben und der Container absichtlich überläuft — das ist kein Fehler, sondern das korrekte Muster. Ausnahmen sind explizit zu benennen.

---

## 🏗️ CORE PRINCIPLE: Flex-Based Layouts
Alle Frames verwenden Auto Layout (`flex-row` oder `flex-col`). Kein manuelles Positionieren von Elementen.

---

## 🏛️ Structural Design Principles

### Principle 1: Hierarchical Nesting
Frames sind verschachtelt, nicht flach auf dem Canvas platziert.

### Principle 2: Component Separation
Jedes semantisch eigenständige UI-Element erhält einen eigenen Frame oder eine Component.

### Principle 3: Blöcke = Frames mit Auto Layout
Zusammenhängende Inhalte (Sektionen, Karten, Listen, Header etc.) werden in einen eigenen Frame gruppiert. Jeder Block-Frame hat Auto Layout aktiviert. Elemente werden nicht lose in übergeordnete Frames gelegt — der übergeordnete Frame organisiert seine Kind-Frames selbst per Auto Layout.

**Beispiel: Zweispaltiges Layout**
```
PageFrame (flex-col)
├── HeaderBlock          ← globale Elemente, die das gesamte Layout überspannen
└── ColumnsFrame (flex-row)
    ├── SidebarFrame (flex-col)
    │   ├── SectionBlock-A (flex-col)
    │   └── SectionBlock-B (flex-col)
    └── MainContentFrame (flex-col)
        ├── SectionBlock-C (flex-col)
        └── SectionBlock-D (flex-col)
```

### Principle 4: Globale Elemente über Spalten-Layout
Elemente, die das gesamte Layout überspannen (z.B. Name, Seitentitel, globale Navigation), werden direkt in den Root-Frame gelegt — nicht in eine der Spalten. Der Root-Frame ist `flex-col`: globaler Header oben, Spalten-Container darunter.

```
RootFrame (flex-col)
├── GlobalHeader  → fill, liegt über allem
└── ColumnsFrame (flex-row)
    ├── Sidebar
    └── MainContent
```

### Principle 5: Sizing in flex-row — Fill/Hug-Regel
In einem `flex-row`-Container gilt: Mindestens ein Kind trägt `fill` — andernfalls läuft der Container über.

```
flex-row
├── ChildA  → width: fill   ✅ nimmt verfügbaren Platz
└── ChildB  → width: hug    ✅ passt sich Inhalt an
```

**Praxisbeispiel: Fixed/Fluid-Layout**
```
flex-row
├── Sidebar      → width: hug (shrink-0)   feste Breite
└── MainContent  → width: fill             nimmt restlichen Platz
```

*Ausnahme: Karussell oder horizontaler Scroll — alle Kinder `hug`, Container overflows absichtlich.*

### Principle 6: Sizing in flex-col — Querachse fill
Kind-Frames in einem `flex-col`-Container erben standardmäßig `fill` auf der Querachse (width). Das gilt auch für verschachtelte Container-Frames wie `SectionLabel` oder Wrapper-Frames — sie erben `fill` vom Elternelement, solange ihr Inhalt dynamisch oder textuell ist.

```
flex-col (fill)
├── SectionLabel  → fill   ✅ passt sich Containerbreite an
├── ContentFrame  → fill   ✅
└── AnotherBlock  → fill   ✅
```

*Ausnahme: Elemente mit wirklich fixer, nicht-textbasierter Größe — z.B. ein quadratisches Icon, ein Avatar, ein Badge mit fester Pixelgröße. Textbasierte Elemente, auch kurze Labels, bekommen immer `fill`.*

### Principle 7: flex-wrap und Grid — Wahl nach Struktur
`flex-wrap` für dynamische Inhalte ohne bekannte Anzahl. Grid (`grid-cols`) wenn Spaltenanzahl fix und vorhersehbar. Kinder in beiden Fällen standardmäßig `fill` — sie teilen den verfügbaren Platz gleichmäßig auf.

```
// Dynamisch, Anzahl unbekannt → flex-wrap
flex-row + flex-wrap (w-full)
├── Item → fill   ✅
└── Item → fill   ✅ (umbricht automatisch)

// Fix, Anzahl bekannt → grid
grid-cols-2
├── Item → fill   ✅
├── Item → fill   ✅
├── Item → fill   ✅
└── Item → fill   ✅
```

*Ausnahme: Elemente mit stark variierendem Inhalt können `hug` behalten, wenn gleichmäßige Verteilung unerwünscht ist.*

### Principle 8: Intrinsische Breite — `hug` + `whitespace-nowrap`
Elemente mit vorhersehbarem, kurzem Inhalt (Datum, Status, Badge) erhalten `hug` und `whitespace-nowrap` statt einer fixen Pixelbreite. Der Text definiert seine eigene Breite — keine manuelle Pflege erforderlich.

```
flex-row
├── JobInfo  → fill              Titel + Subtitle, nimmt restlichen Platz
└── Date     → hug + nowrap      "Current since January 2024", nie umbrechen
```

### Principle 9: SectionLabel als separater Frame *(optional)*
Titel und Inhalt einer Sektion können in getrennten Kind-Frames liegen (`SectionLabel` + Content-Frame), um die semantische Trennung im Layer-Panel sichtbar zu machen. Bei großen Dateien ist eine durchgängige Benennung nicht immer erforderlich.

### Principle 10: Scrollable Container Pattern
Scrollbare Inhalte erhalten einen expliziten Container-Frame mit entsprechendem Scroll-Verhalten (`clip content` aktiviert, Overflow scroll).

### Principle 11: Component Variants
Wiederverwendbare Elemente werden als Components mit Variants angelegt.

### Principle 12: Granular & Semantic Naming
Jede Ebene trägt einen aussagekräftigen Namen, der Funktion oder Inhalt beschreibt (z.B. `HeaderFrame`, `TabsNavigation`, `FeedContent`).

### Principle 13: Text Styles konsequent verknüpfen
Jeder Textknoten ist mit einem Text Style verknüpft. Direkte Font-Properties ohne Style-Verknüpfung sind nur temporär während der Erstellung zulässig. Globale Änderungen (Font, Größe, Farbe) sollen über den Style wirken — nicht durch manuelle Einzelanpassungen.

Empfohlener Workflow: Styles werden vor der eigentlichen Datei-Erstellung angelegt (siehe `figma-kollaboration-workflows.md`).

---

## 📛 Naming-Konventionen

- **Container:** `[Element]Container` — z.B. `FeedContainer`, `CardContainer`
- **Layout:** `flex-row`, `flex-col` (Tailwind-Konvention, lowercase)
- **Scroll:** `scroll`, `scroll-x-auto`, `scroll-y-auto`
- **Components:** PascalCase — z.B. `TabsNavigation`, `Button`, `Card`

---

## 📐 Spacing & Gap Guide
- 4px – Micro
- 8px – Tight (STANDARD)
- 12px – Standard
- 16px – Generous
- 24px – Large
- 32px – Extra large

---

## Typography Tokens (3-Layer)

**Primitive:** font-size-12/14/16/20/24/32 · line-height-120/130/140/150/160 · font-weight-light/regular/medium/bold/extra-bold

**Semantic:** Display/Extra Bold · Headline/Bold · Title/Bold · Body/Regular · Body/Medium · Caption/Light · Caption/Regular

**Component:** Button/Label · Card/Title · Card/Caption

---

*Diese Prinzipien gelten für alle Figma-Designs, Komponenten und Layout-Strukturen.*
