# Technischer Workflow: Claude + Figma MCP Zuverlässig Nutzen

**Status:** Best Practice basierend auf echten Tests (Mai 2026, aktualisiert Juli 2026)  
**Autor:** Claude + Nutzer Feedback  
**Ziel:** Figma-Dateien fehlerfrei in Echtzeit bearbeiten

---

## 🎯 Kernprinzip (aktualisiert 15.07.2026)

**Beim Remote-MCP (`use_figma` via Figma-Connector) ist der `fileKey` der echte Zielort.** Die Datei muss **nicht** in Figma geöffnet sein — der Remote-Server arbeitet serverseitig. Setup & Details: `figma-schreibzugriff-use_figma.md`.

> **Legacy-Hinweis:** Die frühere Regel „Das aktive Figma-Tab ist der echte Zielort, der fileKey nur Referenz" galt für den **lokalen Dev-Mode-Server** (127.0.0.1:3845, nur Lesen). Für `use_figma` gilt sie nicht mehr.

### `setCurrentPageAsync()` — Seitenwechsel per Code

Claude kann per Code die aktive Seite wechseln, unabhängig davon, welche Seite der User gerade geöffnet hat:

```javascript
const page = figma.root.children.find(p => p.name === "CV EN");
await figma.setCurrentPageAsync(page);
// Ab hier arbeitet Claude auf dieser Seite — auch ohne User-Aktion
```

**Konsequenzen:**
- Claude kann Seiten bearbeiten, die der User gerade nicht sieht
- Hat der User die Datei offen, sieht er ggf. einen plötzlichen Seitenwechsel — das kann verwirren
- **Der Seitenkontext resettet zwischen `use_figma`-Aufrufen** auf die erste Seite — pro Aufruf max. **einmal** wechseln; Multi-Page-Arbeit auf parallele Aufrufe aufteilen
- Der Sync-Setter `figma.currentPage = page` funktioniert in `use_figma` **nicht** (wirft Fehler) — immer die Async-Variante

---

## 1️⃣ PRE-FLIGHT CHECKLIST (Vor jeder Bearbeitung)

### A) Server-Status überprüfen
```
Claude → Figma:get_metadata(fileKey=...)
         ↓
         Antwortet mit XML? → ✅ API läuft
         Error? → ❌ API nicht verfügbar
```

### B) Ziel-Datei verifizieren
**Remote-MCP (`use_figma`):** Datei-URL bzw. `fileKey` von der Userin geben lassen und mit `get_metadata` gegenprüfen. Kein offenes Tab nötig.  
**Legacy (lokaler Dev-Mode-Server):** Richtiges Figma-Tab aktivieren lassen und verifizieren.

### C) Test-Operation durchführen
```javascript
// IMMER zuerst einen Mini-Test (Font laden nicht vergessen!):
await figma.loadFontAsync({ family: "Inter", style: "Regular" });
const page = figma.currentPage; // ← Zur PAGE, nicht root!
const testNode = figma.createText();
testNode.characters = "[VERIFY_FIGMA_WRITE_WORKS]";
testNode.x = 200; testNode.y = -200; // weg von (0,0), nicht auf bestehenden Inhalt
page.appendChild(testNode);
return { createdNodeIds: [testNode.id] };
```

**User schaut nach:** Sehe ich `[VERIFY_FIGMA_WRITE_WORKS]` irgendwo in der Datei?  
- ✅ Ja → Weitermachen mit echten Edits (Test-Node danach wieder löschen!)
- ❌ Nein → Write-Permissions prüfen → Fallback-Strategie (unten)

---

## 2️⃣ FONT-LOADING (Das Hauptproblem)

### Standard-Pattern (Sicher)
```javascript
async function loadAllFontsInNode(node) {
  // getStyledTextSegments liefert alle Fonts im Node — schneller als Zeichen-Loop
  const segments = node.getStyledTextSegments(['fontName']);
  for (const seg of segments) {
    try {
      await figma.loadFontAsync(seg.fontName);
    } catch (e) {
      // Font nicht verfügbar — Fallback nötig (siehe unten)
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
    // Inter auch nicht verfügbar — Abbruch melden via return
  }
  node.characters = newText;
}
```

---

## 3️⃣ TEXT ÄNDERN (Workflow)

### Sichere Batch-Operation
```javascript
async function batchUpdateTexts(updates) {
  // getNodeById (sync) ist deprecated und wirft in use_figma Fehler — immer die Async-Variante!
  for (const update of updates) {
    const node = await figma.getNodeByIdAsync(update.nodeId);
    if (node && node.type === 'TEXT') await loadAllFontsInNode(node);
  }
  
  let changedCount = 0;
  const errors = [];
  for (const update of updates) {
    try {
      const node = await figma.getNodeByIdAsync(update.nodeId);
      if (node && node.type === 'TEXT') {
        const newText = node.characters.replace(update.oldText, update.newText);
        if (node.characters !== newText) {
          node.characters = newText;
          changedCount++;
        }
      }
    } catch (e) {
      errors.push(update.nodeId + ": " + e.message); // NICHT console.log — unsichtbar!
    }
  }
  
  return { changedCount, errors };
}
```

---

## 4️⃣ VERIFIZIERUNG (Nicht via console.log!)

### ❌ Falsch: Console.log
```javascript
console.log("Update fertig"); // Claude sieht das NICHT!
```

### ✅ Richtig: return-Wert (use_figma)
```javascript
return { changedCount: 5, nodeIds: [...] }; // Claude sieht NUR den return-Wert
```

### ✅ Richtig: get_metadata / Screenshot
```javascript
Figma:get_metadata(fileKey, nodeId)  // Struktur als XML
await node.screenshot()              // visueller Check direkt im use_figma-Aufruf
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
| "Setting figma.currentPage is not supported" | Sync-Setter benutzt | `await figma.setCurrentPageAsync(page)` |
| "This resource couldn't be accessed" | Remote: fileKey falsch / keine Berechtigung. Legacy: falsches Tab aktiv | fileKey prüfen bzw. User Tab wechseln lassen |
| "No response from get_metadata" | API antwortet nicht | Connector-Verbindung / MCP Server prüfen |
| Text ändert sich nicht sichtbar | Browser-Cache | User: F5 oder Datei zu/auf |

---

## 6️⃣ FALLBACK-STRATEGIE

Falls API nicht schreibt:
1. **Figma-Connector neu verbinden** (siehe `figma-schreibzugriff-use_figma.md`, Entscheidungsbaum)
2. **Claude Code via Desktop Commander** (Weg 2 in derselben Doku)
3. **Claude in Chrome** (Browser-Automation)
4. **User manuell** mit Figmas Find & Replace (Ctrl+H)

---

## 📋 SUMMARY: Die 5 Goldenen Regeln

1. **fileKey zählt (Remote-MCP)** – Datei muss nicht offen sein; Seite wechselt Claude per `setCurrentPageAsync()` (max. 1× pro Aufruf)
2. **Fonts sind das Hauptproblem** – `getStyledTextSegments(['fontName'])` + `loadFontAsync()` ist nicht optional
3. **Console.log ist unsichtbar** – `return`-Wert bzw. `get_metadata()` zur Verifizierung nutzen
4. **Verifizieren, nicht vertrauen** – Nach jedem Update prüfen (Screenshot, Metadata oder User)
5. **Kein "Fertig" ohne Beweis** – Erst bestätigen, dann weitermachen

### ⚠️ Was NICHT funktioniert
- ❌ console.log() als Feedback
- ❌ figma.notify() (wirft "not implemented")
- ❌ `figma.getNodeById()` / `getLocalVariableCollections()` (sync) — Async-Varianten nutzen
- ✅ ~~Variables erstellen/bearbeiten~~ **funktioniert seit `use_figma`** (früher ❌) — siehe `figma-api-reference.md`

---

**Version:** 2.0  
**Letzte Aktualisierung:** 15.07.2026  
**Status:** Produktionsreif – an Remote-MCP (`use_figma`) angepasst
