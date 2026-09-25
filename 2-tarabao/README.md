# 2 · Tarabao B2C: Einstieg

Dieser Ordner beschreibt das Design-System des Tarabao-B2C-Shops: wie die Seiten in Figma aufgebaut sind und wie Du sie in Tailwind CSS umsetzt. Figma-Datei: [B2C und CI](https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI).

## In dieser Reihenfolge liest Du Dich ein

| # | Datei | Worum es geht |
| --- | --- | --- |
| 1 | [2.7 Layout](2.7-layout/README.md) | So bauen sich Page, Section und Komponenten auf. Hier beginnst Du. |
| 2 | [2.5 Breakpoints und Width-Variablen](2.5-breakpoints-und-width.md) | Breakpoints, Breitenbereiche und Breiten, in Figma und in Tailwind |
| 3 | [2.3 Tailwind-Dev-Handoff](2.3-tailwind-dev-handoff.md) | So nutzt Du die Tokens im Code |
| 4 | [2.2 Komponenten-Liste](2.2-komponenten-liste.md) | Katalog aller Komponenten mit Link nach Figma |
| 5 | [2.4 Buttons](2.4-buttons-aufbau.md) | Aufbau der Buttons: Fill oder Hug, SVG-Form, Code-Vertrag |
| 6 | [2.1 UX/UI-Dokumentation](2.1-ux-ui-dokumentation-tarabao.md) | Inhaltsstruktur, UX/UI-Befunde, Box-Spacing-Muster |

## Für die Pflege des Design-Systems

| Datei | Worum es geht |
| --- | --- |
| [2.3 Design-Tokens Tailwind v4](2.3-design-tokens-tailwind-v4.md) | Wie die Figma-Variablen in `app.tcss` landen, Namensregeln |
| [2.6 Breiten-Audit](2.6-breiten-audit.md) | Protokoll der Breiten-Prüfungen und offene Entscheidungen |
| [app.tcss](app.tcss) | Tailwind-v4-Token-Datei, spiegelt die Figma-Variablen 1:1 |
| [token-check/](token-check/) | Abgleich Figma ↔ `app.tcss` (`figma-dump.js`, `token_check.py`) |
| [offene-punkte.md](offene-punkte.md) | Offene Punkte für Tarabao |
