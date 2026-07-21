# Offene Punkte & unbeendete Aufgaben — Tarabao

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben rund um Tarabao (B2C-Shop, Figma-Datei „B2C-und-CI", Inhalte). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei. Claude-/technikbezogene Punkte: `1-figma-claude-technical/offene-punkte.md`.

## Offen (Stand 21.07.2026)

1. **Verwaiste Variables: Rest-Entscheidungen (Kategorie C/D)** — Alles Bindbare ist gebunden; übrig sind nur Werte neben der Skala und Ausreißer. Vollständige Liste: `2-tarabao/2.2-verwaiste-variables-liste.md`. Pro Wert entscheiden: runden auf Nachbar-Token / Sonder-Variable / bewusst hartkodiert lassen. Enthält auch: Nav 1px-Paddings (2761:6816) und 6× 31px in Cards/MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).

2. **Component-Set "Buttons with desciptions" kaputt** (Node 4014:28940) — laut paralleler Cowork-Session ist die Einordnung nicht eindeutig: kein reiner Deprecated-Rest, aber auch keine Test-/Ablage-Seite — die Seite "RESPONSIVE GUIDE" ist Referenz-/Styleguide-Dokumentation für responsives Verhalten. Entscheidung, wie damit umgegangen wird (reparieren, umbenennen, dokumentieren als bewusster Ausnahmefall), steht noch aus. Details vermutlich in `entwurf-doku-updates.md` (Cowork-Artefakt, 20.07.2026, 15:58 CEST) — diese Datei lag der aktuellen Session nicht vor.

3. **Hero/TabContent-Slot-Umbau (läuft, noch kein voller Überblick)** — Ziele: (a) Section/Hero (6604:17025) entscheidet nur noch das Layout (2 Varianten: Split, FullW); was im Textbereich steht, bestimmt eine Content-Module-Instanz im Slot. Die Varianten-Achsen `Text?`, `CTA?`, `Cards/Review?`, `Contact Formular?` entfallen danach. (b) Components/TabContent (7448:20255) analog: Content = Content-Module-Instanz im Slot; vorher bei Volle-Breite-Blöcken fehlende max-w nachtragen. (c) Dafür vier Spaltenblöcke als Content Modules anlegen: Text, Text+CTA, Benefits, ContactForm (min/max-w 384/512 nehmen sie mit). Stand 21.07.: Typo-Primitives (Headline H1/H2, Headlines H3, Paragraphs, Stars) angelegt; H3-Ersetzung abgeschlossen, H1/H2-Ersetzung in Arbeit; die vier Spaltenblöcke existieren noch nicht als Komponenten. Daria hat noch keinen vollen Überblick über den Endzustand — Doku wird nach Abschluss konsolidiert. Nomenklatur: `2-tarabao/2.1-ux-ui-dokumentation-tarabao.md`, Abschnitt „Komponenten-Hierarchie“.

4. **Naming-Harmonisierung neue Nomenklatur** — „Headline“ (H1/H2) vs. „Headlines“ (H3); Leerzeichen am Ende von „Primitives / Stars “ (7565:24038). Details: 2.1, „Zu klären: Komponenten-Naming“.

## Klarstellungen (keine Fehler)

- Ungebundene Abstände auf Component-Set-Rahmen und Canvas-Ordnungsframes sind **Absicht** (nur innerhalb von Varianten sind sie ein Befund).
- Die alte Variablen-Gruppe `spacings/*` (tcss) existiert nicht mehr: keine eigene Collection, aus „Lyt scl / Width" entfernt, alle Bindungen im ganzen File (Master + Screens, 780 gesamt) auf `gap-*`/`box-spacing-*` migriert. Nicht neu anlegen.
