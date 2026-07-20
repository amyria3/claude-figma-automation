# Offene Punkte & unbeendete Aufgaben

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben (Nutzerin + alle Claude-Instanzen). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei.

## Offen (Stand 20.07.2026)

1. **Installierter Cowork-Skill `figma-automation` veraltet** — Die lokal installierte Kopie behauptet noch „Variables erstellen/verknüpfen ❌ API nicht unterstützt" und nennt alte Dateipfade. Nur die Nutzerin kann sie ersetzen: Einstellungen → Capabilities, aktuelle Repo-Version `1-figma-claude-technical/1.6-figma-automation-skill.md` verwenden. (Der Skill enthält seit 20.07. einen Versionsstempel + Sync-Check gegen die Repo-Version.)

2. **Verwaiste Variables: Rest-Entscheidungen (Kategorie C/D)** — Alles Bindbare ist gebunden; übrig sind nur Werte neben der Skala und Ausreißer. Vollständige Liste: `2-tarabao/2.2-verwaiste-variables-liste.md`. Pro Wert entscheiden: runden auf Nachbar-Token / Sonder-Variable / bewusst hartkodiert lassen. Enthält auch: Nav 1px-Paddings (2761:6816) und 6× 31px in Cards/MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).

3. **49/50px-Radio-Einrückung vereinheitlichen** — 9 Stellen, gleiche Funktion, zwei Werte: 7× 50px, 2× 49px (RadioButtonGroup 3793:15649, 6811:20436, 6811:20444, 3793:15655, 3795:12766, 3799:18277, 3799:18302 = 50; RadioButtonGroup 3795:12642 und ShippingAddressFormRadioButton 3780:14942 = 49). Beim Variantenpaar Content=Component springt der Inhalt beim Auswählen um 1px. Entscheidung: alle auf `box-spacing-xxl (48px)`, alle auf 50 (Sonder-Variable nötig) oder anderer Zielwert.

4. **Alte Collection `spacings/*` (tcss) — Löschung/Deprecation?** — In Master-Komponenten am 20.07. vollständig auf `gap-*`/`box-spacing-*` migriert (0 Rest in Mastern). Die Collection könnte aber noch von Screen-/Mockup-Seiten oder Instanz-Overrides referenziert werden. Entscheidung der Nutzerin: prüfen und dann löschen oder als deprecated behalten.

## Klarstellungen (keine Fehler)

- `user-is-learning-terminal-commands` (README-Index #8) liegt **bewusst nur lokal** bei der Nutzerin und wird nicht gepusht.
- Die „TEST/PRACTICE FOR CLAUDE"-Aufgaben liefen über den Figma-Connector (`use_figma`, Remote-MCP); Referenzdateien wurden via Raw-URLs gelesen — Docker/GitHub-MCP war nicht beteiligt.
- Ungebundene Abstände auf Component-Set-Rahmen und Canvas-Ordnungsframes sind **Absicht** (nur innerhalb von Varianten sind sie ein Befund).
