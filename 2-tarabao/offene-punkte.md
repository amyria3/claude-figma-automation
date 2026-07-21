# Offene Punkte & unbeendete Aufgaben — Tarabao

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben rund um Tarabao (B2C-Shop, Figma-Datei „B2C-und-CI", Inhalte). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei. Claude-/technikbezogene Punkte: `1-figma-claude-technical/offene-punkte.md`.

## Offen (Stand 22.07.2026)

1. **Verwaiste Variables: Rest-Entscheidungen (Kategorie C/D)** — Alles Bindbare ist gebunden; übrig sind nur Werte neben der Skala und Ausreißer. Vollständige Liste: `2-tarabao/2.2-verwaiste-variables-liste.md`. Pro Wert entscheiden: runden auf Nachbar-Token / Sonder-Variable / bewusst hartkodiert lassen. Enthält auch: Nav 1px-Paddings (2761:6816) und 6× 31px in Cards/MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).

2. **Component-Set "Buttons with desciptions" kaputt** (Node 4014:28940) — laut paralleler Cowork-Session ist die Einordnung nicht eindeutig: kein reiner Deprecated-Rest, aber auch keine Test-/Ablage-Seite — die Seite "RESPONSIVE GUIDE" ist Referenz-/Styleguide-Dokumentation für responsives Verhalten. Entscheidung, wie damit umgegangen wird (reparieren, umbenennen, dokumentieren als bewusster Ausnahmefall), steht noch aus. Details vermutlich in `entwurf-doku-updates.md` (Cowork-Artefakt, 20.07.2026, 15:58 CEST) — diese Datei lag der aktuellen Session nicht vor.

3. **Primitives für Zeilen-Texte & Links fehlen** — Bei der Absatz-Migration (22.07.2026) bewusst nicht auf `Primitives / Paragraphs / Default` umgestellt: Link-Texte („Passwort vergessen?", „Kein Account?", „Adresse manuell eingeben", „Oder zurück …") sowie kurze Einzelzeilen/Nachrichten in schmalen Karten und Formularen (240–367 px) — das sind Zeilen, keine Absätze. Kandidaten für eigene Primitives: `Primitives / Link`, evtl. `Primitives / Notice`. Endstand der Migration: 34 lose Absätze laufen auf dem Primitive (min 384 / max 512); die 3 überbreiten (Hero FullW, Disclosure-Content, TabContent „Verwendung") sind bewusst auf 512 gekappt (Zeilenlänge).

## Klarstellungen (keine Fehler)

- Ungebundene Abstände auf Component-Set-Rahmen und Canvas-Ordnungsframes sind **Absicht** (nur innerhalb von Varianten sind sie ein Befund).
- Die alte Variablen-Gruppe `spacings/*` (tcss) existiert nicht mehr: keine eigene Collection, aus „Lyt scl / Width" entfernt, alle Bindungen im ganzen File (Master + Screens, 780 gesamt) auf `gap-*`/`box-spacing-*` migriert. Nicht neu anlegen.
