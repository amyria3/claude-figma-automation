# Offene Punkte & unbeendete Aufgaben — Tarabao

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben rund um Tarabao (B2C-Shop, Figma-Datei „B2C-und-CI", Inhalte). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei. Claude-/technikbezogene Punkte: `1-figma-claude-technical/offene-punkte.md`.

## Figma: Breiten und Breakpoints

1. **Footer in den alten Screens schaltet nicht mit.** In den Sections „max-w 1259, min-w 564 …“ (Tablet) und „max-w 563“ (Mobile) sowie einmal im Check-Out-Workflow steht `viewport-range` am Footer fest auf md oder lg, statt an der gleichnamigen Variable zu hängen. Binden oder die alten Screens entfernen.
2. **Welche Untergrenze bindet `Templates / Page`?** Die Page bindet min-w an `min-w-content`. Die Beschreibung von `min-w-screen` sagt „Nur an Templates / Page binden“. Entscheiden und Bindung oder Beschreibung anpassen.
3. **Beschreibungen der Breakpoint-Variablen veraltet.** `base`, `md` und `lg` sprechen von „Page-Varianten“. Die Beschreibung von `viewport-range` nennt nur Footer und Nutmixer, gebunden sind auch NavBar, Nav und PromoBar.
4. **MegaCard und MegaCards auf `viewport-range` base · md · lg umstellen.** Beide nutzen noch die Achse `Min/Max` (min 1260 / max 1259), die Varianten von `Cards / MegaCard` tragen einen Pin auf einen gelöschten Modus von `Lyt scl / Width`.
5. **Mega Cards: 4 ungruppierte `button-LG-primary-*` ohne Code-Syntax.** Gruppieren und Code-Syntax setzen oder löschen.
6. **`Cards / ProductCard / CompactSize` bindet `Cards/DefaultSize/min-w` · `max-w` (240 · 384)** statt `Cards/CompactSize/…` (240 · 328). Umbinden ändert das Maximum auf 328.
7. **Ungenutzte Width-Variablen:** `Cards/CompactSize/min-w` und `Cards/CompactSize/Img/max-w`. Entweder CompactSize darauf umbinden oder löschen.
8. **`Primitives / ProductImg`** in `Cancellation / SelectProducts` und `OrderCancellation` nutzt `Cards/CompactSize/max-w` (328). Für ein Bild passt `Cards/CompactSize/Img/max-w` (208).

## Figma: Komponenten und Namen

9. **`Components / Nutmixer / Item`** hat zwei Properties für dasselbe: die Variante `Show Image?=False` und das Boolean `Show Image?`. Die Variante ist überflüssig.
10. **`_veraltet / Navigation / Header (window-w-min 1260)`** ist veröffentlicht und steht noch im File. Löschen?
11. **`Components / TabContent` (7448:20255)** steht noch im File, die Content Modules ersetzen es. Verwendungen prüfen, dann löschen.
12. **Component-Set „Buttons with desciptions" (4014:28940) ist kaputt.** Reparieren, umbenennen oder als Ausnahme dokumentieren.
13. **Inputs:** `Input / Input Field plain` und `Input / Component` sind parallele Sets mit denselben Feldtypen. Festlegen, welches Set gilt, und die Kategorie wählen (Vorschlag: `Components / Input / …`).
14. **Tippfehler in Figma-Namen:** `Sections / Account / Nuss-Abo Verwanltung`, `Switches / SustainabilitCategoryNavigation` und `SustainabilitCategoryNavigationButton`, Variante „Search Acrive“ an `Navigation / Header`.
15. **Komponenten ohne Kategorie-Präfix:** `ArrowUpOrDown`, `Choice`, `Information Bubble`, `NutmixerTabs`, `SustainabilitCategoryNavigationButton`.
16. **Text- und Preisfarben binden die Palette direkt statt eines semantischen Content-Text-Tokens:** Nav (Kategorie-Labels, 2761:6772), Cart / CartPage (Preis, 3155:6091), CartElements / Calculation (2260:4084), Cards / CategoryCard / MD (2638:2654), Cards / ProductCard (Name, 2356:2667), CartElements / MarketingMessage (3480:19750), Components / Checkout / ShippingAddressFormRadioButton (3782:14948), Components / Checkout / FinalCheckout (3807:19305), Primitives / InlineFeedbackElement (2337:1353). Daria korrigiert selbst.
17. **Ungebundene Rest-Werte:** Nav 1px-Paddings (2761:6816), 6× 31px `counterAxisSpacing` in den text-block-wrappern von Cards / MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).
18. **Inhalt von `PaddingWrapperForScrollableContent` als Komponente anlegen.** Der Wrapper enthält in den alten Screens (Tablet 04/04b/04c, Mobile 04/04a/04b) die komplette Produktseite als kopierte Frames. Dort liegen auch stillose 48px-Headlines.

## Inhalte und Daten

19. **Welche Inhalte kommen aus dem CMS, welche aus Produktdaten?** Die Taxonomie der Content Modules ist nicht mit Lukas und Carsten abgestimmt. Beispiel: `BulletedList` und `ReviewStars` in `ContentModules / CTA` sind Produkt- bzw. Laufzeitdaten.
20. **„Im Pfandglas“:** Sammlung oder Verpackungsfilter quer durch die festen Kategorien? Ob und wie Sammlungen in der Hauptnavigation erscheinen, ist offen.

## Doku

21. **Zustände im Code:** Welche CSS-Zustände gehören zu `-hover`, `-focused`, `-selected`, `-inactive` (z. B. `hover:`, `focus-visible:`, `aria-selected`, `aria-disabled`)? Festlegen und in 2.6 §9.1 ergänzen.
22. **Schriften und Icons:** Quelle der Schriftdateien und `@font-face` für LUMOSKY, BROWN NOW ONE/TWO und Manrope; Export der Icons (SVG, `currentColor`).
23. **Grafik in 2.7:** Die dritte Beschriftung („Komponente in einen anderen“) ist abgeschnitten. Im Figma-Frame „layout-ebenen“ (9023:23570) ergänzen und neu exportieren.
