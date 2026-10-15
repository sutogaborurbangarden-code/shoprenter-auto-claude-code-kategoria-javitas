# Babylon – Growbox, termesztő sátor (sandbox-főkategória, 2026-10-15)
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='Kis growbox (80×80 cm-ig)', sheet='1 Kis growbox', fo='mini growbox',
      area='Termesztősátor 1–4 növényhez – alapterület legfeljebb 80×80 cm (30×30 … 80×80, 60×40, 100×60)',
      place='2. szint – navigációs (méret szerinti) kategória; a sandbox-név jó',
      note='Méretre szinte nincs keresés (mini growbox 10, growbox 40x40 10, growbox 80x80 10). A kategória navigációs: a vásárló méret szerint választ. SEO-szöveg a „kis termesztősátor / mini growbox” témára, a fő kulcsszó (termesztősátor) céloldala a főkategória.',
      kws='''mini growbox|S|F
grow box mini|S|E
growbox 40x40|S|E
growbox 60x60x120|S|E
growbox 80x80|S|E'''),
 dict(name='Közepes growbox (100×100 – 120×120 cm)', sheet='2 Közepes growbox', fo='growbox 120x120',
      area='Termesztősátor 4–9 növényhez – 90×90, 100×100, 120×60, 120×90, 120×120 cm',
      place='2. szint – navigációs kategória; a sandbox-név jó',
      note='Méretkeresések 10/hó körül (growbox 100x100, 120x120, 90x90, 120x60). Navigációs szerep.',
      kws='''growbox 120x120|S|F
growbox 100x100|S|E
growbox 90x90|S|E
growbox 120x60|S|E'''),
 dict(name='Nagy growbox (150×150 cm-től)', sheet='3 Nagy growbox', fo='growbox 150x150',
      area='Termesztősátor 9+ növényhez – 150×150, 200×200, 240×120, 240×240, 300×150, 300×300 cm',
      place='2. szint – navigációs kategória; a sandbox-név jó',
      note='Méretkeresések 10/hó (growbox 150x150, growbox 200x200x200). Kevés, de magas kosárértékű termék.',
      kws='''growbox 150x150|S|F
growbox 200x200x200|S|E'''),
 dict(name='Palántanevelő és propagátor sátor', sheet='4 Palántanevelő sátor', fo='palántanevelő sátor',
      area='Alacsony nevelősátor palántákhoz, dugványokhoz, anyanövényhez (Dark Propagator, Propagator Box); gombatermesztő sátor',
      place='2. szint – a sandbox-név jó; a Palántanevelő ágban kereszt-link (egy céloldal: itt)',
      note='A „palántanevelő sátor” (110) az ág egyik legjobb kulcsszava – több, mint maga a „growbox” (70). A „palántanevelő” (720) a Palántanevelő főkategória fő szava, nem ide.',
      kws='''palántanevelő sátor|S|F
növénynevelő sátor|S|S
gombatermesztő sátor|L|E
palántanevelő|LN|N'''),
 dict(name='Komplett growbox szett', sheet='5 Growbox szett', fo='növénytermesztő sátor szett',
      area='Sátor + lámpa (LED / HPS) + szellőzés egy csomagban – kezdő és haladó szettek',
      place='2. szint – a sandbox-név jó; a szettek másodlagosan a méret szerinti kategóriákban is',
      note='Kis keresés (növénytermesztő sátor szett 40, grow box szett 20, termesztő sátor szett 20), de nagy kosárérték és kezdő vásárlók – a „szett” szót a címben tartsuk meg.',
      kws='''növénytermesztő sátor szett|S|F
grow box szett|S|S
termesztő sátor szett|S|S
növény sátor szett|S|E
grow box led|S|E'''),
 dict(name='Growbox kiegészítő – háló, tálca, felfüggesztő', sheet='6 Kiegészítő', fo='növénytartó háló',
      area='Növénytartó / SCROG háló, yoyo, vízgyűjtő tálca, lámpafelfüggesztő, sátoralkatrész, sátorjavító',
      place='2. szint (sandbox: „Growbox kiegészítő – háló, tálca, polc”) – a „polc” helyett „felfüggesztő”: polc termékünk nincs, a növénypolc (30) más szándék',
      note='A „növénytartó háló” (50) és a „scrog” (20) tiszta szándékú. Az „uborkaháló” (720) kerti futtatóháló – ugyanaz a hálótípus, de kerti szándék (LN, a leírásban említhető). A „növénytámasz” (880) karó / spirál – nem ide.',
      kws='''növénytartó háló|S|F
scrog|S|S
uborkaháló|LN|N
uborka háló|LN|N
uborka futtató háló|LN|N
vízgyűjtő tálca|S|E
sátor javító készlet|L|E
növénypolc|LN|N
növénytámasz|LN|N'''),
 dict(name='Fényvisszaverő fólia', sheet='7 Fólia', fo='fényvisszaverő fólia',
      area='Mylar, fekete-fehér és gyémántmintás fényvisszaverő fólia termesztőtér bélelésére',
      place='2. szint – a sandbox-név jó',
      note='Az ág legerősebb önálló kulcsszava (fényvisszaverő fólia 390, mylar fólia 170). Az ablakra / autóra szánt fényvisszaverő fólia (140 / 40) más termék – kizárva.',
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

OLD_SHEET = 'Sandbox menünevek'
OLD = [
 ('Growbox, termesztő sátor (főkategória)', 'Jó név; a keresők egybeírják: „termesztősátor” (90), „growbox” (70), „grow box” (70). Javasolt: „Growbox, termesztősátor”.', '''termesztősátor|S
growbox|S
grow box|S
növénysátor|S'''),
 ('Kis growbox 1–4 növényhez (80×80 cm és alatta)', 'Marad – navigációs, méretre alig van keresés.', '''mini growbox|S
growbox 80x80|S'''),
 ('Közepes growbox 4–9 növényhez (100×100 – 120×120 cm)', 'Marad – navigációs.', '''growbox 100x100|S
growbox 120x120|S'''),
 ('Nagy growbox 9+ növényhez (150×150 cm és felette)', 'Marad – navigációs.', '''growbox 150x150|S'''),
 ('Palántanevelő és propagátor sátor', 'Marad; erős kulcsszó (110).', '''palántanevelő sátor|S'''),
 ('Komplett growbox szett', 'Marad.', '''növénytermesztő sátor szett|S
grow box szett|S'''),
 ('Growbox kiegészítő – háló, tálca, polc', '„polc” → „felfüggesztő” (nincs polc termék).', '''növénytartó háló|S
növénypolc|LN'''),
 ('Fényvisszaverő fólia', 'Marad; az ág legerősebb kulcsszava.', '''fényvisszaverő fólia|S
mylar fólia|S'''),
]

EXT = [
 ('Kerti növénytámasz, uborkaháló', 'Nagy volumen, kerti szándék – a SCROG-háló leírásában említhető, külön kategória csak kínálatbővítéssel', '''uborkaháló|L
növénytámasz|L
uborka háló|L'''),
 ('Gombatermesztés', 'Kis, de tiszta téma – a MushPro sátrakkal hub-tartalom lehet', '''gombatermesztés otthon|L
gombatermesztő sátor|S'''),
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

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Growbox, termesztősátor (termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet, a Google Shopping-feed termékei (1999 db) és a Kulcsszótervező adatai. Termékszám = elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'Growbox, termesztősátor'
STRUCT = [
 (1, FO, '–', 'termesztősátor', 'S', 'Főkategória', 'A fő kulcsszavak (termesztősátor 90, growbox 70, grow box 70, növénysátor 50, homebox 140 márka) céloldala a főkategória.', None),
 (2, 'Kis growbox (80×80 cm-ig)', FO, 'mini growbox', 'S', 'Navigációs kategória', 'Méret szerinti bontás – keresés nincs, de a vásárlói döntést segíti.', 'Kis growbox (80×80 cm-ig)'),
 (2, 'Közepes growbox (100×100 – 120×120 cm)', FO, 'growbox 120x120', 'S', 'Navigációs kategória', 'Legtöbb sátormodell itt.', 'Közepes growbox (100×100 – 120×120 cm)'),
 (2, 'Nagy growbox (150×150 cm-től)', FO, 'growbox 150x150', 'S', 'Navigációs kategória', 'Darkroom, Hydro Shoot W, Homebox Q150+ … R300+.', 'Nagy growbox (150×150 cm-től)'),
 (2, 'Palántanevelő és propagátor sátor', FO, 'palántanevelő sátor', 'S', 'Önálló kategória', 'Palántanevelő sátor 110 – az ág második legjobb termékszava.', 'Palántanevelő és propagátor sátor'),
 (2, 'Komplett growbox szett', FO, 'növénytermesztő sátor szett', 'S', 'Önálló kategória', 'Szettek elsődlegesen itt, másodlagosan méret szerint.', 'Komplett growbox szett'),
 (2, 'Growbox kiegészítő – háló, tálca, felfüggesztő', FO, 'növénytartó háló', 'S', 'Önálló kategória', 'Sandbox: „… háló, tálca, polc” – polc termék nincs.', 'Growbox kiegészítő – háló, tálca, felfüggesztő'),
 (2, 'Fényvisszaverő fólia', FO, 'fényvisszaverő fólia', 'S', 'Önálló kategória', 'Fényvisszaverő fólia 390, mylar fólia 170.', 'Fényvisszaverő fólia'),
]
NOT_CATS = [
 ('Márka szerinti sátor-alkategória (Homebox, Secret Jardin)', 'homebox', 'A „homebox” 140 – de a Telekom Home Box miatt vegyes; a márka legyen szűrő, ne kategória.'),
 ('Növénypolc / palántanevelő állvány', 'növénypolc', 'Nincs ilyen termék.'),
 ('Szárítóháló', None, 'A Növényfeldolgozás ágba való (ott van céloldala).'),
 ('HPS / LED lámpaszett sátor nélkül', None, 'A Világítás ágba való.'),
]
PRODUCT_NOTE = [
 'Forrás: a Babylon Google Ads fiók Shopping-termékadatai (termékkód = Shopping item ID, terméknév = feed-cím), 2024-10-01 – 2026-10-14, összesen 1999 termék. A Shoprenter API és az éles oldal a felhőből nem érhető el.',
 'Figyelem: ez a Google-ben hirdetett termékkör, nem feltétlenül a teljes katalógus. A gyártó és a gyűjtőtermék (GYUJTO…) adat a feedben nem érhető el.',
 'Méret szerinti besorolás az alapterület alapján: Kis ≤ 0,64 m² (80×80), Közepes ≤ 1,44 m² (120×120), Nagy > 1,44 m². Ahol a terméknévben nincs méret (pl. DR150, DS150W, Q200+, Cultibox Light 120), a modellszámból becsültük – ellenőrizendő.',
 'A komplett szettek elsődlegesen a „Komplett growbox szett” kategóriában, másodlagosan a méretüknek megfelelő kategóriában.',
]

TITLE = 'babylon-grow.eu – Growbox, termesztősátor főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok (a 10-es érték a Kulcsszótervező legkisebb lépcsője). Termékek: Google Shopping-feed (1999 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a growbox-téma keresési volumene nagyon kicsi (termesztősátor 90, growbox 70, grow box 70, növénysátor 50). Méretre (80x80, 120x120, 150x150) csak ~10/hó keresés van – a méret szerinti alkategóriák navigációs szerepűek, a SEO-forgalmat a főkategória és a márkás modellnevek hozzák.',
 'A két legerősebb önálló alkategória-kulcsszó: fényvisszaverő fólia (390) és palántanevelő sátor (110).',
 'A „homebox” (140) a Telekom Home Box miatt vegyes; márkaszűrő, nem kategória.',
 'A „termesztő sátor” különírva nem mért keresés – a menünévben és a H1-ben egybeírva: „termesztősátor”.',
]
OLD_TITLE = 'A sandbox „Growbox, termesztő sátor” menünevei – keresési volumen és javaslat'
OLD_SUB = 'Sandbox-tervezet: Kis / Közepes / Nagy growbox; Palántanevelő és propagátor sátor; Komplett growbox szett; Growbox kiegészítő – háló, tálca, polc; Fényvisszaverő fólia.'
EXT_TITLE = 'Rokon területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Nagy volumenű, de kerti / más szándékú témák – csak kínálatbővítés esetén.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO0817 GRO2425 GRO2437 GRO2438 GRO2439 GRO2697 GRO3141 GRO3142 GRO3904 GRO3906 GRO3907 GRO3921 GRO3922 GRO4137 GRO4138 GRO4237 GRO4238 GRO4274', 'Kis growbox (80×80 cm-ig)', [], 'Erős', 'Termesztősátor, alapterület ≤ 80×80 cm (0,64 m²)'),
 ('GRO0816 GRO0963 GRO2421 GRO2426 GRO2427 GRO2458 GRO2459 GRO2586 GRO2701 GRO2702 GRO2861 GRO3143 GRO3144 GRO3446 GRO3552 GRO3755 GRO3882 GRO3920 GRO4231 GRO4239', 'Közepes growbox (100×100 – 120×120 cm)', [], 'Erős', 'Termesztősátor, 0,64–1,44 m² (90×90, 100×100, 120×60, 120×90, 120×120)'),
 ('GRO2422 GRO2424 GRO2703 GRO3140 GRO3145 GRO3146 GRO3196 GRO3197 GRO3326 GRO3327 GRO3328 GRO3368 GRO3553 GRO3554 GRO3555 GRO3556 GRO3560 GRO4325', 'Nagy growbox (150×150 cm-től)', [], 'Erős', 'Termesztősátor, > 1,44 m² (150×150, 240×120, 300×150…)'),
 ('GRO2435 GRO2734 GRO3558 GRO4134 GRO4135 GRO4136 GRO2699', 'Palántanevelő és propagátor sátor', [], 'Erős', 'Alacsony nevelősátor (Dark Propagator, Propagator Box, Homebox R80S)'),
 ('GRO4343 GRO4344 GRO4577', 'Palántanevelő és propagátor sátor', [], 'Laza', 'Probox MushPro gombatermesztő sátor (gombatermesztő sátor 30)'),
 ('GYSZ0012 GYSZ0013 GYSZ0013V GYSZ0054 GYSZ0054V GYSZ0059 GYSZ0059V GYSZ0062 GYSZ0062V GYSZ0063 GYSZ0063V GRO4142 GRO4143 GRO4106', 'Komplett growbox szett', ['Kis growbox (80×80 cm-ig)'], 'Erős', 'Komplett szett (sátor + lámpa + szellőzés) – méret szerint a Kis growbox kategóriában is'),
 ('GYSZ0015 GYSZ0015V GYSZ0016 GYSZ0016V GYSZ0018 GYSZ0018V GYSZ0060 GYSZ0060V GYSZ0064 GYSZ0064V GYSZ0065 GYSZ0065V GRO4144 GRO4188 GRO4189 GRO4583', 'Komplett growbox szett', ['Közepes growbox (100×100 – 120×120 cm)'], 'Erős', 'Komplett szett (sátor + lámpa + szellőzés) – méret szerint a Közepes growbox kategóriában is'),
 ('GYSZ0066 GYSZ0066V GYSZ0067 GYSZ0067V', 'Komplett growbox szett', ['Nagy growbox (150×150 cm-től)'], 'Erős', 'Komplett szett (sátor + lámpa + szellőzés) – méret szerint a Nagy growbox kategóriában is'),
 ('GYSZ0053V', 'Komplett growbox szett', ['Growbox kiegészítő – háló, tálca, felfüggesztő'], 'Laza', 'Kiegészítő csomag sátorszettekhez'),
 ('GRO1956 GRO2444 GRO2445 GRO3396 GRO3442 GRO3689 GRO3690 GRO4313 GRO4314 GRO4315 GRO4316 GRO4302 GRO4330 GRO4563 GRO3878 GRO3879 GRO3880', 'Growbox kiegészítő – háló, tálca, felfüggesztő', [], 'Erős', 'Növénytartó / SCROG háló (WEBIT, Web Plant Support)'),
 ('GRO1112', 'Growbox kiegészítő – háló, tálca, felfüggesztő', [], 'Erős', 'Yoyo növényfelfüggesztő'),
 ('GRO3124 GRO4667 GRO4668 GRO4669 GRO4670 GRO4671 GRO4672 GRO4673 GRO4674', 'Growbox kiegészítő – háló, tálca, felfüggesztő', [], 'Erős', 'Vízgyűjtő tálca a sátor aljába'),
 ('GRO0770 GRO4270 GRO4123 GRO4124 GRO3398 GRO3723', 'Growbox kiegészítő – háló, tálca, felfüggesztő', [], 'Erős', 'Lámpa- / trafó-felfüggesztő, akasztókészlet, kábelakasztó'),
 ('GRO2442 GRO2443 GRO3691 GRO3725 GRO3726 GRO3329 GRO3331 GRO3109 GRO3110 GRO3530 GRO3506 GRO3507', 'Growbox kiegészítő – háló, tálca, felfüggesztő', [], 'Erős', 'Sátoralkatrész: sarokelem, Space Booster, DF16 keret / csatlakozó, sátorjavító matrica'),
 ('GRO2576', 'Growbox kiegészítő – háló, tálca, felfüggesztő', [], 'Laza', 'Pollenháló (szellőzőnyílásra)'),
 ('GRO0050 GRO0052 GRO0825 GRO4336 GRO4337 GRO4338 GRO4551 GRO4552 GRO4553 GRO4554 GRO4555 GRO4556', 'Fényvisszaverő fólia', [], 'Erős', 'Mylar, fekete-fehér, gyémántmintás fényvisszaverő fólia'),
 ('GRO0676', 'Tápok ág – tápszett', [], 'Más főkategória', 'Plagron Top Grow Box – tápszett, nem sátor'),
 ('GYSZ0005 GYSZ0005V GYSZ0006 GYSZ0006V GYSZ0007 GYSZ0007V GYSZ0023 GYSZ0023V', 'Világítás ág – HPS lámpaszett', [], 'Más főkategória', 'Lámpaszett sátor nélkül'),
 ('GRO0826 GRO0827 GRO2844 GRO2845 GRO4129 GRO4130 GRO4299 GRO4569 GRO4570', 'Növényfeldolgozás ág – Szárítóháló', [], 'Más főkategória', 'Szárítóháló – a sátorba akasztható, de a Növényfeldolgozás ágba való'),
 ('GRO3909', 'Palántanevelő ág – Propagátor kiegészítő', [], 'Más főkategória', 'Secret Jardin fűtőlap'),
]
