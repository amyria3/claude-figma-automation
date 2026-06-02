# Kollaborations-Workflows: Claude + Arkadieff

> Diese Datei dokumentiert bewährte Arbeitsweisen für die Zusammenarbeit zwischen Claude und dem User bei Figma-Projekten. Technische API-Details stehen in `figma-workflow-technisch.md`.

---

## Workflow 1: Text Styles vor der Datei-Erstellung

**Problem:** Werden Textknoten ohne Style-Verknüpfung erstellt, müssen Styles nachträglich manuell oder per Workaround zugewiesen werden.

**Lösung:** Styles existieren, bevor die eigentliche Datei gebaut wird.

### Ablauf

**Schritt 1 — Claude erstellt Dummy-Frame**
Claude baut einen minimalistischen Frame mit je einem Beispiel-Textknoten pro geplantem Style (Label, Default Text, Headline, Subtitle etc.) — ohne Inhalt, nur zur Style-Referenz.

**Schritt 2 — User erstellt Text Styles**
Der User wählt jeden Beispielknoten an und erstellt daraus einen benannten Text Style in Figma (`CV/Label`, `CV/Default Text` etc.).

**Schritt 3 — Style-IDs auslesen**
Der User wendet jeden Style einmal auf einen Knoten an. Claude liest die Style-IDs aus den verknüpften Knoten aus (siehe `figma-stylesheet-workaround.md`).

**Schritt 4 — Echte Datei bauen**
Claude erstellt alle Textknoten der echten Datei und verknüpft sie direkt beim Erstellen mit den korrekten Style-IDs.

### Ergebnis
- Keine nachträgliche Style-Zuweisung
- Alle Textknoten von Anfang an konsistent verknüpft
- Globale Änderungen (Font, Größe) wirken sofort auf die gesamte Datei

---

*Weitere Workflows folgen.*
