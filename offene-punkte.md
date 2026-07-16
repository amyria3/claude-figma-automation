# Offene Punkte & unbeendete Aufgaben

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben (Nutzerin + alle Claude-Instanzen). Erledigtes hier streichen; Details gehören in die jeweilige Fachdatei.

## Offen (Stand 16.07.2026)

1. **`verwaiste-variables-liste.md` ins Repo übertragen** — Die vollständige Fundliste (12 gesicherte Funde + 3 Kandidaten, 32/118 Komponenten geprüft) liegt laut Nutzerin sicher im Speicher/Kontext des Web-Chats ( „Figma-Schreibverbindung wiederherstellen"), aber noch nicht im Repo. Referenziert von `2-tarabao/2.1-ux-ui-dokumentation-tarabao.md` (TODO #1). → Diese Instanz bitten, die Liste hierher zu committen.
2. ~~**`1-figma/1.3-figma-api-reference.md`: Async-Fix**~~ — ✅ erledigt 16.07. (`getNodeById` → `await getNodeByIdAsync` im `updateText()`-Beispiel).
3. ~~**`test.md` löschen**~~ — ✅ erledigt 16.07. (Commit 5e71b4f, Nutzerin direkt — es gab keine zweite aktive Instanz; auch der README-Commit „Stilistic changes“ war die Nutzerin).
4. **Audit 15.07.: „vier übrige Doku-Fixes" unklar** — Der Original-Fehlerbericht (8 Befunde) ist nicht mehr rekonstruierbar. Neuprüfung am 16.07. fand nur Punkt 2 sowie die Setup-Widersprüche (github-mcp-setup, Skill-Datei — am 16.07. korrigiert). Falls eine Instanz die 8 Befunde noch im Kontext hat: hier eintragen.
5. **Installierter Cowork-Skill `figma-automation` veraltet** — Die lokal installierte Kopie behauptet noch „Variables erstellen/verknüpfen ❌ API nicht unterstützt". Nur die Nutzerin kann sie ersetzen: Einstellungen → Capabilities, aktuelle Repo-Version `1-figma/1.7-figma-automation-skill.md` verwenden.
6. **Verwaiste-Variables-Prüfung unvollständig** — 86 von 118 Komponenten ungeprüft (restliche Buttons, Filter & Search, Checkout-Details, Cancellation, Patterns).

## Klarstellungen (keine Fehler)

- `user-is-learning-terminal-commands` (README-Index #8) liegt **bewusst nur lokal** bei der Nutzerin und wird nicht gepusht.
- Die „TEST/PRACTICE FOR CLAUDE"-Aufgaben liefen über den Figma-Connector (`use_figma`, Remote-MCP); Referenzdateien wurden via Raw-URLs gelesen — Docker/GitHub-MCP war nicht beteiligt.

