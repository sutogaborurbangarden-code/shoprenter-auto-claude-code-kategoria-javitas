# Babylon – Aktív szénszűrő, légtechnika (2026-10-16, 2. változat)
# Csak a FŐKATEGÓRIA NEVE alapján: a korábbi / sandbox alkategória-nevek és -szerkezet figyelmen kívül;
# alkategóriák az élő termékkínálat és a kulcsszóadat alapján.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 {'name': 'Csőventilátor, elszívó ventilátor', 'sheet': '1 Csőventilátor', 'fo': 'csőventilátor', 'area': 'Elszívás / befúvás a termesztőtérben – centrifugális, kevert áramlású és EC csőventilátor', 'place': '2. szint – a sandbox-név jó; alá kerül a „Ventilátor-vezérlő, termosztát” (3. szint)', 'note': 'Az „elszívó ventilátor” (1900) nagyobb, de vegyes (fürdőszoba, konyha, ipar); a „csőventilátor” (1000) pontosabb – ez legyen a fő kulcsszó, az „elszívó ventilátor” a név második fele / H2. Átmérő szerinti szűrő érdemes (csőventilátor 100: 320, 150: 140, 125: 90). Fürdőszobai / WC / páraérzékelős elszívó nem a mi termékünk.', 'kws': 'csőventilátor|S|F\nelszívó ventilátor|S|S\nelszívóventilátor|S|E\ncsőventilátorok|S|E\ncsoventillator|S|E\ncsö ventilátor|S|E\ncső elszívó ventilátor|S|E\ncsőventilátor 100|S|S\ncsőventilátor 125|S|S\ncsőventilátor 150|S|S\ncsőventilátor 200|S|E\n125 csőventilátor|S|E\nelszívó ventilátor 125|S|E\ncentrifugális ventilátor|S|E\nradiális csőventilátor|S|E\naxiális csőventilátor|S|E\nfém csőventilátor|S|E\nhalk csőventilátor|S|E\ncsendes csőventilátor|S|E\ncsendes elszívó ventilátor|S|E\nszabályozható csőventilátor|S|E\nmini csőventilátor|S|E\nipari csőventilátor|S|E\nlégcsatorna ventilátor|S|E\nszagelszívó ventilátor|L|E\nec ventilátor|S|E\nelszívó ventilátor visszacsapó szeleppel|L|E\nipari elszívó ventilátor|L|E\nvents ventilátor|S|G\ncsőventilátor bekötése|S|I\nhelios csőventilátor|LN|N\npáraérzékelős csőventilátor|LN|N\nfürdőszobai elszívó|LN|N\nwc elszívó ventilátor|LN|N\nkonyhai elszívó ventilátor|LN|N\ncsőventilátor praktiker|X|X'},
 {'name': 'Aktív szénszűrő, előszűrő', 'sheet': '2 Szénszűrő', 'fo': 'aktív szénszűrő', 'area': 'Szagszűrés a termesztőtérből elszívott levegőből – aktív szénszűrő, előszűrő, utántöltő szén', 'place': '2. szint (sandbox: „Aktív Szénszűrő csőventilátorhoz”) – a „csőventilátorhoz” toldat a H1 / leírás része legyen, ne a menünévé', 'note': 'Kis, de tiszta szándékú klaszter (aktív szénszűrő 210, szénszűrő 170, aktívszén szűrő 140). A „szénszűrős páraelszívó” (480) és a „szagelszívó szénszűrő” (140) konyhai páraelszívó – nem a mi termékünk (LN). Growshop-specifikus kifejezés (pl. „szénszűrő csőventilátorhoz”) 20 alatt.', 'kws': 'aktív szénszűrő|S|F\nszénszűrő|S|S\naktívszén szűrő|S|S\naktív szenes szűrő|S|E\naktív szén szűrő filter|S|E\naktív szén szűrőbetét|L|E\naktívszén szűrőbetét|L|E\naktívszenes légtisztító|L|E\nszagelszívó szűrő|LN|N\nszagelszívó szénszűrő|LN|N\nszénszűrős szagelszívó|LN|N\nszénszűrős páraelszívó|LN|N\nszénszűrős páraelszívó kivezetés nélkül|LN|N\npáraelszívó szénszűrő|LN|N'},
 {'name': 'Légtechnikai cső, idom, bilincs', 'sheet': '3 Légtechnikai cső', 'fo': 'légtechnika cső', 'area': 'Flexibilis légcsatorna (Aluflex, Sonoflex, Combiflex), idom, bővítő / szűkítő, csőtoldó, visszacsapó szelep, bilincs, ragasztószalag, ventilátor-hangtompító', 'place': '2. szint – a legtöbb termékes alkategória; 3. szintű szűrő: cső / idom / bilincs / szalag / hangtompító', 'note': 'A keresők „légtechnika csövet” keresnek (880), nem légcsatornát (320); légtechnikai idom 210, légtechnika idomok 210. A „flexibilis cső” (2400), „visszacsapó szelep” (2400) és „hangtompító” (880) jórészt vízvezeték / autó – LN.', 'kws': 'légtechnika cső|S|F\nlégtechnikai idom|S|S\nlégtechnika idomok|S|S\nlégcsatorna|S|S\nszellőző cső|S|S\nflexibilis légcsatorna|S|S\naluflex cső|S|S\nflexibilis alumínium cső|S|E\nflexibilis alumínium cső 150 mm|S|E\nalu flexibilis cső|S|E\naluminium flexibilis cső|S|E\nsonoflex|S|G\nsonoflex cső|S|G\nlégcsatorna cső|S|E\nszellőztető cső|S|E\nflexibilis szellőző cső|S|E\nhőszigetelt légcsatorna|S|E\nszigetelt légcsatorna|S|E\nszigetelt szellőző cső|S|E\nműanyag légcsatorna|L|E\nlégcsatorna idomok|S|E\nszellőzőcső idomok|S|E\nszűkítő idom|S|E\nlégtechnikai bilincs|S|E\nalumínium ragasztószalag|S|S\nalu ragasztószalag|S|E\nduct tape|L|E\nflexibilis cső|LN|N\nvisszacsapó szelep|LN|N\nhangtompító|LN|N\ncsőbilincs|LN|N'},
 {'name': 'Szagsemlegesítő, ózongenerátor', 'sheet': '4 Szagsemlegesítő', 'fo': 'szagsemlegesítő', 'area': 'Szagkezelés szénszűrő mellett / helyett – ONA gél, tömb, spray, légcsatornába építhető ONA szűrő, ózongenerátor', 'place': '2. szint – a sandbox-név jó', 'note': 'Az „ózongenerátor” (6600) a legnagyobb szó az egész ágban, de csak 1 ózongenerátor termékünk van – a fő kulcsszó a „szagsemlegesítő” (260) legyen, az ózongenerátor H2 / szűrő. Ha bővül az ózongenerátor-kínálat, külön 3. szintű kategóriát érdemel. A „szagtalanító spray” (390) jó az ONA spray-re.', 'kws': 'szagsemlegesítő|S|F\nszagsemlegesítő spray|S|S\nszagtalanító|S|S\nszagtalanító spray|S|S\nszagtalanító készülék|S|E\nlevegő szagtalanító|S|E\nszagelnyelő|S|E\nona gel|S|G\nózongenerátor|S|S\nozon generátor|S|E\nózon generator|S|E\nózóngenerátor|S|E\nózón generátor|S|E\nózongenerátor ár|S|E\nlegjobb ózongenerátor|S|E\nózongenerátor lakásba|S|E\nózongenerátor penész ellen|L|E\nózongenerátor fertőtlenítés|L|E\nózongenerátor autóba|L|E\nmini ózongenerátor|S|E\nhordozható ózongenerátor|S|E\nózonos szagtalanítás|S|E\nózongenerátor használata|S|I\nózongenerátor mire jó|S|I\nmire jó az ózongenerátor|S|I\nózongenerátor tisztítás|L|I\nionizátor|L|E\nlevegő ionizátor|L|E\ndm szagtalanító spray|X|X\nsanytol szagtalanító|X|X'},
 {'name': 'Keringető ventilátor', 'sheet': '5 Keringető', 'fo': 'padlóventilátor', 'area': 'Légmozgatás a növények között – csíptetős (Monkey Fan, Cloudray), padló-, álló- és fali ventilátor', 'place': '2. szint (sandbox: „Keringető ventilátor growboxba”) – név marad, a „growboxba” a H1-be / leírásba', 'note': 'A „keringető ventilátor” és a „csíptetős ventilátor” 20 alatti. A forgalmat a háztartási típusszavak hozzák (padlóventilátor 1300, fali ventilátor 880, ipari ventilátor 1000) – ezek laza kötődésűek, de ugyanaz a termékkör. A „ventilátor” (18100) és az „álló ventilátor” (4400) túl általános (LN).', 'kws': 'padlóventilátor|S|F\npadló ventilátor|S|S\npadló ventilátor 50 cm|L|E\nipari padló ventilátor|S|E\nfali ventilátor|L|S\nipari ventilátor|L|S\nszellőztető ventilátor|L|E\noszcilláló ventilátor|S|E\nkis ventilátor|L|E\nnagy teljesítményű ventilátor|L|E\nipari fali ventilátor|L|E\nventilátor|LN|N\nálló ventilátor|LN|N\nasztali ventilátor|LN|N'},
 {'name': 'Páramentesítő', 'sheet': '6 Páramentesítő', 'fo': 'páramentesítő', 'area': 'Páratartalom csökkentése a termesztőtérben, szárításnál – kompresszoros / Peltier páramentesítő', 'place': '3. szint a „Klímaszabályozás, párásítás, párátlanítás” alatt', 'note': 'Az ág legerősebb termékszava (páramentesítő 9900, párátlanító 3600) – a két szinonima egy céloldalra (H1: „Páramentesítő, párátlanító készülék”). Az „ipari páramentesítő” (320) jó a nagy Cornwall gépre.', 'kws': 'páramentesítő|S|F\npárátlanító|S|S\npáramentesítő gép|S|S\npáramentesítő készülék|S|S\npárátlanító készülék|S|S\npárátlanító gép|S|S\nipari páramentesítő|S|S\nelektromos páramentesítő|S|E\nlegjobb páramentesítő|S|E\nnagy teljesítményű páramentesítő|S|E\nkompresszoros páramentesítő|S|E\npáramentesítő penész ellen|L|E\npáramentesítő fürdőszobába|LN|N\nipari páramentesítő bérlés|X|X'},
 {'name': 'Párásító', 'sheet': '7 Párásító', 'fo': 'párásító', 'area': 'Páratartalom növelése a termesztőtérben – ultrahangos / hideg párásító, ködgenerátor, vezérlő', 'place': '3. szint a „Klímaszabályozás, párásítás, párátlanítás” alatt', 'note': 'Nagy, tiszta klaszter (párásító 5400, párásító készülék 4400, ultrahangos párásító 1000, hidegpárásító 720). A márkás háztartási szavak (Xiaomi, Philips, Vivamax) és a diffúzor / babaszobai szavak nem a mi termékeink.', 'kws': 'párásító|S|F\npárásító készülék|S|S\nultrahangos párásító|S|S\nhidegpárásító|S|S\nlevegő párásító|S|E\npárásító gép|S|E\nhideg párásító készülék|S|E\nhidegpárásító készülék|S|E\nultrahangos párásító készülék|S|E\nultrahangos hideg párásító|S|E\nlevegő párásító készülék|S|E\nipari párásító|S|E\nlegjobb párásító|S|E\nelektromos párásító|S|E\nokos párásító|S|E\npárásítók|S|E\npárásító ventilátor|LN|N\npárásító diffúzor|LN|N\npárásító babáknak|LN|N'},
 {'name': 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát', 'sheet': '8 Klímavezérlő', 'fo': 'ventilátor fordulatszám szabályzó', 'area': 'Csőventilátor fordulatszám-, hőmérséklet-, páratartalom- és nyomásszabályzása; környezeti vezérlő (AC Infinity, GSE, OptiClimate)', 'place': '2. szint – önálló kategória: ventilátorok, párásítók, fűtés vezérlése egy helyen (környezetvezérlő)', 'note': 'Kis keresésű, de konverziós kategória (ventilátor fordulatszám szabályzó 110, ventilátor vezérlő 70, páratartalom szabályzó 70). A „digitális termosztát” (390) nagyrészt fűtés-termosztát – laza. A „pc ventilátor vezérlő” számítógépes – kizárva.', 'kws': 'ventilátor fordulatszám szabályzó|S|F\nventilátor vezérlő|S|S\nventilátor szabályzó|S|S\n230v ventilátor fordulatszám szabályzó|S|E\nventilátor fordulatszám szabályzó 230v|S|E\nventilátor vezérlés|S|E\nfordulatszám szabályzós ventilátor|S|E\npáratartalom szabályzó|S|S\nhigrosztát|S|S\nhőmérséklet és páratartalom szabályzó|S|E\ndigitális hőfokszabályzó|L|E\ndigitális hőmérséklet szabályozó|L|E\nhőmérséklet szabályzó|L|E\nkonnektoros termosztát|L|E\ndigitális termosztát|L|E\npc ventilátor vezérlő|X|X'},
 {'name': 'Hő- és páratartalom-mérő', 'sheet': '9 Páratartalom-mérő', 'fo': 'páratartalom mérő', 'area': 'Hőmérséklet és relatív páratartalom mérése – digitális thermo-higrométer', 'place': '3. szint a Klíma alatt VAGY a Mérőműszer ágban (pH / EC mellett) – egy céloldal, a másik helyen link', 'note': 'Meglepően erős klaszter (páratartalom mérő 1600, páratartalommérő 1600, higrométer 480) – 7 termékünk van. Érdemes saját kategória, nem csak szűrő.', 'kws': 'páratartalom mérő|S|F\npáratartalommérő|S|S\nhigrométer|S|S\nhő és páratartalom mérő|S|S\nhőmérséklet és páratartalom mérő|S|E\nhőmérő páratartalom mérő|S|E\ndigitális hőmérő páratartalom mérő|S|E\ndigitális páramérő|S|E\nparatartalom mero|S|E'},
 {'name': 'CO2-pótlás, CO2-mérő', 'sheet': '10 CO2', 'fo': 'co2 mérő', 'area': 'CO2-szint emelése és mérése – CO2 zsák, tabletta, palack + reduktor, propános CO2 generátor, CO2 érzékelő / szabályzó', 'place': '2. szint (sandbox: „CO2”) – a puszta „CO2” név túl általános', 'note': 'A „co2” (1900) kémiai / általános keresés (LN). A „co2 palack” (1000) és a „co2 reduktor” (260) főleg hegesztés / szódagép – laza. Tiszta termékszavak: co2 mérő 210, co2 érzékelő 170, szén dioxid mérő 260, co2 zsák 50, co2 generátor 40.', 'kws': 'co2 mérő|S|F\nco2 érzékelő|S|S\nszén dioxid mérő|S|S\nszén dioxid érzékelő|S|S\nco2 szenzor|S|E\nco2 mérő műszer|S|E\nco2 zsák|S|S\nco2 generátor|S|E\nco2 tabletta|S|E\nco2 palack|L|E\nco2 reduktor|L|E\nco2 nyomáscsökkentő|L|E\nco2|LN|N\nszénsav palack|LN|N'},
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'A „légtechnika” (1300) a legerősebb általános szó; az „aktív szénszűrő” (210) a névadó termék. Javasolt menünév marad: „Aktív szénszűrő, légtechnika”; H1: „Légtechnika – aktív szénszűrő, csőventilátor, légtechnikai cső”.', '''légtechnika|S
légtechnikai bolt|S
légtechnika bolt|S
légtechnika webáruház|S
aktív szénszűrő|S'''),
 ('Elszívás', '→ Csőventilátor, elszívó ventilátor', '''csőventilátor|S
elszívó ventilátor|S'''),
 ('Szagszűrés, szagkezelés', '→ Aktív szénszűrő; Szagsemlegesítő', '''aktív szénszűrő|S
szagsemlegesítő|S
ózongenerátor|S'''),
 ('Csövezés', '→ Légtechnikai cső, idom, bilincs', '''légtechnika cső|S
légtechnikai idom|S
légcsatorna|S'''),
 ('Légkeringetés', '→ Keringető ventilátor', '''padlóventilátor|S'''),
 ('Páratartalom', '→ Páramentesítő; Párásító; Hő- és páratartalom-mérő', '''páramentesítő|S
párásító|S
páratartalom mérő|S'''),
 ('Vezérlés', '→ Klímavezérlő', '''ventilátor fordulatszám szabályzó|S
higrosztát|S'''),
 ('CO2', '→ CO2-pótlás, CO2-mérő', '''co2 mérő|S'''),
]

EXT = [
 ('Háztartási ventilátor (álló, asztali, torony)', 'Nagy volumen, de nem growshop-termék – csak kínálatbővítés esetén', '''ventilátor|L
álló ventilátor|L
asztali ventilátor|L'''),
 ('Fürdőszobai / konyhai elszívó', 'Nem a mi termékünk', '''fürdőszobai elszívó|LN
wc elszívó ventilátor|LN
konyhai elszívó ventilátor|LN'''),
 ('Konyhai páraelszívó szénszűrője', 'Nem a mi termékünk', '''szénszűrős páraelszívó|LN
páraelszívó szénszűrő|LN'''),
 ('Ózongenerátor-kínálat bővítése', 'Erős kereslet (6600) – kínálatbővítés esetén saját 3. szintű kategória', '''ózongenerátor|S
ózongenerátor fertőtlenítés|L
ozon generátor|S'''),
 ('Lakás-szellőztetés, légtisztító', 'Háztartási / épületgépészeti szándék – nem a mi termékünk', '''szellőzés|LN
szellőztető rendszer|LN
hővisszanyerős szellőztető rendszer|LN
légtisztító|LN'''),
 ('Szobatermosztát', 'Fűtéstechnika – nem a mi termékünk', '''digitális termosztát|L
konnektoros termosztát|L'''),
]

MAKERS = '''vents ventilátor
sonoflex
ona gel
exhale co2
helios csőventilátor'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Aktív szénszűrő, légtechnika (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A korábbi és a sandbox alkategória-neveket és -szerkezetet NEM vettük figyelembe. Kiindulás: a főkategória neve, az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [(1, 'Aktív szénszűrő, légtechnika', '–', 'légtechnika', 'S', 'Főkategória', 'Légtechnika 1300 (+ légtechnikai bolt 720) – a főkategória H1-je: „Légtechnika, aktív szénszűrő, csőventilátor”.', None), (2, 'Csőventilátor, elszívó ventilátor', 'Aktív szénszűrő, légtechnika', 'csőventilátor', 'S', 'Önálló kategória', 'Csőventilátor 1000, elszívó ventilátor 1900 (vegyes); átmérő / EC = szűrő.', 'Csőventilátor, elszívó ventilátor'), (2, 'Aktív szénszűrő, előszűrő', 'Aktív szénszűrő, légtechnika', 'aktív szénszűrő', 'S', 'Önálló kategória', 'Aktív szénszűrő 210 – a főkategória névadó terméke.', 'Aktív szénszűrő, előszűrő'), (2, 'Légtechnikai cső, idom, bilincs', 'Aktív szénszűrő, légtechnika', 'légtechnika cső', 'S', 'Önálló kategória', 'Légtechnika cső 880 – a legtöbb termék (~100 élő).', 'Légtechnikai cső, idom, bilincs'), (2, 'Szagsemlegesítő, ózongenerátor', 'Aktív szénszűrő, légtechnika', 'szagsemlegesítő', 'S', 'Önálló kategória', 'Szagsemlegesítő 260; ózongenerátor 6600, de 1 termék.', 'Szagsemlegesítő, ózongenerátor'), (2, 'Keringető ventilátor', 'Aktív szénszűrő, légtechnika', 'padlóventilátor', 'S', 'Önálló kategória', 'Padlóventilátor 1300, fali ventilátor 880 (laza).', 'Keringető ventilátor'), (2, 'Páramentesítő', 'Aktív szénszűrő, légtechnika', 'páramentesítő', 'S', 'Önálló kategória', 'Páramentesítő 9900 – az ág legnagyobb kulcsszava.', 'Páramentesítő'), (2, 'Párásító', 'Aktív szénszűrő, légtechnika', 'párásító', 'S', 'Önálló kategória', 'Párásító 5400, ultrahangos párásító 1000.', 'Párásító'), (2, 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát', 'Aktív szénszűrő, légtechnika', 'ventilátor fordulatszám szabályzó', 'S', 'Önálló kategória', 'Ventilátor fordulatszám szabályzó 110, higrosztát 70, páratartalom szabályzó 70.', 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát'), (2, 'Hő- és páratartalom-mérő', 'Aktív szénszűrő, légtechnika', 'páratartalom mérő', 'S', 'Önálló kategória', 'Páratartalom mérő 1600 – vagy a Mérőműszer ágban (egy céloldal).', 'Hő- és páratartalom-mérő'), (2, 'CO2-pótlás, CO2-mérő', 'Aktív szénszűrő, légtechnika', 'co2 mérő', 'S', 'Önálló kategória', 'Co2 mérő 210, co2 érzékelő 170.', 'CO2-pótlás, CO2-mérő')]
NOT_CATS = [
 ('Klíma gyűjtőkategória (párásító + páramentesítő + mérő egy ág alatt)', 'páramentesítő', 'A páramentesítő (9900) és a párásító (5400) erős önálló kulcsszó – közvetlenül 2. szinten jobb.'),
 ('Ózongenerátor (külön kategória)', 'ózongenerátor', 'Nagy kereslet, de 1 termék – szűrő / H2, bővítés esetén saját kategória.'),
 ('Hangtompító (külön kategória)', 'hangtompító', 'A „hangtompító” (880) autós kipufogó – a ventilátor-hangtompító a Légtechnikai cső alatt szűrő.'),
 ('Lakás-szellőztetés, légtisztító', 'légtisztító', 'Épületgépészet / háztartás – nem a mi termékünk.'),
 ('Fürdőszobai elszívó', 'fürdőszobai elszívó', 'Nem a mi termékünk.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A szerkezet csak a főkategória nevéből, a termékek típusából és a keresési szándékból készült – a korábbi és a sandbox alkategóriák figyelmen kívül.',
 'Beépített szabályzós csőventilátorok elsődlegesen a Csőventilátorba, másodlagosan a Klímavezérlőbe kerültek.',
]
TITLE = 'babylon-grow.eu – Aktív szénszűrő, légtechnika kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15/16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: csak a főkategória neve („Aktív szénszűrő, légtechnika”) adott; az alkategóriák a termékek funkciójából (elszívás, szagszűrés, csövezés, keringetés, páratartalom, vezérlés, CO2) és a keresési szándékból épülnek, lapos (2 szintű) szerkezetben.',
 'Fő megállapítások: a „légtechnika” (1300) és a „légtechnika cső” (880) erősebb, mint a „légcsatorna” (320) → a csőkategória fő szava „légtechnika cső”. A legnagyobb termékkulcsszavak a klímán vannak (páramentesítő 9900, párásító 5400, páratartalom mérő 1600) → önálló 2. szintű kategóriák.',
 'A „légtechnikai bolt” (720) / „légtechnika webáruház” (110) bolt-keresés – a főkategória title-jében érdemes kiszolgálni.',
 'A nagy általános szavak (ventilátor 18100, légtisztító 5400, szellőzés 2900, flexibilis cső 2400, visszacsapó szelep 2400, hangtompító 880) más szándékúak – LN.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a jelenlegi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más szándékú vagy nem kínált témák, bővítési lehetőségek.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO2776', 'Hidropónia ág – Vízszűrő, fordított ozmózis', [], 'Más főkategória', 'Víztisztító pót szénszűrő – nem légszűrő'),
 ('GRO1763 GRO2625 GRO4266 GRO4267 GRO4268 GRO4269', 'Hidropónia ág – kiegészítők', [], 'Más főkategória', 'Levegőztető cső idom / Aqua Master szonda-tartó – nem légtechnika'),
 ('GRO3329 GRO3331 GRO3878 GRO3879 GRO3880', 'Termesztősátor ág – sátor kiegészítő', [], 'Más főkategória', 'Secret Jardin DF16 keret / Space Booster – sátoralkatrész'),
 ('GRO1992 GRO1993 GRO2624', 'Hidropónia ág – Tápoldat-adagoló, vízhűtő', [], 'Más főkategória', 'Hailea vízhűtő (chiller) – tápoldathűtés, nem légkondi'),
 ('GRO2467 GRO3462 GRO3531', 'Mérőműszer ág – pH / EC mérő', [], 'Más főkategória', 'Talaj- / tápoldat-mérő'),
 ('GRO4303', 'Aktív szénszűrő, előszűrő', ['Csőventilátor, elszívó ventilátor'], 'Erős', 'AC Infinity légszűrő rendszer (ventilátor + szénszűrő)'),
 ('GRO1044 GRO1075 GRO1076 GRO1077 GRO1078 GRO1079 GRO1080 GRO1081 GRO1663 GRO2182 GRO2220 GRO2510 GRO2921 GRO3212 GRO3213 GRO3247 GRO3248 GRO3249 GRO3276 GRO3353 GRO3413 GRO3414 GRO3415 GRO3416 GRO3466 GRO3532 GRO3533 GRO3534 GRO3535 GRO3536 GRO3538 GRO3539 GRO3540 GRO3547 GRO3548 GRO3612 GRO3613 GRO3614 GRO3618 GRO3619 GRO3620 GRO3621 GRO3622 GRO3623 GRO3624 GRO3625 GRO3626 GRO3627 GRO3628 GRO3630 GRO3631 GRO3632 GRO3633 GRO3634 GRO3635 GRO3794 GRO3795 GRO3797 GRO3798 GRO3799 GRO3812 GRO4037 GRO4145 GRO4322 GRO4323 GRO4328 GRO4342 GRO4002', 'Aktív szénszűrő, előszűrő', [], 'Erős', 'Aktív szénszűrő (Can-Lite, Can Original, Can-Inline, Prima Klima, DF16, AC Infinity…)'),
 ('GRO3211 GRO3214 GRO3417 GRO3418 GRO3419 GRO3421 GRO3422 GRO3423 GRO3424 GRO3425 GRO3426 GRO3427 GRO3428 GRO3429 GRO3487 GRO3504 GRO3946 GRO3948 GRO3949 GRO3950 GRO3951 GRO3953 GRO4111 GRO4112 GRO4214 GRO4215 GRO4216', 'Aktív szénszűrő, előszűrő', [], 'Erős', 'Előszűrő, utántöltő szénpellet'),
 ('GRO3778 GRO3779', 'Légtechnikai cső, idom, bilincs', [], 'Erős', 'ONA ragasztószalag légcsatornához'),
 ('GRO3571 GRO3572', 'Szagsemlegesítő, ózongenerátor', ['Keringető ventilátor'], 'Erős', 'ONA ventilátor (szagsemlegesítő-párologtató)'),
 ('GRO2485 GRO2486 GRO2487 GRO2488 GRO2489 GRO2653', 'Szagsemlegesítő, ózongenerátor', ['Légtechnikai cső, idom, bilincs'], 'Erős', 'ONA Air Filter – légcsatornába építhető'),
 ('GRO0797', 'Szagsemlegesítő, ózongenerátor', [], 'Erős', 'Ózongenerátor'),
 ('GRO2472 GRO2473 GRO2474 GRO2475 GRO2476 GRO2477 GRO2478 GRO2479 GRO2480 GRO2481 GRO2482 GRO2483 GRO2781 GRO2782 GRO2785 GRO2786 GRO2802 GRO2803 GRO3159 GRO3160 GRO3161 GRO3162 GRO3163 GRO3168 GRO3169 GRO3397 GRO3399 GRO3400 GRO3401 GRO3402 GRO3403 GRO3404 GRO3405 GRO3406 GRO3407 GRO3408 GRO3409 GRO3693 GRO3694 GRO3695 GRO3845 GRO3936 GRO3937 GRO3938 GRO3939', 'Szagsemlegesítő, ózongenerátor', [], 'Erős', 'ONA gél, tömb, spray, folyadék'),
 ('GRO0774 GRO1456 GRO1458 GRO1460 GRO2826 GRO2827 GRO3035 GRO3433 GRO3891 GRO3892 GRO4196 GRO4197 GRO4242 GRO4381 GRO1459 GRO4236 GRO4208 GRO3865 GRO3866', 'Keringető ventilátor', [], 'Erős', 'Csíptetős / padló / fali keringető ventilátor'),
 ('GRO3637 GRO3640 GRO3642 GRO3645 GRO4080 GRO4081 GRO4082 GRO4191 GRO4192 GRO4193 GRO4194 GRO3699 GRO3700 GRO3701 GRO3716 GRO4195 GRO4364 GRO2047 GRO2051 GRO2054 GRO2131 GRO2183 GRO3105 GRO3106 GRO3107', 'Csőventilátor, elszívó ventilátor', ['Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát'], 'Erős', 'Csőventilátor beépített / mellékelt szabályzóval (TC, Un, Cloudline)'),
 ('GRO3134 GRO3477 GRO3478 GRO3479 GRO3480 GRO3481 GRO3482 GRO4600 GRO4601 GRO3970', 'Csőventilátor, elszívó ventilátor', [], 'Erős', 'EC motoros csőventilátor'),
 ('GRO0346 GRO0776 GRO0777 GRO0778 GRO0779 GRO0780 GRO0781 GRO1108 GRO1267 GRO1268 GRO1597 GRO1655 GRO1656 GRO1659 GRO1660 GRO1661 GRO1865 GRO2045 GRO2048 GRO2052 GRO2055 GRO2056 GRO2136 GRO2137 GRO2314 GRO2595 GRO2752 GRO2753 GRO2754 GRO2895 GRO2989 GRO2990 GRO2991 GRO2992 GRO3123 GRO3128 GRO3132 GRO3133 GRO3204 GRO3250 GRO3251 GRO3252 GRO3253 GRO3354 GRO3636 GRO3638 GRO3639 GRO3641 GRO3643 GRO3644 GRO3646 GRO3813 GRO3815 GRO4107 GRO4108 GRO4116 GRO4117 GRO4118 GRO4119 GRO4120 GRO4121 GRO4280 GRO1662 GRO3611 GRO3763', 'Csőventilátor, elszívó ventilátor', [], 'Erős', 'Csőventilátor (Can-Fan, Vents, Prima Klima, AC Infinity, Garden Highpro, DF16)'),
 ('GRO0788 GRO1237 GRO1239 GRO1352 GRO2039 GRO2132 GRO2447 GRO3184 GRO3376 GRO4198 GRO4199 GRO4339 GRO3272', 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát', [], 'Erős', 'Ventilátor fordulatszám-, hőmérséklet-, nyomásszabályzó, környezeti vezérlő'),
 ('GRO0789 GRO2392 GRO2799', 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát', [], 'Erős', 'Termosztát (fűtés / hűtés / ventilátor kapcsolása)'),
 ('GRO0790 GRO3186', 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát', ['Párásító', 'Páramentesítő'], 'Erős', 'Páratartalom-szabályzó (higrosztát)'),
 ('GRO1439', 'Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát', ['CO2-pótlás, CO2-mérő'], 'Erős', 'Superpro klímaszabályzó (hő, pára, CO2)'),
 ('GRO4368', 'Párásító', ['Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát'], 'Erős', 'Párásító vezérlő'),
 ('GRO1461 GRO3323 GRO3841 GRO4200 GRO4209 GRO4575 GRO4658', 'Párásító', [], 'Erős', 'Párásító (ultrahangos, Cloudforge, Dark Fogger)'),
 ('GRO0791 GRO2089 GRO3787 GRO4497 GRO4409', 'Páramentesítő', [], 'Erős', 'Páramentesítő'),
 ('GRO0795 GRO0796 GRO3565 GRO4125 GRO4126 GRO4127 GRO4271', 'Hő- és páratartalom-mérő', [], 'Erős', 'Digitális hő- és páratartalom-mérő (thermo-higrométer) – a Mérőműszer ágban is'),
 ('GRO2490 GRO3790 GRO3902 GRO3903 GRO4095 GRO4096', 'CO2-pótlás, CO2-mérő', [], 'Erős', 'CO2 zsák, CO2 termelő doboz, tabletta'),
 ('GRO4160 GRO4247 GRO3811', 'CO2-pótlás, CO2-mérő', [], 'Erős', 'CO2 palack, adapter, reduktor'),
 ('GRO4162 GRO4163', 'CO2-pótlás, CO2-mérő', [], 'Erős', 'CO2 generátor (propán)'),
 ('GRO3563 GRO3734 GRO4340', 'CO2-pótlás, CO2-mérő', ['Klímavezérlő: ventilátor-szabályzó, termosztát, higrosztát'], 'Erős', 'CO2 érzékelő, szabályzó'),
 ('GRO3109 GRO3110 GRO3530', 'Légtechnikai cső, idom, bilincs', [], 'Laza', 'Secret Jardin DF16 csatlakozó sátor kivágáshoz'),
 ('GRO1436 GRO1664 GRO1834 GRO2094 GRO2736 GRO3059 GRO3542 GRO3543 GRO3544 GRO3545 GRO3546', 'Légtechnikai cső, idom, bilincs', ['Csőventilátor, elszívó ventilátor'], 'Erős', 'Ventilátor hangtompító (Can Filters Silencer)'),
 ('GRO0306 GRO0307 GRO0308 GRO0310 GRO0312 GRO0317 GRO0318 GRO0319 GRO0321 GRO0322 GRO0330 GRO0331 GRO0332 GRO0334 GRO0335 GRO0336 GRO1771 GRO2382 GRO2383 GRO3023 GRO3025 GRO3028 GRO3747 GRO4305 GRO4501 GRO4529 GRO4703 GRO4705', 'Légtechnikai cső, idom, bilincs', [], 'Erős', 'Flexibilis légcsatorna cső (Aluflex, Sonoflex, Combiflex)'),
 ('GRO2140 GRO2141 GRO2142 GRO2391 GRO2596 GRO2597 GRO2889 GRO2890 GRO2891', 'Légtechnikai cső, idom, bilincs', [], 'Erős', 'Alumínium / Duct Tape ragasztószalag'),
 ('GRO1668 GRO1669 GRO1670 GRO2153 GRO2154 GRO2155 GRO2156 GRO2157 GRO2601 GRO2602 GRO2603 GRO2756 GRO3718 GRO3719 GRO3720 GRO3721 GRO3722 GRO4304', 'Légtechnikai cső, idom, bilincs', [], 'Erős', 'Légtechnikai bilincs'),
 ('GRO0355 GRO0358 GRO0361 GRO0604 GRO0700 GRO1056 GRO1060 GRO1062 GRO1934 GRO1935 GRO1936 GRO1941 GRO1959 GRO1960 GRO1961 GRO1962 GRO1963 GRO1964 GRO1966 GRO1968 GRO1971 GRO1972 GRO1973 GRO1974 GRO1975 GRO1976 GRO1978 GRO2143 GRO2144 GRO2164 GRO2168 GRO2316 GRO2317 GRO2390 GRO2587 GRO2588 GRO2589 GRO2590 GRO2591 GRO2592 GRO2593 GRO2594 GRO2598 GRO2604 GRO3275 GRO3576 GRO3578 GRO3579 GRO3580 GRO3581 GRO3582 GRO3583 GRO3584 GRO3585 GRO3586 GRO3587 GRO3588 GRO3589 GRO3590 GRO3591 GYUJTO0485 GRO1967 GRO1969 GRO1970 GRO3577', 'Légtechnikai cső, idom, bilincs', [], 'Erős', 'Idom, bővítő / szűkítő, csőtoldó, visszacsapó szelep, csőkapcsoló'),
]
