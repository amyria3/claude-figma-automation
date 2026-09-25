# Offene Punkte & unbeendete Aufgaben — Tarabao

Zentrale Ablage **ausschließlich** für unklare Punkte und unbeendete Aufgaben rund um Tarabao (B2C-Shop, Figma-Datei „B2C-und-CI", Inhalte). Erledigtes wird gelöscht (Historie: Git-History). Details gehören in die jeweilige Fachdatei. Claude-/technikbezogene Punkte: `1-figma-claude-technical/offene-punkte.md`.

## Figma: Breiten und Breakpoints

1. **Page-Instanzen tragen einen eigenen Modus von `Lyt scl / Width`.** Product Page (8232:25333), Unser Blog (8927:28029), Mein Account (8975:27217) und die Product Page im Check-Out-Workflow (9086:29510) stehen selbst auf lg. Schaltet die Designerin die Section um, bleiben diese Seiten auf lg. Den Modus an den Instanzen entfernen (Regel in 2.5).
2. **Footer schaltet nicht mit.** Die Property `Breakpoint` der Footer-Instanzen hängt nicht an `viewport-range`, sondern steht fest auf md oder lg. Dasselbe gilt für `viewport-range` an der Nutmixer-Instanz. Binden.
3. **Welche Untergrenze bindet `Templates / Page`?** Die Page bindet min-w an `min-w-content`. Die Beschreibung von `min-w-screen` sagt „Nur an Templates / Page binden“. Entscheiden und Bindung oder Beschreibung anpassen.
4. **Beschreibungen der Breakpoint-Variablen veraltet.** `base`, `md` und `lg` sprechen von „Page-Varianten“. Die Beschreibung von `viewport-range` nennt nur Footer und Nutmixer, gebunden sind auch NavBar, Nav und PromoBar.
5. **MegaCard und MegaCards auf `Breakpoint` base · md · lg umstellen.** Beide nutzen noch die Achse `Min/Max` (min 1260 / max 1259), die Varianten von `Cards / MegaCard` tragen einen Pin auf einen gelöschten Modus von `Lyt scl / Width`.
6. **Mega Cards: 4 ungruppierte `button-LG-primary-*` ohne Code-Syntax.** Gruppieren und Code-Syntax setzen oder löschen.
7. **`Cards / ProductCard / CompactSize` bindet `Cards/DefaultSize/min-w` · `max-w` (240 · 384)** statt `Cards/CompactSize/…` (240 · 328). Umbinden ändert das Maximum auf 328.
8. **Ungenutzte Width-Variablen:** `Cards/CompactSize/min-w` und `Cards/CompactSize/Img/max-w`. Entweder CompactSize darauf umbinden oder löschen.
9. **`Primitives / ProductImg`** in `Cancellation / SelectProducts` und `OrderCancellation` nutzt `Cards/CompactSize/max-w` (328). Für ein Bild passt `Cards/CompactSize/Img/max-w` (208).

## Figma: Komponenten und Namen

10. **`Components / Nutmixer / Item`** hat zwei Properties für dasselbe: die Variante `Show Image?=False` und das Boolean `Show Image?`. Die Variante ist überflüssig.
11. **`_veraltet / Navigation / Header (window-w-min 1260)`** ist veröffentlicht und steht noch im File. Löschen?
12. **`Components / TabContent` (7448:20255)** steht noch im File, die Content Modules ersetzen es. Verwendungen prüfen, dann löschen.
13. **Component-Set „Buttons with desciptions" (4014:28940) ist kaputt.** Reparieren, umbenennen oder als Ausnahme dokumentieren.
14. **Inputs:** `Input / Input Field plain` und `Input / Component` sind parallele Sets mit denselben Feldtypen. Festlegen, welches Set gilt, und die Kategorie wählen (Vorschlag: `Components / Input / …`).
15. **Tippfehler in Figma-Namen:** `Sections / Account / Nuss-Abo Verwanltung`, `Switches / SustainabilitCategoryNavigation` und `SustainabilitCategoryNavigationButton`, Variante „Search Acrive“ an `Navigation / Header`.
16. **Komponenten ohne Kategorie-Präfix:** `ArrowUpOrDown`, `Choice`, `Information Bubble`, `NutmixerTabs`, `SustainabilitCategoryNavigationButton`.
17. **Text- und Preisfarben binden die Palette direkt statt eines semantischen Content-Text-Tokens:** Nav (Kategorie-Labels, 2761:6772), Cart / CartPage (Preis, 3155:6091), CartElements / Calculation (2260:4084), Cards / CategoryCard / MD (2638:2654), Cards / ProductCard (Name, 2356:2667), CartElements / MarketingMessage (3480:19750), Components / Checkout / ShippingAddressFormRadioButton (3782:14948), Components / Checkout / FinalCheckout (3807:19305), Primitives / InlineFeedbackElement (2337:1353). Daria korrigiert selbst.
18. **Ungebundene Rest-Werte:** Nav 1px-Paddings (2761:6816), 6× 31px `counterAxisSpacing` in den text-block-wrappern von Cards / MegaCard (wirkungslos, `layoutWrap: NO_WRAP`).
19. **Inhalt von `PaddingWrapperForScrollableContent` als Komponente anlegen.** Der Wrapper enthält in den alten Screens (Tablet 04/04b/04c, Mobile 04/04a/04b) die komplette Produktseite als kopierte Frames. Dort liegen auch stillose 48px-Headlines.

## Inhalte und Daten

20. **Welche Inhalte kommen aus dem CMS, welche aus Produktdaten?** Die Taxonomie der Content Modules ist nicht mit Lukas und Carsten abgestimmt. Beispiel: `BulletedList` und `ReviewStars` in `ContentModules / CTA` sind Produkt- bzw. Laufzeitdaten.
21. **„Im Pfandglas“:** Sammlung oder Verpackungsfilter quer durch die festen Kategorien? Ob und wie Sammlungen in der Hauptnavigation erscheinen, ist offen.

## Doku

22. **Zustände im Code:** Welche CSS-Zustände gehören zu `-hover`, `-focused`, `-selected`, `-inactive` (z. B. `hover:`, `focus-visible:`, `aria-selected`, `aria-disabled`)? Festlegen und in 2.3 §9.1 ergänzen.
23. **Schriften und Icons:** Quelle der Schriftdateien und `@font-face` für LUMOSKY, BROWN NOW ONE/TWO und Manrope; Export der Icons (SVG, `currentColor`).
24. **Grafik in 2.7:** Die dritte Beschriftung („Komponente in einen anderen“) ist abgeschnitten. Im Figma-Frame „layout-ebenen“ (9023:23570) ergänzen und neu exportieren.
