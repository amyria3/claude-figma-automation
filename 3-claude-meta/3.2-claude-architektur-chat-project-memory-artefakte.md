# Claude-Architektur: Wo liegt was?

**Chats, Projects, Memory, Artefakte, Arbeitsordner — allgemein, unabhängig von diesem Repo**

> Diese Datei ist bewusst NICHT Figma- oder Tarabao-spezifisch. Sie beschreibt, wie Claude als Produkt (Chat + Cowork) strukturell aufgebaut ist: was an einen einzelnen Chat gebunden ist, was an ein Projekt, was am Claude-Account bzw. Claude-Desktop-Programm hängt — und was ein Löschen des Chats übersteht und was nicht. Quellen: offizielle Claude-Hilfe-Artikel (support.claude.com), ergänzt um technische Beobachtungen aus eigener Systemperspektive als Agent in einer Cowork-Sitzung.

---

## 1. Grundunterscheidung: Chat vs. Cowork

Chat und Cowork teilen sich seit 2026 dieselbe Oberfläche (dieselbe Nachrichtenbox auf Web, Desktop und Mobile) — der Umschalter "Chat" / "Cowork" entscheidet, welcher Modus aktiv ist.

- **Chat:** klassische Konversation. Kein Dateizugriff, keine Shell, keine Sub-Agents.
- **Cowork:** agentischer Modus (dieselbe Architektur wie Claude Code, ohne Terminal). Direkter Zugriff auf lokale Dateien (Desktop), isolierte Shell/Code-Ausführung, Sub-Agent-Koordination für parallelisierbare Arbeit, Scheduled Tasks, Projects mit eigenem Memory.
- Cowork-Sitzungen laufen (in der Beta) **remote** auf Anthropic-Servern — sie folgen dem Account über Web/Desktop/Mobile hinweg und laufen weiter, auch wenn der Laptop zugeklappt wird. Für Aktionen, die den eigenen Rechner brauchen (lokale Dateien, Browser, Screen), reicht Claude über die geöffnete Desktop-App durch.

---

## 2. Projects — Vorsicht, zwei verschiedene Dinge mit demselben Namen

**"Chat-Projects"** (klassisch, in claude.ai) und **"Cowork-Projects"** (im Cowork-Modus) sind NICHT dasselbe, auch wenn Cowork-Projects daraus importiert werden können.

| | Chat-Project | Cowork-Project |
|---|---|---|
| Wo gespeichert | Cloud (Account-gebunden) | **Lokal auf dem Desktop-Rechner** |
| Cloud-Sync | Ja | **Nein** (aktuell keine Cloud-Synchronisierung von Projekt-Daten) |
| Enthält | Dateien, System-Instruktionen, eigenes Memory | Dateien/Ordner, Instruktionen, Scheduled Tasks, eigenes Memory |
| Voraussetzung | keine (Web/Desktop/Mobile) | **Claude Desktop** nötig (macOS/Windows) |
| Teilen (Team/Enterprise) | Ja (Projekt-Sharing) | **Nein**, aktuell nicht unterstützt |
| Erstellung | direkt in Chat | 3 Wege: "Start from scratch", "Import from a Claude project" (aus Chat-Project), "Use an existing folder" |

**Wichtig:** Ein Cowork-Project bleibt bestehen, wenn ein einzelner Chat/Task darin gelöscht wird — die Projekt-Metadaten, Dateien und das Memory des Projekts sind unabhängig vom einzelnen Task. Wird ein Cowork-Project archiviert, verschwinden nur die Metadaten aus der UI — lokale Dateien/Ordner bleiben unangetastet.

---

## 3. Memory — drei komplett getrennte Pools

Claude hat **drei isolierte Memory-Bereiche**, die nicht miteinander kommunizieren:

1. **Chat-Memory** (klassisch, außerhalb von Projects): Claude fasst Konversationen automatisch zusammen und erstellt daraus eine laufend aktualisierte Synthese (alle 24h), die als Kontext für jeden neuen Chat außerhalb von Projects dient.
2. **Chat-Project-Memory**: jedes Chat-Project hat eine eigene, getrennte Memory-/Summary-Ebene — Kontext aus einem Projekt fließt nicht in ein anderes.
3. **Cowork-Project-Memory**: analog dazu, aber lokal und Cowork-spezifisch. *"Memory is scoped to the project, so what Claude learns in one project doesn't carry over to others."* Memory aus normalen Chats fließt aktuell **nicht** in Cowork-Sitzungen — und umgekehrt.

### Technische Ebene (aus eigener Beobachtung als Agent)

Innerhalb einer Cowork-Sitzung ist das Memory faktisch ein **datei-basiertes System**, das an das jeweilige Cowork-Project ("space") gebunden ist:

- Ein Verzeichnis mit einer Index-Datei `MEMORY.md` (Kurzverweise, max. ~150 Zeichen pro Zeile, immer in den Kontext geladen).
- Einzelne Memory-Dateien als Markdown mit YAML-Frontmatter: `name`, `description`, `metadata.type` — die vier Typen sind **user** (Rolle/Präferenzen der Nutzerin), **feedback** (Korrekturen/bestätigte Vorgehensweisen), **project** (laufende Projektfakten mit Warum/Wie-Anwenden), **reference** (Verweise auf externe Systeme).
- Claude liest/schreibt diese Dateien selbständig während der Sitzung — kein manuelles Kuratieren durch die Nutzerin nötig, außer auf expliziten Wunsch ("merk dir…" / "vergiss…").

**Konsequenz fürs Chat-Löschen:** Diese Memory-Dateien hängen am **Cowork-Project**, nicht am einzelnen Chat/Task. Ein gelöschter Chat nimmt sein Memory NICHT mit — vorausgesetzt, die Erkenntnis wurde vorher tatsächlich in eine Memory-Datei geschrieben (nicht nur im Chat-Verlauf erwähnt). Was nur im Chat-Text steht und nie ins Memory-Verzeichnis geschrieben wurde, ist nach dem Löschen weg.

---

## 4. Artefakte (Artifacts)

**Was:** eigenständige, editierbare Inhalte in einem separaten Fenster neben der Konversation — Code, Dokumente (Markdown/Text), Single-Page-HTML, SVG, Diagramme, React-Komponenten. Claude erstellt ein Artefakt, wenn der Inhalt umfangreich (>~15 Zeilen), eigenständig und wahrscheinlich weiterverwendbar ist.

**Wo es "liegt":**
- Ein Artefakt erscheint zunächst NUR im jeweiligen Chat/Task, in dem es erstellt wurde.
- Es taucht **nicht automatisch** im Artifacts-Bereich der Sidebar auf — dafür muss es explizit über "Publish" veröffentlicht werden. Erst danach ist es account-weit im Artifacts-Bereich auffindbar, unabhängig vom ursprünglichen Chat.
- Ältere Chat-Versionen (durch Bearbeiten vorheriger Nachrichten) erzeugen eigene Artefakt-Versionen — ein Versions-Umschalter erlaubt den Wechsel.

**Cowork-Sonderfall — Live Artifacts:** persistente HTML-Dashboards, die sich über MCP mit angebundenen Tools verbinden und bei jedem Öffnen aktuelle Daten nachladen (kein manuelles Neu-Erstellen nötig). Können in Team-/Enterprise-Orgs innerhalb der Organisation geteilt werden. Live Artifacts und Plugins mit lokalen MCP-Servern funktionieren nur über die Desktop-App.

**Speicherorte-Kurzfassung:** vor "Publish" faktisch chat-gebunden; nach "Publish" account-gebunden (Sidebar), unabhängig vom ursprünglichen Chat.

---

## 5. Dateien & Arbeitsordner in Cowork

In einer Cowork-Sitzung gibt es mehrere unterschiedliche "Orte", die leicht verwechselt werden:

- **Verbundene Ordner** (vom Nutzer ausgewählt): echte Dateien auf dem eigenen Rechner. Claude liest/schreibt hier direkt, ohne Umweg über Up-/Download. Diese Dateien bleiben nach Sitzungsende ganz normal auf dem Rechner bestehen — unabhängig von Claude.
- **Scratchpad/Outputs-Ordner** (temporärer Arbeitsbereich): dient als Zwischenablage während der Sitzung. Wird kein verbundener Ordner genutzt, ist dies der einzige Ort, an dem Claude neue Dateien ablegen kann — sichtbar/abrufbar für die Nutzerin über die Dateifreigabe-Funktion, aber nicht zwingend dauerhaft wie ein selbst gewählter Ordner.
- **Sandboxed Linux Shell:** isolierte, sitzungseigene VM für Code-/Skript-Ausführung, getrennt vom eigentlichen Rechner der Nutzerin. Pfade in dieser Shell unterscheiden sich von den Pfaden, die die Datei-Werkzeuge (Lesen/Schreiben/Bearbeiten) sehen — ein Mapping zwischen beiden ist nötig, wenn man z. B. eine erzeugte Datei per Shell-Befehl weiterverarbeiten will.
- **Uploads:** von der Nutzerin hochgeladene Dateien, read-only, nur für die aktuelle Sitzung nutzbar.

**Sicherheitsrahmen laut offizieller Doku:** Claude kann nur in Ordnern lesen/schreiben, die explizit freigegeben wurden; Netzwerkzugriff folgt den konfigurierten Einstellungen; vor dem endgültigen Löschen von Dateien fragt Claude in Cowork immer explizit nach Erlaubnis.

---

## 6. Skills & Plugins

Skills und Plugins (Bündel aus Skills, Connectors, Sub-Agents) werden **account- bzw. Cowork-weit** installiert (über Settings), nicht an einen einzelnen Chat gebunden. Einmal hinzugefügt, stehen sie in jeder folgenden Sitzung zur Verfügung — unabhängig davon, welches Cowork-Project gerade aktiv ist.

Manche Skills liegen zusätzlich **projekt-/repo-spezifisch** ab (z. B. eigene, im GitHub-Repo gepflegte Skills wie in diesem Fall `tarabao-etiketten` oder `figma-automation`) — deren Bindung ist dann an das jeweilige Repo/Projekt gekoppelt, nicht an Claude als Programm.

---

## 7. Scheduled Tasks

An den **Account** gebunden, nicht an ein einzelnes Chat-Fenster. Sie laufen remote und unabhängig davon, ob ein Gerät gerade online ist oder die Desktop-App offen ist. Innerhalb eines Cowork-Projects lassen sich projekt-eigene Scheduled Tasks anlegen.

---

## 8. Globale vs. Ordner-/Projekt-Instruktionen

- **Global Instructions** (Settings > Cowork): gelten für **jede** Cowork-Sitzung, account-weit — z. B. bevorzugter Tonfall, Format, Rollen-Hintergrund.
- **Ordner-/Projekt-Instruktionen**: nur für das jeweilige Cowork-Project relevant, wenn ein lokaler Ordner ausgewählt wird. Claude kann diese während der Sitzung selbständig aktualisieren.

---

## 9. Zusammenfassung: Was übersteht das Löschen eines einzelnen Chats?

| Element | Gebunden an | Übersteht Löschen des Chats? |
|---|---|---|
| Chat-Verlauf selbst | einzelner Chat/Task | ❌ Nein |
| Chat-Memory-Synthese | Account (alle Nicht-Projekt-Chats) | ⚠️ Teilweise — der Beitrag dieses Chats zur Synthese verschwindet, andere bleiben |
| Chat-Project + dessen Memory | Chat-Project (Cloud) | ✅ Ja |
| Cowork-Project (Dateien, Instruktionen, Memory) | Cowork-Project (lokal, Desktop) | ✅ Ja |
| Artefakt vor "Publish" | einzelner Chat | ❌ Nein |
| Artefakt nach "Publish" / Live Artifact | Account/Organisation | ✅ Ja |
| Dateien in einem verbundenen Ordner | Dateisystem der Nutzerin | ✅ Ja (unabhängig von Claude) |
| Scratchpad/Outputs (nicht in verbundenen Ordner kopiert) | einzelne Sitzung | ❌ Nein |
| Scheduled Tasks | Account | ✅ Ja |
| Skills/Plugins | Account- bzw. Cowork-Einstellungen | ✅ Ja |
| Projekt-/repo-eigene Skill-Dateien (z. B. in GitHub) | das jeweilige Repo | ✅ Ja (unabhängig von Claude) |

**Praktische Faustregel:** Alles, was nur als Text im Chat-Verlauf existiert und nicht aktiv in eine Memory-Datei, ein veröffentlichtes Artefakt, eine Datei in einem verbundenen Ordner oder ein externes Repo geschrieben wurde, ist nach dem Löschen des Chats weg.

---

## Quellen

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Use Claude's chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)

Ergänzt um technische Beobachtungen aus eigener Systemperspektive als Agent innerhalb einer laufenden Cowork-Sitzung (Memory-Dateistruktur, Arbeitsordner-Trennung).

---

**Stand:** 14.07.2026
