# figma-automation — Claude Skill

> **Diese Datei ist für den Download und die lokale Installation als Claude Skill vorgesehen.**
> Sie enthält die vollständige Skill-Definition, die Claude anweist wie es bei Figma-Aufgaben vorgehen soll.
>
> **Installation:** Datei herunterladen → Claude.ai → Einstellungen → Skills → Skill hinzufügen

---

```
---
name: figma-automation
description: "Figma Automation & Text-Operationen mit Claude. NUTZE DIESEN SKILL bei JEDER Figma-Erwähnung: Texte übersetzen, korrigieren, Batch-Operationen, Edit-Links verarbeiten, Screenshots validieren, Nodes bearbeiten, Design-Prinzipien anwenden. Beim Laden automatisch die Referenzdateien von GitHub lesen."
---
```

## ⚙️ Einrichtung

### Voraussetzungen
- Figma MCP in Claude.ai: **Einstellungen → Connectors → Figma** aktivieren
- GitHub MCP: Docker Desktop muss laufen (gilt für Claude.ai UND Desktop)
  → Details: `github-mcp-setup.md`

### Schnellstart
1. Figma Edit-Link teilen: **Share → Copy edit link**
2. Aufgabe beschreiben — Claude lädt automatisch die Referenzdateien
3. Bei Variables-Themen: `figma-stylesheet-workaround.md` wird gesondert geladen

---

## 📂 Pflichtlektüre beim Start (via GitHub MCP)

Bei jeder Figma-Aufgabe diese Dateien aus dem Repository laden:

| Reihenfolge | Datei | Inhalt |
|---|---|---|
| 1 | `figma-workflow-technisch.md` | Pre-flight Checklist, Golden Rules |
| 2 | `figma-api-reference.md` | API-Referenz, Code-Patterns, Limitations |
| 3 | `figma-design-principles-arkadieff.md` | Design-Prinzipien (Flex, Spacing, Typography) |
| 4 | `figma-stylesheet-workaround.md` | Variables-Workaround (bei Bedarf) |
| 5 | `figma-kollaboration-workflows.md` | Empfohlene Workflows (bei Workflow-Fragen) |

> Falls GitHub MCP nicht verfügbar: Nutzerin bitten, Dateien manuell einzufügen oder als Text zu teilen.

---

## 🎨 Design-Prinzipien (Kurzreferenz)

Vollständige Prinzipien: `figma-design-principles-arkadieff.md` auf GitHub.

- **Alle Layouts** als `flex-row` oder `flex-col`
- **Naming:** `[Element]Container`, Tailwind-Konventionen (lowercase)
- **Spacing:** 4 / 8 / 12 / 16 / 24 / 32px
- **Variables:** Nicht per API erstellbar → Stylesheet-Workaround nutzen

---

## 🛠️ Operationen

- **Text:** Übersetzen, korrigieren, ersetzen, Batch über mehrere Nodes
- **Styling:** Farben, Fills, Strokes lesen & setzen
- **Layout:** Flex VERTICAL/HORIZONTAL, Alignment, Sizing
- **Nodes:** Erstellen, löschen, umbenennen, verschachteln
- **Validierung:** Screenshots via `get_metadata()` zur Verifikation

---

## ❌ Bekannte Einschränkungen

| Feature | Status |
|---|---|
| Variables erstellen/verknüpfen | ❌ API nicht unterstützt |
| **Workaround** | Stylesheet in Figma anlegen → Claude liest Screenshot → wendet Werte an |
