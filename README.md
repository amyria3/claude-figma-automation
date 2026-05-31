# Claude + Figma Automation

Complete reference and workflows for automating Figma with Claude via MCP.

## Instructions for Claude

> **Whenever the user mentions Figma, load these files from this repo before starting any task:**
> 1. `figma-workflow-technisch.md` – pre-flight checklist & golden rules
> 2. `figma-api-reference.md` – what works, what doesn't, code patterns
> 3. `figma-design-principles-arkadieff.md` – design system rules
> 4. `figma-stylesheet-workaround.md` – variables workaround (load when Variables topic comes up)
>
> **Access:** via GitHub MCP Connector in Claude.ai (no Docker needed for claude.ai)  
> **Docker only required for:** Claude Desktop App

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
- Setup guide for GitHub MCP via Docker (Claude Desktop only)
- PAT creation, config file path, start order
- Diagnostic terminal commands

### 6. `user-system-setup-documentation.md`
- macOS system status (Git, Docker, Node, Python, Homebrew)
- Installed tools log

### 7. `user-is-learning-terminal-commands`
- Terminal commands with explanations for beginners
- Split into: already known / learning / not yet needed

## Quick Start

1. Create design tokens/stylesheet in Figma
2. Share screenshot with Claude
3. Claude parses values and applies to elements
4. User manually links to Figma Variables

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

May 31, 2026
