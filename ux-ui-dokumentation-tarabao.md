# UX/UI-Dokumentation Tarabao

Sammlung von UX/UI- und Content-Struktur-Erkenntnissen zu tarabao.bio, die für Figma-Arbeit, Sitemap-Modellierung und Frontend-Umsetzung relevant sind. Ergänzt die komponentenbezogenen Prinzipien in `figma-design-principles-arkadieff.md`.

---

## Content-Struktur: Kategorien vs. Sammlungen

### Feste Kategorien (Navigation)
- Bilden die Hauptnavigation und die Sitemap-Baumstruktur.
- Jedes Produkt gehört zu **genau einer** festen Kategorie – exklusiv!
- Beispiele: Nüsse, Trockenfrüchte, Saaten & Superfoods, Feinkost, Müsli & Backen, Snacks.

### Sammlungen (thematische Produktgruppen)
- Zusätzliche, thematische Zusammenstellungen quer durch mehrere feste Kategorien.
- Ein Produkt kann in **mehreren** Sammlungen gleichzeitig auftauchen – nicht exklusiv.
- Eigene URLs/Kollektionsseiten, aber **nicht** Teil des Kategorie-Baums.
- Beispiele: "Alles fürs Radfahren", "Alles mit Schokolade", "Alles zum Selbstbacken", "Im Pfandglas", "Neu", "Voll beliebt", "Im Angebot" (noch zu verifizieren).
- Ob und wie Sammlungen in der Hauptnavigation angezeigt werden, wird später besprochen und ggf. implementiert._

*(Weitere UX/UI-Erkenntnisse werden hier ergänzt.)*


### Für Claude
#### Korrektur ggü. bisheriger Sitemap-Arbeit
- "Im Pfandglas" wurde in einer früheren Sitemap-Version fälschlich als feste Kategorie mit eigenen Unterkategorien modelliert. Tatsächlich ist es vermutlich eine Sammlung/Verpackungsfilter, der quer durch die festen Kategorien geht.
- Für zukünftige Sitemap-Arbeit: Sammlungen visuell/strukturell getrennt von festen Kategorien darstellen, nicht als gleichwertige Äste im Baum.
- Offen: zu verifizieren, ob "Aufbewahren" und "Im Angebot" echte feste Kategorien oder ebenfalls Sammlungen sind.

---


