# GitHub MCP Setup für Claude Desktop

## Voraussetzungen
- Claude Desktop App installiert
- Docker Desktop installiert und gestartet
- GitHub Personal Access Token (PAT) mit Repo-Zugriff

## Konfigurationsdatei
**Pfad:** `~/Library/Application Support/Claude/claude_desktop_config.json`

Den folgenden Block in die Datei einfügen (bestehende Einträge behalten):

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

## PAT erstellen / erneuern
1. github.com → Settings → Developer Settings → Personal Access Tokens
2. "Fine-grained token" → Repository-Zugriff auf gewünschte Repos
3. Token sofort kopieren (wird nur einmal angezeigt)
4. Token anstelle von `DEIN_PAT_HIER` in `claude_desktop_config.json` eintragen

## Startreihenfolge (wichtig!)
1. **Docker Desktop** starten → warten bis Whale-Icon in Menüleiste stabil ist
2. **Claude Desktop** starten

## Nützliche Terminal-Befehle

| Befehl | Zweck |
|--------|-------|
| `docker ps` | Prüfen ob Docker läuft |
| `docker images \| grep github-mcp-server` | Prüfen ob Image vorhanden |
| `cat ~/Library/Application\ Support/Claude/claude_desktop_config.json` | Config anzeigen |
| `open ~/Library/Application\ Support/Claude/claude_desktop_config.json` | Config im Editor öffnen |
| `cat ~/Library/Logs/Claude/mcp-server-github.log` | Fehler-Log anzeigen |

## Sicherheit
- PAT **niemals** in Screenshots, Chats oder öffentlichen Dateien teilen
- Bei Verdacht sofort auf github.com/settings/tokens widerrufen und neu erstellen
- Docker muss **vor** Claude Desktop gestartet sein, sonst schlägt die Verbindung fehl
