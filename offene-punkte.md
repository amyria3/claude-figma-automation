# Offene Punkte & unbeendete Aufgaben

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben (Nutzerin + alle Claude-Instanzen). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei.

## Offen (Stand 20.07.2026)

1. **Installierter Cowork-Skill `figma-automation` veraltet** — Die lokal installierte Kopie behauptet noch „Variables erstellen/verknüpfen ❌ API nicht unterstützt" und nennt alte Dateipfade. Nur die Nutzerin kann sie ersetzen: Einstellungen → Capabilities, aktuelle Repo-Version `1-figma-claude-technical/1.6-figma-automation-skill.md` verwenden. (Der Skill enthält seit 20.07. einen Versionsstempel + Sync-Check gegen die Repo-Version.)

2. **Verwaiste Variables: Rest-Entscheidungen (Kategorie C/D)** — Alles Bindbare ist gebunden; übrig sind nur Werte neben der Skala und Ausreißer. Vollständige Liste: `2-tarabao/2.2-verwaiste-variables-liste.md`. Pro Wert entscheiden: runden auf Nachbar-Token / Sonder-Variable / bewusst hartkodiert lassen. Enthält auch: Nav 1px-Paddings (2761:6816) und 6× 31px in Cards/MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).

3. **Component-Set "Buttons with desciptions" kaputt** (Node 4014:28940) — laut paralleler Cowork-Session ist die Einordnung nicht eindeutig: kein reiner Deprecated-Rest, aber auch keine Test-/Ablage-Seite — die Seite "RESPONSIVE GUIDE" ist Referenz-/Styleguide-Dokumentation für responsives Verhalten. Entscheidung, wie damit umgegangen wird (reparieren, umbenennen, dokumentieren als bewusster Ausnahmefall), steht noch aus. Details vermutlich in `entwurf-doku-updates.md` (Cowork-Artefakt, 20.07.2026, 15:58 CEST) — diese Datei lag der aktuellen Session nicht vor.

4. **Zwei technische Doku-Ergänzungen aus paralleler Cowork-Session noch nicht eingepflegt** — laut Briefing der anderen Instanz (20.07.2026) fehlen in `1-figma-claude-technical/1.2-figma-workflow-technisch.md` noch: (a) Ergänzung 5b zu einem "Gotcha #5" — Instanz-Name kann veraltet bleiben, ohne dass ein Strukturfehler vorliegt; (b) ein neuer Methodik-Punkt zu `componentPropertyDefinitions` vs. `variantGroupProperties`. Konnte nicht eingetragen werden, da nur die Zusammenfassung über `entwurf-doku-updates.md` vorlag, nicht die Datei selbst mit den technischen Details — bitte Inhalt der Datei bereitstellen, dann nachtragen. Achtung laut Briefing: Nummerierung von "Gotcha #5" kann sich seit der aktuellen Restrukturierung von 1.2 verschoben haben (die Datei nutzt inzwischen nummerierte Abschnitte 1️⃣–6️⃣, keine "Gotcha #N"-Zählung mehr) — beim Einpflegen prüfen, welcher Abschnitt tatsächlich gemeint ist.

## Klarstellungen (keine Fehler)

- `user-is-learning-terminal-commands` (README-Index #8) liegt **bewusst nur lokal** bei der Nutzerin und wird nicht gepusht.
- Die „TEST/PRACTICE FOR CLAUDE"-Aufgaben liefen über den Figma-Connector (`use_figma`, Remote-MCP); Referenzdateien wurden via Raw-URLs gelesen — Docker/GitHub-MCP war nicht beteiligt.
- Ungebundene Abstände auf Component-Set-Rahmen und Canvas-Ordnungsframes sind **Absicht** (nur innerhalb von Varianten sind sie ein Befund).
- Die alte Variablen-Gruppe `spacings/*` (tcss) existiert nicht mehr: keine eigene Collection, aus „Lyt scl / Width" entfernt, alle Bindungen im ganzen File (Master + Screens, 780 gesamt) auf `gap-*`/`box-spacing-*` migriert. Nicht neu anlegen.
