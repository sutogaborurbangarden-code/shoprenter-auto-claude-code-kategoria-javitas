# Babylon – Propagátor, propagátor kiegészítő (2026-10-16, 2. változat)
# Csak a FŐKATEGÓRIA NEVE alapján: a korábbi kategórianevek és -szerkezet figyelmen kívül;
# alkategóriák az élő termékkínálat és a kulcsszóadat alapján.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 {'name': 'Propagátor, mini üvegház', 'sheet': '1 Propagátor', 'fo': 'mini üvegház', 'area': 'Fűtés nélküli propagátor (szellőzős fedeles láda), mini üvegház, önöntöző és aeropóniás propagátor', 'place': '2. szint – a „propagátor” (70) helyett a vásárlói szó a „mini üvegház” (590) / „mini melegház” (140); H1: „Propagátor, mini üvegház”', 'note': 'Mini üvegház 590, szaporítóláda / propagátor 70; a „palántanevelő” (880) a főkategória szava.', 'kws': 'mini üvegház|S|F\nmini melegház|S|S\nmini üvegház erkélyre|S|S\nüvegház mini|S|E\nmelegház erkélyre|L|E\nszobai mini üvegház|S|E\nmini növényház|S|E\nkis melegház|L|E\npolcos melegház|L|E\nmini üvegház használata|S|I\nmini melegház házilag|LN|N\nmelegház|LN|N\nnövényház|LN|N\nobi mini üvegház|X|X\nmini melegház lidl|X|X\npropagátor|S|S\npalanta nevelo|S|S\npalantanevelo|S|E\nszaporítóláda|S|S\npropagator|S|E\npalántanevelő láda|S|E\npalántanevelő szett|S|E\npalántanevelő edény|S|E\npalántanevelő üvegház|S|E\npalántanevelő doboz|S|E\npropagátor eladó|S|E\nszaporítóláda használata|S|I'},
 {'name': 'Fűthető propagátor', 'sheet': '2 Fűthető propagátor', 'fo': 'fűthető palántanevelő', 'area': 'Beépített fűtésű propagátor (X-Stream Heat, fűtött tálcás propagátorok)', 'place': '2. szint', 'note': 'Kis volumen, de erős vásárlási szándék. Valószínűleg elég szűrőként / termékcímben kezelni.', 'kws': 'fűthető palántanevelő|S|F\nfűthető propagátor|S|S\nfűthető mini üvegház|S|S\npropagátor fűtés|S|E\nmini üvegház fűtése|S|I\nfűtött palántanevelő|S|E'},
 {'name': 'Palántanevelő tálca, propagátor fedél', 'sheet': '3 Tálca, fedél', 'fo': 'palántanevelő tálca', 'area': 'Palántanevelő (cellás) tálca, propagátor alsó tálca és fedél, kapilláris szőnyeg', 'place': '2. szint – a legerősebb termékszó (1000)', 'note': 'Palántanevelő tálca 1000, szaporító tálca 320, magvető tálca 110, vetőtálca 70.', 'kws': 'palántanevelő tálca|S|F\npalántázó tálca|S|S\npalánta tálca|S|S\nszaporító tálca|S|S\nszaporítótálca|S|E\nvetőtálca|S|E\npalanta nevelo talca|S|E\npalántázó tálca tetővel|S|E\npalánta nevelő tálca|S|E\nműanyag palántanevelő tálca|S|E\ngyökereztető tálca|S|E\nnövény szaporító tálca|S|E\npalánta ültető tálca|S|E\nnikecell palántanevelő tálca|S|E\npalántanevelő tálca használata|S|I\nmikrozöld tálca|L|E\nhasznált palántanevelő tálca eladó|X|X\npalántázó tálca lidl|X|X\npalántázó tálca aldi|X|X\nmagvető tálca|S|S'},
 {'name': 'Palántanevelő cserép, tőzegcserép', 'sheet': '4 Palántanevelő cserép', 'fo': 'palántanevelő cserép', 'area': 'Lebomló tőzegcserép (Jiffy), rostcserép (Garland), kis műanyag palántázócserép', 'place': '2. szint', 'note': '', 'kws': 'palántanevelő cserép|S|F\npalánta cserép|S|S\ntőzegcserép|S|S\ntőzeg cserép|S|E\npalántanevelő pohár|S|E\nszaporító cserép|S|E\nkókuszrost cserép|S|E\ntőzegcserép használata|S|I\npalánta cserép obi|X|X'},
 {'name': 'Fűtőlap, termosztát', 'sheet': '5 Fűtőlap, termosztát', 'fo': 'fűtőlap', 'area': 'Propagátor-fűtőlap, földmelegítő kábel és a hozzá való termosztát (konnektoros / digitális)', 'place': '2. szint – a fűtés és a szabályzása együtt (egy vásárlási döntés)', 'note': 'Fűtőlap 170, termosztátos konnektor 140, palánta fűtés 70. A „fűtőszőnyeg” (1300) és a „termosztát” (5400) háztartási / kisállat – LN.', 'kws': 'fűtőlap|S|F\npalánta fűtőszőnyeg|S|S\nheat mat|S|S\nfűtőlap termosztáttal|S|S\npalánta fűtőlap|S|E\nfűtő lap|S|E\nfutolap|S|E\nterrárium fűtőlap|L|E\nfűtőlap terrárium|L|E\nfűtőszőnyeg|LN|N\nelektromos fűtőszőnyeg|LN|N\nfűtő szőnyeg|LN|N\nkisállat fűtőszőnyeg|LN|N\nkutyaház fűtőlap|LN|N\npalánta fűtés|S|S\ntermosztátos konnektor|S|S\ntermosztát konnektor|S|S\nkonnektoros termosztát|S|S\ntermosztátos dugalj|S|S\nkonnektor termosztát|S|E\nfűtőszőnyeg termosztát|S|E\ntermosztát dugalj|S|E\ndugalj termosztát|S|E\nkeltető termosztát|L|E\nkonnektorba dugható termosztát|S|E\nwifi konnektor termosztát|S|E\ndigitális konnektoros termosztát|S|E\ndigitális termosztát|LN|N\ntermosztát|LN|N\nkonnektoros termosztát praktiker|X|X\nkonnektoros termosztát obi|X|X'},
 {'name': 'Dugványozás: gyökereztető gél', 'sheet': '6 Dugványozás', 'fo': 'gyökereztető hormon', 'area': 'Dugványozás: gyökereztető gél (Clonex), aeropóniás klónozó; a dugványhoz való kocka / korong a Termesztő közeg ágban', 'place': '2. szint – ÚJ: a „gyökereztető hormon” (1300) és „gyökereztető por” (720) a propagátor-téma legnagyobb szava', 'note': 'Gyökereztető hormon 1300, gyökereztető por 720, dugványozás 390 (I), gyökereztető hormon házilag 390 (I). Termék: Clonex gél – a kínálat bővíthető (gyökereztető por).', 'kws': 'gyökereztető hormon|S|F\ngyökereztető por|S|S\ngyökereztető hormon por|S|E\ngyökereztető gél|S|S\nclonex gyökereztető gél|S|G\nclonex gyökereztető|S|G\ndugványozó|S|E\ndugványozás|S|I\ndugvány|L|I\ngyökereztető hormon házilag|L|I\nlevendula dugványozás|L|I\nmuskátli dugvány|L|I\nobi gyökereztető hormon|X|X'},
 {'name': 'Palántanevelő LED lámpa', 'sheet': '7 Palántanevelő lámpa', 'fo': 'palántanevelő lámpa', 'area': 'Kis teljesítményű LED palántákhoz, dugványokhoz (Urban Garden Clone LED); LED-es propagátor', 'place': '2. szint – a 2026-10-09-i döntés szerint a „palántanevelő lámpa” céloldala ez az ág; a LED ágban link', 'note': 'Ha a lámpák a Világítás főkategóriában lesznek, itt elég egy „Palántanevelő lámpa” al-/kereszt-kategória a kis teljesítményű LED-ekkel.', 'kws': 'palántanevelő lámpa|S|F\npalánta nevelő lámpa|S|S\npalánta lámpa|S|S\npalántanevelő led lámpa|S|S\npalanta nevelo lampa|S|E\npalánta világítás|S|E\npalántanevelő led|S|E\npalánta nevelő led|S|E\npalántanevelő led szalag|S|E\npalántanevelő led izzó|S|E\npalántanevelő fénycső|S|E\npalánta led|S|E\nnövény palántanevelő led lámpa|S|E\npalántanevelő lámpa használata|S|I\npalántanevelő lámpa obi|X|X'},
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'A „propagátor” (70) kicsi, a „palántanevelő” (880) a vásárlói szó. Javasolt menünév: „Palántanevelő, propagátor”.', '''palántanevelő|S
palanta nevelo|S
propagátor|S
palántanevelés|S'''),
 ('Doboz / üvegház', '→ Propagátor, mini üvegház; Fűthető propagátor', '''mini üvegház|S
mini melegház|S
fűthető palántanevelő|S'''),
 ('Vetés', '→ Palántanevelő tálca; Palántanevelő cserép', '''palántanevelő tálca|S
szaporító tálca|S
palántanevelő cserép|S'''),
 ('Hő', '→ Fűtőlap, termosztát', '''fűtőlap|S
termosztátos konnektor|S'''),
 ('Dugványozás', '→ Dugványozás: gyökereztető gél (ÚJ)', '''gyökereztető hormon|S
gyökereztető por|S'''),
 ('Fény', '→ Palántanevelő LED lámpa', '''palántanevelő lámpa|S'''),
]

EXT = [
 ('Dugványozás (tartalom)', 'Nagy, kérdés jellegű keresés – útmutató tartalom a Dugványozás kategóriához', '''dugványozás|L\ngyökereztető hormon házilag|L\nlevendula dugványozás|L\nmuskátli dugvány|L'''),
 ('Gyökereztető kocka, tőzegkorong', 'Céloldal a Termesztő közeg ágban – innen link', '''tápkocka|S\njiffy|S\ntőzegtabletta|S'''),
 ('Csíráztatás, mikrozöld', 'Csak ha van csíráztató / mikrozöld termék – különben blog', '''csíráztató|L
csíráztató edény|L
csíráztatás|L
mikrozöld|L
csíráztató üveg|L
csíráztató tál|L
mikrozöldek|L
csíráztatás otthon|L
mikrozöld termesztés|L
csíráztató magok|L
csíráztató szett|L
csíráztatás házilag|L
mag csíráztatás|L
mikrozöld tálca|L'''),
 ('Dugványozás, gyökereztetés (információs)', 'Blog / GYIK a propagátor és a gyökereztető kategóriához', '''dugványozás|L
gyökereztetés|L
gyökereztetés vízben|L
levendula dugványozás|L
dugványozó|L
muskátli dugványozás|L
félfás dugványozás|L
rózsa gyökereztetés|L'''),
]

MAKERS = '''jiffy
jiffy 7
grodan
grodan kőzetgyapot
grodan kocka
root riot
rootit
rootit gel
clonex
clonex gel
radix gyökereztető
plagron power roots
nutleys
vitopod'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Propagátor, propagátor kiegészítő (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A korábbi kategórianeveket és -szerkezetet NEM vettük figyelembe. Kiindulás: a főkategória neve, az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [(1, 'Propagátor, propagátor kiegészítő', '–', 'palántanevelő', 'S', 'Főkategória', 'Palántanevelő 880 ≫ propagátor 70 – javasolt menünév: „Palántanevelő, propagátor”; H1: „Palántanevelő és propagátor kiegészítők”.', None), (2, 'Propagátor, mini üvegház', 'Propagátor, propagátor kiegészítő', 'mini üvegház', 'S', 'Önálló kategória', 'Mini üvegház 590 – fűtés nélküli propagátorok.', 'Propagátor, mini üvegház'), (2, 'Fűthető propagátor', 'Propagátor, propagátor kiegészítő', 'fűthető palántanevelő', 'S', 'Önálló kategória', 'Fűthető palántanevelő 70.', 'Fűthető propagátor'), (2, 'Palántanevelő tálca, propagátor fedél', 'Propagátor, propagátor kiegészítő', 'palántanevelő tálca', 'S', 'Önálló kategória', 'Palántanevelő tálca 1000, szaporító tálca 320.', 'Palántanevelő tálca, propagátor fedél'), (2, 'Palántanevelő cserép, tőzegcserép', 'Propagátor, propagátor kiegészítő', 'palántanevelő cserép', 'S', 'Önálló kategória', 'Palántanevelő cserép 140, tőzegcserép 90.', 'Palántanevelő cserép, tőzegcserép'), (2, 'Fűtőlap, termosztát', 'Propagátor, propagátor kiegészítő', 'fűtőlap', 'S', 'Önálló kategória', 'Fűtőlap 170, termosztátos konnektor 140.', 'Fűtőlap, termosztát'), (2, 'Dugványozás: gyökereztető gél', 'Propagátor, propagátor kiegészítő', 'gyökereztető hormon', 'S', 'Önálló kategória', 'Gyökereztető hormon 1300, gyökereztető por 720 – ÚJ.', 'Dugványozás: gyökereztető gél'), (2, 'Palántanevelő LED lámpa', 'Propagátor, propagátor kiegészítő', 'palántanevelő lámpa', 'S', 'Önálló kategória', 'Palántanevelő lámpa 390 (céloldal itt).', 'Palántanevelő LED lámpa'), (2, 'Palántaszállító csomagolás', 'Propagátor, propagátor kiegészítő', None, '-', 'Navigációs kategória', '5 élő termék, mérhető keresés nélkül (palántaszállító doboz < 20).', None)]
NOT_CATS = [
 ('Gyökereztető kocka, tőzegtabletta', 'tápkocka', 'Közeg – céloldal a Termesztő közeg ágban; itt link.'),
 ('Páratartalom mérő', 'páratartalom mérő', 'Céloldal a Légtechnika ágban.'),
 ('Permetező flakon', 'permetező flakon', 'Céloldal a Hidropónia ágban (kézi permetező).'),
 ('Termosztát külön kategóriában', 'termosztátos konnektor', 'A fűtőlappal együtt vásárolják – egy kategória.'),
 ('Nevelősátor', 'palántanevelő sátor', 'Céloldal a Growbox ágban.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A szerkezet csak a főkategória nevéből, a termékek típusából és a keresési szándékból készült – a korábbi kategórianevek figyelmen kívül.',
]
TITLE = 'babylon-grow.eu – Propagátor, propagátor kiegészítő kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-09 és 2026-10-16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: csak a főkategória neve adott; az alkategóriák a palántanevelés eszközei szerint épülnek: doboz (propagátor, fűthető propagátor), vetés (tálca, cserép), hő (fűtőlap + termosztát), dugványozás, fény, szállítás.',
 'Fő megállapítások: palántanevelő tálca 1000, palántanevelő 880, mini üvegház 590, palántanevelő lámpa 390 – a „propagátor” csak 70. ÚJ: a „gyökereztető hormon” (1300) és a „gyökereztető por” (720) a téma legnagyobb szavai → külön Dugványozás kategória (Clonex gél), bővítési lehetőséggel.',
 'A gyökereztető kocka / tőzegkorong a Termesztő közeg ágba került (közeg), itt link.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a korábbi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Tartalmi lehetőségek, kereszt-linkek és nem célzott témák.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO0804 GRO3889 GRO3262 GRO2797 GRO2798 GRO2821 GRO2824 GRO2823 GRO3927', 'Propagátor, mini üvegház', [], 'Erős', 'Fűtés nélküli propagátor (vékony falú, Garland High Dome, X-Stream L)'),
 ('GRO2939', 'Propagátor, mini üvegház', ['Palántanevelő tálca, propagátor fedél'], 'Erős', 'Önöntöző propagátor kapilláris szőnyeggel'),
 ('GRO1222', 'Propagátor, mini üvegház', ['Dugványozás: gyökereztető gél'], 'Erős', 'X-Stream Clone Master aeropóniás klónozó propagátor'),
 ('GRO4307', 'Propagátor, mini üvegház', ['Palántanevelő LED lámpa'], 'Erős', 'AC Infinity LED-es propagátor'),
 ('GRO2941 GRO2938 GRO0807 GRO2940 GRO2820 GYSZ0024V GRO1758 GRO1757', 'Fűthető propagátor', [], 'Erős', 'Fűthető propagátor'),
 ('GRO4635 GRO4633 GRO4634 GRO2987 GRO4349 GRO2246', 'Palántanevelő tálca, propagátor fedél', [], 'Erős', 'Palántanevelő / magvető tálca, korongtálca'),
 ('GRO4618 GRO4620 GRO4609 GRO4614 GRO4619 GRO4687 GRO4686 GRO4684', 'Palántanevelő tálca, propagátor fedél', ['Propagátor, mini üvegház'], 'Erős', 'Propagátor fedél és alsó tálca (Garland, utántöltő)'),
 ('GRO4611', 'Palántanevelő tálca, propagátor fedél', [], 'Erős', 'Kapilláris szőnyeg'),
 ('GRO3773 GRO3774 GRO1909 GRO1910', 'Palántanevelő tálca, propagátor fedél', ['Cserép, tálca ág'], 'Laza', 'Garland kis műanyag tálca'),
 ('GRO3924 GRO3432 GRO4360 GRO2236 GRO2237 GRO4676 GRO4377 GRO3925 GRO2239', 'Palántanevelő cserép, tőzegcserép', [], 'Erős', 'Jiffy tőzegcserép'),
 ('GRO4413 GRO4415 GRO4414 GRO2900 GRO3232', 'Palántanevelő cserép, tőzegcserép', [], 'Erős', 'Rostcserép, kis palántázócserép'),
 ('GRO4365 GRO4366 GRO1867 GRO1868 GRO4345 GRO4493 GRO3909', 'Fűtőlap, termosztát', [], 'Erős', 'Propagátor fűtőlap'),
 ('GRO1896 GRO1897', 'Fűtőlap, termosztát', [], 'Erős', 'Földmelegítő kábel beépített termosztáttal'),
 ('GRO2251', 'Fűtőlap, termosztát', ['Fűthető propagátor'], 'Erős', 'X-Stream Heat Thermoset digitális termosztát'),
 ('GRO0789 GRO2799 GRO2392', 'Légtechnika ág – Klímavezérlő', ['Fűtőlap, termosztát'], 'Más főkategória', 'Digitális / mechanikus termosztát – fűtőlaphoz is'),
 ('GRO0073', 'Dugványozás: gyökereztető gél', [], 'Erős', 'Clonex gyökereztető gél'),
 ('GRO4097 GRO4098 GRO4099', 'Palántanevelő LED lámpa', ['LED ág – LED sáv'], 'Erős', 'Urban Garden Clone LED (30–60 W) palántához, dugványhoz'),
 ('GRO4540 GRO4680 GRO4681 GRO4682 GRO4683', 'Palántaszállító csomagolás', [], 'Erős', 'Palántaszállító csomagolás, doboz'),
 ('GRO2707 GRO2708 GRO2709 GRO2710 GRO2711 GRO2712 GRO2794 GRO2795 GRO4371 GRO4416 GRO4417 GRO4411 GRO4412 GRO4675 GRO1325 GRO1326 GRO4751 GRO4754 GRO4755', 'Termesztő közeg ág – Gyökereztető kocka, tőzeg- és kókuszkorong', ['Dugványozás: gyökereztető gél'], 'Más főkategória', 'Magvető / dugványozó kocka, korong – céloldal a Termesztő közeg ágban'),
 ('GRO4134 GRO4135 GRO4136 GRO2734 GRO2435 GRO3558', 'Growbox ág – Nevelősátor', ['Propagátor, mini üvegház'], 'Más főkategória', 'Nevelősátor – céloldal a Growbox ágban'),
 ('GRO0811', 'Hidropónia ág – Kézi permetező', [], 'Más főkategória', 'Kézi permetező flakon'),
 ('GRO1342', 'Tápok ág', [], 'Más főkategória', 'Plagron Seedbooster csíráztató tápoldat'),
 ('GRO1906 GRO1907 GRO1911 GRO3775 GRO3777 GRO1463 GRO3138 GRO3437', 'Cserép, tálca ág – Műanyag tálca', [], 'Más főkategória', 'Nagy Garland / Nutriculture tálca'),
 ('GRO3661 GRO3662 GRO4358 GRO4359 GRO4636 GRO4637', 'Mikrozöld ág – mikrozöld tálca', ['Palántanevelő tálca, propagátor fedél'], 'Más főkategória', 'Mikrozöld tálca'),
]
