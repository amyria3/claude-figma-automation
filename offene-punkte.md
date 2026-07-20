# Offene Punkte & unbeendete Aufgaben

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben (Nutzerin + alle Claude-Instanzen). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei.

## Offen (Stand 20.07.2026)

1. **Installierter Cowork-Skill `figma-automation` veraltet** — Die lokal installierte Kopie behauptet noch „Variables erstellen/verknüpfen ❌ API nicht unterstützt" und nennt alte Dateipfade. Nur die Nutzerin kann sie ersetzen: Einstellungen → Capabilities, aktuelle Repo-Version `1-figma-claude-technical/1.6-figma-automation-skill.md` verwenden. (Der Skill enthält seit 20.07. einen Versionsstempel + Sync-Check gegen die Repo-Version.)

2. **Verwaiste Variables: Rest-Entscheidungen (Kategorie C/D)** — Alles Bindbare ist gebunden; übrig sind nur Werte neben der Skala und Ausreißer. Vollständige Liste: `2-tarabao/2.2-verwaiste-variables-liste.md`. Pro Wert entscheiden: runden auf Nachbar-Token / Sonder-Variable / bewusst hartkodiert lassen. Enthält auch: Nav 1px-Paddings (2761:6816) und 6× 31px in Cards/MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).

## Klarstellungen (keine Fehler)

- `user-is-learning-terminal-commands` (README-Index #8) liegt **bewusst nur lokal** bei der Nutzerin und wird nicht gepusht.
- Die „TEST/PRACTICE FOR CLAUDE"-Aufgaben liefen über den Figma-Connector (`use_figma`, Remote-MCP); Referenzdateien wurden via Raw-URLs gelesen — Docker/GitHub-MCP war nicht beteiligt.
- Ungebundene Abstände auf Component-Set-Rahmen und Canvas-Ordnungsframes sind **Absicht** (nur innerhalb von Varianten sind sie ein Befund).
- Die alte Variablen-Gruppe `spacings/*` (tcss) existiert nicht mehr: keine eigene Collection, aus „Lyt scl / Width" entfernt, alle Bindungen im ganzen File (Master + Screens, 780 gesamt) auf `gap-*`/`box-spacing-*` migriert. Nicht neu anlegen.
