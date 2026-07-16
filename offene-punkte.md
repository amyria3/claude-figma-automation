# Offene Punkte & unbeendete Aufgaben

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben (Nutzerin + alle Claude-Instanzen). Erledigtes hier streichen; Details gehören in die jeweilige Fachdatei.

## Offen (Stand 16.07.2026)

1. **`verwaiste-variables-liste.md` ins Repo übertragen** — Die vollständige Fundliste (12 gesicherte Funde + 3 Kandidaten, 32/118 Komponenten geprüft) liegt sicher im Speicher/Kontext einer Claude-Instanz (Web-Chat „Figma-Schreibverbindung wiederherstellen"), aber noch nicht im Repo. Referenziert von `ux-ui-dokumentation-tarabao.md` (TODO #1). → Diese Instanz bitten, die Liste hierher zu committen.
2. **`figma-api-reference.md`: Async-Fix ausstehend** — Im `updateText()`-Beispiel steht noch synchrones `figma.getNodeById(nodeId)`; laut workflow v2.0 Async-Variante nutzen: `const node = await figma.getNodeByIdAsync(nodeId);`. Der am 15.07. im Web-Editor vorbereitete Fix ging beim Session-Limit verloren.
3. ~~**`test.md` löschen**~~ — ✅ erledigt 16.07. (Commit 5e71b4f, andere Instanz).
4. **Audit 15.07.: „vier übrige Doku-Fixes" unklar** — Der Original-Fehlerbericht (8 Befunde) ist nicht mehr rekonstruierbar. Neuprüfung am 16.07. fand nur Punkt 2 sowie die Setup-Widersprüche (github-mcp-setup, Skill-Datei — am 16.07. korrigiert). Falls eine Instanz die 8 Befunde noch im Kontext hat: hier eintragen.
5. **Installierter Cowork-Skill `figma-automation` veraltet** — Die lokal installierte Kopie behauptet noch „Variables erstellen/verknüpfen ❌ API nicht unterstützt". Nur die Nutzerin kann sie ersetzen: Einstellungen → Capabilities, aktuelle Repo-Version `figma-automation-skill.md` verwenden.
6. **Verwaiste-Variables-Prüfung unvollständig** — 86 von 118 Komponenten ungeprüft (restliche Buttons, Filter & Search, Checkout-Details, Cancellation, Patterns).

## Klarstellungen (keine Fehler)

- `user-is-learning-terminal-commands` (README-Index #8) liegt **bewusst nur lokal** bei der Nutzerin und wird nicht gepusht.
- Die „TEST/PRACTICE FOR CLAUDE"-Aufgaben liefen über den Figma-Connector (`use_figma`, Remote-MCP); Referenzdateien wurden via Raw-URLs gelesen — Docker/GitHub-MCP war nicht beteiligt.

