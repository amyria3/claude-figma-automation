# Figma-Schreibzugriff (`use_figma`) — Setup & Nutzung

**Stand:** 15. Juli 2026 (erweitert um primären Lösungsweg, verifiziert in Session vom 15.07.2026)

## Was das ist

Figmas **Remote-MCP-Server** (`https://mcp.figma.com/mcp`) unterstützt **Schreibzugriff auf die Canvas** (aktuell kostenlose Beta) — im Gegensatz zum lokalen Dev-Mode-Server (`http://127.0.0.1:3845/mcp`, nur Lesen: `get_metadata`, `get_design_context`, `get_screenshot`).

Es gibt **zwei Wege**, diesen Remote-Server zu nutzen. Weg 1 ist der primäre.

---

## Weg 1 (PRIMÄR): Figma-Connector direkt in Cowork/claude.ai verbinden

**Kein Terminal, kein Claude Code, kein Desktop Commander nötig.** Der Figma-Remote-MCP ist als Connector im MCP-Registry von Claude verfügbar und lässt sich direkt in der Session verbinden.

> ⚠️ **Hinweis für Claude:** Dieser Weg wurde in früheren Sessions häufig übersehen und stattdessen der umständliche Claude-Code-Umweg (Weg 2) verfolgt. **Immer zuerst prüfen, ob der Figma-Connector direkt verfügbar/verbunden ist** (`search_mcp_registry` mit ["figma"] bzw. Tool-Liste nach `use_figma` durchsuchen), bevor Weg 2 in Betracht gezogen wird.

### Setup

1. Claude sucht im MCP-Registry nach "Figma" (`mcp__mcp-registry__search_mcp_registry`) und schlägt den Connector vor (`suggest_connectors`).
2. Nutzerin klickt **Connect** → Browser-OAuth-Login bei Figma bestätigen.
3. Danach stehen die Remote-MCP-Tools direkt in der Session zur Verfügung.

### Verfügbare Tools nach dem Verbinden (Auswahl)

| Tool | Wofür |
|---|---|
| `use_figma` | **Schreibzugriff**: JavaScript via Figma Plugin API ausführen (Nodes erstellen/ändern, Variablen, Komponenten etc.) |
| `get_metadata`, `get_design_context`, `get_screenshot`, `get_variable_defs` | Lesen |
| `get_figma_skill` | Pflicht-Skill `figma-use` laden (siehe unten) |
| `create_new_file`, `generate_diagram`, `search_design_system`, `whoami` | Weitere Funktionen |

**Achtung:** Die Registry-Beschreibung des Connectors listet nur Lese-Tools — `use_figma` erscheint erst **nach** dem Verbinden in der Tool-Liste. Nicht davon täuschen lassen.

### Pflicht-Vorbereitung vor jedem use_figma-Aufruf

Skill laden via `get_figma_skill` mit URI `skill://figma/figma-use/SKILL.md`, dann beim `use_figma`-Aufruf `skillNames: "resource:figma-use"` mitgeben. Wichtigste Regeln aus dem Skill:

- Code ist plain JavaScript mit top-level `await` und `return` (kein IIFE, kein `figma.closePlugin()`)
- Vor Text-Mutationen: `await figma.loadFontAsync(...)`
- Seitenwechsel nur via `await figma.setCurrentPageAsync(page)`
- Alle erzeugten/geänderten Node-IDs per `return` zurückgeben
- Max. ~10 logische Operationen pro Aufruf, inkrementell arbeiten
- Neue Top-Level-Nodes weg von (0,0) positionieren

### Test-Check nach jedem Neuaufsetzen

`use_figma` mit `fileKey` aus der Datei-URL, Code erstellt Text-Node `[TEST_SCHREIBZUGRIFF_OK]`.

✅ **Verifiziert am 15.07.2026** in der B2C-Datei (`rLwATluwV4CSS5rXceLptH`): Node `7485:2` auf Seite COVER erstellt — Schreibzugriff funktioniert direkt im Chat.

### Unterschiede zu Weg 2

- Figma-Datei muss **nicht** in der Desktop-App offen sein (Remote-Server arbeitet serverseitig).
- Datei-URL bzw. File-Key wird weiterhin benötigt (`fileKey`-Parameter).
- Auth läuft per OAuth im Browser, kein Terminal nötig.

---

## Weg 2 (FALLBACK): Claude Code via Terminal-Tool fernsteuern

Nur nötig, wenn der Connector nicht verfügbar ist. Offizielles Figma-Plugin für Claude Code (`figma@claude-plugins-official`), verbunden mit demselben Remote-MCP-Server. Läuft nur in **Claude Code** (Terminal); Claude steuert Claude Code über ein Terminal-Tool (z. B. Desktop Commander) fern.

### Installation (einmalig)

```bash
# 1. Offizielles Plugin-Marketplace hinzufügen
claude plugin marketplace add anthropics/claude-plugins-official

# 2. Figma-Plugin installieren
claude plugin install figma@claude-plugins-official

# 3. Verbindung prüfen
claude mcp list
# → sollte zeigen: plugin:figma:figma  https://mcp.figma.com/mcp (HTTP) - ! Needs authentication
```

**Authentifizierung** (braucht ein echtes, interaktives Terminal-Fenster — kein Hintergrundprozess):
```bash
claude
```
Dann in der Session z. B. eingeben: „Authentifiziere dich bei Figma" → Browser-Login bestätigen.

Danach zeigt `claude mcp list`:
```
plugin:figma:figma: https://mcp.figma.com/mcp (HTTP) - ✓ Connected
```

### Nutzung (Weg 2)

- **Figma-Datei muss in der Desktop-App offen sein.**
- Claude braucht die **Datei-URL** (Share → Copy link, Format `https://www.figma.com/design/XXXX/...`) — ohne File-Key kein Schreibzugriff.
- Vor jedem `use_figma`-Aufruf lädt Claude automatisch den Skill `figma:figma-use`.

**Typischer Ablauf (Beispielprompt):**
> „Nutze use_figma, um in [Datei-URL] auf der aktiven Seite einen Text-Node mit Inhalt '...' zu erstellen."

**Weitere relevante Skills im selben Plugin:**

| Skill | Wofür |
|---|---|
| `figma-create-new-file` | Neue Figma/FigJam/Slides-Datei anlegen |
| `figma-generate-design` | Ganze Seiten/Screens aus Code/Beschreibung bauen |
| `figma-generate-library` | Design-System (Variablen, Komponenten) aufbauen |
| `figma-generate-diagram` | Flowcharts, ERDs etc. in FigJam |
| `figma-code-connect` | Figma-Komponenten mit Code verknüpfen |

### Bekannte Stolpersteine (Weg 2)

- `claude` ohne echtes Terminal (z. B. als Hintergrundprozess) startet **keine** interaktive Session → Auth-Flow schlägt fehl. Auth einmalig im echten Terminal durchführen, danach bleibt der Token gültig.
- Lokaler Lese-Server (127.0.0.1:3845) und Remote-Schreib-Server sind **zwei getrennte Verbindungen** — beide können parallel bestehen.
- Ohne Datei-URL kann `use_figma` den File-Key nicht ermitteln, selbst wenn die Datei in Figma Desktop offen ist.

---

## Entscheidungsbaum

```
Figma-Schreibzugriff gewünscht?
├── use_figma in der Tool-Liste? → direkt nutzen (Skill figma-use vorher laden)
├── Figma-Connector im Registry? → vorschlagen, verbinden lassen → Weg 1
└── sonst → Weg 2 (Desktop Commander → Claude Code)
```
