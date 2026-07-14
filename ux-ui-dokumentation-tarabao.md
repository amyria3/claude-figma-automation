# UX/UI-Dokumentation Tarabao

Sammlung von UX/UI- und Content-Struktur-Erkenntnissen zu tarabao.bio, die für Figma-Arbeit, Sitemap-Modellierung und Frontend-Umsetzung relevant sind. Ergänzt die allgemeineren Prinzipien in `figma-design-principles-arkadieff.md`.

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

### Header, Footer & Navigation
- NavBar: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3175-6184&m=dev]
- Nav: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2761-6772&m=dev]
- NavBlocks: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3164-5344&m=dev]
- Header / window-w-min 1260: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=1-105&m=dev]
- Header / window-w-max 1259: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3175-9316&m=dev]
- Footer: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6315-16206&m=dev]
- Checkout (Kontakt-/E-Mail-Schritt, ehem. "Payment"): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3501-5794&m=dev]
- Cart / CartPage: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3155-6091&m=dev]

### Sections
- Section / Search & Filter: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2302-2041&m=dev]
- Section / MegaCards: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2156-4072&m=dev]
- Section / Hero: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6604-17025&m=dev]
- Section / ContactForm: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6810-17863&m=dev]
- Section / CardRow: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6604-17026&m=dev]
- Section / ProductHeader: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=4221-28723&m=dev]
- Section / Accordion: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6604-17023&m=dev]
- Section / Tabs / DesktopSize: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=7448-19299&m=dev]
- Section / Editorial: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3164-4506&m=dev]
- Section / BlogCards: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6605-16723&m=dev]

### Cards
- Cards / ProductCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2356-2667&m=dev]
- Cards / CategoryCard / SM: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2628-2698&m=dev]
- Cards / CategoryCard / MD: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2638-2654&m=dev]
- Cards / MegaCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2143-2061&m=dev]
- Cards / VoucherCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3912-19811&m=dev]
- Cards / PromotionPostCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3912-19740&m=dev]
- Cards / ReviewCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2194-1982&m=dev]
- Cards / Featured: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6704-18568&m=dev]
- Cards / DiscoveryCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6708-16673&m=dev]
- Cards / PurchaseCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6748-17300&m=dev]
- Cards / Insta: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2066-1664&m=dev]
- Cards / BlogCard: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=380-881&m=dev]

### CartElements
- CartElements / Summary: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3307-5882&m=dev]
  - CartElements / LogIn: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3238-10265&m=dev]
  - CartElements / ProductItem: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3280-9437&m=dev]
  - CartElements / Calculation (steckt in generisch benanntem Wrapper-Frame "wrapper"): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2260-4084&m=dev]
  - CartElements / VoucherInput: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3325-5910&m=dev]
  - CartElements / MarketingMessage: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3480-19750&m=dev]

### Account
- Account / LogInStatus: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3220-18844&m=dev]
- Account / CollapsibleSection: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3912-19582&m=dev]
  - Components / Account / SummaryItem: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3941-19715&m=dev]
  - Components / Account / DataBlock: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3941-19858&m=dev]

### Components / Checkout
- Components / Checkout / OrderConfirmation: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3826-18648&m=dev]
- Components / Checkout / Payment: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3773-14405&m=dev]
- Components / Checkout / DeliveryAddress: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3674-12341&m=dev]
- Components / Checkout / Identification: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6617-16895&m=dev]
- Components / Checkout / AddressFieldset: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3685-13778&m=dev]
- Components / Checkout / SummaryDataset: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3773-11559&m=dev]
- Components / Checkout / WelcomeDataset: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3501-6526&m=dev]
- Components / Checkout / ShippingAddressFormRadioButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3782-14948&m=dev]
- Components / Checkout / DeliveryMethodRadioGroup: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3674-12469&m=dev]
- Components / Checkout / VoucherUIPattern: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2406-2720&m=dev]
- Components / Checkout / Contact: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3953-24967&m=dev]
- Components / Checkout / FinalCheckout: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3807-19305&m=dev]

### Components / Cancellation
- Components / OrderCancellation: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6811-20710&m=dev]
  - Components / Cancellation / SelectOrder: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6811-20517&m=dev]
  - Components / Cancellation / SelectProducts: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6810-20264&m=dev]
- Components / SearchPurchase (Name in Figma noch als "SearchPurchease" zu korrigieren; steckt in generischem Wrapper "wrapper"): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6955-21898&m=dev]

### Components (Sonstige)
- Components / Product / BuyBox: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3175-5241&m=dev]
- Components / Product / ImageCarousel: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2531-2860&m=dev]
- Components / BlockElements / Newsletter: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6315-17848&m=dev]
- Components / RadioButtonGroup: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3793-15664&m=dev]
- Components / Disclosure: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=283-633&m=dev]
- Components / OverlayComponents / Message: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2784-3621&m=dev]
- Components / TabContent: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=7448-20255&m=dev]

### Filter & Search
- Filter / FilterPanel: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2211-2165&m=dev]
  - Filter / FilterChip: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2165-2011&m=dev]
  - Filter / PriceFilterInputField: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2810-2830&m=dev]
  - Filter / PriceFilterInput: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2849-1395&m=dev]
  - Filter / PriceRange: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2605-2931&m=dev]
    - Filter / PriceRange / Drop Down Button: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2829-2901&m=dev]
    - Filter / PriceRange / Chip: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6093-25636&m=dev]
    - Filter / PriceRange / Chips: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2609-2771&m=dev]
- Search / Input: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2339-2155&m=dev]
- Search / QueryState: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2216-2060&m=dev]

### Buttons
- Buttons / LG / PrimaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=509-1251&m=dev]
- Buttons / LG / Inline: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2342-2047&m=dev]
- Buttons / MD / PrimaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2310-2156&m=dev]
- Buttons / MD / SecondaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2342-2052&m=dev]
- Buttons / SM / PrimaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2342-2053&m=dev]
- Buttons / SM / SecondaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6799-19379&m=dev]
- Buttons / SM / Inline: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2359-3245&m=dev]
- Buttons / SM / Segment Control: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3658-9719&m=dev]
- Buttons / XS / ToggleButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=272-2159&m=dev]
- Buttons / XS / SegmentControlButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3925-20314&m=dev]
- Buttons / XXS / PrimaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2328-2172&m=dev]
- Buttons / XXS / SecondaryButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3911-18672&m=dev]
- Buttons / XXS / Inline: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3517-8568&m=dev]
- Buttons / XXXS / Inline: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6799-20185&m=dev]
- Buttons / IconButton: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2588-2421&m=dev]
- Buttons / Radio: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3795-12348&m=dev]
- Buttons / CarouselNav: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2038-4884&m=dev]
- Buttons / Payment: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3230-22134&m=dev]
- Buttons / Counter: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2442-2491&m=dev]
- Buttons / ReactionCounter: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2070-1506&m=dev]
- Buttons / PlusMinus: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2228-2503&m=dev]
- TabControl (ohne "Buttons /"-Präfix, liegt aber im Buttons-Ordner): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3970-22955&m=dev]
- Layout / PromoBar (steckt in einem generisch benannten Wrapper-Frame "fr"): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3164-11788&m=dev]
- Add to Basket for mobile (ohne "Buttons /"-Präfix): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3986-23589&m=dev]

### Inputs
- Input Field plain (großes Variant-Set: Voucher, E-mail, Passwort, Land, Vorname, Nachname, Addresse, Telefonnummer, PLZ, Stadt, Bestellnummer): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2406-1053&m=dev]
- Input (paralleles Variant-Set mit "Nr="-Nummerierung statt Boolean-Properties, gleiche Feldtypen; Hinweis: manchmal steht ein Button neben dem Input): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2328-2155&m=dev]

### Patterns
- Patterns / ValidationSign: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2406-1344&m=dev]
- Patterns / BulletedList: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=4221-27964&m=dev]
- Patterns / Inline Question & Button: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6072-33346&m=dev]
- Patterns / InlineFeedbackElement: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2337-1353&m=dev]
- Patterns / PurchaseSummary (Name in Figma noch als "PurcheaseSummary" zu korrigieren): [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6794-18851&m=dev]
- Patterns / Ingredients: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=7448-20925&m=dev]
- Patterns / CarouselThumbnail: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2543-2114&m=dev]
- Patterns / ProductImg: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6810-20272&m=dev]
- Patterns / TextAndImg: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=7448-20380&m=dev]
- Patterns / SearchInput: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2171-2737&m=dev]
- Patterns / TableElement: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2040-1345&m=dev]
- Patterns / Breadcrumb: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=3155-5202&m=dev]
- Patterns / InputText: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=2182-1829&m=dev]
- Patterns / UserMessage & Explanation: [https://www.figma.com/design/rLwATluwV4CSS5rXceLptH/B2C-und-CI?node-id=6811-20757&m=dev]

*(Weitere UX/UI-Erkenntnisse werden hier ergänzt.)*

---

## 🔤 Design Tokens: Text Styles

Stand 14.07.2026, ausgelesen aus der Komponentenbibliothek-Section (`get_variable_defs` auf Node 3267:6614, "PATTERNS, BUTTONS, ELEMENTS, COMPONENTS" — deckt alle Top-Level-Sections außer den Screens/Mockups in "PAGES" ab; ggf. existieren dort noch weitere, hier nicht erfasste Styles).

| Style-Name | Font-Familie | Stil | Größe | Gewicht | Line-Height | Letter-Spacing |
|---|---|---|---|---|---|---|
| Label/default | BROWN NOW TWO | TWO | 16 | 400 | 16 | 0 |
| Label/Selected | BROWN NOW ONE | ONE | 16 | 400 | 16 | 0 |
| UserMessage/LG | BROWN NOW TWO | TWO | 16 | 400 | 16 ([twuc]-4) | -2 |
| UserMessage/X-LG | BROWN NOW TWO | TWO | 20 | 400 | 16 ([twuc]-4) | -2 |
| UserMessage/Default | Manrope | Regular | 12 | 400 | 12 | 0 |
| Input/InputText | Manrope | Regular | 18 | 400 | 14 | 2 |
| Input/LabelDefault | Manrope | Regular | 14 | 400 | 14 | -1 |
| Input/Label SM | Manrope | Light | 9 | 300 | 9 | -1 |
| Input/Warning&DefaultText | Manrope | Regular | 12 | 400 | 14 | 0 |
| Cards/ProductTitle | Manrope | Bold | 16 | 700 | 18 | 2 |
| Cards/MD | BROWN NOW TWO | TWO | 22 | 400 | 14 | 5 |
| Cards/Light | Manrope | Light | 10 | 300 | 10 | -3 |
| Cards/MegaCard/Lumo | LUMOSKY | Regular | 40 | 400 | 40 | 6 |
| Cards/MegaCard/Body | Manrope | Regular | 20 | 400 | 28 ([twuc]-7) | -2 |
| Cards/Featured/Title | LUMOSKY | Regular | 24 | 400 | 30 | -3 |
| Cards/Blog/Title | Manrope | Light | 19 | 300 | 1.3 | 0 |
| Buttons/LG | BROWN NOW ONE | ONE | 34 | 400 | 40 | -2 |
| Buttons/LG Underlined | BROWN NOW ONE | ONE | 34 | 400 | 40 | 2 |
| Buttons/MD | BROWN NOW TWO | TWO | 24 | 400 | 0.8 | 5 |
| Buttons/MD Underlined | BROWN NOW TWO | TWO | 24 | 400 | 0.8 | 5 |
| Buttons/SM | BROWN NOW ONE | ONE | 20 | 400 | 20 | -2 |
| Buttons/X-SM | BROWN NOW TWO | TWO | 18 | 400 | 18 | -2 |
| Buttons/XX-SM | BROWN NOW ONE | ONE | 14 | 400 | 16 | -2 |
| Buttons/XX-SM underlined | BROWN NOW ONE | ONE | 14 | 400 | 16 | -2 |
| Buttons/XXXS Inline | BROWN NOW ONE | ONE | 12 | 400 | 12 | -2 |
| Buttons/Quantity&Packaging | Manrope | SemiBold | 14 | 600 | 14 | 0 |
| H1 Subtitle | BROWN NOW TWO | TWO | 40 | 400 | 0.8 | -2 |
| H2 | LUMOSKY | Regular | 32 | 400 | 1 | 2 |
| H2 Produktkategorie | LUMOSKY | Regular | 40 | 400 | 1 | 2 |
| H2 Subtitle | BROWN NOW TWO | TWO | 24 | 400 | 24 | -2 |
| H2 Alternative | BROWN NOW ONE | ONE | 26 | 400 | 1 | 6 |
| H3 | BROWN NOW ONE | ONE | 26 | 400 | 20 | -2 |
| DefaultText LG | Manrope | Light | 16 | 300 | 1.2 | 0.5 |
| DefaultText MD | Manrope | Regular | 14 | 400 | 1.5 | 1.5 |
| DefaultText S | Manrope | Regular | 12 | 400 | 100 (%) | 0 |
| BulletPoints | Manrope | Regular | 14 | 400 | 100 (%) | 0 |
| Link | Manrope | SemiBold | 16 | 600 | 18 | -1 |
| Comment | Manrope | Light | 12 | 300 | 16 | 0 |
| Comment/BodyText | Manrope | Regular | 16 | 400 | 100 (%) | 0 |
| Navigation/Route | Manrope | Medium | 12 | 500 | 1 | 5 |
| Navigation/FullScreen/MainCategory | Manrope | ExtraBold | 16 | 800 | 1.1 | 0 |
| Navigation/FullScreen/SubCategory | Manrope | SemiBold | 16 | 600 | 1.1 | 0 |
| Navigation/SideNavigation/MainCategory | Manrope | SemiBold | 13 | 600 | 13 | 0 |
| Navigation/SideNavigation/SubCategory | Manrope | Regular | 14 | 400 | 14 | 0 |
| ProductPage/ProductTitle | Manrope | ExtraBold | 24 | 800 | 26 | 0 |
| ProductPage/Hightlighted | Manrope | ExtraBold | 16 | 800 | 0.8 | 0 |
| ProductPage/Dropdown/Summary | Manrope | Bold | 18 | 700 | 18 | 1 |
| ProductPage/Dropdown/H3 ManufacturerName | Manrope | SemiBold | 16 | 600 | 100 (%) | 1 |
| ProductPage/Dropdown/H4 Question | Manrope | Regular | 16 | 400 | 26 | 0 |
| ProductPage/Dropdown/BodyText - Responce | Manrope | Regular | 16 | 400 | 26 | 0 |
| ShoppingCart & Checkout/MainHeadline | BROWN NOW TWO | TWO | 34 | 400 | 1 | -2 |
| ShoppingCart & Checkout/Headline | Manrope | ExtraBold | 14 | 800 | 14 | -1 |
| ShoppingCart & Checkout/Body | Manrope | Medium | 14 | 500 | 14 | 0 |
| ShoppingCart & Checkout/Subtle | Manrope | Regular | 11 | 400 | 11 | 0 |
| ShoppingCart & Checkout/Hightlighted | Manrope | Bold | 14 | 700 | 14 | -3 |
| DataBlocks/SummaryItemTitle | Manrope | Medium | 16 | 500 | 16 | 0 |
| DataBlocks/SummaryItemContent | Manrope | Regular | 14 | 400 | 18 | 0 |
| PriceRangeFilter/Label | Manrope | Medium | 10 | 500 | 10 | 0 |
| Table/\<th\> | Manrope | SemiBold | 18 | 600 | 18 | 0 |
| Table/Cell | Manrope | Regular | 20 | 400 | 20 | 0 |

*Hinweis: "100 (%)" bei Line-Height bedeutet 100% Zeilenhöhe (relativ zur Schriftgröße), keine feste px-Angabe — anders als die übrigen Zeilen, die meist einen px- oder Multiplikator-Wert zeigen.*

---

## 📐 Design Tokens: Box-Spacing & Gap

Beide Skalen verwenden — soweit im gescannten Bereich vorhanden — **identische px-Werte pro Größenlabel**, lassen sich also in einer gemeinsamen Tabelle führen. Rem-Werte auf Basis von 16px = 1rem (Browser-Standard):

| Label | px | rem |
|---|---|---|
| xxxs | 2 | 0,125rem |
| xxs | 4 | 0,25rem |
| xs | 6 | 0,375rem |
| sm | 8 | 0,5rem |
| md-sm | 12 | 0,75rem |
| md | 16 | 1rem |
| md-l | 20 | 1,25rem |
| lg | 28 | 1,75rem |
| xl | 40 | 2,5rem |
| xxl | 48 | 3rem *(im gescannten Bereich nicht als Gap gefunden, nur als Box-Spacing)* |
| xxxl | 56 | 3,5rem *(im gescannten Bereich nicht als Gap gefunden, nur als Box-Spacing)* |

**Wichtig — Namenskollision mit einer dritten, unabhängigen Skala:** Es gibt zusätzlich eine Variable-Familie `spacings/spacing-*`, die dieselben Größenlabels (xxxs, xxs, xs, sm, md, lg) verwendet, aber **andere px-Werte** liefert — diese Familie ist stattdessen direkt an die Tailwind-Spacing-Einheit (`n-tcss` = n × 4px) gekoppelt:

| Label | Tailwind-Einheit (tcss) | px | rem |
|---|---|---|---|
| xxxxs | 0,5 tcss | 2 | 0,125rem |
| xxxs | 1 tcss | 4 | 0,25rem |
| xxs | 2 tcss | 8 | 0,5rem |
| xs | 3 tcss | 12 | 0,75rem |
| sm | 4 tcss | 16 | 1rem |
| md | 5 tcss | 20 | 1,25rem |
| lg | 10 tcss | 40 | 2,5rem |
| xxxxl | 14 tcss | 56 | 3,5rem |

**Beispiel Kollision:** `box-spacing-xxxs` = 2px (0,125rem), aber `spacings/spacing-xxxs` = 4px (0,25rem) — gleiches Label "xxxs", unterschiedliche Skala. Beim Lesen von Variable-Namen immer auf das Präfix achten (`box-spacing-`/`gap-` vs. `spacings/spacing-`), nicht nur auf das Größenlabel.

---

## 📏 Design Tokens: Tailwind-Utility-Scale ↔ Figma-px (persönliche Referenz, nur für Maria)

Aus der Variable-Familie `[twuc]-N (X rem)` — zeigt, welche Tailwind-rem-Werte tatsächlich im File verwendet werden, statt nur die resultierenden px-Zahlen zu sehen. Formel bei korrekter Umsetzung: `px = N × 4`, `rem = N × 0,25`.

| [twuc]-N | rem | px (Figma-Wert) | px nach Formel (N×4) | Stimmt überein? |
|---|---|---|---|---|
| 4 | 1rem | 16 | 16 | ✅ |
| 7 | 1,75rem | 28 | 28 | ✅ |
| 8 | 2rem | 32 | 32 | ✅ |
| 9 | 2,25rem | 36 | 36 | ✅ |
| 10 | 2,5rem | 40 | 40 | ✅ |
| 11 | 2,75rem | 44 | 44 | ✅ |
| 12 | 3rem | 48 | 48 | ✅ |
| 15 | 3,75rem | 60 | 60 | ✅ |
| 16 | 4rem | 64 | 64 | ✅ |
| 18 | 4,5rem | 72 | 72 | ✅ |
| 20 | 5rem | 80 | 80 | ✅ |
| 22 | 5,5rem | 88 | 88 | ✅ |
| 24 | 6rem | 96 | 96 | ✅ |
| 28 | 7rem | 112 | 112 | ✅ |
| 32 | 8rem | 128 | 128 | ✅ |
| 40 | 10rem | **144** | 160 | ❌ (−16px = −1rem) |
| 41 | 10,25rem | 164 | 164 | ✅ |
| 48 | 12rem | **176** | 192 | ❌ (−16px = −1rem) |
| 56 | 14rem | 224 | 224 | ✅ |
| 60 | 15rem | 240 | 240 | ✅ |
| 64 | 16rem | 256 | 256 | ✅ |
| 96 | 24rem | 384 | 384 | ✅ |
| 112 | 28rem | 448 | 448 | ✅ |
| 128 | 32rem | 512 | 512 | ✅ |
| 160 | 40rem | 640 | 640 | ✅ |
| 192 | 48rem | **674** | 768 | ❌ (−94px) |
| 224 | 56rem | 896 | 896 | ✅ |

**Auffällig:** Drei Werte weichen von der Formel ab: `[twuc]-40` (zeigt 144px statt 160px), `[twuc]-48` (zeigt 176px statt 192px) — beide exakt um 16px/1rem zu niedrig, ein systematisches Muster, das nach einem Tippfehler oder einer versehentlich falsch verknüpften Variable aussieht. `[twuc]-192` weicht stärker ab (674px statt 768px) — hier ist unklar, ob das ein bewusster Sondertwert (z.B. ein spezifischer Breakpoint) oder ebenfalls ein Fehler ist. Alle drei ggf. in Figma direkt gegenprüfen.

---

## ✅ Offene TODOs (Figma-Schreibzugriff nötig — Claude kann nur lesen)

Claude hat aktuell nur lesenden Zugriff auf Figma (Dev Mode MCP Server). Folgende Korrekturen müssen manuell in Figma vorgenommen werden (oder sobald ein schreibfähiger Figma-Connector verbunden ist):

### 1. Drei `[twuc]`-Werte korrigieren (siehe Tabelle oben)
- `[twuc]-40`: 144px → **160px**
- `[twuc]-48`: 176px → **192px**
- `[twuc]-192`: 674px → vermutlich **768px** (Ursache/Absicht unklar, bitte gegenprüfen)

### 2. `spacings/spacing-*`-Bindungen durch `gap-*`/`box-spacing-*` ersetzen
Regel: **Gap-Variable für Flexbox-Gaps, Box-Spacing-Variable für Padding/Margin.** Labels sind zwischen den Skalen NICHT wertgleich (`spacing-md`=20px ≠ `gap-md`=16px) — immer nach dem tatsächlichen px-Wert mappen, nicht nach Label-Name.

Bisher bekannte Fundstellen (Stichprobe aus 5 geprüften Komponenten, keine vollständige Suche):

| Komponente | Property | Bisherige Variable | Neue Variable |
|---|---|---|---|
| Filter/FilterPanel (2211:2165), äußerer Container | gap | spacings/spacing-xxxs (4px) | **gap-xxs (4px)** |
| NavBar (1:115), "Icons / Tools"-Reihe | gap | spacings/spacing-md (20px) | **gap-md-l (20px)** |
| Components/Product/BuyBox, "Titel und Bewertungen" | gap | spacings/spacing-xs (12px) | **gap-md-sm (12px)** |
| Components/Product/BuyBox, "Titel und Bewertungen" | padding-bottom | spacings/spacing-md (20px) | **box-spacing-md-l (20px)** |
| Components/Product/BuyBox, "Benefits"-Liste | gap | spacings/spacing-xxs (8px) | **gap-sm (8px)** |
| Components/Product/BuyBox, "Benefits"-Liste | padding-bottom | spacings/spacing-md (20px) | **box-spacing-md-l (20px)** |
| Components/Product/BuyBox, "Menge, Verpackung, Preis" | gap | spacings/spacing-md (20px) | **gap-md-l (20px)** |
| Components/Product/BuyBox, Preis-Label (flex-col) | gap | spacings/spacing-xxxxs (2px) | **gap-xxxs (2px)** |
| Components/Product/BuyBox, "Menge und Preis" | gap | spacings/spacing-xxs (8px) | **gap-sm (8px)** |

### 3. Verwaiste Variables (hartkodierte Werte statt Variable-Bindung)
32 von 118 Komponenten geprüft (Stand 14.07.2026), 12 gesicherte Funde + 3 unsichere Kandidaten. Auffälligste Muster: Nav (2761:6772) hat 6× identisches hartkodiertes `gap-[6px]` in den Kategorie-Headern (Nachbar-Block "B2B Shop" im selben Component macht es korrekt → Fehler steckt im Master); Footer (6315:16206) hat mehrere hartkodierte Werte direkt neben korrekt gebundenen Geschwister-Properties; Cards/Featured und Cards/MegaCard haben durchgängig hartkodierte Paddings (20px/28px); Buttons/CarouselNav (2038:4884) reproduziert denselben Fehler in mind. 2 verschiedenen Verwendungskontexten. Vollständige Fundliste liegt lokal bereit (`verwaiste-variables-liste.md`), noch nicht hierher übertragen — Rest der 113 Komponenten (v. a. restliche Buttons, Filter & Search, Checkout-Details, Cancellation, Patterns) noch nicht geprüft.

---

## Buttons: Hug / Fill / Fixed-Verhalten
- Figma übersetzt Hug/Fill-Einstellungen manchmal in absolute Fixed-Werte. Das ist nicht so gedacht – Ausnahmen sind Min/Max-Constraints und (absolut selten) bewusst gesetzte Fixwerte. In 99% der Fälle sind Fixwerte mit einer Variable verknüpft, nicht hart kodiert. Immer die Properties Fixed / Fill / Hug prüfen statt absolute Werte zu übernehmen.
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
- "Aufbewahren" ist eine feste kategorie, "Im Angebot" eine Sammlung.

#### Komponenten-Liste "COMPONENTS & SCREENS" (14.07.2026)

**Struktur der Seite:** Canvas "COMPONENTS & SCREENS" (2001:522) hat 3 direkte Kinder: Section "PAGES" (3658:9149, Screens – ausgeschlossen), Section "PATTERNS, BUTTONS, ELEMENTS, COMPONENTS" (3267:6614, enthält die gesamte Komponentenbibliothek) und Frame "PRACTICE FOR CLAUDE" (7372:19291, Testartefakt, ausgeschlossen). Innerhalb von 3267:6614 liegen die Top-Level-Sections: SECTIONS, HEADER & FOOTER, FILTER & SEARCH, BUTTONS, INPUTS, CARDS, COMPONENTS, ICONS, PATTERNS, NOTES, VISUALS.

**Ausgeschlossen (bewusst):** ICONS (1:133, nicht im Detail durchsucht), NOTES (6611:18283, verifiziert nur Screenshots/Notizen), VISUALS (6663:16082, auf Wunsch nicht aufgenommen), PRACTICE FOR CLAUDE (7372:19291, nur 2 Button-Instanzen, kein Master).

**Offene Punkte / bitte in Figma prüfen:**
1. "Buttons / XS / SegmentControlButton" und "Buttons / SM / Segment Control" – uneinheitliche Schreibweise für vermutlich denselben Zweck.
2. "Input Field plain" (2406:1053) und "Input" (2328:2155) – zwei parallele Varianten-Sets mit identischen Feldtypen, aber unterschiedlicher Property-Struktur (Boolean vs. "Nr="-Nummerierung). Sieht nach Altlast/Duplikat aus.
3. Tippfehler in Figma noch nicht korrigiert (in dieser Liste bereits richtig geschrieben): "PurcheaseSummary" (6794:18851) → Purchase, "SearchPurchease" (6955:21898) → Purchase. "DecktopSize" (7448:19299) wurde von der Nutzerin bereits in Figma korrigiert. Claude hat keinen Schreibzugriff auf Figma (nur lesende Dev-Mode-MCP-Tools) – die restlichen zwei bitte manuell umbenennen.
4. Generische Wrapper-Frames ("fr", "wrapper", "gr") um "Layout / PromoBar" (3164:11788), "CartElements / Calculation" (2260:4084) und "Components / SearchPurchase" (6955:21898) sind laut Nutzerin bewusstes Design (Größenbeschränkung für sonst unlimitierte Komponenten), keine Namensfehler.
5. "TabControl" (3970:22955), "Add to Basket for mobile" (3986:23589) liegen ohne "Buttons /"-Präfix direkt im Buttons-Ordner. ("IconButton" wurde von der Nutzerin bereits zu "Buttons / IconButton" korrigiert.)
6. "Account / LogInStatus" liegt physisch bei den CartElements/CARD-ELEMENTS-Komponenten, "Account / CollapsibleSection" physisch bei den Section/*-Komponenten – hier aber thematisch unter "Account" einsortiert.

**Hierarchie-Verifikation (per `get_design_context`, echte Instanz-Prüfung statt nur Namenslogik):** Bestätigt verschachtelt: Filter/FilterPanel (enthält FilterChip- und eine PriceRange-Instanz, dort aber als "FilterPanel / PriceRange" benannt – Namensabweichung zum hier gelisteten Master 2605:2931, bitte prüfen), CartElements/Summary (enthält ProductItem, Calculation, LogIn), Account/CollapsibleSection (enthält SummaryItem, DataBlock), Components/OrderCancellation (enthält SelectOrder-Instanz, SelectProducts sehr wahrscheinlich analog). Geprüft und NICHT verschachtelt (daher als gleichrangige Einträge gelistet): NavBar/Nav/NavBlocks sind eigenständig, ebenso Components/Product/BuyBox und ImageCarousel.
