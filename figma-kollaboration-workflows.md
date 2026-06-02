# Empfohlene Workflows für die Zusammenarbeit mit Claude

> Diese Datei enthält Vorschläge für Arbeitsweisen, die die Zusammenarbeit mit Claude in Figma effizienter machen. Sie sind keine Pflicht — sondern Empfehlungen aus der Praxis, die du annehmen oder anpassen kannst.

---

## Workflow 1: Text Styles vor der Datei-Erstellung anlegen

**Warum?**
Werden Textknoten ohne Style-Verknüpfung erstellt, müssen Styles nachträglich manuell oder per Workaround zugewiesen werden — das kostet Zeit und ist fehleranfällig.

**Empfehlung:** Styles existieren, bevor die eigentliche Datei gebaut wird.

### Ablauf

**Schritt 1 — Claude erstellt einen Dummy-Frame**
Auf Anfrage baut Claude einen minimalistischen Frame mit je einem Beispiel-Textknoten pro geplantem Style (Label, Default Text, Headline, Subtitle etc.) — ohne echten Inhalt, nur zur Style-Referenz.

**Schritt 2 — Du erstellst die Text Styles**
Du wählst jeden Beispielknoten an und erstellst daraus einen benannten Text Style in Figma (`CV/Label`, `CV/Default Text` etc.).

**Schritt 3 — Claude liest die Style-IDs aus**
Du wendest jeden Style einmal manuell auf einen Knoten an. Claude liest die IDs automatisch aus und speichert sie für die Erstellung.

**Schritt 4 — Claude baut die echte Datei**
Claude erstellt alle Textknoten und verknüpft sie direkt beim Erstellen mit den korrekten Style-IDs — kein nachträgliches Zuweisen nötig.

### Ergebnis
- Alle Textknoten von Anfang an konsistent verknüpft
- Globale Änderungen (Font, Größe) wirken sofort auf die gesamte Datei
- Kein manuelles Nacharbeiten

---

*Weitere Workflow-Vorschläge folgen aus der gemeinsamen Praxis.*
