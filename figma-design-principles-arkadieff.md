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

**Ergänzung (21.07.2026) — Primitives & Slot-Einsatz:** Gilt insbesondere für Typo-Primitives (Headlines, Paragraphs) und Content Modules: Der Textknoten übernimmt per `fill` die Breite seines Frames — auf jeder Verschachtelungsebene, auch innerhalb von Wrapper-Frames wie `Title`. Wird eine Instanz in einen Slot oder ein Modul gesetzt (auch nach Instance-Swap), sind Frame UND Textknoten auf `fill` zu prüfen. Breiten-Constraints (min-/max-w) gehören an den Container — nie an den Textknoten oder das Primitive selbst (vgl. max-w-Entfernung am Master von Primitives / Headlines / H3, 21.07.2026).

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

Empfohlener Workflow: Styles werden vor der eigentlichen Datei-Erstellung angelegt (siehe `figma-kollaboration-workflows.md`). Vollständige Liste der aktuell definierten Text Styles: siehe `ux-ui-dokumentation-tarabao.md`, Abschnitt "🔤 Design Tokens: Text Styles".

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

*Diese Prinzipien gelten für alle Figma-Designs, Komponenten und Layout-Strukturen. Design-Tokens (Text Styles, Box-Spacing & Gap, Tailwind-Utility-Scale) und offene TODOs stehen in `ux-ui-dokumentation-tarabao.md`.*
