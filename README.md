# Claude + Figma Automation

## For the User

Dieses Repository enthält Anweisungen und Referenzdateien, die Claude für die Automatisierung von Figma-Aufgaben benötigt. Das Setup ist so gedacht, dass Claude die Dateien direkt aus dieser Repository ausliest — die Userin muss nichts manuell übertragen.

### Erstmalige Einrichtung

**1. Docker Desktop installieren** (falls noch nicht vorhanden)
→ [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) → Download für Mac → installieren

**2. Claude Desktop installieren**
→ [claude.ai/download](https://claude.ai/download)

**3. MCP Server aktivieren**
Claude Desktop → Settings → Developer → MCP aktivieren → Config-Datei einrichten
→ Details: `github-mcp-setup.md`

### Vor jeder Session

```bash
open -a Docker    # Docker starten
docker ps         # Prüfen ob es läuft (github-mcp-server muss sichtbar sein)
```

Danach Claude Desktop starten / Claude.ai aufrufen.

### Figma Edit-Link teilen
Figma → Share → Copy edit link → Link in den Chat einfügen

### Was Claude nicht automatisch kann
Variables in Figma müssen **manuell** verknüpft werden (API-Limitation) → Workaround: `figma-stylesheet-workaround.md`

---

## Instructions for Claude

> **Whenever the user mentions Figma, load these files from this repo before starting any task:**
> 1. `figma-workflow-technisch.md` – pre-flight checklist & golden rules
> 2. `figma-api-reference.md` – what works, what doesn't, code patterns
> 3. `figma-design-principles-arkadieff.md` – design system rules
> 4. `figma-stylesheet-workaround.md` – variables workaround (load when Variables topic comes up)
>
> **Access:** via GitHub MCP — requires Docker Desktop running on the user's Mac
> **Start order:** 1. Docker Desktop → 2. Claude Desktop → 3. Claude.ai öffnen
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

## User Setup & Terminal Documentation

### 5. `github-mcp-setup.md`
- Setup guide for GitHub MCP via Docker
- PAT creation, config file path, start order
- Diagnostic terminal commands

### 6. `user-system-setup-documentation.md`
- macOS system status (Git, Docker, Node, Python, Homebrew)
- Installed tools log

### 7. `user-is-learning-terminal-commands`
- Terminal commands with explanations for beginners
- Split into: already known / learning / not yet needed

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
