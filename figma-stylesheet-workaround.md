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

**Beispiel Screenshot-Content:**
```
PRIMARY BLUE
Color: #3366CC
RGB: (51, 102, 204)
Variable Name: BlueSky

HEADING
Font: Inter Bold
Size: 24px
Line Height: 130% (31.2px)
Variable Name: HeadingL
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
    },
    'successGreen': {
      hex: '#00AA44',
      rgb: { r: 0, g: 0.667, b: 0.267 },
      variable: 'Success'
    },
    'errorRed': {
      hex: '#EE3333',
      rgb: { r: 0.933, g: 0.2, b: 0.2 },
      variable: 'Error'
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

**Wenn User sagt:** "Erstelle einen Heading mit Primary Blue"

**Ich mache:**

```javascript
async function createHeadingWithToken(text, tokenName = 'headingL') {
  const heading = figma.createText();
  heading.characters = text;
  heading.name = `HEADING_${text}`;
  
  // Aus Stylesheet:
  const token = designTokens.typography[tokenName];
  
  // Font laden
  await figma.loadFontAsync({
    family: token.family,
    style: token.style
  });
  
  // ALLE Styles setzen:
  heading.fontSize = token.size;
  heading.setRangeFontName(0, heading.characters.length, {
    family: token.family,
    style: token.style
  });
  heading.lineHeight = token.lineHeight;
  
  // Farbe (z.B. Primary Blue):
  heading.fills = [{
    type: 'SOLID',
    color: designTokens.colors.primaryBlue.rgb
  }];
  
  return heading;
}

// Nutzen:
const myHeading = await createHeadingWithToken('Welcome to My App');
```

**Ergebnis:**
- ✅ Text mit korrekter Größe, Font, Farbe
- ✅ Alle Styles aus dem Stylesheet
- ✅ BEREIT zur manuellen Variable-Verknüpfung

---

### Schritt 5️⃣: User verknüpft manuell mit Variablen

**Nach ich die Elemente erstellt habe:**

```
Claude hat erstellt:
  ✓ Heading "Welcome" - 24px, Inter Bold, #3366CC
  ✓ Button Text "Click Me" - 14px, Inter Regular, #3366CC

User verknüpft dann manuell in Figma:
  1. Select Heading
  2. Text Properties → Fill
  3. Choose Variable → BlueSky ✓
  
  4. Select Button Text
  5. Text Properties → Fill
  6. Choose Variable → BlueSky ✓
  
  7. Fertig! ✓
```

---

## 📐 Template: Design Token Stylesheet

**Kopiere diesen Frame in deine Figma-Datei:**

```
═══════════════════════════════════════════════════════════
                    DESIGN TOKENS
═══════════════════════════════════════════════════════════

COLORS
───────────────────────────────────────────────────────────
Name: Primary Blue
Hex: #3366CC
RGB: 51, 102, 204
Variable: BlueSky
Description: Primary brand color

Name: Success Green
Hex: #00AA44
RGB: 0, 170, 68
Variable: Success
Description: Success/positive color

Name: Error Red
Hex: #EE3333
RGB: 238, 51, 51
Variable: Error
Description: Error/negative color

Name: Neutral Gray
Hex: #666666
RGB: 102, 102, 102
Variable: TextPrimary
Description: Primary text color

Name: Light Background
Hex: #F5F5F5
RGB: 245, 245, 245
Variable: BGLight
Description: Light background

TYPOGRAPHY
───────────────────────────────────────────────────────────
Name: Heading Large
Font: Inter Bold
Size: 24px
Line Height: 130% (31.2px)
Variable: HeadingL
Description: Page titles

Name: Heading Medium
Font: Inter Bold
Size: 20px
Line Height: 130% (26px)
Variable: HeadingM
Description: Section titles

Name: Body
Font: Inter Regular
Size: 14px
Line Height: 150% (21px)
Variable: Body
Description: Regular text content

Name: Caption
Font: Inter Regular
Size: 12px
Line Height: 140% (16.8px)
Variable: Caption
Description: Small text, metadata

SPACING
───────────────────────────────────────────────────────────
Name: Large Spacing
Value: 32px
Variable: Spacing-L
Description: Page/section margins

Name: Medium Spacing
Value: 16px
Variable: Spacing-M
Description: Component margins

Name: Small Spacing
Value: 8px
Variable: Spacing-S
Description: Internal padding

Name: Extra Small Spacing
Value: 4px
Variable: Spacing-XS
Description: Micro spacing

═══════════════════════════════════════════════════════════
```

---

## ✅ Checkliste für diesen Workaround

**Bevor User mir Styles zeigt:**
- [ ] Stylesheet Frame erstellt
- [ ] Alle Farben dokumentiert (Name + Hex)
- [ ] Alle Typographie dokumentiert (Font, Size, Weight, Line-Height)
- [ ] Alle Spacing-Werte dokumentiert
- [ ] Variable-Namen dokumentiert (optional)

**Wenn ich Elemente erstelle:**
- [ ] Alle Werte aus Stylesheet gelesen
- [ ] Fonts geladen bevor Text gesetzt
- [ ] Alle Properties gesetzt (nicht nur Größe!)
- [ ] Konsistent über alle Elemente
- [ ] Screenshot gemacht zur Verifizierung

**Nach Erstellung:**
- [ ] User verifiziert Styles optisch
- [ ] User verknüpft mit Variablen (manuell)
- [ ] Fertig! 🎉

---

## 🎯 Vorteile dieses Workflows

| Aspekt           | Vorteil                                          |
| ---------------- | ------------------------------------------------ |
| **Konsistenz**   | Alle Elemente nutzen gleiche Styles              |
| **Flexibilität** | User kontrolliert Variable-Verknüpfung           |
| **Effizienz**    | Schneller als manuell, keine Variable-API-Limits |
| **Wartbarkeit**  | Stylesheet ist zentrale Referenz                 |
| **Skalierbar**   | Funktioniert für beliebig viele Elemente         |

---

**Version:** 1.0  
**Status:** Praktisch & empfohlen  
**Getestet:** 31.05.2026