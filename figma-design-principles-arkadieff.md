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
PageFrame (flex-row)
├── SidebarFrame (flex-col)
│   ├── SectionBlock-A (flex-col)
│   ├── SectionBlock-B (flex-col)
│   └── SectionBlock-C (flex-col)
└── MainContentFrame (flex-col)
    ├── SectionBlock-D (flex-col)
    ├── SectionBlock-E (flex-col)
    └── SectionBlock-F (flex-col)
```

### Principle 4: Sizing in flex-row — Fill/Hug-Regel
In einem `flex-row`-Container gilt: Kind-Frames haben entweder `fill` oder `hug` auf der Hauptachse (width). Haben mehrere Kinder `hug`, muss mindestens eines `fill` haben — andernfalls läuft der Container über.

**Regel:** Mindestens ein Kind pro `flex-row` trägt `fill`, um den verfügbaren Platz zu belegen.

```
flex-row
├── ChildA  → width: fill   ✅ nimmt verfügbaren Platz
└── ChildB  → width: hug    ✅ passt sich Inhalt an
```

```
flex-row
├── ChildA  → width: hug    ⚠️ beide hug ohne fill
└── ChildB  → width: hug    → Container läuft über
```

*Ausnahme: Karussell oder horizontaler Scroll — alle Kinder `hug`, Container overflows absichtlich.*

### Principle 5: Scrollable Container Pattern
Scrollbare Inhalte erhalten einen expliziten Container-Frame mit entsprechendem Scroll-Verhalten (`clip content` aktiviert, Overflow scroll).

### Principle 6: Component Variants
Wiederverwendbare Elemente werden als Components mit Variants angelegt.

### Principle 7: Granular & Semantic Naming
Jede Ebene trägt einen aussagekräftigen Namen, der Funktion oder Inhalt beschreibt (z.B. `HeaderFrame`, `TabsNavigation`, `FeedContent`).

---

## 📐 Layout-Struktur & Sizing

### flex-row
- Width: `fill` (mind. ein Kind) / `hug` (inhaltsgeprägte Kinder)
- Height: `hug`
- Verwendet für: Nav bars, Buttons, Header, Zeilen

### flex-col
- Width: `fill`
- Height: `hug`
- Verwendet für: Seiten-Layout, Cards, Feeds, Sektionen

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
