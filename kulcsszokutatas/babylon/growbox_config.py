# Babylon – Growbox, termesztősátor (2026-10-16, 2. változat)
# A jelenlegi éles ÉS sandbox alkategória-elrendezést NEM vettük figyelembe:
# a szerkezet kizárólag az élő termékkínálatból és a kulcsszóadatból készült.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='Termesztősátor (growbox)', sheet='1 Termesztősátor', fo='termesztősátor',
      area='Fényzáró, fényvisszaverő belsejű beltéri termesztősátor (Secret Jardin, Homebox, Cultibox, Garden Highpro, GF) – 30×30 cm-től 480×240 cm-ig',
      place='2. szint – a termékkör magja; méret (alapterület), magasság és márka = szűrő, nem alkategória',
      note='A keresés kicsi, de tiszta: termesztősátor 90, grow tent 70, növénysátor 50, növénytermesztő sátor 50. Méretre és modellre csak ~10/hó (growbox 80x80, 120x120, 150x150, hydro shoot…) – ezért a méret szűrő. A „homebox” (140) a Telekom Home Box miatt vegyes.',
      kws='''termesztősátor|S|F
növénysátor|S|S
növény sátor|S|E
növénytermesztő sátor|S|S
grow tent|S|S
beltéri sátor|S|E
beltéri növény sátor|S|E
termeszto sator|S|E
mini growbox|S|E
grow box mini|S|E
growbox 40x40|S|E
growbox 60x60x120|S|E
growbox 80x80|S|E
growbox 90x90|S|E
growbox 100x100|S|E
growbox 120x60|S|E
growbox 120x120|S|E
growbox 150x150|S|E
growbox 200x200x200|S|E
használt termesztő sátor|L|E
grow box eladó|S|E
homebox|L|G
homebox ambient|S|G
secret jardin|S|G
secret jardin darkroom|S|G
secret jardin hydro shoot|S|G
secret jardin dark street|S|G
dark street|S|G
hydro shoot|S|G
cultibox|S|G
growbox mars hydro|X|X
telekom home box|X|X'''),
 dict(name='Nevelősátor – palánta, dugvány, anyanövény', sheet='2 Nevelősátor', fo='palántanevelő sátor',
      area='Alacsony, kis alapterületű nevelősátor palántához, dugványozáshoz, anyanövényhez (Secret Jardin Dark Propagator, Garden Highpro Propagator Box, Homebox R80S)',
      place='2. szint – saját terméktípus és saját keresés; a Palántanevelő ágban kereszt-link (céloldal itt)',
      note='A „palántanevelő sátor” (110) a branch második legnagyobb terméktípus-kulcsszava – több, mint maga a „growbox” (70). A „palántanevelő fóliasátor” (40) kerti – laza.',
      kws='''palántanevelő sátor|S|F
növénynevelő sátor|S|S
palántanevelő fóliasátor|L|E
palántanevelő|LN|N'''),
 dict(name='Gombatermesztő sátor', sheet='3 Gombatermesztő sátor', fo='gombatermesztő sátor',
      area='Párás, zárt gombatermesztő sátor (Probox MushPro) – laskagomba, shiitake, otthoni gombatermesztés',
      place='2. szint (kicsi, 3 termék) – vagy a Nevelősátor alatt 3. szinten; tartalomra épülő kategória (gombatermesztés otthon)',
      note='A sátorra kicsi a keresés (30), de a téma nagy: gomba termesztés 320, laskagomba termesztés 210, gombatermesztő készlet 170 – útmutató-tartalommal ide terelhető. Bővítési lehetőség: termőblokk, gombacsíra (laskagomba termőblokk 70).',
      kws='''gombatermesztő sátor|S|F
gombatermesztés otthon|S|S
gombatermesztés házilag|S|I
gomba termesztés|L|I
laskagomba termesztés|L|I
gombatermesztő készlet|L|E
laskagomba termőblokk|LN|N'''),
 dict(name='Komplett growbox szett', sheet='4 Growbox szett', fo='növénytermesztő sátor szett',
      area='Sátor + lámpa (LED / HPS) + szellőzés egy csomagban – kezdő és haladó szettek',
      place='2. szint – a „szett” keresések egyetlen céloldala (a LED ágból ide link)',
      note='Kis keresés (növénytermesztő sátor szett 40, grow box szett 20, termesztő sátor szett 20), de nagy kosárérték és kezdő vásárló. Méret és lámpatípus (LED / HPS) = szűrő.',
      kws='''növénytermesztő sátor szett|S|F
grow box szett|S|S
termesztő sátor szett|S|S
növény sátor szett|S|E
grow box led|S|E'''),
 dict(name='Növénytámasztó háló (SCROG), yoyo', sheet='5 SCROG háló', fo='növénytartó háló',
      area='SCROG / növénytartó háló a sátor keretére (WEBIT, Web Plant Support, AC Infinity), yoyo ágfelfüggesztő',
      place='2. szint – saját terméktípus (~17 termék)',
      note='A „növénytartó háló” (50) és a „scrog” (20) tiszta szándékú. Az „uborkaháló” (720) kerti futtatóháló – ugyanaz a hálótípus, de kerti szándék (LN, a leírásban említhető). A „növénytámasz” (880) karó / spirál – nem ide.',
      kws='''növénytartó háló|S|F
scrog|S|S
uborkaháló|LN|N
uborka háló|LN|N
uborka futtató háló|LN|N
növénytámasz|LN|N'''),
 dict(name='Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító', sheet='6 Sátorkiegészítő', fo='vízgyűjtő tálca',
      area='Vízgyűjtő tálca a sátor aljába, sarokelem, Space Booster bővítő, DF16 keret / csatlakozó, sátorjavító matrica, pollenháló',
      place='2. szint (kiegészítő) – a vásárló sátormárka / -méret szerint keres',
      note='Kis keresés (vízgyűjtő tálca 20, sátor javító készlet 40, sátor javítás 40 – utóbbi jórészt kemping). A lámpafüggesztő (Rope Ratchet) céloldala a LED ágban – itt másodlagosan jelenik meg.',
      kws='''vízgyűjtő tálca|S|F
sátor javító készlet|L|S
sátor javítás|L|E
sátor cipzár javítás|LN|N'''),
 dict(name='Fényvisszaverő fólia', sheet='7 Fólia', fo='fényvisszaverő fólia',
      area='Mylar, fekete-fehér és gyémántmintás fényvisszaverő fólia termesztőtér / szoba bélelésére (méterre és tekercsben)',
      place='2. szint – a branch legerősebb kulcsszava; a LED ágból kereszt-ajánlás',
      note='Fényvisszaverő fólia 390, mylar fólia 170, fekete fehér fólia 50. Az ablakra / autóra szánt fólia (140 / 40) más termék – kizárva.',
      kws='''fényvisszaverő fólia|S|F
mylar fólia|S|S
fekete fehér fólia|S|S
reflexiós fólia|S|E
ezüst fólia|L|E
fekete fehér fólia ár|S|E
öntapadós fényvisszaverő fólia|L|E
fényvisszaverő fólia ablakra|LN|N
fényvisszaverő ablakfólia|LN|N
fényvisszaverő fólia autóra|LN|N'''),
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'A keresők egybeírják: „termesztősátor” (90); „growbox” (70), „grow box” (70). Javasolt menünév: „Growbox, termesztősátor”.', '''growbox|S
grow box|S
termesztősátor|S'''),
 ('Sátor vásárlása', '→ Termesztősátor (growbox)', '''termesztősátor|S
növénysátor|S
grow tent|S'''),
 ('Méret szerinti keresés', 'Csak szűrő – ~10/hó', '''growbox 80x80|S
growbox 120x120|S
growbox 150x150|S'''),
 ('Palánta, dugvány', '→ Nevelősátor', '''palántanevelő sátor|S
növénynevelő sátor|S'''),
 ('Gomba', '→ Gombatermesztő sátor (+ tartalom)', '''gombatermesztő sátor|S
gombatermesztés otthon|S'''),
 ('Kezdő, „minden egyben”', '→ Komplett growbox szett', '''növénytermesztő sátor szett|S
grow box szett|S'''),
 ('Sátor felszerelése', '→ SCROG háló; Sátorkiegészítő; Fényvisszaverő fólia', '''növénytartó háló|S
vízgyűjtő tálca|S
fényvisszaverő fólia|S'''),
]

EXT = [
 ('Fóliasátor (kerti)', 'Nagyon nagy, de kerti szándék (fóliasátor 5400, fóliasátor váz 1000) – nem a mi termékünk, a „sátor” szó miatt figyelni kell a hirdetésekben (negatív kulcsszó)', '''fóliasátor|LN
mini fóliasátor|LN'''),
 ('Mini üvegház, beltéri üvegház', 'Céloldal a Palántanevelő, mini üvegház ágban – innen link a nevelősátorhoz', '''mini üvegház|L
beltéri üvegház|L
növényház|L'''),
 ('Gombatermesztés', 'Tartalom + kínálatbővítés (termőblokk, gombacsíra)', '''gomba termesztés|L
laskagomba termesztés|L
gombatermesztő készlet|L
laskagomba termőblokk|L'''),
 ('Kerti növénytámasz, uborkaháló', 'Kerti szándék – a SCROG-háló leírásában említhető', '''uborkaháló|L
növénytámasz|L'''),
 ('Lámpa, szellőzés a sátorba', 'Céloldal a LED és a Légtechnika ágban – a sátorlapokon kereszt-ajánlás (lámpa, csőventilátor, szénszűrő)', '''növénynevelő lámpa|L'''),
 ('Ablak- / autófólia', 'Nem a mi termékünk', '''fényvisszaverő fólia ablakra|LN
fényvisszaverő fólia autóra|LN'''),
]

MAKERS = '''homebox
homebox ambient
secret jardin
secret jardin darkroom
secret jardin hydro shoot
secret jardin dark street
dark street
cultibox
growbox mars hydro'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Growbox, termesztősátor (csak termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A jelenlegi éles és sandbox alkategória-elrendezést NEM vettük figyelembe. Kiindulás: az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'Growbox, termesztősátor'
STRUCT = [
 (1, FO, '–', 'growbox', 'S', 'Főkategória (hub)', 'Growbox 70, grow box 70 – a főkategória gyűjtőoldal; a „termesztősátor” (90) céloldala a sátor-alkategória.', None),
 (2, 'Termesztősátor (growbox)', FO, 'termesztősátor', 'S', 'Önálló kategória', 'Minden termesztősátor; méret / magasság / márka = szűrő.', 'Termesztősátor (growbox)'),
 (2, 'Nevelősátor – palánta, dugvány, anyanövény', FO, 'palántanevelő sátor', 'S', 'Önálló kategória', 'Palántanevelő sátor 110.', 'Nevelősátor – palánta, dugvány, anyanövény'),
 (2, 'Gombatermesztő sátor', FO, 'gombatermesztő sátor', 'S', 'Kis kategória + tartalom', 'Gomba termesztés 320 – tartalommal terelhető.', 'Gombatermesztő sátor'),
 (2, 'Komplett growbox szett', FO, 'növénytermesztő sátor szett', 'S', 'Önálló kategória', 'A szett-keresések egyetlen céloldala.', 'Komplett growbox szett'),
 (2, 'Növénytámasztó háló (SCROG), yoyo', FO, 'növénytartó háló', 'S', 'Önálló kategória', 'Növénytartó háló 50, scrog 20.', 'Növénytámasztó háló (SCROG), yoyo'),
 (2, 'Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító', FO, 'vízgyűjtő tálca', 'S', 'Kiegészítő kategória', 'Tálca, sarokelem, bővítő, javító.', 'Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító'),
 (2, 'Fényvisszaverő fólia', FO, 'fényvisszaverő fólia', 'S', 'Önálló kategória', 'A branch legerősebb kulcsszava (390).', 'Fényvisszaverő fólia'),
]
NOT_CATS = [
 ('Méret szerinti alkategória (kis / közepes / nagy growbox)', 'growbox 120x120', 'Méretre ~10/hó – szűrő, nem kategória.'),
 ('Márka szerinti alkategória (Homebox, Secret Jardin)', 'homebox', 'Kis és vegyes (Telekom Home Box) – márkaszűrő.'),
 ('Fóliasátor', 'fóliasátor', 'Kerti termék – nem célozni; negatív kulcsszó a hirdetésekben.'),
 ('Lámpafüggesztő', None, 'Céloldala a LED ágban (Növénylámpa-kiegészítő).'),
 ('Szárítóháló', None, 'A Növényfeldolgozás ágba való.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak azok a termékek kaptak kategóriát, amelyek az elmúlt 30 napban szerepeltek a Babylon Google Shopping-feedben (1525 termék) – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak, javasolt kategóriával.',
 'A kategóriaszerkezet a jelenlegi éles és sandbox alkategóriáktól függetlenül, terméktípus és keresési szándék alapján készült. Az éles oldal (babylon-grow.eu) és a Shoprenter API a felhőből nem érhető el.',
 'A sátrak méretszűrője alapterület szerint: kis ≤ 80×80 cm, közepes 90×90 – 120×120 cm, nagy 150×150 cm-től (a megjegyzés oszlopban). Ahol a névben nincs méret, a modellszámból becsültük – ellenőrizendő.',
]

TITLE = 'babylon-grow.eu – Growbox, termesztősátor kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15/16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok (a 10-es érték a legkisebb lépcső). Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: a jelenlegi alkategóriákat (éles és sandbox) figyelmen kívül hagytuk – a szerkezet a termékek típusából (sátor, nevelősátor, gombasátor, szett, háló, kiegészítő, fólia) és a keresési szándékból épül.',
 'Fő megállapítás: a growbox-téma keresése kicsi (termesztősátor 90, growbox 70); a méretre ~10/hó → méret = szűrő. A legerősebb terméktípus-kulcsszavak: fényvisszaverő fólia 390, palántanevelő sátor 110.',
 'Új javaslat: Gombatermesztő sátor – kicsi termékkör, de a gombatermesztés-téma nagy (gomba termesztés 320, laskagomba termesztés 210) → tartalommal és bővítéssel.',
 'A „fóliasátor” (5400) kerti termék – a „sátor” szó miatt negatív kulcsszóként kezelendő a hirdetésekben.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a jelenlegi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más ágban lévő céloldalak, kereszt-linkek, kínálatbővítési lehetőségek és kerülendő (negatív) témák.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO0817 GRO2425 GRO2437 GRO2438 GRO2439 GRO2697 GRO3141 GRO3142 GRO3904 GRO3906 GRO3907 GRO3921 GRO3922 GRO4137 GRO4138 GRO4237 GRO4238 GRO4274', 'Termesztősátor (growbox)', [], 'Erős', 'Termesztősátor – méretszűrő: ≤ 80×80 cm (kis, 1–4 növény)'),
 ('GRO0816 GRO0963 GRO2421 GRO2426 GRO2427 GRO2458 GRO2459 GRO2586 GRO2701 GRO2702 GRO2861 GRO3143 GRO3144 GRO3446 GRO3552 GRO3755 GRO3882 GRO3920 GRO4231 GRO4239', 'Termesztősátor (growbox)', [], 'Erős', 'Termesztősátor – méretszűrő: 90×90 – 120×120 cm (közepes, 4–9 növény)'),
 ('GRO2422 GRO2424 GRO2703 GRO3140 GRO3145 GRO3146 GRO3196 GRO3197 GRO3326 GRO3327 GRO3328 GRO3368 GRO3553 GRO3554 GRO3555 GRO3556 GRO3560 GRO4325', 'Termesztősátor (growbox)', [], 'Erős', 'Termesztősátor – méretszűrő: 150×150 cm-től (nagy, 9+ növény)'),
 ('GRO2435 GRO2734 GRO3558 GRO4134 GRO4135 GRO4136 GRO2699', 'Nevelősátor – palánta, dugvány, anyanövény', [], 'Erős', 'Alacsony nevelősátor (Dark Propagator, Propagator Box, Homebox R80S)'),
 ('GRO4343 GRO4344 GRO4577', 'Gombatermesztő sátor', ['Nevelősátor – palánta, dugvány, anyanövény'], 'Erős', 'Probox MushPro gombatermesztő sátor'),
 ('GYSZ0012 GYSZ0013 GYSZ0013V GYSZ0054 GYSZ0054V GYSZ0059 GYSZ0059V GYSZ0062 GYSZ0062V GYSZ0063 GYSZ0063V GRO4142 GRO4143 GRO4106', 'Komplett growbox szett', ['Termesztősátor (growbox)'], 'Erős', 'Komplett szett (sátor + lámpa + szellőzés) – méretszűrő: Kis growbox'),
 ('GYSZ0015 GYSZ0015V GYSZ0016 GYSZ0016V GYSZ0018 GYSZ0018V GYSZ0060 GYSZ0060V GYSZ0064 GYSZ0064V GYSZ0065 GYSZ0065V GRO4144 GRO4188 GRO4189 GRO4583', 'Komplett growbox szett', ['Termesztősátor (growbox)'], 'Erős', 'Komplett szett (sátor + lámpa + szellőzés) – méretszűrő: Közepes growbox'),
 ('GYSZ0066 GYSZ0066V GYSZ0067 GYSZ0067V', 'Komplett growbox szett', ['Termesztősátor (growbox)'], 'Erős', 'Komplett szett (sátor + lámpa + szellőzés) – méretszűrő: Nagy growbox'),
 ('GYSZ0053V', 'Komplett growbox szett', ['Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító'], 'Laza', 'Kiegészítő csomag sátorszettekhez'),
 ('GRO1956 GRO2444 GRO2445 GRO3396 GRO3442 GRO3689 GRO3690 GRO4313 GRO4314 GRO4315 GRO4316 GRO4302 GRO4330 GRO4563 GRO3878 GRO3879 GRO3880', 'Növénytámasztó háló (SCROG), yoyo', [], 'Erős', 'Növénytartó / SCROG háló (WEBIT, Web Plant Support)'),
 ('GRO1112', 'Növénytámasztó háló (SCROG), yoyo', [], 'Erős', 'Yoyo növényfelfüggesztő'),
 ('GRO3124 GRO4667 GRO4668 GRO4669 GRO4670 GRO4671 GRO4672 GRO4673 GRO4674', 'Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító', [], 'Erős', 'Vízgyűjtő tálca a sátor aljába'),
 ('GRO0770 GRO4270 GRO4123 GRO4124 GRO3398 GRO3723', 'LED ág – Növénylámpa-kiegészítő (függesztő)', ['Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító'], 'Más főkategória', 'Lámpa- / trafó-felfüggesztő – céloldal a LED ágban'),
 ('GRO2442 GRO2443 GRO3691 GRO3725 GRO3726 GRO3329 GRO3331 GRO3109 GRO3110 GRO3530 GRO3506 GRO3507', 'Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító', [], 'Erős', 'Sátoralkatrész: sarokelem, Space Booster, DF16 keret / csatlakozó, sátorjavító matrica'),
 ('GRO2576', 'Sátorkiegészítő: vízgyűjtő tálca, alkatrész, javító', [], 'Laza', 'Pollenháló (szellőzőnyílásra)'),
 ('GRO0050 GRO0052 GRO0825 GRO4336 GRO4337 GRO4338 GRO4551 GRO4552 GRO4553 GRO4554 GRO4555 GRO4556', 'Fényvisszaverő fólia', [], 'Erős', 'Mylar, fekete-fehér, gyémántmintás fényvisszaverő fólia'),
 ('GRO0676', 'Tápok ág – tápszett', [], 'Más főkategória', 'Plagron Top Grow Box – tápszett, nem sátor'),
 ('GYSZ0005 GYSZ0005V GYSZ0006 GYSZ0006V GYSZ0007 GYSZ0007V GYSZ0023 GYSZ0023V', 'Világítás ág – HPS lámpaszett', [], 'Más főkategória', 'Lámpaszett sátor nélkül'),
 ('GRO0826 GRO0827 GRO2844 GRO2845 GRO4129 GRO4130 GRO4299 GRO4569 GRO4570', 'Növényfeldolgozás ág – Szárítóháló', [], 'Más főkategória', 'Szárítóháló – a sátorba akasztható, de a Növényfeldolgozás ágba való'),
 ('GRO3909', 'Palántanevelő ág – Propagátor kiegészítő', [], 'Más főkategória', 'Secret Jardin fűtőlap'),
]
