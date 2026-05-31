# Technischer Workflow: Claude + Figma MCP Zuverlässig Nutzen

**Status:** Best Practice basierend auf echten Tests (Mai 2026)  
**Autor:** Claude + Nutzer Feedback  
**Ziel:** Figma-Dateien fehlerfreie in Echtzeit bearbeiten

---

## 🎯 Kernprinzip

**Das Aktive Figma-Tab ist der echte Zielort** – nicht der `fileKey`. Der `fileKey` ist nur eine Referenz. Die API spricht immer mit dem Tab, das der User gerade offen hat.

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
  // Alle im Node verwendeten Fonts sammeln
  const fonts = new Set();
  
  for (let i = 0; i < node.characters.length; i++) {
    const fontRef = node.getRangeFontName(i, i + 1);
    
    if (typeof fontRef === "object" && fontRef.family) {
      fonts.add(JSON.stringify(fontRef));
    }
  }
  
  // Jeden Font laden (mit Try-Catch für fehlerhafte Fonts)
  for (const fontStr of fonts) {
    try {
      const fontObj = JSON.parse(fontStr);
      await figma.loadFontAsync(fontObj);
      console.log(`✓ Loaded: ${fontObj.family} ${fontObj.style}`);
    } catch (e) {
      console.log(`⚠ Failed to load: ${fontStr}`);
    }
  }
}
```

### Aggressive Fallback (Bei kaputten Fonts)
```javascript
async function setTextSafely(node, newText) {
  // 1. Alle aktuellen Fonts laden
  await loadAllFontsInNode(node);
  
  // 2. Wenn das fehlschlägt: Fallback-Font auf ganzen Range
  try {
    await figma.loadFontAsync({ family: "Inter", style: "Regular" });
    node.setRangeFontName(0, node.characters.length, {
      family: "Inter",
      style: "Regular"
    });
  } catch (e) {
    console.log("⚠ Inter auch nicht verfügbar");
  }
  
  // 3. JETZT Text setzen
  node.characters = newText;
}
```

---

## 3️⃣ TEXT ÄNDERN (Workflow)

### Sichere Batch-Operation
```javascript
async function batchUpdateTexts(updates) {
  // updates = [{ nodeId: "...", oldText: "...", newText: "..." }]
  
  // SCHRITT 1: Alle Fonts präventiv laden
  for (const update of updates) {
    const node = figma.getNodeById(update.nodeId);
    if (node && node.type === 'TEXT') {
      await loadAllFontsInNode(node);
    }
  }
  
  // SCHRITT 2: Updates durchführen
  let changedCount = 0;
  for (const update of updates) {
    try {
      const node = figma.getNodeById(update.nodeId);
      
      if (node && node.type === 'TEXT') {
        const oldText = node.characters;
        const newText = oldText.replace(update.oldText, update.newText);
        
        if (oldText !== newText) {
          node.characters = newText;
          changedCount++;
          
          // Feedback für User (sichtbar in Figma!)
          figma.notify(`✓ Updated: "${newText.substring(0, 50)}"`, { timeout: 3000 });
        }
      }
    } catch (e) {
      figma.notify(`✗ Error: ${e.message}`, { timeout: 5000 });
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
// Nach Update:
Figma:get_metadata(fileKey, nodeId)
      ↓
      Zeigt aktuelle XML mit Text-Content
      ↓
      Claude überprüft: Hat sich der Text wirklich geändert?
```

### ❌ NICHT FUNKTIONIERT: figma.notify
```javascript
figma.notify("✓ 5 Texte aktualisiert", { timeout: 15000 });
// ❌ User sieht das NICHT in Figma-UI!
// Deshalb: NICHT verwenden!
```

### ✅ Und richtig: User-Bestätigung
```
Claude: "Neu laden (F5) und schau, ob 'Misha Weber' zu 'Maria' geändert wurde"
User:   "Ja, ich sehe es!" oder "Nein, immer noch alt"
```

---

## 5️⃣ KOMPLETTER WORKFLOW (Praktisches Beispiel)

### Aufgabe: "Ersetze 'Misha Weber' durch 'Maria Arkadieff' überall"

```
SCHRITT 1: PRE-FLIGHT
├─ get_metadata() → Server läuft? ✅
├─ User: "Öffne Maria Arkadieff Datei"
└─ Test-Write durchführen

SCHRITT 2: ANALYSE
├─ Alle Text-Nodes durchlaufen
├─ Suche nach "Misha Weber"
└─ Sammle NodeIds und Positionen

SCHRITT 3: FONTS LADEN
├─ Für jeden betroffenen Node:
│  └─ loadAllFontsInNode(node)
└─ Bei Fehlern: Aggressive Fallback

SCHRITT 4: UPDATES DURCHFÜHREN
├─ node.characters = newText
├─ figma.notify() für Feedback
└─ changedCount sammeln

SCHRITT 5: VERIFIZIERUNG
├─ get_metadata() auf sample Nodes
├─ User: "Neu laden und überprüfen"
└─ User bestätigt: ✅ Oder ❌ Fallback
```

---

## 6️⃣ ERROR HANDLING

| Fehler                                    | Ursache             | Lösung                                        |
| ----------------------------------------- | ------------------- | --------------------------------------------- |
| "Cannot write to node with unloaded font" | Font nicht geladen  | `loadFontAsync()` vor `node.characters = ...` |
| "Cannot unwrap symbol"                    | Custom Font kaputt  | Aggressive Fallback zu Inter verwenden        |
| "This resource couldn't be accessed"      | Falsches Tab aktiv  | User Tab wechseln lassen + erneut versuchen   |
| "No response from get\_metadata"          | API antwortet nicht | MCP Server down → Chrome-Automation versuchen |
| Text ändert sich nicht sichtbar           | Browser-Cache       | User: F5 oder Datei zu/auf                    |

---

## 7️⃣ WORKFLOW FÜR MEHRSPRACHIGE DATEIEN (DE/EN)

```
1. Quell-Datei (z.B. Misha DE) → get_metadata(fileKey_DE)
   ├─ Identifiziere alle Texte
   └─ Speichere: nodeId → Content

2. User: "Wechsel zu Ziel-Datei (Misha EN)"

3. Ziel-Datei → get_metadata(fileKey_EN)
   ├─ Vergleiche Struktur mit Quell-Datei
   ├─ Identifiziere Unterschiede
   └─ Batch-Update erstellen

4. Führe Updates durch:
   ├─ Fonts laden (für EN-Datei)
   ├─ Text-Updates batchen (5-10 Nodes pro Batch)
   ├─ figma.notify() nach jedem Batch
   └─ get_metadata() zur Verifizierung

5. User-Bestätigung:
   ├─ "Schau auf EN-Datei"
   └─ "Sieht das Update so aus?"
```

---

## 8️⃣ CHECKLISTE FÜR CLAUDE (Vor jeder Figma-Task)

- [ ] `get_metadata()` aufgerufen → Server läuft?
- [ ] User aufgefordert, richtiges Tab zu öffnen?
- [ ] Test-Operation durchgeführt?
- [ ] User bestätigt: "Test funktioniert"?
- [ ] Alle Fonts mit `getRangeFontName()` identifiziert?
- [ ] `loadFontAsync()` für JEDEN Font?
- [ ] Nach Update: `get_metadata()` zur Verifizierung?
- [ ] User aufgefordert: "Neu laden und schauen"?
- [ ] User bestätigt Änderung oder meldet Fehler?
- [ ] **KEIN "Fertig!" ohne User-Bestätigung!**

---

## 9️⃣ FALLBACK-STRATEGIE (Wenn API nicht schreiben darf)

Falls nach all dem:
- ❌ Test-Write schlägt fehl
- ❌ Fonts laden fehlschlag
- ❌ Keine Veränderung sichtbar

**Dann:**
1. Versuche **Claude in Chrome** (Browser-Automation)
2. Falls auch das nicht geht: **User macht es manuell** mit Figmas Find & Replace (Ctrl+H)

---

## 🔟 EFFICIENCY TIPS

| Aktion                 | Zeit  | Best Practice                          |
| ---------------------- | ----- | -------------------------------------- |
| Single Text Change     | \~2s  | Direkt, kein Batchen nötig             |
| 3-5 Text Changes       | \~5s  | Batch, 1 Font-Load                     |
| 10+ Text Changes       | \~15s | Multi-Batch, pro Batch 2-3 Tests       |
| Übersetzen (20+ Nodes) | \~30s | Frame-by-Frame, nicht alles auf einmal |

---

## 📋 SUMMARY: Die 5 Goldenen Regeln

1. **Aktives Tab zuerst** – User muss die Datei offen haben
2. **Fonts sind das Hauptproblem** – `getRangeFontName()` + `loadFontAsync()` ist nicht optional
3. **Console.log ist unsichtbar** – `get_metadata()` zur Verifizierung nutzen (NICHT figma.notify())
4. **Verifizieren, nicht vertrauen** – Nach jedem Update User fragen: "Siehst du die Änderung?"
5. **Kein "Fertig" ohne Beweis** – Erst bestätigen, dann weitermachen

### ⚠️ Zusatz: Was NICHT funktioniert
- ❌ Variables erstellen/bearbeiten (Figma erlaubt das aktuell nicht via MCP)
- ❌ console.log() als Feedback (unsichtbar)
- ❌ figma.notify() (User sieht das nicht)
- ❌ Return-Values aus use\_figma (kommen nicht an)

---

**Version:** 1.1  
**Letzte Aktualisierung:** Mai 31, 2026  
**Status:** Produktionsreif – Alle Limitations dokumentiert