# Claude + Figma Automation

## For the User

Dieses Repository enthält überwiegend Anweisungen und Referenzdateien, die Claude für die Automatisierung von Figma-Aufgaben benötigt. Das Setup ist so gedacht, dass Claude die Dateien direkt aus dieser Repository ausliest — die Userin muss nichts manuell übertragen.
Enjoy KI, enjoy liebe*r Nutzer *in. 


### Setup (aktueller Stand — Juli 2026)

**Für Figma-Schreibzugriff ist keine lokale Installation mehr nötig.**

1. In claude.ai / Cowork den **Figma-Connector** verbinden (Claude schlägt ihn bei Bedarf selbst vor → Connect klicken → OAuth-Login bei Figma bestätigen)
2. Figma-Datei-URL mit Claude teilen (Figma → Share → Copy link)

Details & Fallback-Weg: `figma-schreibzugriff-use_figma.md`

### Legacy-Setup: GitHub MCP via Docker (optional)

**Nicht mehr erforderlich** — das Repo ist öffentlich, Claude liest die Dateien direkt über die Raw-URLs (siehe Instructions unten). Das alte Setup funktioniert weiterhin, falls gewünscht:

1. Docker Desktop installieren → [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Claude Desktop installieren → [claude.ai/download](https://claude.ai/download)
3. MCP einrichten: Claude Desktop → Settings → Developer → MCP aktivieren; Config-Datei einrichten — _Details: `github-mcp-setup.md`_
4. Vor jeder Session: `open -a Docker`, dann `docker ps` prüfen

### Was Claude inzwischen automatisch kann: Variables

Früher mussten Variables **manuell** verknüpft werden (Limitation der alten API-Anbindung). **Seit dem `use_figma`-Schreibzugriff kann Claude Variables selbst erstellen, Modes/Scopes setzen und an Properties binden.** Der `figma-stylesheet-workaround.md` ist nur noch Fallback/Archiv.

### Claude Skill installieren
Den `figma-automation` Skill lokal installieren damit Claude bei jeder Figma-Erwähnung automatisch die richtigen Dateien lädt:
→ [`figma-automation-skill.md`](./figma-automation-skill.md) herunterladen → Claude.ai → Einstellungen → Skills → Skill hinzufügen

---

## Instructions for Claude

> **Whenever the user mentions Figma, load these files from this repo before starting any task:**
> 1. `figma-workflow-technisch.md` – pre-flight checklist & golden rules
> 2. `figma-api-reference.md` – what works, what doesn't, code patterns
> 3. `figma-design-principles-arkadieff.md` – design system rules
> 4. `figma-stylesheet-workaround.md` – variables workaround (LEGACY — nur noch Fallback, siehe Nr. 11)
> 5. `figma-kollaboration-workflows.md` – recommended collaboration workflows (load for workflow questions)
> 11. `figma-schreibzugriff-use_figma.md` – **Schreibzugriff-Setup (`use_figma`)**: primärer Weg = Figma-Connector direkt in Cowork/claude.ai verbinden, Fallback = Claude Code via Desktop Commander (load when Figma write access is needed, not yet connected, or failing)
>
> **Whenever the user discusses tarabao.bio content, IA, or UX/UI (independent of Figma), load:**
> 10. `ux-ui-dokumentation-tarabao.md` – content structure & UX/UI findings
>
> **Access (primär):** Repo ist öffentlich — Dateien direkt lesen via `https://raw.githubusercontent.com/amyria3/claude-figma-automation/main/<datei>`. Kein Docker, kein GitHub MCP nötig. Schreiben ins Repo: GitHub-Web-Editor via Claude in Chrome — Techniken in `github-web-editor-notes.md`.
> **Access (legacy, optional):** GitHub MCP via Docker (`github-mcp-setup.md`); Start order: 1. Docker Desktop → 2. Claude Desktop → 3. Claude.ai
> **Achtung Konsistenz:** Dokus 1–5 entstanden teils vor dem `use_figma`-Schreibzugriff. Bei Widersprüchen (z. B. zu Variables-Limitationen) gilt `figma-schreibzugriff-use_figma.md` bzw. der aktuelle `figma-use`-Skill.

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

### 4. `figma-stylesheet-workaround.md` (LEGACY)
- Stylesheet-based styling workflow — entstand als Workaround für die frühere Variables-Limitation
- Seit `use_figma`-Schreibzugriff nur noch Fallback/Archiv
- Design token templates (copy-paste ready)

### 5. `figma-kollaboration-workflows.md`
- Recommended workflows for working with Claude in Figma
- Text Styles vor Datei-Erstellung anlegen
- Frame spiegeln (EN → DE oder umgekehrt)

### 11. `figma-schreibzugriff-use_figma.md`
- Schreibzugriff auf die Figma-Canvas via Remote-MCP (`use_figma`)
- Weg 1 (primär): Figma-Connector direkt in Cowork/claude.ai verbinden — kein Terminal nötig
- Weg 2 (Fallback): Claude Code via Desktop Commander fernsteuern
- Entscheidungsbaum + verifizierter Test-Check (15.07.2026)

## Content & UX/UI-Dokumentation (tarabao.bio)

### 10. `ux-ui-dokumentation-tarabao.md`
- UX/UI- und Content-Struktur-Erkenntnisse zu tarabao.bio, getrennt von den Figma-Komponentenprinzipien
- Aktuell: Kategorien vs. Sammlungen (feste Navigationskategorien vs. thematische, produktübergreifende Sammlungen)

## User Setup & Terminal Documentation

### 6. `github-mcp-setup.md` (LEGACY, optional)
- Setup guide for GitHub MCP via Docker — nicht mehr erforderlich, Repo-Zugriff läuft via Raw-URLs
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

### 12. `github-web-editor-notes.md`
- Technische Hinweise für Claude zum Bearbeiten von Repo-Dateien über den GitHub-Web-Editor (CodeMirror 6)
- selectAll+insertText-Komplettersatz, Virtualisierung, Preview-Verifikation, Commit-Workflow

---

## Feature Status

| Feature | Status | Notes |
|---------|--------|-------|
| Schreibzugriff auf Canvas (`use_figma`) | ✅ Working | via Figma-Connector (Remote-MCP), verifiziert 15.07.2026 |
| Text operations | ✅ Working | All typography properties supported |
| Styling (colors, fills) | ✅ Working | Can read & apply colors |
| Flex layouts | ✅ Working | VERTICAL, HORIZONTAL, alignment |
| Node operations | ✅ Working | Create, delete, rename |
| Verification via get_metadata() | ✅ Working | XML-based confirmation |
| Variables (create/link) | ✅ Working | via `use_figma` (früher ❌ — doc #4 nur noch Fallback) |

## Related

- [Figma Plugin API Docs](https://www.figma.com/plugin-docs/)
- [Claude MCP Documentation](https://docs.anthropic.com/)

## Last Updated

July 15, 2026
