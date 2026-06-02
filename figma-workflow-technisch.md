# Technischer Workflow: Claude + Figma MCP Zuverlässig Nutzen

**Status:** Best Practice basierend auf echten Tests (Mai 2026)  
**Autor:** Claude + Nutzer Feedback  
**Ziel:** Figma-Dateien fehlerfreie in Echtzeit bearbeiten

---

## 🎯 Kernprinzip

**Das Aktive Figma-Tab ist der echte Zielort** – nicht der `fileKey`. Der `fileKey` ist nur eine Referenz. Die API spricht immer mit dem Tab, das der User gerade offen hat.

### ⚠️ Ausnahme: `setCurrentPageAsync()` — Tab-unabhängiger Seitenwechsel

Claude kann per Code die aktive Seite wechseln, **unabhängig davon, welche Seite der User gerade geöffnet hat**:

```javascript
const page = figma.root.children.find(p => p.name === "CV EN");
await figma.setCurrentPageAsync(page);
// Ab hier arbeitet Claude auf dieser Seite — auch ohne User-Aktion
```

**Konsequenzen:**
- Claude kann Seiten bearbeiten, die der User gerade nicht sieht
- Der User sieht in Figma einen plötzlichen Seitenwechsel — das kann verwirren
- Die Datei muss geöffnet sein, aber nicht die spezifische Seite

**Wann verwenden:**
- Wenn Claude explizit auf eine bestimmte Seite zugreifen soll (z.B. "Passe die Short EN an")
- Wenn mehrere Seiten in einem Durchgang bearbeitet werden

**Wann NICHT verwenden:**
- Wenn der User gerade auf einer Seite arbeitet und Claude nur einen kleinen Fix machen soll — dann lieber die aktive Seite lassen und den User darauf hinweisen

---

## 1️⃣ PRE-FLIGHT CHECKLIST (Vor jeder Bearbeitung)

### A) Server-Status überprüfen
```
Claude → Figma:get_metadata(fileKey=...)
         ↓
         Antwortet mit XML? → ✅ API läuft
         Error? → ❌ API nicht verfügbar
```

### B) Richtiges Tab aktivieren
**User:** Öffne das Figma-Tab mit der Datei, die ich bearbeiten soll  
**Claude:** Verifiziere mit `get_metadata` dass das richtige Tab aktiv ist

### C) Test-Operation durchführen
```javascript
// IMMER zuerst einen Mini-Test:
const page = figma.root.children[0]; // ← WICHTIG: Zur PAGE, nicht root!
const testNode = figma.createText();
testNode.characters = "[VERIFY_FIGMA_WRITE_WORKS]";
page.appendChild(testNode);
```

**User schaut nach:** Sehe ich `[VERIFY_FIGMA_WRITE_WORKS]` irgendwo in der Datei?  
- ✅ Ja → Weitermachen mit echten Edits
- ❌ Nein → API hat keine Write-Permissions → Fallback zu manueller Bearbeitung

---

## 2️⃣ FONT-LOADING (Das Hauptproblem)

### Standard-Pattern (Sicher)
```javascript
async function loadAllFontsInNode(node) {
  const fonts = new Set();
  
  for (let i = 0; i < node.characters.length; i++) {
    const fontRef = node.getRangeFontName(i, i + 1);
    if (typeof fontRef === "object" && fontRef.family) {
      fonts.add(JSON.stringify(fontRef));
    }
  }
  
  for (const fontStr of fonts) {
    try {
      const fontObj = JSON.parse(fontStr);
      await figma.loadFontAsync(fontObj);
    } catch (e) {
      console.log(`⚠ Failed to load: ${fontStr}`);
    }
  }
}
```

### Aggressive Fallback (Bei kaputten Fonts)
```javascript
async function setTextSafely(node, newText) {
  await loadAllFontsInNode(node);
  
  try {
    await figma.loadFontAsync({ family: "Inter", style: "Regular" });
    node.setRangeFontName(0, node.characters.length, { family: "Inter", style: "Regular" });
  } catch (e) {
    console.log("⚠ Inter auch nicht verfügbar");
  }
  
  node.characters = newText;
}
```

---

## 3️⃣ TEXT ÄNDERN (Workflow)

### Sichere Batch-Operation
```javascript
async function batchUpdateTexts(updates) {
  for (const update of updates) {
    const node = figma.getNodeById(update.nodeId);
    if (node && node.type === 'TEXT') await loadAllFontsInNode(node);
  }
  
  let changedCount = 0;
  for (const update of updates) {
    try {
      const node = figma.getNodeById(update.nodeId);
      if (node && node.type === 'TEXT') {
        const newText = node.characters.replace(update.oldText, update.newText);
        if (node.characters !== newText) {
          node.characters = newText;
          changedCount++;
        }
      }
    } catch (e) {
      console.log(`Error: ${e.message}`);
    }
  }
  
  return changedCount;
}
```

---

## 4️⃣ VERIFIZIERUNG (Nicht via console.log!)

### ❌ Falsch: Console.log
```javascript
console.log("Update fertig"); // Claude sieht das NICHT!
```

### ✅ Richtig: get\_metadata
```javascript
Figma:get_metadata(fileKey, nodeId)
// Zeigt aktuelle XML mit Text-Content
```

### ✅ Richtig: User-Bestätigung
```
Claude: "Schau ob sich X geändert hat"
User:   "Ja" oder "Nein"
```

---

## 5️⃣ ERROR HANDLING

| Fehler | Ursache | Lösung |
| --- | --- | --- |
| "Cannot write to node with unloaded font" | Font nicht geladen | `loadFontAsync()` vor `node.characters = ...` |
| "Cannot unwrap symbol" | Custom Font kaputt | Aggressive Fallback zu Inter |
| "This resource couldn't be accessed" | Falsches Tab aktiv | User Tab wechseln lassen |
| "No response from get\_metadata" | API antwortet nicht | MCP Server down |
| Text ändert sich nicht sichtbar | Browser-Cache | User: F5 oder Datei zu/auf |

---

## 6️⃣ FALLBACK-STRATEGIE

Falls API nicht schreibt:
1. **Claude in Chrome** (Browser-Automation)
2. **User manuell** mit Figmas Find & Replace (Ctrl+H)

---

## 📋 SUMMARY: Die 5 Goldenen Regeln

1. **Aktives Tab zuerst** – Datei muss offen sein; Seite kann Claude per `setCurrentPageAsync()` selbst wechseln
2. **Fonts sind das Hauptproblem** – `getRangeFontName()` + `loadFontAsync()` ist nicht optional
3. **Console.log ist unsichtbar** – `get_metadata()` zur Verifizierung nutzen
4. **Verifizieren, nicht vertrauen** – Nach jedem Update User fragen
5. **Kein "Fertig" ohne Beweis** – Erst bestätigen, dann weitermachen

### ⚠️ Was NICHT funktioniert
- ❌ Variables erstellen/bearbeiten
- ❌ console.log() als Feedback
- ❌ figma.notify() (User sieht das nicht)

---

**Version:** 1.2  
**Letzte Aktualisierung:** 02.06.2026  
**Status:** Produktionsreif – Alle Limitations dokumentiert
