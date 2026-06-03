# ✅ Figma API Reference für Claude
**Alle Funktionen validiert + ALLE Limitations dokumentiert**

**Version:** 2.4  
**Status:** Production Ready  
**Überprüft am:** 31.05.2026 / 03.06.2026

---

## 🔬 VARIABLES: KOMPLETT BLOCKIERT ⚠️

**Getestet am:** 31.05.2026  
**Ergebnis:** Figma blockiert ALLE Variable-Operationen via MCP

### Was funktioniert ✅
```javascript
const collection = figma.variables.createVariableCollection('MyVariables');
const collections = figma.variables.getLocalVariableCollections();
const variables = figma.variables.getLocalVariables();
variables.forEach(v => console.log(v.name, v.resolvedType));
```

### Was NICHT funktioniert ❌
- ❌ Variablen erstellen
- ❌ Variable-Werte auslesen
- ❌ Variablen mit Nodes verknüpfen
- ❌ Variable-Binding in fills

### Workaround
Siehe `figma-stylesheet-workaround.md`

---

## 1️⃣ TEXT OPERATIONEN (✅ FUNKTIONIERT)

### Text ändern
```javascript
async function updateText(nodeId, newContent) {
  const node = figma.getNodeById(nodeId);
  if (!node || node.type !== 'TEXT') return;
  const fontRef = node.getRangeFontName(0, 1);
  await figma.loadFontAsync({ family: fontRef?.family || 'Inter', style: fontRef?.style || 'Regular' });
  node.characters = newContent;
}
```

### Alle Typography-Properties kopieren
```javascript
async function copyAllTypography(source, target) {
  const font = source.getRangeFontName(0, 1);
  await figma.loadFontAsync({ family: font?.family || 'Inter', style: font?.style || 'Regular' });
  target.fontSize = source.fontSize;
  target.lineHeight = source.lineHeight;
  target.letterSpacing = source.letterSpacing;
  target.textCase = source.textCase;
  target.textDecoration = source.textDecoration;
  target.textAlignHorizontal = source.textAlignHorizontal;
  target.setRangeFontName(0, target.characters.length, { family: font?.family || 'Inter', style: font?.style || 'Regular' });
  if (source.fills?.length > 0) target.fills = JSON.parse(JSON.stringify(source.fills));
}
```

---

## 2️⃣ FLEX-LAYOUT OPERATIONEN (✅ FUNKTIONIERT)

### Flex Frame erstellen
```javascript
const frame = figma.createFrame();
frame.layoutMode = 'VERTICAL'; // oder 'HORIZONTAL'
frame.itemSpacing = 16;
frame.paddingLeft = 20; frame.paddingRight = 20;
frame.paddingTop = 20; frame.paddingBottom = 20;
frame.primaryAxisAlignItems = 'MIN';
frame.counterAxisAlignItems = 'CENTER';
page.appendChild(frame);
```

### Kind zu Flex hinzufügen (Reihenfolge wichtig!)
```javascript
// ERST appendChild, DANN layoutSizing setzen
frame.appendChild(item);
item.layoutSizingHorizontal = 'FILL';
item.layoutSizingVertical = 'FIXED';
```

---

## 3️⃣ GRID LAYOUT (✅ FUNKTIONIERT — Eigenheiten beachten)

**Getestet am:** 03.06.2026

### Korrekte Reihenfolge (zwingend einhalten)

```javascript
frame.layoutMode = "GRID";
frame.gridColumnCount = 2;       // 1. erst Anzahl
frame.gridRowCount = 1;          // 2. erst Anzahl
frame.gridColumnSizes = [...];   // 3. dann Größen
frame.gridRowSizes = [...];      // 4. dann Größen
frame.gridColumnGap = 40;
frame.gridRowGap = 0;
```

### Erlaubte Typen für `gridColumnSizes` / `gridRowSizes`

```javascript
// ✅ Erlaubt:
{ type: "FLEX", value: 1 }    // 1fr
{ type: "FIXED", value: 42 }  // feste Pixelbreite
{ type: "HUG" }               // fit-content

// ❌ Nicht erlaubt (wirft Fehler):
{ type: "MIN_CONTENT" }
{ type: "STRETCH" }
```

### `gridColumnSizingCSS` ist read-only
Nur zur Verifikation lesbar — nie schreiben:
```javascript
console.log(frame.gridColumnSizingCSS); // ✅ "fit-content(100%) minmax(0,1fr)"
frame.gridColumnSizingCSS = "...";      // ❌ read-only, wirft Fehler
```

### Kind-Positionen setzen
`setGridChildPosition` erwartet zwei separate Integer — kein Objekt:
```javascript
child.setGridChildPosition(0, 0); // ✅ (rowIndex, columnIndex)
child.setGridChildPosition({ row: 0, column: 0 }); // ❌ wirft Fehler
```

### Alignment für Grid-Kinder
Erlaubte Werte: `"MIN" | "CENTER" | "MAX" | "AUTO"` — nicht `"STRETCH"`:
```javascript
child.gridChildHorizontalAlign = "AUTO"; // ✅
child.gridChildHorizontalAlign = "STRETCH"; // ❌ wirft Fehler
```

### Sizing für Grid-Kinder
`layoutSizingHorizontal` funktioniert **nicht** für Grid-Kinder — Breite wird über `gridColumnSizes` im Parent gesteuert:
```javascript
child.layoutSizingHorizontal = "FILL"; // ❌ wirft Fehler für Grid-Kinder
// ✅ Stattdessen: Spaltenbreite im Parent definieren:
frame.gridColumnSizes = [{ type: "HUG" }, { type: "FLEX", value: 1 }];
```

### Vollständiges Beispiel: 2-Spalten-Grid (fit-content + 1fr)
```javascript
const frame = figma.createFrame();
frame.layoutMode = "GRID";
frame.gridColumnCount = 2;
frame.gridRowCount = 1;
frame.gridColumnSizes = [{ type: "HUG" }, { type: "FLEX", value: 1 }];
frame.gridRowSizes = [{ type: "HUG" }];
frame.gridColumnGap = 40;
frame.gridRowGap = 0;

const left = figma.createFrame();
const right = figma.createFrame();
frame.appendChild(left);
frame.appendChild(right);

left.setGridChildPosition(0, 0);
right.setGridChildPosition(0, 1);
left.gridChildHorizontalAlign = "AUTO";
right.gridChildHorizontalAlign = "AUTO";
```

---

## ⚠️ WICHTIGE LIMITATIONS

- ❌ `console.log()` — Claude sieht das nicht
- ❌ `figma.notify()` — User sieht das nicht
- ❌ `figma.root.appendChild()` — stattdessen `page.appendChild()`
- ❌ Variables — komplett blockiert
- ❌ `layoutSizingHorizontal` für Grid-Kinder — über `gridColumnSizes` steuern
- ✅ Text ändern (mit Font-Loading vorher)
- ✅ Farben setzen und auslesen
- ✅ Flex- und Grid-Layouts erstellen
- ✅ `get_metadata()` zur Verifizierung

---

## ✅ VERIFIZIERUNG

| Feature | Status | Datum |
|---|---|---|
| Text-Änderung | ✅ | 31.05.2026 |
| Font-Loading | ✅ | 31.05.2026 |
| Flex-Layouts | ✅ | 31.05.2026 |
| Farben | ✅ | 31.05.2026 |
| Grid-Layout | ✅ | 03.06.2026 |
| Variables | ❌ | 31.05.2026 |
