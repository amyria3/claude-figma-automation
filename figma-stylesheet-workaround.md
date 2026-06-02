# 🎨 Workaround: Stylesheet-basierte Style-Anwendung
**Praktische Lösung für Figma Variable-Limitation**

**Status:** Empfohlen  
**Getestet am:** 31.05.2026  
**Scenario:** Variables können nicht via MCP verknüpft werden

---

## 📋 Überblick

**Problem:** 
- Ich KANN Variablen nicht mit Nodes verknüpfen
- Figma blockiert alle Variable-APIs

**Lösung:**
- User erstellt **Stylesheet** (Design Tokens)
- User zeigt mir **Screenshots**
- Ich lese Werte und **setze sie DIREKT**
- User verknüpft dann **manuell mit Variablen**

**Ergebnis:** ✅ Consistent, kontrolliert, praktisch!

---

## 🔄 Workflow (Schritt-für-Schritt)

### Schritt 1️⃣: User erstellt Stylesheet

**In Figma:** Erstelle einen Frame "DESIGN\_TOKENS" mit:

```
┌─────────────────────────────────────────┐
│ DESIGN TOKENS / STYLESHEET              │
├─────────────────────────────────────────┤
│                                         │
│ COLORS:                                 │
│ ▰ Primary Blue   #3366CC  [BlueSky]    │
│ ▰ Success Green  #00AA44  [Success]    │
│ ▰ Error Red      #EE3333  [Error]      │
│ ▰ Text Gray      #333333  [Text]       │
│                                         │
│ TYPOGRAPHY:                             │
│ H1: Inter Bold 24px, line-height 130%  │
│ H2: Inter Bold 20px, line-height 130%  │
│ Body: Inter Regular 14px, line-height 150% │
│ Caption: Inter Regular 12px, line-height 140% │
│                                         │
│ SPACING:                                │
│ Large (32px), Medium (16px), Small (8px) │
│                                         │
└─────────────────────────────────────────┘
```

**Was wichtig ist:**
- ✅ Klare Namen (z.B. "Primary Blue", nicht nur "Blue")
- ✅ Hex-Codes oder RGB-Werte sichtbar
- ✅ Alle Eigenschaften dokumentiert (Size, Weight, Line-Height)
- ✅ Referenz zu Variable-Namen (optional, aber hilfreich)

---

### Schritt 2️⃣: User zeigt mir Screenshots

**Hochladen im Chat:**
```
📸 Screenshot des DESIGN_TOKENS Frames
   → Ich lese die Werte aus
```

---

### Schritt 3️⃣: Ich parse und speichere die Styles

**Ich lese aus dem Screenshot:**

```javascript
const designTokens = {
  colors: {
    'primaryBlue': {
      hex: '#3366CC',
      rgb: { r: 0.2, g: 0.4, b: 0.8 },
      variable: 'BlueSky'
    }
  },
  typography: {
    'headingL': {
      family: 'Inter',
      style: 'Bold',
      size: 24,
      lineHeight: { value: 130, unit: 'PERCENT' },
      variable: 'HeadingL'
    },
    'body': {
      family: 'Inter',
      style: 'Regular',
      size: 14,
      lineHeight: { value: 150, unit: 'PERCENT' },
      variable: 'Body'
    }
  },
  spacing: {
    'large': { value: 32, variable: 'Spacing-L' },
    'medium': { value: 16, variable: 'Spacing-M' },
    'small': { value: 8, variable: 'Spacing-S' }
  }
};
```

---

### Schritt 4️⃣: Ich erstelle Elemente mit Stylesheet-Werten

```javascript
async function createHeadingWithToken(text, tokenName = 'headingL') {
  const heading = figma.createText();
  heading.characters = text;
  const token = designTokens.typography[tokenName];
  await figma.loadFontAsync({ family: token.family, style: token.style });
  heading.fontSize = token.size;
  heading.lineHeight = token.lineHeight;
  heading.fills = [{ type: 'SOLID', color: designTokens.colors.primaryBlue.rgb }];
  return heading;
}
```

---

### Schritt 5️⃣: User verknüpft manuell mit Variablen

Nach der Erstellung verknüpft der User die Elemente manuell in Figma mit den entsprechenden Variablen.

---

## 🔗 Workaround: Library Text Styles via textStyleId übertragen

**Problem:** `figma.getLocalTextStylesAsync()` gibt leere Arrays zurück, wenn Styles aus einer verbundenen Library stammen (nicht lokal definiert).

**Lösung:** Style-ID von einem bereits verknüpften Knoten auslesen und auf alle passenden Knoten übertragen.

**Voraussetzung:** Der User wendet den gewünschten Style einmal manuell auf einen Knoten an.

```javascript
// Schritt 1: Alle Knoten mit Style-ID finden (einer muss bereits verknüpft sein)
const allText = page.findAllWithCriteria({ types: ["TEXT"] });
const withStyle = allText.filter(n => n.textStyleId && n.textStyleId !== "");
// → withStyle[n].textStyleId enthält die gesuchte ID

// Schritt 2: ID identifizieren (z.B. nach Font-Familie/Größe filtern)
const styleId = withStyle.find(n =>
  n.fontName.family === "Hanken Grotesk" && n.fontSize === 9
)?.textStyleId;

// Schritt 3: Style auf alle passenden Knoten anwenden
const targets = allText.filter(n =>
  n.fontName !== figma.mixed &&
  n.fontName.family === "Hanken Grotesk" &&
  n.fontName.style === "Regular" &&
  n.fontSize === 9
);

for (const node of targets) {
  node.textStyleId = styleId;
}
```

**Ergebnis:** Alle passenden Textknoten sind mit dem Library Style verknüpft — ohne manuelle Einzelauswahl.

---

## ✅ Checkliste für diesen Workaround

**Bevor User mir Styles zeigt:**
- [ ] Stylesheet Frame erstellt
- [ ] Alle Farben dokumentiert (Name + Hex)
- [ ] Alle Typographie dokumentiert (Font, Size, Weight, Line-Height)
- [ ] Alle Spacing-Werte dokumentiert

**Wenn ich Elemente erstelle:**
- [ ] Alle Werte aus Stylesheet gelesen
- [ ] Fonts geladen bevor Text gesetzt
- [ ] Alle Properties gesetzt (nicht nur Größe!)
- [ ] Konsistent über alle Elemente

**Nach Erstellung:**
- [ ] User verifiziert Styles optisch
- [ ] User verknüpft mit Variablen (manuell)
- [ ] Fertig! 🎉

---

**Version:** 1.1  
**Status:** Praktisch & empfohlen  
**Getestet:** 31.05.2026 / 02.06.2026
