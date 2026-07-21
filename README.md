# Claude + Figma Automation

## For the User

Dieses Repository enthält überwiegend Anweisungen und Referenzdateien, die Claude für die Automatisierung von Figma-Aufgaben braucht. Das Setup ist so gedacht, dass Claude die Dateien direkt aus dieser Repository ausliest — die Userin muss nichts manuell übertragen.

Enjoy KI, enjoy liebe*r Nutzer *in. 

### Setup (Stand Juli 2026)

**Für Figma-Schreibzugriff ist keine lokale Installation mehr nötig.**

1. In claude.ai / Cowork den **Figma-Connector** verbinden (Claude schlägt ihn bei Bedarf selbst vor → Connect klicken → OAuth-Login bei Figma bestätigen)
2. Figma-Datei-URL mit Claude teilen (Figma → Share → Copy link)

Details & Fallback-Weg: `1-figma-claude-technical/1.1-figma-schreibzugriff-use_figma.md`

### Legacy-Setup: GitHub MCP via Docker (optional, nicht mehr erforderlich)

Da diese Repo öffentlich ist, liest Claude die Dateien direkt über die Raw-URLs (siehe Instructions unten). Das Setup mit Docker funktioniert weiterhin, falls in Ausnahmefällen benötigt — Anleitung: `4-setup-legacy/4.1-github-mcp-setup.md`

### Was Claude inzwischen automatisch kann: Variables

Ursprünglich musste die Userin Variables **manuell** verknüpfen (Limitation der alten API-Anbindung). **Seit wir `use_figma`-Schreibzugriff nutzen, kann Claude ebenfalls Variables erstellen, Modes/Scopes setzen und an Properties binden.** Der `1-figma-claude-technical/1.5-figma-stylesheet-workaround.md` ist nur noch Fallback/Archiv.

### Claude Skill installieren
Es ist erforderlich, den `figma-automation` Skill lokal zu installieren, damit Claude aufs Stichwort 'Figma' die richtigen Dateien aufruft:
→ [`1-figma-claude-technical/1.6-figma-automation-skill.md`](./1-figma-claude-technical/1.6-figma-automation-skill.md) herunterladen → Claude.ai → Einstellungen → Skills → Skill hinzufügen

---

## Instructions for Claude

> **Language rule (agreed 2026-07-16, clarified 2026-07-16):** Write everything that is purely Claude-facing — instructions, technical notes, this block, commit messages — in English to reduce token usage. Exceptions: anything the user reads or edits herself, and German language examples (`3-claude-meta/3.3-german-stilguide-claude.md`). Existing German docs stay as they are; apply the rule to new or substantially rewritten content.
>
> **Scope clarification:** files under `1-figma-claude-technical/` (e.g. `1.2-figma-workflow-technisch.md`, `1.3-figma-api-reference.md`) are purely Claude-facing in their entirety, not just their new sections — translate the whole file to English when editing it, do not leave it partly German/partly English. This applies per-file, not per-added-content. Files the user actively reads or co-writes with Claude (e.g. `2-tarabao/2.1-ux-ui-dokumentation-tarabao.md`, `2-tarabao/offene-punkte.md`) stay in German regardless of this rule.
>
> **Whenever the user mentions Figma, load these files before starting any task:**
> - `1-figma-claude-technical/1.2-figma-workflow-technisch.md` — pre-flight checklist & golden rules
> - `1-figma-claude-technical/1.3-figma-api-reference.md` — what works, what doesn't, code patterns
> - `figma-design-principles-arkadieff.md` — design system rules
> - `1-figma-claude-technical/1.4-figma-kollaboration-workflows.md` — collaboration workflows (load for workflow questions)
> - `1-figma-claude-technical/1.5-figma-stylesheet-workaround.md` — variables workaround (LEGACY — fallback only, see 1.1)
> - `1-figma-claude-technical/1.1-figma-schreibzugriff-use_figma.md` — **write-access setup (`use_figma`)**: primary = Figma connector in Cowork/claude.ai, fallback = Claude Code via Desktop Commander (load when write access is needed, not yet connected, or failing)
>
> **Whenever the user discusses tarabao.bio content, IA, or UX/UI in the context of her day job (independent of Figma), load:** `2-tarabao/2.1-ux-ui-dokumentation-tarabao.md`
>
> **When editing repo files via the GitHub web editor:** `3-claude-meta/3.1-github-web-editor-notes.md`
> **When writing or correcting German text for the user:** `3-claude-meta/3.3-german-stilguide-claude.md`
> **Open tasks & unclear points:** `2-tarabao/offene-punkte.md` — check at session start, update before session end.
>
> **Access (primary):** repo is public — read files via `https://raw.githubusercontent.com/amyria3/claude-figma-automation/main/<pfad>`. No Docker, no GitHub MCP. Writing to the repo: GitHub web editor via Claude in Chrome — techniques in `3-claude-meta/3.1-github-web-editor-notes.md`.
> **Access (legacy, optional):** GitHub MCP via Docker (`4-setup-legacy/4.1-github-mcp-setup.md`); start order: 1. Docker Desktop → 2. Claude Desktop → 3. Claude.ai
> **Consistency:** docs 1.2–1.5 partly predate `use_figma` write access. On contradictions (e.g. variables limitations), `1-figma-claude-technical/1.1-figma-schreibzugriff-use_figma.md` and the current `figma-use` skill win.

---

## Verzeichnis

### 1-figma-claude-technical/ — Figma-Automatisierung (Anweisungen für Claude)

| Datei | Inhalt |
|---|---|
| `1.1-figma-schreibzugriff-use_figma.md` | Schreibzugriff via Remote-MCP (`use_figma`): Connector-Weg (primär) + Claude-Code-Fallback, Entscheidungsbaum, Test-Check (15.07.2026) |
| `1.2-figma-workflow-technisch.md` | Pre-flight Checklist, Font-Loading, Verifikation via get_metadata, Error Handling, Golden Rules |
| `1.3-figma-api-reference.md` | Komplette API-Referenz mit Code-Beispielen, Limitations, Quick-Start-Templates |
| `1.4-figma-kollaboration-workflows.md` | Empfohlene Workflows: Text Styles vor Datei-Erstellung, Frames spiegeln (EN↔DE) |
| `1.5-figma-stylesheet-workaround.md` | **LEGACY** — Stylesheet-Workaround aus der Zeit vor dem Variables-Zugriff, nur noch für Sonderfälle |
| `1.6-figma-automation-skill.md` | Downloadbare Skill-Definition für Claude (Einstellungen → Skills) |

### 2-tarabao/ — Content & UX/UI (tarabao.bio)

| Datei | Inhalt |
|---|---|
| `2.1-ux-ui-dokumentation-tarabao.md` | UX/UI- und Content-Struktur-Erkenntnisse, Kategorien vs. Sammlungen, TODOs (u.a. verwaiste Variables) |

### 3-claude-meta/ — Claudes Arbeitsweise

| Datei | Inhalt |
|---|---|
| `3.1-github-web-editor-notes.md` | Techniken für Repo-Bearbeitung über den GitHub-Web-Editor (CodeMirror 6): selectAll+insertText, Commit-Workflow |
| `3.2-claude-architektur-chat-project-memory-artefakte.md` | Wie Chats, Project Memory und Artefakte zusammenhängen; was persistent ist und was nicht |
| `3.3-german-stilguide-claude.md` | Deutscher Schreibstil für Claude: aktiv statt passiv, Verbstil, einfache Wörter — aus Darias Korrekturen abgeleitet |
| `3.4-geteilte-claude-projekte.md` | Verzeichnis geteilter Claude-Projekte (claude.ai): Zweck/Zielgruppe + Link — u. a. Geschäftsführung & IT |

### 4-setup-legacy/ — System-Setup (Legacy/optional)

| Datei | Inhalt |
|---|---|
| `4.1-github-mcp-setup.md` | **LEGACY** — GitHub MCP via Docker: PAT, Config-Pfad, Startreihenfolge, Diagnose |
| `4.2-user-system-setup-documentation.md` | macOS-Systemstand: Git, Docker, Node, Python, Homebrew |
| `user-is-learning-terminal-commands` | Terminal-Befehle mit Erklärungen — **liegt bewusst nur lokal bei der Nutzerin, wird nicht gepusht** |

### Wurzel

| Datei | Inhalt |
|---|---|
| `figma-design-principles-arkadieff.md` | Design-Prinzipien: Flex-Layouts, Naming, Spacing- & Typography-Tokens |
| `2-tarabao/offene-punkte.md` | Zentrale Liste ausschließlich für unklare Punkte und unbeendete Aufgaben — bei Session-Ende aktualisieren |
| `SCOPE.md` | Was in dieses Repo gehört und was nicht |

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
| Variables (create/link) | ✅ Working | via `use_figma` (früher ❌ — 1.5 nur noch Fallback) |

## Related

- [Figma Plugin API Docs](https://www.figma.com/plugin-docs/)
- [Claude MCP Documentation](https://docs.anthropic.com/)

## Last Updated

July 21, 2026
