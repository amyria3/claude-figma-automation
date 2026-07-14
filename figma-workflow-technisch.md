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

## 7️⃣ GITHUB WEB-EDITOR (CodeMirror) – Mehrzeilige Edits per Browser-Automation

**Kernproblem:** Simuliertes Tippen von mehrzeiligem Markdown-Text in GitHubs Web-Editor (CodeMirror 6) triggert bei jedem Enter die automatische Listen-Fortsetzung – dupliziert sich mit dem eigenen "- " im Text und kaskadiert über das ganze Dokument.

### ❌ Was NICHT funktioniert
- Zeichen für Zeichen tippen (inkl. Newlines) über simulierte Tastatur
- `navigator.clipboard.writeText()` aus injiziertem Skript (Timeout)
- `document.execCommand('copy')` aus injiziertem Skript (liefert `false`)
- Koordinaten von einem älteren Screenshot wiederverwenden, nachdem sich das Layout geändert hat (Gefahr: falscher Klick, z. B. "Cancel changes" statt "Commit changes")
- `.cm-line` Elemente abfragen, bevor sie durch echtes Scrollen ins Sichtfeld geholt wurden (CodeMirror rendert/virtualisiert Zeilen erst dann)

### ✅ Zuverlässiges Pattern
```javascript
// 1. Echtes Scrollen (Mausrad, kein scrollTop-Hack), bis Zielzeile sichtbar ist
// 2. Zielzeile per Textinhalt in .cm-line finden
const el = document.querySelector('.cm-content');
const target = Array.from(el.querySelectorAll('.cm-line'))
  .find(l => l.textContent.startsWith('## Zielueberschrift'));

// 3. Cursor per Selection/Range an den Zeilenanfang setzen
let node = target;
while (node.firstChild) node = node.firstChild;
const range = document.createRange();
range.setStart(node.nodeType === Node.TEXT_NODE ? node : target, 0);
range.collapse(true);
window.getSelection().removeAllRanges();
window.getSelection().addRange(range);

// 4. Text in einem Rutsch einfuegen -- bypassed die Enter-Listenfortsetzung
document.execCommand('insertText', false, mehrzeiligerText);
```

### Verifizierung
Sofort per JS nachlesen (`.cm-line` Texte vergleichen), nicht per Screenshot – Screenshots/`find`/`read_page` waren in der Ursprungssession zeitweise instabil, während `javascript_tool`-Aufrufe zuverlässig liefen.

**Quelle:** Claude (Cowork), Modell `claude-sonnet-5` – Erkenntnis aus echter Session, 2026-07-13.

---

## 8️⃣ Testlauf-Erkenntnisse: Component-Swap zwischen unterschiedlichen Button-Familien (14.07.2026)

**Kontext:** Test-Session auf Wunsch der Userin: zwei `Buttons / MD / PrimaryButton`-Instanzen im Frame "PRACTICE FOR CLAUDE" wurden zu `Buttons / MD / SecondaryButton` geswapt, Icon auf `ArrowUpOrDown` gewechselt, Label-Variable gewechselt, Interaktion angepasst. Mehrere neue, bisher nicht dokumentierte Verhaltensweisen kamen dabei zutage:

**a) Verschachtelte Icon-Instanz-Namen sind NICHT über Button-Familien hinweg konsistent.** `Buttons / MD / PrimaryButton` nutzt intern eine verschachtelte Instanz namens `Icons / ButtonIcons` (Variants: Cart/Delivery/Heart/Checkout/Log In). `Buttons / MD / SecondaryButton` nutzt für denselben visuellen Zweck ("Show Icon?"-Slot) eine strukturell und namentlich komplett andere Instanz: `Icons / CartLive` (ein Warenkorb-Badge-System mit Properties wie `Add to cart?`, `One Item?`, `Zero Items?`, `2 Items?`). Ein Icon-Swap-Skript, das den Namen aus einer Button-Familie fest annimmt (z.B. "Icons / ButtonIcons"), findet nach einem Wechsel auf eine andere Familie **keine passende Instanz** — der Swap schlägt still fehl (kein Error, aber `iconSwapResult` bleibt `null`), wenn nicht defensiv geprüft wird.
**How to apply:** Nach jedem Component-Swap zwischen unterschiedlichen Button-/Komponenten-Familien die verschachtelten Instanzen **neu per `findAllWithCriteria({ types: ['INSTANCE'] })` auflisten und den tatsächlichen Namen prüfen**, statt den Namen von einer anderen Familie zu übernehmen.

**b) Manche Component-Varianten bieten NUR EINEN Color-Mode-Wert — "Farbmodus ändern" ist dann technisch nicht möglich.** `Buttons / MD / SecondaryButton` hat als einzige Color-Mode-Property `color-mode: cole-tint-transparent ?` mit genau einer erlaubten Variante (`True`) — im Gegensatz zu `Buttons / MD / PrimaryButton`, das zwischen drei Modi wählen lässt (`cole-tint-warm-white`, `purple-tint-warm-white`, `cole-tint-snow-white`). Ein Auftrag wie "ändere den Farbmodus, wenn möglich" kann für SecondaryButton MD nur mit "nicht möglich, da nur ein Modus existiert" beantwortet werden — es gibt keine Alternative zum Auswählen.
**How to apply:** Vor einer Farbmodus-Änderung immer `componentPropertyDefinitions` der Zielkomponente (nicht der Quellkomponente) auf `variantOptions.length > 1` prüfen. Bei nur einer Option transparent kommunizieren statt zu versuchen, einen Modus zu erzwingen.

**c) CHANGE_TO-Reactions remappen automatisch auf die neue Komponente — jetzt auch über komplett unterschiedliche Component-Familien hinweg bestätigt.** Bereits dokumentiert war das automatische Ummappen von `CHANGE_TO`-Reactions innerhalb derselben Button-Familie (z.B. LG→MD). In diesem Test wurde bestätigt, dass es auch beim Sprung zwischen **strukturell verschiedenen** Component-Sets funktioniert: Ein `ON_HOVER`-Reaction, der ursprünglich auf die Hover-Variante von `Buttons / MD / PrimaryButton` zeigte, wurde nach dem Swap zu `SecondaryButton` automatisch auf die entsprechende Hover-Variante von `SecondaryButton` umgebogen — ohne eigenes Zutun.

**d) Reactions lassen sich NICHT direkt per Zuweisung setzen — `instance.reactions = [...]` ist nur lesbar.** Die funktionierende API ist `await instance.setReactionsAsync(reactionsArray)`. Eine reine Eigenschafts-Zuweisung wirft keinen Fehler, verändert aber auch nichts (oder wird gar nicht erst versucht, je nach Laufzeitverhalten) — immer die async Methode verwenden.
```javascript
const newReactions = instance.reactions.map(r =>
  r.trigger.type === 'ON_CLICK' ? { ...r, trigger: { type: 'ON_PRESS' } } : r
);
await instance.setReactionsAsync(newReactions); // ✅ einzig funktionierender Weg
```

**e) Figmas Plugin-API kennt keinen separaten "Touch"-Trigger.** Die vollständige `Trigger`-Union umfasst nur: `ON_CLICK`, `ON_HOVER`, `ON_PRESS`, `ON_DRAG`, `AFTER_TIMEOUT`, `MOUSE_ENTER`, `MOUSE_LEAVE`, `MOUSE_UP`, `MOUSE_DOWN`, `ON_KEY_DOWN`, `ON_MEDIA_HIT`, `ON_MEDIA_END`. "Click" ist der generische Tap-/Klick-Trigger für Maus **und** Touch-Geräte gleichermaßen — es gibt keine 1:1-Entsprechung für eine Anfrage wie "statt Click mach Touch". Bei einer solchen Anfrage sollte transparent nachgefragt werden, was gemeint ist (z.B. Wechsel zu `ON_PRESS` für Press-and-Hold, falls das inhaltlich gewünscht ist), statt stillschweigend etwas Falsches oder gar nichts zu ändern.

**f) `setBoundVariable('characters', ...)` schlägt bei kaputten Custom Fonts NICHT fehl — aber das sichtbare Rendering kann trotzdem hängen bleiben.** Bestätigt: Das Umbinden einer Text-Variable erfordert wie dokumentiert kein vorheriges `loadFontAsync()` und wirft auch bei einem defekten Font (hier: "BROWN NOW TWO", siehe [[feedback_figma_use_figma_gotchas]]) keinen Fehler — `textNode.characters` liest danach sofort korrekt den neuen Wert. **Neu und bisher nicht dokumentiert:** Der `get_screenshot`-Render zeigte in diesem Fall trotzdem weiterhin den ALTEN Text, auch nach mehrfachem erneutem Rendern. Ein expliziter Versuch, den Font per `figma.loadFontAsync({family: "BROWN NOW TWO", style: "TWO"})` zu laden, schlug mit `"The font family 'BROWN NOW TWO' does not exist"` fehl — der Font ist im File grundsätzlich nicht vorhanden/ladbar, nicht nur in der `use_figma`-Sandbox.
**How to apply:** Bei Textänderungen über gebundene Variablen mit bekannt kaputten/fehlenden Fonts gilt: Die Datenebene (API-Wert, `characters`-Property) ist korrekt und zuverlässig — das sichtbare Rendering kann trotzdem veraltet bleiben, bis der Font-Fehler im File selbst behoben wird (z.B. Font neu hochladen oder Textknoten auf einen verfügbaren Font umstellen). Der Userin sollte in so einem Fall transparent gemeldet werden, dass die Änderung technisch korrekt gesetzt ist, aber visuell erst nach Font-Fix sichtbar wird.

---

## 📋 SUMMARY: Die 5 Goldenen Regeln

1. **Aktives Tab zuerst** – Datei muss offen sein; Seite kann Claude per `setCurrentPageAsync()` selbst wechseln
2. **Fonts sind das Hauptproblem** – `getRangeFontName()` + `loadFontAsync()` ist nicht optional
3. **Console.log ist unsichtbar** – `get_metadata()` zur Verifizierung nutzen
4. **Verifizieren, nicht vertrauen** – Nach jedem Update User fragen
5. **Kein "Fertig" ohne Beweis** – Erst bestätigen, dann weitermachen

### ⚠️ Was NICHT funktioniert
- ✅ Variables lesen/schreiben/erstellen (Korrektur 13.07.2026 — Prefix `VariableID:` nötig, siehe `figma-api-reference.md`)
- ❌ console.log() als Feedback
- ❌ figma.notify() (User sieht das nicht)
- ❌ `instance.reactions = [...]` direkt zuweisen (nur lesbar) — `await instance.setReactionsAsync(...)` verwenden (Korrektur 14.07.2026)

---

## 🔄 Laufende Erkenntnis-Protokollierung (wichtig für Kontinuität)

**Regel:** Neue technische oder inhaltliche Erkenntnisse aus einem laufenden Chat werden **zwischendurch**, nicht erst am Ende, in dieses Repo (`amyria3/claude-figma-automation`) gepusht.

**Warum:** Chats können durch Sitzungsverlust, durch Löschen des Chats durch die Nutzerin oder durch andere technische Unterbrechungen vorzeitig enden. Erkenntnisse, die nur im Chat-Verlauf existieren und nicht ins Repo geschrieben wurden, gehen dann unwiederbringlich verloren. Das Repo ist der einzige Ort, der Sitzungs- und Chat-Verluste übersteht.

**Wie anwenden:**
- Sobald während einer Aufgabe eine neue, nicht-triviale technische Erkenntnis auftritt (z.B. ein Gotcha, eine widerlegte frühere Annahme, ein neues API-Verhalten), wird sie zeitnah in die passende Datei dieses Repos eingetragen — nicht erst am Ende der Konversation gesammelt.
- Bei rein technischen Erkenntnissen (Plugin-API-Verhalten, Swap-Mechanik, Doku-Korrekturen) ist keine Rückfrage bei der Nutzerin nötig, bevor dokumentiert wird.
- Bei inhaltlichen Fragen (z.B. mehrdeutige Anforderungen, Design-Entscheidungen ohne eindeutig richtige Antwort) wird weiterhin nachgefragt, bevor etwas festgeschrieben wird — siehe Beispiel oben unter Punkt "e) Touch-Trigger".
- Ziel: ein Repo-Stand, der jederzeit — auch mitten in einer Sitzung — den aktuellen Wissensstand widerspiegelt, nicht nur am Ende eines Chats.

---

**Version:** 1.5  
**Letzte Aktualisierung:** 14.07.2026  
**Status:** Produktionsreif – Alle Limitations dokumentiert
