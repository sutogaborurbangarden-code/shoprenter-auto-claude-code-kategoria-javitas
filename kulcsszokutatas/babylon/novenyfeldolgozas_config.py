# Babylon – Növényfeldolgozás, afterharvest (sandbox-főkategória, 2026-10-15)
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='Szárítóháló, növényszárító', sheet='1 Szárítóháló', fo='szárítóháló',
      area='Termés, gyógy- és fűszernövény szárítása – függő hálós szárító',
      place='2. szint – a sandbox „Növényszárítás” helyett / H1-ként; a „növényszárítás” névre alig van keresés (10)',
      note='A „szárító állvány” (480) ruhaszárító, az „aszalógép” (2900) elektromos gyümölcsaszaló – egyik sem a mi termékünk (az aszalógép a Bővítés lapon).',
      kws='''szárítóháló|S|F
szárító háló|S|S
növényszárító háló|S|S
növényszárító|S|S
gyógynövény szárító|S|E
fűszer szárító|L|E
gyógynövény szárító háló|S|E
dry net|S|E
függő szárító|S|E
szárító kosár|S|E
szárító zsák|S|E
növény szárító|S|E
növény szárítás|S|I
fűszernövény szárítás|L|I
fűszer szárítás|L|I
fűszernövények szárítása|L|I
gomba szárítása|L|I
gyógynövény szárítása|L|I
levendula szárítása|L|I
szárított gyógynövények tárolása|L|I
gyógynövény szárítógép|LN|N
szárító állvány|LN|N
aszalógép|LN|N'''),
 dict(name='Trimmelő olló, trimmelő gép', sheet='2 Trimmelés', fo='trimmelő gép',
      area='Betakarítás utáni levélvágás – kézi olló, tál, elektromos trimmelő',
      place='2. szint – a sandbox „Trimmelés” helyett; a „trimmelés” (390) főleg jelentés-keresés, a „trimmelő” (1600) / „trimmer” (880) szakállvágó',
      note='A „trimmelő gép” (320) vegyes (szakállvágó is), de a termékoldalakon a „trimmelő olló” / „trimmelő tál” egyértelmű. A „metszőolló” (2900) kerti olló – laza kötődés, csak említés.',
      kws='''trimmelő gép|L|F
trimmelő olló|S|S
trimmer gép|L|S
trimmelők gep|L|E
trimmelő asztal|S|E
olló élező|L|E
bonsai olló|L|E
szüretelő olló|L|E
kézi metszőolló|L|E
bonsai metszőolló|L|E
saboten|S|G
chikamasa|S|G
trimmelés|L|I
trimmeles|L|I
olló élezése|L|I
metszőolló tisztítása|L|I
metszőolló|LN|N
trimmelő|LN|N
trimmer|LN|N'''),
 dict(name='Páratartalom-szabályzó tasak', sheet='3 Páratartás', fo='boveda',
      area='Érlelés (curing) és tárolás – kétirányú páratartalom-szabályzás, terpén',
      place='2. szint – a sandbox „Fermentáció” helyett: a „fermentálás” (6600) élelmiszer-fermentálás, a kínálat pedig Boveda / Integra Boost tasak',
      note='A „fermentálás”, „fermentáló üveg” (1300), „fermentált káposztalé” (1600) savanyúság-készítés – nem a mi vevőnk. A „páratartalom-szabályzó tasak” kifejezésre nincs mérhető keresés; a márkanév (Boveda 210) viszi.',
      kws='''boveda|S|F
integra boost|S|S
humidor|L|S
terpének|L|E
terpén|L|E
boveda 50|S|G
boveda 84|S|G
integra boost 72|S|G
integra 62|S|G
boveda használata|S|I
gyógynövény tároló|L|E
kúrálás|S|I
érlelés|L|I
száraz fermentálás|L|I
érlelő tasak|LN|N
fermentáció|LN|N
fermentálás|LN|N
fermentálás házilag|LN|N
fermentáló üveg|LN|N
humidorshop|X|X'''),
 dict(name='Vákuumzsák, simítózáras tasak', sheet='4 Csomagolás', fo='simítózáras tasak',
      area='Szárított termés tárolása, csomagolása – vákuum- és zipzáras tasak',
      place='2. szint – a sandbox „Csomagolás” helyett / H1-ként; a „csomagoló tasak” (110) és „csomagoló zacskó” (320) általános csomagolás',
      note='A „vákuum zsák utazáshoz” (210) és „vákuum ruhazsák” (210) ruhatároló zsák; a „fóliahegesztő” (720) és a vákuumozó gépek nincsenek a kínálatban (Bővítés lap). A „mylar tasak” (140) fényálló tasak – a vasalható vákuumzsák ilyen.',
      kws='''simítózáras tasak|S|F
vákuum zsák|S|S
mylar tasak|S|S
simítózáras zacskó|S|S
ziplock zacskó|S|E
cipzáras tasak|S|E
önzáró tasakok|S|E
mylar zacskó|S|E
vákuumozható zsák|S|E
simitózáras tasak|S|E
simitozaras tasak|S|E
talpas simítózáras tasak|S|E
vakuum zsak|S|E
légmentes tároló doboz|L|E
simítózáras műanyag tasak|S|E
vákuum tároló zsák|L|E
cipzáras műanyag tasak|S|E
zip zacskó|S|E
légmentes tároló|L|E
grove bag|S|G
légmentesen zárható tasak|S|E
visszazárható műanyag tasak|S|E
vákuumos tároló tasak|S|E
ziploc zacskó|S|E
csomagoló tasak|L|E
csomagoló zacskó|LN|N
vákuum zsák utazáshoz|LN|N
vákuum ruhazsák|LN|N
fóliahegesztő|LN|N
simítózáras tasak rossmann|X|X'''),
 dict(name='Kivonatoló zsák, extraktor', sheet='5 Extrakció', fo='kivonatolás',
      area='Gyanta / trichoma kivonatolás – hideg vizes (ice) zsák, szitáló gép',
      place='2. szint – a sandbox „Extrakció, kivonatolás” maradhat; kis keresés, de egyértelmű termékkör',
      note='Nagyon kis keresés: kivonatolás 20, bubble bag 20, ice bubble / pollen box 10. Az „extrakció” (170) orvosi / fogászati, a „rosin” (210) hegedűgyanta is, az „1 mikronos szűrőzsák” (170) víztisztítás.',
      kws='''kivonatolás|L|F
bubble bag|S|S
ice bubble|S|S
pollen box|S|E
növényi kivonat készítése|L|I
tinktúra készítés|L|I
tinktúra készítése házilag|L|I
gyógynövény tinktúra készítése|L|I
rosin|LN|N
extrakció|LN|N
1 mikronos szűrőzsák|LN|N'''),
 dict(name='Digitális mérleg, zsebmérleg', sheet='6 Mérleg', fo='digitális mérleg',
      area='Kis tömegek mérése – 0,01 g-os zseb- és precíziós mérleg, kalibráló súly',
      place='2. szint – a sandbox-név maradhat; H1 / SEO title: „Digitális precíziós mérleg, zsebmérleg”',
      note='A „digitális mérleg” (1600) vegyes (személy- és konyhai mérleg is); a „gramm mérleg” (720), „ékszermérleg” / „ékszer mérleg” / „ékszerész mérleg” (egyenként 480) és „precíziós mérleg” (320) a pontos vásárlói szavak. A „digitális konyhai mérleg” (880) nem a mi termékünk.',
      kws='''digitális mérleg|S|F
gramm mérleg|S|S
ékszermérleg|S|S
precíziós mérleg|S|S
ékszer mérleg|S|E
ékszerész mérleg|S|E
digitalis merleg|S|E
zsebmérleg|S|S
analitikai mérleg|L|E
digitális gramm mérleg|S|E
mérleg grammos|S|E
mini mérleg|S|E
kis mérleg|S|E
0.01 g mérleg|S|E
precíziós mérleg 0 01g|S|E
precizios merleg|S|E
mérleg kalibrálás|S|I
aranymérleg|L|E
digitális zsebmérleg|S|E
kalibráló súly|S|E
hordozható mérleg|S|E
gramm pontos mérleg|S|E
zsebmerleg|S|E
laboratóriumi mérleg|L|E
g scale|S|G
precíziós zsebmérleg|S|E
0.001 g mérleg|S|E
digitális konyhai mérleg|LN|N
ékszer mérleg euronics|X|X
tesco ékszermérleg|X|X'''),
 dict(name='Gumikesztyű, nitril kesztyű', sheet='7 Kesztyű', fo='nitril kesztyű',
      area='Trimmelés, kivonatolás, tápoldatozás – egyszer használatos kesztyű',
      place='3. szint a „Hasznos kiegészítők” alatt – erős saját keresés',
      note='Nagy volumen (gumikesztyű 2900, nitril kesztyű 1000), de általános (háztartási, egészségügyi) szándék – laza kötődés.',
      kws='''nitril kesztyű|L|F
gumikesztyű|L|S
gumikesztyű 100 db|L|S
nitril gumikesztyű|L|S
vinyl kesztyű|L|E
egyszer használatos gumikesztyű|L|E
latex gumikesztyű|L|E
púdermentes nitril kesztyű|L|E'''),
 dict(name='Nagyító, zsebmikroszkóp', sheet='8 Nagyító', fo='kézi nagyító',
      area='Trichomák (érettség) vizsgálata – kézi nagyító, LED-es zsebmikroszkóp',
      place='3. szint a „Hasznos kiegészítők” alatt',
      note='A „nagyító” (2900) és a „mikroszkóp” (3600) nagyrészt olvasó- és gyerekmikroszkóp-keresés; a „zsebmikroszkóp” (110) és az „ékszerész nagyító” (140) a pontosabb szó.',
      kws='''kézi nagyító|L|F
zsebmikroszkóp|S|S
ékszerész nagyító|L|S
kézi nagyító 40x|L|E
kézi mikroszkóp|S|E
mini mikroszkóp|S|E
világítós nagyító|L|E
zsebnagyító|L|E
led nagyító|L|E
nagyító|LN|N
mikroszkóp|LN|N
nagyítós lámpa|LN|N'''),
]

OLD_SHEET = 'Sandbox menünevek'
OLD = [
 ('Növényfeldolgozás, afterharvest (főkategória)', 'A „növényfeldolgozás” és az „afterharvest” kifejezésre nincs mérhető keresés. Menünévnek maradhat; a H1 / SEO title a keresett alkategória-szavakra épüljön (szárítóháló, trimmelő olló, digitális mérleg).', '''betakarítás|L
digitális mérleg|S
szárítóháló|S'''),
 ('Csomagolás', '→ „Vákuumzsák, simítózáras tasak” (a „csomagoló tasak / zacskó” általános csomagolás)', '''csomagoló tasak|L
csomagoló zacskó|LN
simítózáras tasak|S
vákuum zsák|S'''),
 ('Extrakció, kivonatolás', 'Maradhat; az „extrakció” orvosi / fogászati keresés, a „kivonatolás” 20', '''extrakció|LN
kivonatolás|L
bubble bag|S'''),
 ('Fermentáció', '→ „Páratartalom-szabályzó tasak” (Boveda, Integra Boost) – a „fermentálás” élelmiszer-fermentálás', '''fermentálás|LN
fermentáció|LN
boveda|S'''),
 ('Hasznos kiegészítők', 'Navigációs gyűjtőkategória (nincs saját keresés) – alá: Gumikesztyű, nitril kesztyű; Nagyító, zsebmikroszkóp; szemüveg, élező', '''nitril kesztyű|L
kézi nagyító|L'''),
 ('Növényszárítás', '→ „Szárítóháló, növényszárító” (a „növény szárítás” 10, a „szárítóháló” 140)', '''növény szárítás|S
szárítóháló|S'''),
 ('Trimmelés', '→ „Trimmelő olló, trimmelő gép” (a „trimmelés” jelentés-keresés)', '''trimmelés|L
trimmelő gép|L
trimmelő olló|S'''),
 ('Digitális mérleg, zsebmérleg', 'Marad; H1: „Digitális precíziós mérleg, zsebmérleg”', '''digitális mérleg|S
zsebmérleg|S
gramm mérleg|S'''),
]

EXT = [
 ('Aszalógép, gyümölcsaszaló', 'Csak kínálatbővítés esetén – nincs ilyen termék', '''aszalógép|L
gyümölcs aszalógép|L'''),
 ('Fóliahegesztő, vákuumozó gép', 'Csak kínálatbővítés esetén – a vákuumzsákok mellé jó kiegészítő lenne', '''fóliahegesztő|L
vákuumos fóliahegesztő|L
lidl vákuumozó gép|X'''),
 ('Fermentálás (élelmiszer)', 'Nem growshop-téma – blogtéma vagy kihagyás', '''fermentálás|LN
fermentáló üveg|LN
fermentáló edény|LN
fermentált káposztalé|LN'''),
 ('Humidor, szivartárolás', 'Laza kapcsolat a Boveda-tasakokon keresztül – legfeljebb említés', '''humidor|L
humidorshop|X'''),
]

MAKERS = '''boveda
integra boost
saboten
chikamasa
g scale
grove bag'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Növényfeldolgozás, afterharvest (termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet, a Google Shopping-feed termékei (1999 db) és a Kulcsszótervező adatai. Termékszám = elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [
 (1, 'Növényfeldolgozás, afterharvest', '–', None, '-', 'Főkategória', 'A főkategória-névre nincs mérhető keresés – navigációs név; a H1 a keresett alkategória-szavakra épüljön.', None),
 (2, 'Szárítóháló, növényszárító', 'Növényfeldolgozás, afterharvest', 'szárítóháló', 'S', 'Önálló kategória', 'A sandbox „Növényszárítás” utódja: a szárítóháló-klaszter (140 + 70 + 70 + 50 + 50) egyértelmű és sok termék van hozzá.', 'Szárítóháló, növényszárító'),
 (2, 'Trimmelő olló, trimmelő gép', 'Növényfeldolgozás, afterharvest', 'trimmelő gép', 'L', 'Önálló kategória', 'A legtöbb termék (ollók, tálak, gépek). A „trimmelés” / „trimmelő” zömmel szakállvágó-keresés, ezért a menünévben „olló” és „gép” legyen.', 'Trimmelő olló, trimmelő gép'),
 (2, 'Páratartalom-szabályzó tasak', 'Növényfeldolgozás, afterharvest', 'boveda', 'S', 'Önálló kategória', 'A sandbox „Fermentáció” helyett: a kínálat Boveda / Integra Boost tasak, a „fermentálás” pedig savanyúság-készítés. A márkanév (Boveda 210) viszi.', 'Páratartalom-szabályzó tasak'),
 (2, 'Vákuumzsák, simítózáras tasak', 'Növényfeldolgozás, afterharvest', 'simítózáras tasak', 'S', 'Önálló kategória', 'A sandbox „Csomagolás” helyett: simítózáras tasak 720, mylar tasak 140, vákuum zsák 90.', 'Vákuumzsák, simítózáras tasak'),
 (2, 'Kivonatoló zsák, extraktor', 'Növényfeldolgozás, afterharvest', 'kivonatolás', 'L', 'Önálló kategória (kis keresés)', 'Egyértelmű termékkör (Secret Icer, Secret Box), de kicsi a keresés – navigációs szerep.', 'Kivonatoló zsák, extraktor'),
 (2, 'Digitális mérleg, zsebmérleg', 'Növényfeldolgozás, afterharvest', 'digitális mérleg', 'S', 'Önálló kategória', 'Erős klaszter (digitális mérleg 1600, gramm mérleg 720, ékszermérleg 480, precíziós mérleg 320) és sok G-Scale termék.', 'Digitális mérleg, zsebmérleg'),
 (2, 'Hasznos kiegészítők', 'Növényfeldolgozás, afterharvest', None, '-', 'Navigációs kategória', 'Gyűjtőnév saját keresés nélkül; alá a kesztyű és a nagyító, valamint a szemüveg / élező.', None),
 (3, 'Gumikesztyű, nitril kesztyű', 'Hasznos kiegészítők', 'nitril kesztyű', 'L', 'Önálló kategória', 'Nagy volumen (gumikesztyű 2900, nitril kesztyű 1000), 7 termék.', 'Gumikesztyű, nitril kesztyű'),
 (3, 'Nagyító, zsebmikroszkóp', 'Hasznos kiegészítők', 'kézi nagyító', 'L', 'Szűrő / kis kategória', 'Csak 2 termék – vékony oldal; a Hasznos kiegészítők listájában is elég.', 'Nagyító, zsebmikroszkóp'),
]
NOT_CATS = [
 ('Fermentálás (élelmiszer)', 'fermentálás', 'Savanyúság-készítés – nem célozni; a sandbox „Fermentáció” név félrevezető.'),
 ('Aszalógép', 'aszalógép', 'Nincs ilyen termék – csak kínálatbővítés esetén.'),
 ('Fóliahegesztő', 'fóliahegesztő', 'Nincs ilyen termék – csak kínálatbővítés esetén.'),
 ('Terpén, aromatasak', 'terpének', 'Kevés keresés – a Páratartalom-szabályzó tasak kategóriában másodlagosan.'),
 ('Szagsemlegesítés (ONA)', None, 'Az ONA termékek a Szellőzés / szagsemlegesítés ágba valók, nem ide.'),
]
PRODUCT_NOTE = [
 'Forrás: a Babylon Google Ads fiók Shopping-termékadatai (termékkód = Shopping item ID, terméknév = feed-cím), 2024-10-01 – 2026-10-14, összesen 1999 termék. A Shoprenter API és az éles oldal a felhőből nem érhető el.',
 'Figyelem: ez a Google-ben hirdetett termékkör, nem feltétlenül a teljes katalógus. A gyártó és a gyűjtőtermék (GYUJTO…) adat a feedben nem érhető el.',
 'A lapon a teljes termékkínálat szerepel: elöl a Növényfeldolgozás kategóriákba sorolt termékek (Erős, Laza), végül „Nem tartozik ide” jelöléssel az összes többi. Az Illeszkedés oszlopra szűrve csak a besoroltak láthatók.',
]

TITLE = 'babylon-grow.eu – Növényfeldolgozás, afterharvest főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: Google Shopping-feed (1999 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: három sandbox-név félrevezető – „Fermentáció” (= savanyúság-készítés, 6600), „Trimmelés” (= szakállvágó / jelentés), „Csomagolás” (általános). A javasolt nevek a keresett termékszavakra épülnek (Kategóriaszerkezet-ajánlás lap).',
 'A legerősebb klaszterek: digitális / gramm / ékszermérleg (1600 / 720 / 480), simítózáras tasak (720), gumi- / nitril kesztyű (2900 / 1000, laza), szárítóháló (140 + 70 + 70).',
 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe; a javaslat a sandbox-tervezetre, a termékkínálatra és a kulcsszóadatra épül.',
]
OLD_TITLE = 'A sandbox „Növényfeldolgozás, afterharvest” menünevei – keresési volumen és javasolt név'
OLD_SUB = 'Sandbox-tervezet: Csomagolás; Extrakció, kivonatolás; Fermentáció; Hasznos kiegészítők; Növényszárítás; Trimmelés; Digitális mérleg, zsebmérleg.'
EXT_TITLE = 'Rokon, betakarítás utáni területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más szándékú vagy a kínálatban nem szereplő témák – csak kínálatbővítés esetén.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'

HASZNOS = 'Hasznos kiegészítők'
PRODUCTS = [
 ('GRO0826 GRO0827 GRO2844 GRO2845 GRO4129 GRO4130 GRO4299 GRO4569 GRO4570', 'Szárítóháló, növényszárító', [], 'Erős', 'Szárítóháló'),
 ('GRO4571 GRO4572', 'Szárítóháló, növényszárító', [], 'Laza', 'Szárítóháló szűrő (tartozék)'),
 ('GRO1109 GRO1140 GRO3843 GRO3844 GRO4146 GRO4204 GRO4205 GRO4206 GRO4245 GRO4246 GRO4275 GRO4276 GRO4277 GRO4278 GRO4602 GRO4603 GRO4605 GRO4606', 'Trimmelő olló, trimmelő gép', [], 'Erős', 'Trimmelő olló'),
 ('GRO2788 GRO2789 GRO3740 GRO3929 GRO4235 GRO4273 GRO4372 GRO4527 GRO3827', 'Trimmelő olló, trimmelő gép', [], 'Erős', 'Trimmelő tál / gép / zsák'),
 ('GRO4604', 'Trimmelő olló, trimmelő gép', [HASZNOS], 'Laza', 'Ollóélező'),
 ('HED1892 HED1893 HED1944 HED2041 HED2198 HED2199 HED2441 HED2442', 'Páratartalom-szabályzó tasak', ['Vákuumzsák, simítózáras tasak'], 'Erős', 'Boveda kétirányú páraszabályzó tasak'),
 ('HED1894 HED1895 HED1896 HED2196 HED2197 HED2287', 'Páratartalom-szabályzó tasak', ['Vákuumzsák, simítózáras tasak'], 'Erős', 'Integra Boost páraszabályzó tasak'),
 ('HED2288 HED2289 HED2329 HED2330 HED2331 GRO4565 GRO4566 GRO4567 GRO4568', 'Páratartalom-szabályzó tasak', [], 'Laza', 'Terpén- / aromatasak'),
 ('GRO1542 GRO1805 GRO2822 GRO3264 HED2203', 'Vákuumzsák, simítózáras tasak', [], 'Erős', 'Vasalható vákuumzsák / ziplock tasak'),
 ('GRO4540 GRO4680 GRO4681 GRO4682 GRO4683', 'Vákuumzsák, simítózáras tasak', [], 'Laza', 'Palántaszállító csomagolás – a Palántanevelő ágban is'),
 ('GRO1253 GRO1254 GRO3263 GRO3728 GRO3729 GRO3791 HED0724', 'Kivonatoló zsák, extraktor', [], 'Erős', 'Secret Icer / Secret Box / shaker'),
 ('HED1397 HED1701 HED1828 HED1836 HED2156 HED2157 HED2341 HED2401 HED2402 HED2403 HED2404 HED2405', 'Digitális mérleg, zsebmérleg', [], 'Erős', 'Digitális zseb- / precíziós mérleg'),
 ('HED0413 HED0414 HED0415 HED1022 HED1489 HED1490', 'Digitális mérleg, zsebmérleg', [], 'Laza', 'Kalibráló súly'),
 ('GRO4279 GRO4557 GRO4558 GRO4559 GRO4560 GRO4562 GRO4641', 'Gumikesztyű, nitril kesztyű', [HASZNOS], 'Erős', 'Egyszer használatos kesztyű'),
 ('GRO0821 GRO4306', 'Nagyító, zsebmikroszkóp', [HASZNOS], 'Erős', 'Zsebmikroszkóp / LED-es nagyító'),
 ('GRO3829 GRO4203', HASZNOS, [], 'Laza', 'Grow- / védőszemüveg'),
]
