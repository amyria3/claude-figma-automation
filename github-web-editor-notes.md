# GitHub Web-Editor: Technische Hinweise für Claude

Diese Datei ist für Claude selbst gedacht — Erkenntnisse aus Browser-Automation-Sessions beim Bearbeiten von Dateien in diesem Repo über github.com (CodeMirror 6), nicht für die Nutzerin. Relevant, sobald Claude über Claude in Chrome eine Datei in diesem oder einem anderen GitHub-Repo per Web-Editor bearbeitet.

## Mehrzeiligen Text einfügen

Nicht per simuliertem Tippen mit Enter-Keypresses einfügen — CodeMirrors Markdown-Listen-Keymap fügt nach jedem Enter automatisch einen Bullet/Einzug ein, wenn der eingefügte Text bereits eigene "- "-Marker enthält. Das verdoppelt Einrückungen über den Rest des Dokuments hinweg.

Stattdessen: Cursor per DOM-Range/Selection an die Zielposition setzen, dann `document.execCommand('insertText', false, text)` verwenden — fügt mehrzeiligen Text atomar ein, ohne die Enter-Keymap auszulösen.

```javascript
const lines = Array.from(document.querySelectorAll('.cm-line'));
const target = lines.find(l => l.textContent === 'ZIELZEILE');
const contentEl = document.querySelector('.cm-content');
contentEl.focus();
const range = document.createRange();
range.selectNodeContents(target);
range.collapse(false); // Ende der Zeile
const sel = window.getSelection();
sel.removeAllRanges();
sel.addRange(range);
document.execCommand('insertText', false, "\n\nNeuer Inhalt...");
```

## Virtualisierung: .cm-line zeigt nur den sichtbaren Viewport

CodeMirror rendert nur die aktuell sichtbaren Zeilen als `.cm-line`-Elemente. Bei längeren Dateien (~250+ Zeilen) sind oft nur ~19-20 Zeilen gleichzeitig im DOM vorhanden.

**Was NICHT zuverlässig funktioniert, um zu scrollen:**
- `element.scrollTop = ...` (programmatisch) — löst kein Re-Render aus, auch nicht mit anschließend dispatchtem `new Event('scroll')`.
- Synthetisches `KeyboardEvent('keydown', {key:'End', ctrlKey:true})` auf `.cm-content` — wird nicht von CodeMirrors Keymap abgefangen, obwohl der Fokus korrekt gesetzt ist.
- `computer`-Tool `scroll`-Action und Screenshots waren in dieser Umgebung auf dieser Seite wiederholt instabil (Timeouts, "Frame with ID 0 was removed", Extension-Disconnects).

**Was funktioniert:** Bearbeitungen auf Zeilen beschränken, die beim Laden der Seite bereits im sichtbaren Viewport gerendert sind (typischerweise die ersten ~19-20 Zeilen). Neue Abschnitte lieber oben im Dokument einfügen (z.B. direkt nach der Kopfzeile / vor dem ersten `---`) statt mittig oder am Ende — dafür muss nicht gescrollt werden. Bei neuen, leeren Dateien entfällt das Problem komplett (Cursor steht schon an Position 0).

## Inhalt verifizieren: Preview-Tab statt .cm-line auslesen

Nach einem Insert kann der aus `.cm-line` ausgelesene Text irreführend aussehen (z.B. erscheinen zwei eigentlich durch Zeilenumbruch getrennte Abschnitte als ein zusammenhängender String wie `"---# ✅ Titel"`, weil Virtualisierungs-Grenzen den Zeilenumbruch beim Auslesen verschlucken). Das ist ein Anzeige-Artefakt der DOM-Abfrage, keine echte Beschädigung des Dokuments.

**Zuverlässige Verifikation:** Auf den "Preview"-Tab-Button klicken (`Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Preview')`) und den gerenderten Markdown-Text per `get_page_text` prüfen — das zeigt den tatsächlichen Dokumentinhalt, nicht die virtualisierte DOM-Teilansicht.

## Commit-Workflow

1. Im Edit-Tab: Button mit Text "Commit changes..." klicken (öffnet ein Modal, `[role="dialog"]`).
2. GitHub/Copilot füllt automatisch eine Commit-Message aus. Das Modal enthält zwei Buttons: "Cancel" und "Commit changes" — den zweiten (innerhalb des Dialogs) klicken, nicht nochmal den ursprünglichen Auslöser-Button außerhalb des Dialogs.
3. Erfolg prüfen: Die URL wechselt von `.../edit/main/...` zu `.../blob/main/...`.

## Sonstiges

- Die Chrome-Extension-Verbindung kann mitten in einer Session abbrechen ("Claude in Chrome is not connected"). Kein Grund zur Sorge — kurz erneut versuchen (`tabs_context_mcp`), meist erholt sie sich innerhalb weniger Versuche.
- `Ctrl+F` öffnet in dieser Umgebung nicht CodeMirrors eigenes Such-Panel (öffnete stattdessen nur ein generisches Fokus-Hilfe-Panel) — nicht verlässlich zum Navigieren nutzen.
- Bei neuen Dateien (`/new/main?filename=...`) ist der Editor leer und bereits fokussierbar — `execCommand('insertText', ...)` funktioniert dort direkt ohne vorheriges Zeilen-Suchen.

