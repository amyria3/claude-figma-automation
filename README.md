# Claude + Figma Automation

## For the User

Dieses Repository enthält überwiegend Anweisungen und Referenzdateien, die Claude für die Automatisierung von Figma-Aufgaben (Tarabao B2C & CI) benötigt. Claude liest die Dateien direkt aus dem Repository — du musst nichts manuell übertragen.

### Setup (aktueller Stand)

1. **Figma-Connector verbinden:** Cowork/Claude.ai → Einstellungen → Connectors → Figma → Connect (Browser-OAuth). Damit hat Claude Lese- UND Schreibzugriff (`use_figma`). Kein Docker, kein Terminal nötig.
2. **Skill installieren (empfohlen):** [`1-figma-claude-technical/1.6-figma-automation-skill.md`](./1-figma-claude-technical/1.6-figma-automation-skill.md) herunterladen → Einstellungen → Capabilities/Skills → Skill hinzufügen. Dann lädt Claude bei jeder Figma-Erwähnung automatisch die richtigen Referenzdateien. Nach Repo-Updates an 1.6 die installierte Kopie erneuern (der Skill prüft den Versionsstempel selbst und sagt Bescheid).
3. **Figma-Link teilen:** Figma → Share → Copy link. Ohne Datei-URL/File-Key kein Schreibzugriff.

> **Legacy:** Das frühere Setup über Docker + GitHub MCP ist nicht mehr nötig — Dokumentation dazu in [`4-setup-legacy/`](./4-setup-legacy/).

---

## Instructions for Claude

> **Whenever the user mentions Figma, load these files from this repo before starting any task** (via the `figma-automation` skill, or manually):
> 1. `1-figma-claude-technical/1.2-figma-workflow-technisch.md` – process: pre-flight checklist, font policy, verification, golden rules
> 2. `1-figma-claude-technical/1.3-figma-api-reference.md` – API reference (topical): execution model, fonts/text, variables, components/slots, layout, limitations
> 3. `figma-design-principles-arkadieff.md` – design system rules
> 4. `1-figma-claude-technical/1.5-figma-stylesheet-workaround.md` – LEGACY, variable edge cases only
> 5. `1-figma-claude-technical/1.4-figma-kollaboration-workflows.md` – recommended collaboration workflows
>
> **Whenever the user discusses tarabao.bio content, IA, or UX/UI (independent of Figma), load:** `2-tarabao/2.1-ux-ui-dokumentation-tarabao.md`. Design tokens / Tailwind: `2-tarabao/2.3-design-tokens-tailwind-v4.md` + the `tarabao-token-sync` skill (`1-figma-claude-technical/1.7`).
>
> **Access:** read via raw URLs (`https://raw.githubusercontent.com/amyria3/claude-figma-automation/main/<path>`) — ⚠️ raw URLs can serve **days-stale** content; verify version stamps or use the Contents API (details: `3-claude-meta/3.1-github-web-editor-notes.md`). Write via the GitHub web editor with Claude in Chrome (techniques: same file).
>
> **Language rule:** purely Claude-facing content in English; user-facing content in German.
>
> **To-do files:** check `1-figma-claude-technical/offene-punkte.md` (Claude/tech) and `2-tarabao/offene-punkte.md` (Tarabao) at session start; update before session end.

---

## Repository structure

### 1-figma-claude-technical — Claude ↔ Figma (technical)
| File | Content |
|---|---|
| `1.1-figma-schreibzugriff-use_figma.md` | Write access setup: Figma connector (primary), Claude Code fallback, decision tree |
| `1.2-figma-workflow-technisch.md` | Process: pre-flight, font policy, verification, error handling, golden rules |
| `1.3-figma-api-reference.md` | API reference & limitations, topically organized — the main technical file |
| `1.4-figma-kollaboration-workflows.md` | Recommended workflows for working together (user-facing, German) |
| `1.5-figma-stylesheet-workaround.md` | LEGACY: stylesheet workaround for variable edge cases |
| `1.6-figma-automation-skill.md` | Canonical source of the installable `figma-automation` skill |
| `1.7-tarabao-token-sync-skill.md` | Canonical source of the installable `tarabao-token-sync` skill |
| `offene-punkte.md` | Open points: Claude setup, skills, technical docs |

### 2-tarabao — Tarabao B2C content & design system
| File | Content |
|---|---|
| `2.1-ux-ui-dokumentation-tarabao.md` | Content structure & UX/UI findings, design tokens table |
| `2.2-komponenten-liste.md` | Component catalogue |
| `2.3-design-tokens-tailwind-v4.md` | Token architecture Figma → Tailwind v4 (maintainer doc) |
| `2.3-tailwind-dev-handoff.md` | Token usage for developers (consumer doc) |
| `app.tcss` | Tailwind v4 token file (mirrors Figma variables 1:1) |
| `offene-punkte.md` | Open points: Tarabao |

### 3-claude-meta — Claude meta knowledge
`3.1-github-web-editor-notes.md` (web editor techniques, raw-URL staleness), `3.2` (chat/project/memory architecture), `3.3-german-stilguide-claude.md`, `3.4` (shared projects)

### 4-setup-legacy — superseded setup docs
`4.1-github-mcp-setup.md` (Docker/GitHub MCP), `4.2-user-system-setup-documentation.md`

### Root
`figma-design-principles-arkadieff.md` (design principles), `SCOPE.md`

---

## Feature status

Maintained in one place: **`1-figma-claude-technical/1.3-figma-api-reference.md`** (limitations quick list + verification log). Highlights: variables, component swaps, slots and text-style creation all **work** via `use_figma`; the 2025/early-2026 claim "variables not supported" is obsolete (corrected 2026-07-13).

## Related

- [Figma Plugin API Docs](https://www.figma.com/plugin-docs/)
- [Claude Docs](https://docs.claude.com/)

## Last Updated

August 3, 2026
