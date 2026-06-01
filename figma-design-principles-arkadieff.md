# Figma Design-Prinzipien by Arkadieff

## 🏗️ CORE PRINCIPLE: Flex-Based Layouts
**Alle Elemente als `flex-row` oder `flex-col`. Exceptions nur wenn Code- oder optische Logik es erfordert.**

## 🏛️ Structural Design Principles

### Principle 1: Hierarchical Nesting
Frames verschachtelt, nicht flach auf Canvas.

### Principle 2: Component Separation
Jedes bedeutungsvolle UI-Element hat seinen eigenen Frame/Component.

### Principle 3: Blöcke = Frames mit Auto Layout
Zusammenhängende Inhalte (Sektionen, Karten, Listen, Header etc.) werden IMMER in einen eigenen Frame gruppiert. Jeder Block-Frame hat Auto Layout aktiviert. Niemals zusammengehörige Elemente lose auf einen übergeordneten Frame legen. Das übergeordnete Layout organisiert die Block-Frames selbst per Auto Layout.

**Beispiel: Zweispaltiges Seiten-Layout**
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

### Principle 4: Scrollable Container Pattern
Scrollbare Inhalte in explizitem Container mit Scroll-Naming (scroll, scroll-x-auto, scroll-y-auto).

### Principle 5: Component Variants
Wiederverwendbare Elemente sind Components mit Variants.

### Principle 6: Granular & Semantic Naming
Jede Ebene hat aussagekräftigen Namen (Header, Tabs Navigation, Feed Content).

## 📐 Layout-Struktur & Sizing

### Flex-Row
- Width: `Fill`
- Height: `Hug`
- Verwendet für: Nav bars, buttons, header

### Flex-Col
- Width: `Fill`
- Height: `Hug`
- Verwendet für: Seiten-Layout, cards, feeds

## 📛 Naming-Konventionen

- **Container:** `[Element]Container` (FeedContainer, CardContainer)
- **Layout:** `flex-row`, `flex-col` (Tailwind, lowercase)
- **Scroll:** `scroll`, `scroll-x-auto`, `scroll-y-auto`
- **Components:** `TabsNavigation`, `Button`, `Card`

## 📐 Spacing & Gap Guide
- 4px – Micro
- 8px – Tight (STANDARD)
- 12px – Standard
- 16px – Generous
- 24px – Large
- 32px – Extra large

## Typography Tokens (3-Layer)

**Primitive:** font-size-12/14/16/20/24/32, line-height-120/130/140/150/160, font-weight-light/regular/medium/bold/extra-bold

**Semantic:** Typography/Display/Extra Bold, Headline/Bold, Title/Bold, Body/Regular, Body/Medium, Caption/Light, Caption/Regular

**Component:** Button/Label, Card/Title, Card/Caption

---

Diese Prinzipien anwenden bei: Figma-Designs, Komponenten-Erstellung, Layout-Struktur.
