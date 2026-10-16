# Kategóriafa- és kulcsszókutató ügynök — munkajegyzet

Ez a repó a webshopok **kategóriafa-struktúrájának megtervezésére és
kulcsszókutatásra** szolgáló dedikált munkamenet közös memóriája. Minden új
munkamenet először ezt olvassa el, és ide vezeti fel a döntéseket.

## Webshopok (eddigi munkamenetekből ismert)

- **urbangardenshop.hu** — Shoprenter, aldomain: `urbangardenshop`
  (API: `urbangardenshop.api.myshoprenter.hu`). Termesztés / growshop:
  közegek, tápok, világítás, szellőzés, hidro.
- **Babylon**, **Gomoa** — további boltok (termékfeltöltési munkamenetekből
  ismertek, részletek még nincsenek rögzítve).
- A meglévő automatizációs scriptek a felhasználó Windows gépén:
  `C:\shoprenter-auto\` (itt vannak a Shoprenter API-hitelesítések is).
- A felhőkonténer **nem éri el** a Shoprenter API-t (egress proxy tiltja),
  ezért élő adatot exportként (CSV) kell ide hozni, vagy a scriptet helyben
  futtatni.

## Rögzített szabályok

- **Gyűjtőtermék-elv:** a `GYUJTO…` SKU-jú gyűjtőtermék és az összes
  gyereke (változata) pontosan **ugyanazt a kategóriakészletet** kapja.
- Egy termék jellemzően két párhuzamos ágban is szerepel: **márka-ág**
  (pl. Plagron) és **termékkategória-ág** (pl. földkeverékek). Több
  kategória-ID duplán létezik (pl. 6574 és 6829 = Plagron; 6699 és 6821 =
  földkeverékek) — ez a két (vagy kétnyelvű / két fa alatti) ág jele, nem
  hiba, de a kategóriafa újratervezésénél tisztázandó.
- Shoprenter azonosítók: base64(`category-6574`) alak; exportban és a
  jegyzetekben a sima számot használjuk.

## Ismert kategória-ID-k (urbangardenshop, 2026-09 export alapján)

| ID | Megnevezés | ID | Megnevezés |
|---|---|---|---|
| 6551 | árva (1 termék) | 6687 | Integra Boost |
| 6560 | BioBizz | 6697, 6819 | perlit / agyaggolyó |
| 6565 | Canna | 6699, 6821 | földkeverékek |
| 6574, 6829 | Plagron | 6704 | szellőzés / szűrő |
| 6576, 6817 | Terra Aquatica | 6706 | klipsz / padló ventilátor |
| 6591 | növénytartó háló | 6710 | csőventilátor |
| 6600 | fűtött szaporító | 6731 | hidro rendszer |
| 6608 | szaporítóláda | 6744 | mérlegek |
| 6627 | LED lámpák | 6786 | rejtekhely / tárolás |
| 6630 | kábelek / tápegységek | 6666 | kalibráló folyadékok |
| 6644 | Secret Jardin kiegészítők | 6667 | pH mérők |
| 6661 | nem beazonosított (GYUJTO0086 csoport) | 6669 | pH teszt |

## Előzmény: kategória-javítás (2026-09-16)

`claude-code-kategoria-javitas.md` alapján egy Python script készült
(branch: `claude/lucid-thompson-38go7y`, **nem került pusholásra**, a
munkamenet megszakadt): 61 termék kategóriáinak szinkronizálása (76
hozzáadás, 11 törlés, 22 gyűjtő), 2 termék leválasztása rossz szülőről
(HED0118 ← GYUJTO0240, GRO2251 ← GYUJTO0226), majd ellenőrzés.

## Babylon (babylon-grow.eu) – kategóriafa megújítás

- **Az ügynök teljes munkautasítása:** `kulcsszokutatas/MESTERPROMPT.md`
  (Word: `Kulcsszokutato_ugynok_mesterprompt.docx`; forrás:
  `scripts/mesterprompt_content.js`, generálás: `node scripts/mesterprompt_docx.js`).

- Éles oldalon a régi fa, a sandboxban az új kategóriák; a felhasználó mondja
  meg, melyik kategóriával haladunk.
- **Kulcsszóadat-forrás (működik):** Windsor.ai MCP → `google_ads` connector,
  fiók `867-850-6485` (Babylon Adwords). `get_data` mezők: `keyword`,
  `avg_monthly_searches`, `keyword_competition`, `competition_index`;
  options: `keyword_seeds` (max 20, vesszővel), `geo_target_constants: 2348`
  (HU), `language: 1024` (magyar), `keyword_plan_network: GOOGLE_SEARCH`.
  (`keyword_text` NEM megy együtt az `avg_monthly_searches`-szel.)
- Csak valós Kulcsszótervező-számot írunk be, kitalált számot soha.
- **Az éles oldal jelenlegi kategóriáit NEM vesszük figyelembe** (félrevezetők,
  épp ezt újítjuk). A kategóriaszerkezet- és névajánlás a **teljes
  termékkínálat** (termékexport: termékkód + terméknév) és a kulcsszavak
  alapján készül; minden javasolt kategóriának külön lapja van a beleillő
  termékekkel (egy termék több kategóriába is mehet). Termékexport nélkül ezt
  az elején el kell kérni. (2026-10-14)
- Excel-minta: a pH/EC kutatás (`Babylon_pH_EC_kulcsszokutatas_top30`) –
  lapok: Összefoglaló, Bővítés – rokon területek, Összes kulcsszó,
  kategórialapok (#, kulcsszó, havi, kötődés, érdemes, terület, felhasználás),
  Gyártói kulcsszavak. Generátor:
  `python3 scripts/merge.py <adatmappa>` (Windsor `mcp-*.txt` fájlok +
  `inline.tsv` → `all.json`), majd
  `python3 scripts/build.py <adatmappa> <kimenet.xlsx> <kategória_config.py>`.
  A kategóriánkénti adat (CATS, OLD, EXT, MAKERS, lapcímek) a
  `kulcsszokutatas/babylon/*_config.py` fájlokban van; a build leáll, ha egy
  kulcsszó nincs a lekért adatban (így kitalált szám nem kerülhet be).
- Az éles bolt terméklistája (Shoprenter API) a felhőből nem érhető el
  (egress 403) – termékexportot kell kérni.
- **Termékforrás a felhőből (működik, 2026-10-14):** Windsor.ai `google_ads`,
  mezők `product_item_id`, `product_title` (Shopping-feed; item ID = SKU
  kisbetűvel → nagybetűsítve). 2024-10 – 2026-10: 1999 termék →
  `kulcsszokutatas/babylon/babylon_termekek_shopping_feed.json`. Csak a
  hirdetett termékkör; gyártó / gyűjtőtermék nincs benne.

### Kész kategóriák
- [x] 2026-10-09 **Propagátor, propagátor kiegészítő** (új főkat.; al:
  1. Propagátor, 2. Propagátor kiegészítő, propagátor fűtőlap; régi:
  Palántanevelés → Palánta közegek / tápok / Propagátor kiegészítők /
  Propagátorok / Vetőmagok) → `kulcsszokutatas/babylon/`.
  Fő tanulság: „propagátor” 70/hó vs. „palántanevelő” 880, tálcák 3×1000.
- [x] 2026-10-12 **Edények és tálcák** (jelenlegi al: Esővízgyűjtő, Hidro
  cserép, Mérőedény, Speciális cserepek, Tálcák, Virágcserép, Alátét).
  Tanulság: esővízgyűjtő tartály 6600 + esővízgyűjtő 5400 viszi az ágat,
  virágcserép 2400; „Speciális cserepek” névre 0 keresés (→ Air-Pot,
  ültetőzsák, szögletes, önöntöző), „Alátét” = csavaralátét (→ Cserépalátét),
  „Tálcák” = konyhai (→ Műanyag tálca, árapály asztal).
- [x] 2026-10-14 **Cserép, tálca** (sandbox: Virágcserép; Speciális cserép,
  szövetcserép; Tálca, alátét). Javaslat: Virágcserép (+ Nagy virágcserép
  3. szint, szögletes = szűrő, liter = szűrő), Air-Pot cserép, Szövetcserép /
  ültetőzsák, (Önöntöző), Cserépalátét, Műanyag tálca / árapály asztal.
  Termékek a Shopping-feedből besorolva (142 termék a javasolt kategóriákban,
  + más főkategóriába tartozók jelölve). Önöntöző: nincs termék → kimarad.
  build.py: opcionális STRUCT + PRODUCTS (products.json az adatmappában).
- [x] 2026-10-15 **Növényfeldolgozás, afterharvest** (sandbox: Csomagolás;
  Extrakció, kivonatolás; Fermentáció; Hasznos kiegészítők; Növényszárítás;
  Trimmelés; Digitális mérleg, zsebmérleg). Félrevezető nevek: „Fermentáció”
  (= savanyúság, 6600 → Páratartalom-szabályzó tasak / Boveda),
  „Trimmelés” (szakállvágó → Trimmelő olló, trimmelő gép), „Csomagolás”
  (→ Vákuumzsák, simítózáras tasak). 108 termék besorolva.
  Windsor válaszformátum 2026-10-15 óta `data` (nem `result`) – merge.py kezeli.
- [x] 2026-10-15 **Hidropónia, öntözés** (sandbox: Hidropóniás rendszer,
  kiegészítő; Öntözés, vízpumpa, tartály; Vízszűrő, fordított ozmózis).
  A sandbox-nevek jók (gyűjtőnevek) → 3. szintű bontás: Hidropóniás rendszer,
  Levegőztető pumpa / porlasztókő, Agyaggolyó / hidrokosár, Tápoldat-adagoló /
  vízhűtő; Automata öntözőrendszer, Vízpumpa, Víztartály, (Permetező).
  95 termék besorolva. Az agyaggolyó a Közegek ágban is → egy céloldal.
  Széles kerti / háztartási szavak (öntözőrendszer, vízszűrő…) = Laza / Nem,
  hogy ne fújják fel a klaszter-összeget.
- [x] 2026-10-15 **Aktív szénszűrő, légtechnika** (sandbox: Aktív Szénszűrő
  csőventilátorhoz ↳ Ventilátor vezérlő; Szagsemlegesítő és ózongenerátor;
  Csőventilátor és elszívó ventilátor; Keringető ventilátor growboxba;
  Légtechnikai cső, idom, csőrögzítő; Klímaszabályozás…; CO2) →
  `legtechnika_config.py`. A legnagyobb keresés a klímán van (páramentesítő
  9900, párásító 5400, páratartalom mérő 1600), nem a szénszűrőn (210) →
  Klíma 3. szint: Párásító / Páramentesítő / Hő- és páratartalom-mérő (új).
  Ventilátor-vezérlő → a Csőventilátor alá. Ózongenerátor 6600, de 1 termék
  (bővítési lehetőség). Légcsatorna 320 (a „légtechnikai cső” 0). 458 termék.
- [x] 2026-10-15 **Growbox, termesztő sátor** (sandbox: Kis / Közepes / Nagy
  growbox; Palántanevelő és propagátor sátor; Komplett growbox szett;
  Growbox kiegészítő – háló, tálca, polc; Fényvisszaverő fólia) →
  `growbox_config.py`. Nagyon kicsi volumen (termesztősátor 90, growbox 70);
  méretre ~10/hó → a méret-kategóriák navigációsak (alapterület: ≤0,64 /
  ≤1,44 / >1,44 m²; szettek másodlagosan méret szerint is). Erős: fényvisszaverő
  fólia 390, palántanevelő sátor 110. „polc” → „felfüggesztő” (nincs polc
  termék). „homebox” 140 = Telekom-zaj. 159 termék.
- [x] 2026-10-15 **LED növényvilágítás** (sandbox: LED 0-100W / 100-400W /
  400+W; Növénylámpa izzók – HPS, MH, CMH; Speciális LED; Függesztők és
  időzítők; LED growbox szettek) → `led_config.py`. Keresés: növénynevelő
  lámpa 880, növény lámpa 720, növénylámpa 480 (= kis / hobbi lámpa); wattra
  ~10/hó → navigációs. Időkapcsoló a legnagyobb klaszter (időzítő kapcsoló
  1900). HID-ág: trafó + reflektor is ide („HPS, MH, CMH izzó, trafó,
  reflektor”, 116 termék). „Speciális” → „UV, IR és kiegészítő LED” + új
  „LED növénynevelő izzó, csíptethető lámpa” (Sansi). Új: „LED tápegység,
  kábel, vezérlő”. LED growbox szett = navigációs, céloldal a Growbox ágban.
  Mars Hydro / Spider Farmer = versenytárs, nem célozni. 320 termék.
  **2026-10-16: újraépítve az élő kínálatra** (felhasználói kérés: „az éles
  oldalon lévő termékkínálatot vedd alapul”): `ACTIVE_ONLY` a configban →
  csak az elmúlt 30 napban a Shopping-feedben szereplő termék kap kategóriát
  (207 élő; 118 „Nem aktív” a lap végén). HID-ág 116 → 55 élő termék.
- **Élő kínálat = Shopping-feed, elmúlt 30 nap** (az éles oldal továbbra is
  403 a felhőből). A `seen` mező a `babylon_termekek_shopping_feed.json`-ban
  2026-10-16-án frissítve (1525 élő termék). build.py: opcionális
  `ACTIVE_ONLY = 'az elmúlt 30 napban'` a configban.
- [x] 2026-10-15 **Termesztő közeg** (sandbox: Palántaföld; Kertészeti
  kókuszrost, kókusztégla; Kertészeti kőzetgyapot; Kertészeti perlit,
  vermikulit, agyaggolyó). Hiányzik: **Virágföld** (2900; a Plagron földek)
  → új kategória; Palántaföld (1300) csak 2 termék → „Virágföld, palántaföld”.
  Új: Talajjavító, gilisztahumusz. Agyaggolyó céloldala INNEN (Hidro: csak
  kereszt-link). 71 termék besorolva.

## Döntések: kannibalizáció, több helyen szereplő kategóriák (2026-10-09)

- Egy termék, egy URL, több kategória-hozzárendelés; duplikált termék nincs.
- Minden fő kulcsszónak egy céloldala van (title / H1 / URL / H2 csak ott);
  máshol csak említés, linkkel a céloldalra.
- Kis LED: LED-ág „Kis teljesítményű LED, növénylámpa” (növénynevelő lámpa
  880), Palántanevelés-ág „Palántanevelő LED” (palántanevelő lámpa 390),
  Mikrozöld-ág „Mikrozöld LED lámpa” = navigációs (0 keresés).
- Terméknév-séma: [márka] [modell] [W] [terméktípus] – [felhasználás].
- Mikrozöld = hub főkategória (rövid + hosszú leírás, csempék szűrt
  céloldalakra); valódi alkategória ott, ahol saját keresés van
  (mikrozöld mag, csíráztató).

## Nyitott kérdések / következő lépések

- [ ] A kategóriafa-tervezésről és kulcsszókutatásról folytatott korábbi
      (claude.ai chat) beszélgetés tartalma — ide kell felvezetni.
- [ ] Aktuális teljes kategóriafa-export (ID, név, szülő, URL, termékszám)
      boltonként.
- [ ] Kulcsszó-adatforrás: Google Search Console (Windsor.ai-n át elérhető
      lehet), Google Ads Keyword Planner export.
