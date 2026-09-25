# Figma Design-Prinzipien by Arkadieff

> **Ausnahmen:** Jedes Prinzip erlaubt Ausnahmen, sofern das UI-Pattern es erfordert. Beispiel: Ein Karussell erfordert, dass alle Kind-Frames `hug` haben und der Container absichtlich überläuft — das ist kein Fehler, sondern das korrekte Muster. Ausnahmen sind explizit zu benennen.

> **Property-Namen:** Die Variant-Property für den inaktiven Button-Zustand heißt **`Inactive?`**, z. B. an `Buttons / MD / PrimaryButton` (node-id=2310-2156). Vor Code, der Property-Namen referenziert, prüfst Du die Namen live über `componentPropertyDefinitions`. So bleibt der Code auch dann richtig, wenn sich ein Name im File ändert.

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

**Primitives & Slot-Einsatz:** Gilt insbesondere für Typo-Primitives (Headlines, Paragraphs) und Content Modules: Der Textknoten übernimmt per `fill` die Breite seines Frames — auf jeder Verschachtelungsebene, auch innerhalb von Wrapper-Frames wie `Title`. Wird eine Instanz in einen Slot oder ein Modul gesetzt (auch nach Instance-Swap), sind Frame UND Textknoten auf `fill` zu prüfen. Breiten-Constraints (min-/max-w) gehören an den Container — nie an den Textknoten oder das Primitive selbst.

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
Die Seite scrollt als Ganzes. Overflow sitzt nur an der Wurzel von `Templates / Page` (sie steht für den Browser-Viewport) und an echten Scroll-Bereichen wie Karussell, Modal oder Filter-Panel. Diese erhalten einen expliziten Container-Frame mit `clip content` und Overflow.

Sections, `main` und Slots bekommen keinen Overflow. Verschachtelte Scroll-Container fangen im Prototyp das Mausrad ab (die Seite scrollt dann nicht mehr zurück), und der Entwickler übernimmt sie als `overflow-y: auto` mit fester Höhe. Bei Scroll-Problemen prüft die Designerin zuerst, welche Ebenen einen Overflow tragen. Details: [2.7 Layout](2-tarabao/2.7-layout.md).

### Principle 11: Component Variants
Wiederverwendbare Elemente werden als Components mit Variants angelegt.

### Principle 12: Granular & Semantic Naming
Jede Ebene trägt einen aussagekräftigen Namen, der Funktion oder Inhalt beschreibt (z.B. `HeaderFrame`, `TabsNavigation`, `FeedContent`).

**Frame-Naming und Auto-Layout:**
„Frame" ist im Zweifel ein gültiger Name — random Nummerierungen wie `Frame 845`, `Frame 15` etc. werden vermieden. Ein schlichtes `Frame` ist insbesondere gewünscht, wenn der Frame keine erkennbare FE-Relevanz hat. Auto-Layout-Frames sind so oft es geht mit `flex-row` bzw. `flex-col` zu benennen — ihre Layout-Richtung ist FE-relevant.

### Principle 13: Text Styles konsequent verknüpfen
Jeder Textknoten ist mit einem Text Style verknüpft. Direkte Font-Properties ohne Style-Verknüpfung sind nur temporär während der Erstellung zulässig. Globale Änderungen (Font, Größe, Farbe) sollen über den Style wirken — nicht durch manuelle Einzelanpassungen.

Empfohlener Workflow: Styles werden vor der eigentlichen Datei-Erstellung angelegt (siehe `figma-kollaboration-workflows.md`). Alle Text Styles mit ihren Werten: `2-tarabao/app.tcss` §6 (Klassen `type-*`), erklärt in `2-tarabao/2.6-design-tokens-tailwind-v4.md` §6a.

### Principle 14: Clip Content nur explizit setzen
`clipsContent` wird nicht als Default gesetzt — nur dann, wenn Inhalte eines Containers bewusst abgeschnitten werden sollen (z.B. Scroll-Container, Bild-Crop, Karussell). Slides und Layout-Frames erhalten kein Clip Content, solange kein Overflow-Problem vorliegt.

### Principle 15: Variant-Property-Konventionen
Innerhalb von Component-Variant-Namen (z.B. `Hover?=False, Variant=1, Color=blue-tint`) gilt:

- **Boolean-Properties** erhalten immer das Suffix `?` und ausschließlich die Werte `True`/`False` — nie `Yes`/`No`, nie ohne `?`. Beispiel: `Hover?=False`, nicht `Hover=No` oder `Hover?=No`.
- **Enum/Options-Properties** (mehr als zwei mögliche Werte, z.B. Größenstufen oder Farbvarianten) heißen `Variant=` — nicht `Var=`.
- Die Property-Reihenfolge bleibt innerhalb eines Component-Sets über alle Varianten hinweg identisch.
- Enthält das Label selbst bereits ein `?` (z.B. eine Frage wie `"Weiter zu Versandmethoden?"`), wird der Boolean-Marker trotzdem zusätzlich außerhalb der Anführungszeichen ergänzt: `"Weiter zu Versandmethoden?"?=False`. Das sieht mit doppeltem `?` ungewohnt aus, folgt aber derselben Regel wie alle Nachbar-Properties.

**Häufig verwendete Property-Namen zur Orientierung:** `State`, `Variant`, `Hover?`,  `Type`, `Selected?`, `Open?`, `Inactive?`, `Show Icon?`, `Is Active?`, `Has Input?`, `viewport-range`, `Size`. Selten: `color-mode: ...?`

### Principle 16: Seiten wachsen mit dem Inhalt, der Bildschirm ist eine Min-Höhe
Die Designerin setzt eine Seite nie auf eine feste Viewport-Höhe. `Templates / Page` steht auf Hug, die Min-Höhe (792) steht für den Bildschirm und wird im Code zu `min-h-dvh`. Die Bildschirmgröße legt das Device im Prototyp fest. So sieht der Entwickler die ganze Seite auf dem Canvas, ohne zu scrollen.

Nach manuellen Änderungen in der UI prüft die Designerin die Höhe: Instanzen und Slots können dabei auf eine feste Höhe zurückspringen. Details: [2.7 Layout](2-tarabao/2.7-layout.md).

### Principle 17: Header, main und Footer sind Geschwister
Die Ebenen der Seite entsprechen der HTML-Struktur `<header>`, `<main>`, `<footer>`. Der Footer gehört nicht in `main`. Der Header ist sticky (Position: Sticky), und der Frame `Page` steht auf „Canvas stacking: First on top“, damit der Header beim Scrollen über dem Inhalt liegt. Details: [2.7 Layout](2-tarabao/2.7-layout.md).

### Principle 18: Varianten schalten mit dem Modus um, wenn ihre Property an eine Variable gebunden ist
Eine Komponente, die je Modus anders aussieht, bekommt eine Varianten-Property. Die Designerin bindet diese Property an eine Text-Variable. Dann wählt jede Instanz ihre Variante selbst: Schaltet die Designerin den Modus an der Section um, wechseln alle gebundenen Komponenten darin mit.

Beispiel: NavBar, Nav, Footer, PromoBar und Nutmixer haben die Varianten-Property `viewport-range` mit den Werten base, md und lg. Sie ist an die Variable `viewport-range` aus `Lyt scl / Width` gebunden. Diese Variable hat im Modus base den Wert „base“, im Modus md „md“ und im Modus lg „lg“. Stellt die Designerin die Section „{Single Pages} Toggle Lyt / Scl -> Width when changing Page Width“ auf lg, zeigen Header und Footer aller Seiten darin ihre lg-Variante.

- **Die Werte der Variable heißen genau wie die Varianten.** Sonst findet Figma keine passende Variante.
- **Die Property heißt wie die Variable.** So erkennst Du die Kopplung schon am Namen.
- **Die Designerin bindet die Property einmal im Master, in dem die Instanz steckt,** z. B. am Footer in `Templates / Page`. Alle Seiten erben die Bindung. Eine Instanz mit festem Wert schaltet nicht mit.
- **Die Komponente trägt keinen eigenen Modus.** Ein Modus an der Instanz überschreibt den Modus der Section.
- **So siehst Du die Kopplung:** Im Dev Mode zeigt die Property keinen festen Wert wie „md“, sondern die Variable mit dem T-Symbol: `viewport-range`. Im Component Playground („Explore component behavior“) schaltest Du die Varianten von Hand durch.

Im Code braucht die Komponente dafür keine Prop. Was sich je Breitenbereich ändert, setzt der Entwickler mit `md:` und `lg:`. Details: [2.5 Breakpoints und Width](2-tarabao/2.5-breakpoints-und-width.md), [Einstieg §3](2-tarabao/README.md).

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

## 🧩 Slots & Content Modules — Bauprinzip für CMS-abbildende Komponenten

Jeder austauschbare Inhaltsbereich hat einen Slot mit Preferred Values, eine Varianten-Achse je Slot und für optionale Bereiche ein Boolean. So zeigt der Component Playground genau die Zustände, die das CMS erlaubt. Aufbau, Benennung und Beispiel `ContentModules / Basic`: [2.8 Content Modules](2-tarabao/2.8-content-modules-und-slots.md).

---

## 📛 Naming-Konventionen

- **Inhaltliche Container:** `[Element]Container` — z.B. `FeedContainer`, `CardContainer`
- **Layout-Frames (Auto Layout):** Tailwind-Konvention, lowercase — z.B. `flex-row`, `flex-col`
- **Layout-Wrapper mit Ausrichtung:** Tailwind `align-self`-Klassen — z.B. `self-end`, `self-start`, `self-center`. Werden verwendet wenn ein einzelnes Kind-Element eine abweichende Ausrichtung im Container braucht, ohne den Inhalt selbst zu verändern.
- **Scroll:** `scroll`, `scroll-x-auto`, `scroll-y-auto`
- **Layout-Wrapper mit Breitengrenze:** `Wrapper [klasse]`, benannt nach der Tailwind-Klasse, die ihn ausmacht, z. B. „Wrapper [max-w-content]“. Der Name zeigt, dass es eine Figma-Ebene ist und welche Klasse sie im Code wird.
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

## 📐 Breakpoints & Breitenbereiche

Die Designerin setzt den Modus von `Lyt scl / Width` an der Figma-Section, in der die Seiten liegen. So rechnen alle Seiten und Komponenten darin mit den Breiten dieses Breitenbereichs. Begriffe, Werte und alle Regeln: [2.5 Breakpoints und Width](2-tarabao/2.5-breakpoints-und-width.md), Kopplung der Varianten: Principle 18.

---

## 📦 Box-Spacing-Muster (Section-basierte Seiten)

Abstände sitzen nur an der Section (oben und unten) und in der Ebene „Wrapper [max-w-content]“ (seitlich und zwischen den Inhalten). Page und Slots tragen keinen Abstand. So ergibt sich der Abstand zwischen zwei Sections allein aus ihrem Padding. Tabelle und Regeln: [2.7 Layout, So entstehen die Abstände](2-tarabao/2.7-layout.md).

---

*Diese Prinzipien gelten für alle Figma-Designs, Komponenten und Layout-Strukturen. Design-Tokens (Text Styles, Box-Spacing & Gap, Tailwind-Utility-Scale) stehen in `2-tarabao/2.6-design-tokens-tailwind-v4.md` und `2-tarabao/app.tcss`, offene Punkte in `2-tarabao/offene-punkte.md`.*
