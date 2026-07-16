# GitHub MCP Setup (LEGACY, optional)

> **Stand Juli 2026: Dieses Setup ist nicht mehr erforderlich.** Das Repo ist öffentlich — Claude liest die Dateien direkt via Raw-URLs (`https://raw.githubusercontent.com/amyria3/claude-figma-automation/main/<datei>`); Schreiben läuft über den GitHub-Web-Editor via Claude in Chrome (Techniken: `github-web-editor-notes.md`). Die folgende Anleitung gilt nur noch, wenn der GitHub MCP via Docker bewusst genutzt werden soll.

## Docker-Voraussetzung (nur für dieses Legacy-Setup)

**Wenn** der GitHub MCP genutzt wird, ist Docker sowohl für Claude.ai als auch für Claude Desktop nötig.

**Startreihenfolge:**
1. **Docker Desktop** starten → warten bis Whale-Icon stabil ist
2. **Claude Desktop** starten
3. **Claude.ai** im Browser öffnen

**Kein GitHub-Zugriff?** → Docker läuft nicht. Terminal:
```bash
open -a Docker   # Docker starten
docker ps        # Prüfen ob es läuft
```

---

## Setup via Docker

### Voraussetzungen
- Docker Desktop installiert (docker.com) und gestartet
- Claude Desktop App installiert
- GitHub Personal Access Token (PAT) mit Repo-Zugriff

### Konfigurationsdatei
**Pfad:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
"mcpServers": {
  "github": {
    "command": "docker",
    "args": [
      "run", "-i", "--rm",
      "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
      "ghcr.io/github/github-mcp-server"
    ],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "DEIN_PAT_HIER"
    }
  }
}
```

> **Erster Start:** Das Docker-Image wird automatisch heruntergeladen — dauert beim ersten Mal etwas länger.

### PAT erstellen / erneuern
1. github.com → Settings → Developer Settings → Personal Access Tokens
2. „Fine-grained token" → Repository-Zugriff auf gewünschte Repos
3. Token sofort kopieren (wird nur einmal angezeigt)
4. Token anstelle von `DEIN_PAT_HIER` eintragen

### Diagnose

| Befehl | Zweck |
|--------|-------|
| `open -a Docker` | Docker Desktop starten |
| `docker ps` | Prüfen ob Docker läuft |
| `docker images \| grep github-mcp-server` | Image vorhanden? |
| `cat ~/Library/Application\ Support/Claude/claude_desktop_config.json` | Config anzeigen |
| `open ~/Library/Application\ Support/Claude/claude_desktop_config.json` | Config im Editor öffnen |
| `cat ~/Library/Logs/Claude/mcp-server-github.log` | Fehler-Log anzeigen |

### Sicherheit
- PAT **niemals** in Screenshots, Chats oder öffentlichen Dateien teilen
- Bei Verdacht sofort auf github.com/settings/tokens widerrufen und neu erstellen
- Docker muss **vor** Claude Desktop gestartet sein
