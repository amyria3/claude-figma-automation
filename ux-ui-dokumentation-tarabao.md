# UX/UI-Dokumentation Tarabao

Sammlung von UX/UI- und Content-Struktur-Erkenntnissen zu tarabao.bio, die für Figma-Arbeit, Sitemap-Modellierung und Frontend-Umsetzung relevant sind. Ergänzt die komponentenbezogenen Prinzipien in `figma-design-principles-arkadieff.md`.

---

## Content-Struktur 
### Kategorien vs. Sammlungen
#### Feste Kategorien (Navigation)
- Bilden die Hauptnavigation und die Sitemap-Baumstruktur.
- Jedes Produkt gehört zu **genau einer** festen Kategorie – exklusiv!
- Beispiele: Nüsse, Trockenfrüchte, Saaten & Superfoods, Feinkost, Müsli & Backen, Snacks.

#### Sammlungen (thematische Produktgruppen)
- Zusätzliche, thematische Zusammenstellungen quer durch mehrere feste Kategorien.
- Ein Produkt kann in **mehreren** Sammlungen gleichzeitig auftauchen – nicht exklusiv.
- Eigene URLs/Kollektionsseiten, aber **nicht** Teil des Kategorie-Baums.
- Beispiele: "Alles fürs Radfahren", "Alles mit Schokolade", "Alles zum Selbstbacken", "Im Pfandglas", "Neu", "Voll beliebt", "Im Angebot" (noch zu verifizieren).
- Ob und wie Sammlungen in der Hauptnavigation angezeigt werden, wird später besprochen und ggf. implementiert._

## Komponenten (Liste)
- Footer: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6315-16206&m=dev]
- NavBar: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3175-6184&m=dev]
- Header window-w-min 1260: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=1-105&m=dev]
- Header window-w-max 1259: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3175-9316&m=dev&t=IFmWKRz9vuqv2YMT-1]
- Payment [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3501-5794&m=dev]


*(Weitere UX/UI-Erkenntnisse werden hier ergänzt.)*


## Buttons: Hug / Fill / Fixed-Verhalten
- Figma übersetzt Hug/Fill-Einstellungen manchmal in absolute Fixed-Werte. Das ist nicht so gedacht – Ausnahmen sind Min/Max-Constraints und bewusst gesetzte Fixwerte. In 99% der Fälle sind Fixwerte mit einer Variable verknüpft, nicht hart kodiert. Immer die Properties Fixed / Fill / Hug prüfen statt absolute Werte zu übernehmen.
- Das Hintergrund-SVG passt sich grundsätzlich an das Mutter-Frame an.
- Buttons für Tarabao sind so gebaut, dass Hintergrund und Rahmen ein SVG sind.
- Sizing-Regeln Button / Label:
  - Button = Fill → Label = Fill + truncate.
  - Button = Fixed → Label = Fill.
  - Button = Hug → Label = Fill.

## Nur Für Claude
#### Korrektur ggü. bisheriger Sitemap-Arbeit
- "Im Pfandglas" wurde in einer früheren Sitemap-Version fälschlich als feste Kategorie mit eigenen Unterkategorien modelliert. Tatsächlich ist es vermutlich eine Sammlung/Verpackungsfilter, der quer durch die festen Kategorien geht.
- Für zukünftige Sitemap-Arbeit: Sammlungen visuell/strukturell getrennt von festen Kategorien darstellen, nicht als gleichwertige Äste im Baum.
- Offen: zu verifizieren, ob "Aufbewahren" und "Im Angebot" echte feste Kategorien oder ebenfalls Sammlungen sind.

---


