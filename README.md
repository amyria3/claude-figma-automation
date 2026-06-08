# Claude + Figma Automation

## For the User

Dieses Repository enthält überwiegend Anweisungen und Referenzdateien, die Claude für die Automatisierung von Figma-Aufgaben benötigt. Das Setup ist so gedacht, dass Claude die Dateien direkt aus dieser Repository ausliest — die Userin muss nichts manuell übertragen.
Enjoy KI, enjoy liebe*r Nutzer/ *in. 


### Erstmalige Einrichtung

**1. Falls nicht vorhanden, Docker Desktop installieren**
→ [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) → Download für Mac → installieren

**2. Falls nicht vorhanden, Claude Desktop installieren**
→ [claude.ai/download](https://claude.ai/download)

**3. MCP Server einrichten**
1. Claude Desktop → Settings → Developer → MCP aktivieren
2. Claude Config-Datei einrichten - _Details: `github-mcp-setup.md`_

### Vor jeder Session

```bash
open -a Docker    # Docker starten
docker ps         # Prüfen ob es läuft (github-mcp-server muss sichtbar sein)
```

Danach Claude Desktop starten / Claude.ai aufrufen.

### Figma Edit-Link mit Claude teilen
Figma → Share

### Was Claude nicht automatisch kann
Variables in Figma müssen **manuell** verknüpft werden (API-Limitation)
Workaround: `figma-stylesheet-workaround.md`

### Claude Skill installieren
Den `figma-automation` Skill lokal installieren damit Claude bei jeder Figma-Erwähnung automatisch die richtigen Dateien lädt:
→ [`figma-automation-skill.md`](./figma-automation-skill.md) herunterladen → Claude.ai → Einstellungen → Skills → Skill hinzufügen

---

## Instructions for Claude

> **Whenever the user mentions Figma, load these files from this repo before starting any task:**
> 1. `figma-workflow-technisch.md` – pre-flight checklist & golden rules
> 2. `figma-api-reference.md` – what works, what doesn't, code patterns
> 3. `figma-design-principles-arkadieff.md` – design system rules
> 4. `figma-stylesheet-workaround.md` – variables workaround (load when Variables topic comes up)
> 5. `figma-kollaboration-workflows.md` – recommended collaboration workflows (load for workflow questions)
>
> **Access:** via GitHub MCP — requires Docker Desktop running on the user's Mac
> **Start order:** 1. Docker Desktop → 2. Claude Desktop → 3. Claude.ai aufrufen
> **Kein Zugriff?** Docker läuft nicht → Terminal: `open -a Docker` dann `docker ps` prüfen

---

## Figma Documentation

### 1. `figma-workflow-technisch.md`
- Pre-flight checklist (vor jeder Task)
- Font-loading patterns
- Verification methods (get_metadata)
- Error handling
- Golden rules & best practices

### 2. `figma-api-reference.md`
- Complete API reference with code examples
- Text operations (changing, fonts, typography)
- Styling operations (colors, fills, strokes)
- Flex layouts (VERTICAL, HORIZONTAL, alignment)
- Known limitations & workarounds
- Quick-start templates

### 3. `figma-design-principles-arkadieff.md`
- Core design principles (flex-based layouts, naming conventions)
- Spacing & typography tokens

### 4. `figma-stylesheet-workaround.md`
- Stylesheet-based styling workflow (for Variables limitation)
- Step-by-step guide
- Design token templates (copy-paste ready)
- Checklists for both Claude and user

### 5. `figma-kollaboration-workflows.md`
- Recommended workflows for working with Claude in Figma
- Text Styles vor Datei-Erstellung anlegen
- Frame spiegeln (EN → DE oder umgekehrt)

## User Setup & Terminal Documentation

### 6. `github-mcp-setup.md`
- Setup guide for GitHub MCP via Docker
- PAT creation, config file path, start order
- Diagnostic terminal commands

### 7. `user-system-setup-documentation.md`
- macOS system status (Git, Docker, Node, Python, Homebrew)
- Installed tools log

### 8. `user-is-learning-terminal-commands`
- Terminal commands with explanations for beginners
- Split into: already known / learning / not yet needed

### 9. `figma-automation-skill.md`
- Downloadbare Skill-Definition für Claude
- Für lokale Installation unter Einstellungen → Skills

---

## Feature Status

| Feature | Status | Notes |
|---------|--------|-------|
| Text operations | ✅ Working | All typography properties supported |
| Styling (colors, fills) | ✅ Working | Can read & apply colors |
| Flex layouts | ✅ Working | VERTICAL, HORIZONTAL, alignment |
| Node operations | ✅ Working | Create, delete, rename |
| Verification via get_metadata() | ✅ Working | XML-based confirmation |
| Variables (create/link) | ❌ Not supported | Workaround: doc #4 |

## Related

- [Figma Plugin API Docs](https://www.figma.com/plugin-docs/)
- [Claude MCP Documentation](https://docs.anthropic.com/)

## Last Updated

June 8, 2026
