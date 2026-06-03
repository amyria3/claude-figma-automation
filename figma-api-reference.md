# ✅ Figma API Reference für Claude
**Alle Funktionen validiert + ALLE Limitations dokumentiert**

**Version:** 2.5  
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

### `resize()` setzt Höhe auf FIXED
Nach `node.resize(w, h)` ist `textAutoResize` auf `"NONE"` gesetzt — der Text bricht nicht mehr automatisch um und die Höhe passt sich nicht an. Für Textknoten die sich an den Inhalt anpassen sollen:
```javascript
node.resize(width, node.height);         // Breite fixieren
node.textAutoResize = "HEIGHT";          // Höhe hug't Inhalt
// oder:
node.textAutoResize = "WIDTH_AND_HEIGHT"; // Breite und Höhe hug't Inhalt
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

### `gridItemsPositioning` — Auto vs Manual
```javascript
// ✅ ROW_AUTO_FLOW: Kinder werden automatisch in Zeilen platziert (Standard)
frame.gridItemsPositioning = "ROW_AUTO_FLOW";

// ⚠️ MANUAL: Jedes Kind braucht setGridChildPosition() — häufig unerwünschte Nebeneffekte
frame.gridItemsPositioning = "MANUAL";
child.setGridChildPosition(0, 0); // (rowIndex, columnIndex)
```
**Empfehlung:** `ROW_AUTO_FLOW` verwenden — Kinder werden in Reihenfolge automatisch platziert.

### Grid-Frame Höhe — `counterAxisSizingMode`
```javascript
frame.primaryAxisSizingMode = "FIXED";  // Breite fix
frame.counterAxisSizingMode = "AUTO";   // ✅ Höhe hug't Inhalt (ROW_AUTO_FLOW nötig)
frame.counterAxisSizingMode = "FIXED";  // ❌ Höhe bleibt fix — Inhalt kann überlaufen
```

### Vollsize Grid-Frame mit Padding (bevorzugtes Muster)
Statt einem kleinen zentrierten Inner-Frame: Grid-Frame in voller Slide-Größe mit Padding als Margin.
```javascript
// ✅ Sauber: Grid füllt den ganzen Slide, Padding erzeugt Abstand
frame.layoutMode = "GRID";
frame.resize(874, 595);          // Slide-Größe
frame.paddingTop = 78;
frame.paddingBottom = 78;
frame.paddingLeft = 78;
frame.paddingRight = 78;
frame.primaryAxisSizingMode = "FIXED";
frame.counterAxisSizingMode = "FIXED";
frame.x = 0; frame.y = 0;

// ❌ Umständlich: kleiner Inner-Frame muss manuell zentriert werden
inner.x = Math.round((slideW - inner.width) / 2);
inner.y = Math.round((slideH - inner.height) / 2);
```

### Rotierter Text als direktes Grid-Kind
Text-Nodes können direkt Grid-Kinder sein (kein Wrapper-Frame nötig). Position: x:0, y:[textWidth], rotation:90.
```javascript
const heading = figma.createText();
heading.characters = "INHALT";
heading.fontSize = 63.6;
grid.appendChild(heading);

// Nach appendChild: y = original text width, rotation 90°
heading.x = 0;
heading.y = heading.width;  // y = Textbreite (vor Rotation)
heading.rotation = 90;
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
```javascript
console.log(frame.gridColumnSizingCSS); // ✅ lesen zur Verifikation
frame.gridColumnSizingCSS = "...";      // ❌ read-only
```

### Alignment für Grid-Kinder
```javascript
child.gridChildHorizontalAlign = "AUTO"; // ✅ MIN | CENTER | MAX | AUTO
child.gridChildHorizontalAlign = "STRETCH"; // ❌ wirft Fehler
```

### `layoutSizingHorizontal` für Grid-Kinder
```javascript
child.layoutSizingHorizontal = "FILL"; // ❌ wirft Fehler für Grid-Kinder
// ✅ Breite über gridColumnSizes im Parent steuern
```

---

## ⚠️ WICHTIGE LIMITATIONS

- ❌ `console.log()` — Claude sieht das nicht
- ❌ `figma.notify()` — User sieht das nicht
- ❌ `figma.root.appendChild()` — stattdessen `page.appendChild()`
- ❌ Variables — komplett blockiert
- ❌ `layoutSizingHorizontal` für Grid-Kinder
- ❌ `clipsContent` nicht als Default setzen — nur explizit wenn nötig
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
| Grid ROW_AUTO_FLOW | ✅ | 03.06.2026 |
| Grid Vollsize + Padding | ✅ | 03.06.2026 |
| Variables | ❌ | 31.05.2026 |
