# Figma Design-Prinzipien by Arkadieff

> **Ausnahmen:** Jedes Prinzip erlaubt Ausnahmen, sofern das UI-Pattern es erfordert. Beispiel: Ein Karussell erfordert, dass alle Kind-Frames `hug` haben und der Container absichtlich überläuft — das ist kein Fehler, sondern das korrekte Muster. Ausnahmen sind explizit zu benennen.

> **Korrektur 13.07.2026 (durchgängig eingearbeitet):** Die Variant-Property für den inaktiven Button-Zustand heißt **`Inactive?`** (nicht mehr `Deactivated?`, wie manchmal verwendet). Betrifft u.a. `Buttons / MD / PrimaryButton` (node-id=2310-2156). Vor Code, der Property-Namen referenziert, immer live via `componentPropertyDefinitions` gegenprüfen — Namen ändern sich in diesem File, weil wir noch im Prozess sind.

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
Kind-Frames **und Textknoten** in einem `flex-col`-Container erhalten standardmäßig `fill` auf der Querachse (width). Das gilt auf jeder Verschachtelungsebene — sowohl der Frame als auch der Textknoten darin müssen explizit auf `fill` gesetzt werden. Ein Frame auf `fill` zu setzen reicht nicht — der Textknoten innerhalb erbt das nicht automatisch.

```
flex-col (fill)
├── SectionLabel (Frame)  → fill   ✅
│   └── Text              → fill   ✅ muss explizit gesetzt werden!
├── ContentFrame          → fill   ✅
│   └── Text              → fill   ✅
└── AnotherBlock          → fill   ✅
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

**Ergänzung — Frame-Naming und Auto-Layout:**
„Frame" ist im Zweifel ein gültiger Name — random Nummerierungen wie `Frame 845`, `Frame 15` etc. werden vermieden. Ein schlichtes `Frame` ist insbesondere gewünscht, wenn der Frame keine erkennbare FE-Relevanz hat. Auto-Layout-Frames sind so oft es geht mit `flex-row` bzw. `flex-col` zu benennen — ihre Layout-Richtung ist FE-relevant.

### Principle 13: Text Styles konsequent verknüpfen
Jeder Textknoten ist mit einem Text Style verknüpft. Direkte Font-Properties ohne Style-Verknüpfung sind nur temporär während der Erstellung zulässig. Globale Änderungen (Font, Größe, Farbe) sollen über den Style wirken — nicht durch manuelle Einzelanpassungen.

Empfohlener Workflow: Styles werden vor der eigentlichen Datei-Erstellung angelegt (siehe `figma-kollaboration-workflows.md`). Vollständige Liste der aktuell definierten Text Styles: siehe Abschnitt "🔤 Design Tokens: Text Styles" weiter unten.

### Principle 14: Clip Content nur explizit setzen
`clipsContent` wird nicht als Default gesetzt — nur dann, wenn Inhalte eines Containers bewusst abgeschnitten werden sollen (z.B. Scroll-Container, Bild-Crop, Karussell). Slides und Layout-Frames erhalten kein Clip Content, solange kein Overflow-Problem vorliegt.

### Principle 15: Variant-Property-Konventionen
Innerhalb von Component-Variant-Namen (z.B. `Hover?=False, Variant=1, Color=blue-tint`) gilt:

- **Boolean-Properties** erhalten immer das Suffix `?` und ausschließlich die Werte `True`/`False` — nie `Yes`/`No`, nie ohne `?`. Beispiel: `Hover?=False`, nicht `Hover=No` oder `Hover?=No`.
- **Enum/Options-Properties** (mehr als zwei mögliche Werte, z.B. Größenstufen oder Farbvarianten) heißen `Variant=` — nicht `Var=`.
- Die Property-Reihenfolge bleibt innerhalb eines Component-Sets über alle Varianten hinweg identisch.
- Enthält das Label selbst bereits ein `?` (z.B. eine Frage wie `"Weiter zu Versandmethoden?"`), wird der Boolean-Marker trotzdem zusätzlich außerhalb der Anführungszeichen ergänzt: `"Weiter zu Versandmethoden?"?=False`. Das sieht mit doppeltem `?` ungewohnt aus, folgt aber derselben Regel wie alle Nachbar-Properties.

**Häufig verwendete Property-Namen zur Orientierung (Audit vom 01.07.2026, `Inactive?`-Umbenennung berücksichtigt):** `State`, `Variant`, `Hover?`,  `Type`, `Selected?`, `Open?`, `Inactive?`, `Show Icon?`, `Is Active?`, `Has Input?`, `window-w`, `Size`. Selten: `color-mode: ...?`

---

## 🖱️ Interaction & State Behavior

### Button-Verhalten: Inactive State
- **Optik:** Inaktive Buttons verwenden die Variante `Inactive?=True` der jeweiligen Button-Komponente. Beispiel: [`Buttons / MD / PrimaryButton`](https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2310-2156) — dort als Varianten-Parameter `Inactive` hinterlegt. Keine manuelle Nachbildung über Opacity o.ä. — der Zustand ist Teil der Component.
- **Klickbarkeit:** Inaktive Buttons sind **nicht** im Sinne von "nicht klickbar" deaktiviert — sie lassen sich anklicken.
- **Feedback bei Klick:** Ein Klick auf einen inaktiven Button zeigt eine Fehlermeldung, die erklärt, warum die Aktion aktuell nicht möglich ist.
- **Rückkehr zum Ausgangszustand:** Nach dem Click kehrt der Button wieder in die `Inactive`-Optik zurück — es entsteht kein eigener, dauerhafter "Error"-Zustand am Button selbst.

**Warum `Inactive?` statt eines echten `disabled`-Zustands:** Wir setzen bewusst auf eine sichtbar inaktive, aber weiterhin klickbare Variante, damit die Userin trotzdem interagieren kann — ein Klick liefert ihr die Fehlermeldung bzw. Erklärung dafür, warum der Zustand gerade `Inactive` ist (z.B. fehlende Pflichtangabe, nicht erfüllte Voraussetzung). Ein klassisches `disabled` (nicht klickbar, kein Pointer-Event) würde diese Erklärung verschlucken und die Userin ratlos zurücklassen.

```
Button (Variant: Inactive=True)
   │  onClick
   ▼
Fehlermeldung wird angezeigt
   │
   ▼
Button (Variant: Inactive=True)   ← zurück zum Ausgangszustand, kein separater Error-State am Button
```

*Hinweis: Dieses Verhalten unterscheidet sich bewusst von einem klassischen `disabled`-Button (nicht klickbar, kein Pointer-Event). Der Grund für die Klickbarkeit ist, der Nutzerin aktiv mitzuteilen, warum eine Aktion nicht verfügbar ist, statt sie stillschweigend zu ignorieren.*

---

## 📛 Naming-Konventionen

- **Inhaltliche Container:** `[Element]Container` — z.B. `FeedContainer`, `CardContainer`
- **Layout-Frames (Auto Layout):** Tailwind-Konvention, lowercase — z.B. `flex-row`, `flex-col`
- **Layout-Wrapper mit Ausrichtung:** Tailwind `align-self`-Klassen — z.B. `self-end`, `self-start`, `self-center`. Werden verwendet wenn ein einzelnes Kind-Element eine abweichende Ausrichtung im Container braucht, ohne den Inhalt selbst zu verändern.
- **Scroll:** `scroll`, `scroll-x-auto`, `scroll-y-auto`
- **Components:** PascalCase — z.B. `TabsNavigation`, `Button`, `Card`
- **Variant-Properties:** siehe Principle 15 — Booleans immer `Property?=True/False`, Enums immer `Variant=Wert`

**Beispiel: Layout-Wrapper**
```
MainContent (flex-col)
├── ExperienceSection   ← inhaltlicher Block
├── ProjectsSection     ← inhaltlicher Block
└── self-end            ← reiner Layout-Wrapper, schiebt Kind ans untere Ende
    └── BeyondWorkBlock ← inhaltlicher Block
```

---

## 🔤 Design Tokens: Text Styles

Stand 14.07.2026, ausgelesen aus der Komponentenbibliothek-Section (`get_variable_defs` auf Node 3267:6614, "PATTERNS, BUTTONS, ELEMENTS, COMPONENTS" — deckt alle Top-Level-Sections außer den Screens/Mockups in "PAGES" ab; ggf. existieren dort noch weitere, hier nicht erfasste Styles).

| Style-Name | Font-Familie | Stil | Größe | Gewicht | Line-Height | Letter-Spacing |
|---|---|---|---|---|---|---|
| Label/default | BROWN NOW TWO | TWO | 16 | 400 | 16 | 0 |
| Label/Selected | BROWN NOW ONE | ONE | 16 | 400 | 16 | 0 |
| UserMessage/LG | BROWN NOW TWO | TWO | 16 | 400 | 16 ([twuc]-4) | -2 |
| UserMessage/X-LG | BROWN NOW TWO | TWO | 20 | 400 | 16 ([twuc]-4) | -2 |
| UserMessage/Default | Manrope | Regular | 12 | 400 | 12 | 0 |
| Input/InputText | Manrope | Regular | 18 | 400 | 14 | 2 |
| Input/LabelDefault | Manrope | Regular | 14 | 400 | 14 | -1 |
| Input/Label SM | Manrope | Light | 9 | 300 | 9 | -1 |
| Input/Warning&DefaultText | Manrope | Regular | 12 | 400 | 14 | 0 |
| Cards/ProductTitle | Manrope | Bold | 16 | 700 | 18 | 2 |
| Cards/MD | BROWN NOW TWO | TWO | 22 | 400 | 14 | 5 |
| Cards/Light | Manrope | Light | 10 | 300 | 10 | -3 |
| Cards/MegaCard/Lumo | LUMOSKY | Regular | 40 | 400 | 40 | 6 |
| Cards/MegaCard/Body | Manrope | Regular | 20 | 400 | 28 ([twuc]-7) | -2 |
| Cards/Featured/Title | LUMOSKY | Regular | 24 | 400 | 30 | -3 |
| Cards/Blog/Title | Manrope | Light | 19 | 300 | 1.3 | 0 |
| Buttons/LG | BROWN NOW ONE | ONE | 34 | 400 | 40 | -2 |
| Buttons/LG Underlined | BROWN NOW ONE | ONE | 34 | 400 | 40 | 2 |
| Buttons/MD | BROWN NOW TWO | TWO | 24 | 400 | 0.8 | 5 |
| Buttons/MD Underlined | BROWN NOW TWO | TWO | 24 | 400 | 0.8 | 5 |
| Buttons/SM | BROWN NOW ONE | ONE | 20 | 400 | 20 | -2 |
| Buttons/X-SM | BROWN NOW TWO | TWO | 18 | 400 | 18 | -2 |
| Buttons/XX-SM | BROWN NOW ONE | ONE | 14 | 400 | 16 | -2 |
| Buttons/XX-SM underlined | BROWN NOW ONE | ONE | 14 | 400 | 16 | -2 |
| Buttons/XXXS Inline | BROWN NOW ONE | ONE | 12 | 400 | 12 | -2 |
| Buttons/Quantity&Packaging | Manrope | SemiBold | 14 | 600 | 14 | 0 |
| H1 Subtitle | BROWN NOW TWO | TWO | 40 | 400 | 0.8 | -2 |
| H2 | LUMOSKY | Regular | 32 | 400 | 1 | 2 |
| H2 Produktkategorie | LUMOSKY | Regular | 40 | 400 | 1 | 2 |
| H2 Subtitle | BROWN NOW TWO | TWO | 24 | 400 | 24 | -2 |
| H2 Alternative | BROWN NOW ONE | ONE | 26 | 400 | 1 | 6 |
| H3 | BROWN NOW ONE | ONE | 26 | 400 | 20 | -2 |
| DefaultText LG | Manrope | Light | 16 | 300 | 1.2 | 0.5 |
| DefaultText MD | Manrope | Regular | 14 | 400 | 1.5 | 1.5 |
| DefaultText S | Manrope | Regular | 12 | 400 | 100 (%) | 0 |
| BulletPoints | Manrope | Regular | 14 | 400 | 100 (%) | 0 |
| Link | Manrope | SemiBold | 16 | 600 | 18 | -1 |
| Comment | Manrope | Light | 12 | 300 | 16 | 0 |
| Comment/BodyText | Manrope | Regular | 16 | 400 | 100 (%) | 0 |
| Navigation/Route | Manrope | Medium | 12 | 500 | 1 | 5 |
| Navigation/FullScreen/MainCategory | Manrope | ExtraBold | 16 | 800 | 1.1 | 0 |
| Navigation/FullScreen/SubCategory | Manrope | SemiBold | 16 | 600 | 1.1 | 0 |
| Navigation/SideNavigation/MainCategory | Manrope | SemiBold | 13 | 600 | 13 | 0 |
| Navigation/SideNavigation/SubCategory | Manrope | Regular | 14 | 400 | 14 | 0 |
| ProductPage/ProductTitle | Manrope | ExtraBold | 24 | 800 | 26 | 0 |
| ProductPage/Hightlighted | Manrope | ExtraBold | 16 | 800 | 0.8 | 0 |
| ProductPage/Dropdown/Summary | Manrope | Bold | 18 | 700 | 18 | 1 |
| ProductPage/Dropdown/H3 ManufacturerName | Manrope | SemiBold | 16 | 600 | 100 (%) | 1 |
| ProductPage/Dropdown/H4 Question | Manrope | Regular | 16 | 400 | 26 | 0 |
| ProductPage/Dropdown/BodyText - Responce | Manrope | Regular | 16 | 400 | 26 | 0 |
| ShoppingCart & Checkout/MainHeadline | BROWN NOW TWO | TWO | 34 | 400 | 1 | -2 |
| ShoppingCart & Checkout/Headline | Manrope | ExtraBold | 14 | 800 | 14 | -1 |
| ShoppingCart & Checkout/Body | Manrope | Medium | 14 | 500 | 14 | 0 |
| ShoppingCart & Checkout/Subtle | Manrope | Regular | 11 | 400 | 11 | 0 |
| ShoppingCart & Checkout/Hightlighted | Manrope | Bold | 14 | 700 | 14 | -3 |
| DataBlocks/SummaryItemTitle | Manrope | Medium | 16 | 500 | 16 | 0 |
| DataBlocks/SummaryItemContent | Manrope | Regular | 14 | 400 | 18 | 0 |
| PriceRangeFilter/Label | Manrope | Medium | 10 | 500 | 10 | 0 |
| Table/\<th\> | Manrope | SemiBold | 18 | 600 | 18 | 0 |
| Table/Cell | Manrope | Regular | 20 | 400 | 20 | 0 |

*Hinweis: "100 (%)" bei Line-Height bedeutet 100% Zeilenhöhe (relativ zur Schriftgröße), keine feste px-Angabe — anders als die übrigen Zeilen, die meist einen px- oder Multiplikator-Wert zeigen.*

---

## 📐 Design Tokens: Box-Spacing & Gap

Beide Skalen verwenden — soweit im gescannten Bereich vorhanden — **identische px-Werte pro Größenlabel**, lassen sich also in einer gemeinsamen Tabelle führen:

| Label | px (Box-Spacing) | px (Gap) |
|---|---|---|
| xxxs | 2 | 2 |
| xxs | 4 | 4 |
| xs | 6 | 6 |
| sm | 8 | 8 |
| md-sm | 12 | 12 |
| md | 16 | 16 |
| md-l | 20 | 20 |
| lg | 28 | 28 |
| xl | 40 | 40 |
| xxl | 48 | *(im gescannten Bereich nicht als Gap gefunden)* |
| xxxl | 56 | *(im gescannten Bereich nicht als Gap gefunden)* |

**Wichtig — Namenskollision mit einer dritten, unabhängigen Skala:** Es gibt zusätzlich eine Variable-Familie `spacings/spacing-*`, die dieselben Größenlabels (xxxs, xxs, xs, sm, md, lg) verwendet, aber **andere px-Werte** liefert — diese Familie ist stattdessen direkt an die Tailwind-Spacing-Einheit (`n-tcss` = n × 4px) gekoppelt:

| Label | Tailwind-Einheit (tcss) | px | rem |
|---|---|---|---|
| xxxxs | 0,5 tcss | 2 | 0,125rem |
| xxxs | 1 tcss | 4 | 0,25rem |
| xxs | 2 tcss | 8 | 0,5rem |
| xs | 3 tcss | 12 | 0,75rem |
| sm | 4 tcss | 16 | 1rem |
| md | 5 tcss | 20 | 1,25rem |
| lg | 10 tcss | 40 | 2,5rem |
| xxxxl | 14 tcss | 56 | 3,5rem |

**Beispiel Kollision:** `box-spacing-xxxs` = 2px, aber `spacings/spacing-xxxs` = 4px — gleiches Label "xxxs", unterschiedliche Skala. Beim Lesen von Variable-Namen immer auf das Präfix achten (`box-spacing-`/`gap-` vs. `spacings/spacing-`), nicht nur auf das Größenlabel.

---

## 📏 Design Tokens: Tailwind-Utility-Scale ↔ Figma-px (persönliche Referenz, nur für Maria)

Aus der Variable-Familie `[twuc]-N (X rem)` — zeigt, welche Tailwind-rem-Werte tatsächlich im File verwendet werden, statt nur die resultierenden px-Zahlen zu sehen. Formel bei korrekter Umsetzung: `px = N × 4`, `rem = N × 0,25`.

| [twuc]-N | rem | px (Figma-Wert) | px nach Formel (N×4) | Stimmt überein? |
|---|---|---|---|---|
| 4 | 1rem | 16 | 16 | ✅ |
| 7 | 1,75rem | 28 | 28 | ✅ |
| 8 | 2rem | 32 | 32 | ✅ |
| 9 | 2,25rem | 36 | 36 | ✅ |
| 10 | 2,5rem | 40 | 40 | ✅ |
| 11 | 2,75rem | 44 | 44 | ✅ |
| 12 | 3rem | 48 | 48 | ✅ |
| 15 | 3,75rem | 60 | 60 | ✅ |
| 16 | 4rem | 64 | 64 | ✅ |
| 18 | 4,5rem | 72 | 72 | ✅ |
| 20 | 5rem | 80 | 80 | ✅ |
| 22 | 5,5rem | 88 | 88 | ✅ |
| 24 | 6rem | 96 | 96 | ✅ |
| 28 | 7rem | 112 | 112 | ✅ |
| 32 | 8rem | 128 | 128 | ✅ |
| 40 | 10rem | **144** | 160 | ❌ (−16px = −1rem) |
| 41 | 10,25rem | 164 | 164 | ✅ |
| 48 | 12rem | **176** | 192 | ❌ (−16px = −1rem) |
| 56 | 14rem | 224 | 224 | ✅ |
| 60 | 15rem | 240 | 240 | ✅ |
| 64 | 16rem | 256 | 256 | ✅ |
| 96 | 24rem | 384 | 384 | ✅ |
| 112 | 28rem | 448 | 448 | ✅ |
| 128 | 32rem | 512 | 512 | ✅ |
| 160 | 40rem | 640 | 640 | ✅ |
| 192 | 48rem | **674** | 768 | ❌ (−94px) |
| 224 | 56rem | 896 | 896 | ✅ |

**Auffällig:** Drei Werte weichen von der Formel ab: `[twuc]-40` (zeigt 144px statt 160px), `[twuc]-48` (zeigt 176px statt 192px) — beide exakt um 16px/1rem zu niedrig, ein systematisches Muster, das nach einem Tippfehler oder einer versehentlich falsch verknüpften Variable aussieht. `[twuc]-192` weicht stärker ab (674px statt 768px) — hier ist unklar, ob das ein bewusster Sondertwert (z.B. ein spezifischer Breakpoint) oder ebenfalls ein Fehler ist. Alle drei ggf. in Figma direkt gegenprüfen.

---

## ✅ Offene TODOs (Figma-Schreibzugriff nötig — Claude kann nur lesen)

Claude hat aktuell nur lesenden Zugriff auf Figma (Dev Mode MCP Server). Folgende Korrekturen müssen manuell in Figma vorgenommen werden (oder sobald ein schreibfähiger Figma-Connector verbunden ist):

### 1. Drei `[twuc]`-Werte korrigieren (siehe Tabelle oben)
- `[twuc]-40`: 144px → **160px**
- `[twuc]-48`: 176px → **192px**
- `[twuc]-192`: 674px → vermutlich **768px** (Ursache/Absicht unklar, bitte gegenprüfen)

### 2. `spacings/spacing-*`-Bindungen durch `gap-*`/`box-spacing-*` ersetzen
Regel: **Gap-Variable für Flexbox-Gaps, Box-Spacing-Variable für Padding/Margin.** Labels sind zwischen den Skalen NICHT wertgleich (`spacing-md`=20px ≠ `gap-md`=16px) — immer nach dem tatsächlichen px-Wert mappen, nicht nach Label-Name.

Bisher bekannte Fundstellen (Stichprobe aus 5 geprüften Komponenten, keine vollständige Suche):

| Komponente | Property | Bisherige Variable | Neue Variable |
|---|---|---|---|
| Filter/FilterPanel (2211:2165), äußerer Container | gap | spacings/spacing-xxxs (4px) | **gap-xxs (4px)** |
| NavBar (1:115), "Icons / Tools"-Reihe | gap | spacings/spacing-md (20px) | **gap-md-l (20px)** |
| Components/Product/BuyBox, "Titel und Bewertungen" | gap | spacings/spacing-xs (12px) | **gap-md-sm (12px)** |
| Components/Product/BuyBox, "Titel und Bewertungen" | padding-bottom | spacings/spacing-md (20px) | **box-spacing-md-l (20px)** |
| Components/Product/BuyBox, "Benefits"-Liste | gap | spacings/spacing-xxs (8px) | **gap-sm (8px)** |
| Components/Product/BuyBox, "Benefits"-Liste | padding-bottom | spacings/spacing-md (20px) | **box-spacing-md-l (20px)** |
| Components/Product/BuyBox, "Menge, Verpackung, Preis" | gap | spacings/spacing-md (20px) | **gap-md-l (20px)** |
| Components/Product/BuyBox, Preis-Label (flex-col) | gap | spacings/spacing-xxxxs (2px) | **gap-xxxs (2px)** |
| Components/Product/BuyBox, "Menge und Preis" | gap | spacings/spacing-xxs (8px) | **gap-sm (8px)** |

### 3. Dokumentenweite Suche nach verwaisten Variables (in Vorbereitung)
Nächster Schritt: systematische Prüfung möglichst vieler/aller 113 katalogisierten Komponenten auf hartkodierte Werte, die eigentlich eine bekannte Variable sein sollten. Liste folgt.

---

*Diese Prinzipien gelten für alle Figma-Designs, Komponenten und Layout-Strukturen.*
