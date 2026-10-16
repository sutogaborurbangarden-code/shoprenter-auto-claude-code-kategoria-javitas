# Babylon – Növényfeldolgozás, afterharvest (2026-10-16, 2. változat)
# Csak a FŐKATEGÓRIA NEVE alapján: a korábbi / sandbox alkategória-nevek és -szerkezet figyelmen kívül;
# alkategóriák a feldolgozás lépései (szárítás → trimmelés → érlelés / tárolás → kivonatolás), az élő kínálat és a kulcsszóadat alapján.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 {'name': 'Szárítóháló, növényszárító', 'sheet': '1 Szárítás', 'fo': 'szárítóháló', 'area': '1. lépés – szárítás: függő szárítóháló (több szintes), szárítóháló-szűrő', 'place': '2. szint (folyamat-sorrend: szárítás → trimmelés → érlelés / tárolás → kivonatolás)', 'note': 'A „szárító állvány” (480) ruhaszárító, az „aszalógép” (2900) elektromos gyümölcsaszaló – egyik sem a mi termékünk (az aszalógép a Bővítés lapon).', 'kws': 'szárítóháló|S|F\nszárító háló|S|S\nnövényszárító háló|S|S\nnövényszárító|S|S\ngyógynövény szárító|S|E\nfűszer szárító|L|E\ngyógynövény szárító háló|S|E\ndry net|S|E\nfüggő szárító|S|E\nszárító kosár|S|E\nszárító zsák|S|E\nnövény szárító|S|E\nnövény szárítás|S|I\nfűszernövény szárítás|L|I\nfűszer szárítás|L|I\nfűszernövények szárítása|L|I\ngomba szárítása|L|I\ngyógynövény szárítása|L|I\nlevendula szárítása|L|I\nszárított gyógynövények tárolása|L|I\ngyógynövény szárítógép|LN|N\nszárító állvány|LN|N\naszalógép|LN|N'},
 {'name': 'Trimmelő olló', 'sheet': '2 Trimmelő olló', 'fo': 'trimmelő olló', 'area': 'Kézi trimmelő olló (egyenes / ívelt, rugós, Saboten, AC Infinity), ollóélező', 'place': '3. szint a „Trimmelés” alatt', 'note': 'Trimmelő olló 30 – kicsi, de pontos; a „metszőolló” (kerti) LN. Márka (Saboten, chikamasa) = szűrő.', 'kws': 'trimmelő olló|S|F\nolló élező|L|E\nbonsai olló|L|E\nszüretelő olló|L|E\nkézi metszőolló|L|E\nbonsai metszőolló|L|E\nsaboten|S|G\nchikamasa|S|G\ntrimmelés|L|I\ntrimmeles|L|I\nolló élezése|L|I\nmetszőolló tisztítása|L|I\nmetszőolló|LN|N\ntrimmelő|LN|N'},
 {'name': 'Trimmelő gép, trimmelő tál', 'sheet': '3 Trimmelő gép', 'fo': 'trimmelő gép', 'area': 'Kézi és motoros trimmelő tál / gép, trimmelő asztal, trimmelő zsák', 'place': '3. szint a „Trimmelés” alatt', 'note': 'Trimmelő gép 320 (vegyes: szakállvágó is – laza), trimmer gép, trimmelő asztal.', 'kws': 'trimmelő gép|L|F\ntrimmer gép|L|S\ntrimmelők gep|L|E\ntrimmelő asztal|S|E\ntrimmer|LN|N'},
 {'name': 'Páratartalom-szabályzó tasak', 'sheet': '4 Páraszabályzó tasak', 'fo': 'boveda', 'area': 'Kétirányú páratartalom-szabályzó tasak (Boveda, Integra Boost) az érleléshez és tároláshoz', 'place': '3. szint az „Érlelés és tárolás” alatt', 'note': 'A „fermentálás”, „fermentáló üveg” (1300), „fermentált káposztalé” (1600) savanyúság-készítés – nem a mi vevőnk. A „páratartalom-szabályzó tasak” kifejezésre nincs mérhető keresés; a márkanév (Boveda 210) viszi.', 'kws': 'boveda|S|F\nintegra boost|S|S\nhumidor|L|S\nboveda 50|S|G\nboveda 84|S|G\nintegra boost 72|S|G\nintegra 62|S|G\nboveda használata|S|I\ngyógynövény tároló|L|E\nkúrálás|S|I\nérlelés|L|I\nszáraz fermentálás|L|I\nérlelő tasak|LN|N\nfermentáció|LN|N\nfermentálás|LN|N\nfermentálás házilag|LN|N\nfermentáló üveg|LN|N\nhumidorshop|X|X'},
 {'name': 'Terpén aromatasak', 'sheet': '5 Terpén tasak', 'fo': 'terpén', 'area': 'Terpén- / aromatasak (Integra Boost terpén, Neu Bag) – aroma megőrzése tároláskor', 'place': '3. szint az „Érlelés és tárolás” alatt (új)', 'note': 'Saját termékcsoport (9 élő termék); a „terpén” (90) és a „terpének” keresés jórészt ismeretterjesztő – laza, tartalommal.', 'kws': 'terpén|L|F\nterpének|L|I'},
 {'name': 'Vákuumzsák, simítózáras tasak', 'sheet': '6 Vákuumzsák, tasak', 'fo': 'simítózáras tasak', 'area': 'Fényálló, vasalható vákuumzsák, simítózáras (ziplock) tasak – szagzáró tárolás', 'place': '3. szint az „Érlelés és tárolás” alatt', 'note': 'A „vákuum zsák utazáshoz” (210) és „vákuum ruhazsák” (210) ruhatároló zsák; a „fóliahegesztő” (720) és a vákuumozó gépek nincsenek a kínálatban (Bővítés lap). A „mylar tasak” (140) fényálló tasak – a vasalható vákuumzsák ilyen.', 'kws': 'simítózáras tasak|S|F\nvákuum zsák|S|S\nmylar tasak|S|S\nsimítózáras zacskó|S|S\nziplock zacskó|S|E\ncipzáras tasak|S|E\nönzáró tasakok|S|E\nmylar zacskó|S|E\nvákuumozható zsák|S|E\nsimitózáras tasak|S|E\nsimitozaras tasak|S|E\ntalpas simítózáras tasak|S|E\nvakuum zsak|S|E\nlégmentes tároló doboz|L|E\nsimítózáras műanyag tasak|S|E\nvákuum tároló zsák|L|E\ncipzáras műanyag tasak|S|E\nzip zacskó|S|E\nlégmentes tároló|L|E\ngrove bag|S|G\nlégmentesen zárható tasak|S|E\nvisszazárható műanyag tasak|S|E\nvákuumos tároló tasak|S|E\nziploc zacskó|S|E\ncsomagoló tasak|L|E\ncsomagoló zacskó|LN|N\nvákuum zsák utazáshoz|LN|N\nvákuum ruhazsák|LN|N\nfóliahegesztő|LN|N\nsimítózáras tasak rossmann|X|X'},
 {'name': 'Kivonatolás: bubble bag, extraktor', 'sheet': '7 Kivonatolás', 'fo': 'kivonatolás', 'area': 'Hideg kivonatolás: bubble bag (jeges kivonatoló zsák), gyantaszitáló extraktor (Secret Box), shaker', 'place': '2. szint', 'note': 'Nagyon kis keresés: kivonatolás 20, bubble bag 20, ice bubble / pollen box 10. Az „extrakció” (170) orvosi / fogászati, a „rosin” (210) hegedűgyanta is, az „1 mikronos szűrőzsák” (170) víztisztítás.', 'kws': 'kivonatolás|L|F\nbubble bag|S|S\nice bubble|S|S\npollen box|S|E\nnövényi kivonat készítése|L|I\ntinktúra készítés|L|I\ntinktúra készítése házilag|L|I\ngyógynövény tinktúra készítése|L|I\nrosin|LN|N\nextrakció|LN|N\n1 mikronos szűrőzsák|LN|N\nhőprés|LN|N\nszita|LN|N'},
 {'name': 'Digitális mérleg, zsebmérleg', 'sheet': '8 Mérleg', 'fo': 'digitális mérleg', 'area': 'Digitális zseb- és precíziós mérleg (0,01 / 0,001 g), kalibráló súly', 'place': '2. szint – a legerősebb termékkulcsszó (1600)', 'note': 'A „digitális mérleg” (1600) vegyes (személy- és konyhai mérleg is); a „gramm mérleg” (720), „ékszermérleg” / „ékszer mérleg” / „ékszerész mérleg” (egyenként 480) és „precíziós mérleg” (320) a pontos vásárlói szavak. A „digitális konyhai mérleg” (880) nem a mi termékünk.', 'kws': 'digitális mérleg|S|F\ngramm mérleg|S|S\nékszermérleg|S|S\nprecíziós mérleg|S|S\nékszer mérleg|S|E\nékszerész mérleg|S|E\ndigitalis merleg|S|E\nzsebmérleg|S|S\nanalitikai mérleg|L|E\ndigitális gramm mérleg|S|E\nmérleg grammos|S|E\nmini mérleg|S|E\nkis mérleg|S|E\n0.01 g mérleg|S|E\nprecíziós mérleg 0 01g|S|E\nprecizios merleg|S|E\nmérleg kalibrálás|S|I\naranymérleg|L|E\ndigitális zsebmérleg|S|E\nkalibráló súly|S|E\nhordozható mérleg|S|E\ngramm pontos mérleg|S|E\nzsebmerleg|S|E\nlaboratóriumi mérleg|L|E\ng scale|S|G\nprecíziós zsebmérleg|S|E\n0.001 g mérleg|S|E\ndigitális konyhai mérleg|LN|N\nékszer mérleg euronics|X|X\ntesco ékszermérleg|X|X'},
 {'name': 'Munkaeszköz: kesztyű, nagyító, grow szemüveg', 'sheet': '9 Munkaeszköz', 'fo': 'nitril kesztyű', 'area': 'Feldolgozás közbeni munkaeszköz: nitril / vinyl kesztyű, LED-es nagyító, zsebmikroszkóp (trichóma-vizsgálat), grow / védőszemüveg', 'place': '2. szint (kiegészítő) – a három kis termékcsoport (kesztyű, nagyító, szemüveg) együtt', 'note': 'Nitril kesztyű 1000, gumikesztyű 2900, kézi nagyító 390, zsebmikroszkóp 110, védőszemüveg 880 (vegyes) – a szavak nagyok, de általánosak (laza); a termékszám kicsi (6).', 'kws': 'nitril kesztyű|L|F\ngumikesztyű|L|S\ngumikesztyű 100 db|L|S\nnitril gumikesztyű|L|S\nvinyl kesztyű|L|E\negyszer használatos gumikesztyű|L|E\nlatex gumikesztyű|L|E\npúdermentes nitril kesztyű|L|E\nkézi nagyító|L|S\nzsebmikroszkóp|S|S\nékszerész nagyító|L|S\nkézi nagyító 40x|L|E\nkézi mikroszkóp|S|E\nmini mikroszkóp|S|E\nvilágítós nagyító|L|E\nzsebnagyító|L|E\nled nagyító|L|E\nnagyító|LN|N\nmikroszkóp|LN|N\nnagyítós lámpa|LN|N\nvédőszemüveg|L|E\nled szemüveg|L|E\nnagyító szemüveg led világítással|L|E\nmunkavédelmi kesztyű|LN|N'},
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'Az „afterharvest” szóra nincs magyar keresés; „betakarítás” 50, „gyógynövény feldolgozás” 20. Javasolt menünév: „Növényfeldolgozás, szárítás, tárolás”; H1: „Növényfeldolgozás betakarítás után”.', '''betakarítás|L
gyógynövény feldolgozás|L'''),
 ('1. Szárítás', '→ Szárítóháló, növényszárító', '''szárítóháló|S
növényszárító|S'''),
 ('2. Trimmelés', '→ Trimmelő olló; Trimmelő gép', '''trimmelő gép|L
trimmelő olló|S'''),
 ('3. Érlelés, tárolás', '→ Páraszabályzó tasak; Terpén tasak; Vákuumzsák', '''boveda|S
terpén|L
simítózáras tasak|S'''),
 ('4. Kivonatolás', '→ Kivonatolás', '''kivonatolás|L
bubble bag|S'''),
 ('Mérés', '→ Digitális mérleg', '''digitális mérleg|S'''),
 ('Munkaeszköz', '→ Kesztyű, nagyító, szemüveg', '''nitril kesztyű|L
zsebmikroszkóp|S'''),
]

EXT = [
 ('Befőttesüveg, csatos üveg (érlelés üvegben)', 'Nagy kereslet (befőttesüveg 4400) – a légmentes üveg az érlelés klasszikus eszköze; kínálatbővítési lehetőség az Érlelés és tárolás alá', '''befőttesüveg|L\nbefőttes üveg|L\ncsatos befőttes üveg|L'''),
 ('Rosin / hőprés', 'Kivonatolás bővítése (hőprés 390, de jórészt textilnyomó) – csak kínálatbővítés esetén', '''hőprés|L\nhőprés gép|L'''),
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

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Növényfeldolgozás, afterharvest (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A korábbi és a sandbox alkategória-neveket és -szerkezetet NEM vettük figyelembe. Kiindulás: a főkategória neve (a feldolgozás lépései), az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [(1, 'Növényfeldolgozás, afterharvest', '–', 'betakarítás', 'L', 'Főkategória', 'A főkategória-nevekre kicsi a keresés (betakarítás 50, gyógynövény feldolgozás 20) – a forgalmat a termékkategóriák hozzák; a név jó, a folyamatot írja le.', None), (2, 'Szárítóháló, növényszárító', 'Növényfeldolgozás, afterharvest', 'szárítóháló', 'S', 'Önálló kategória', '1. lépés: szárítás – szárítóháló 140.', 'Szárítóháló, növényszárító'), (2, 'Trimmelés', 'Növényfeldolgozás, afterharvest', 'trimmelő gép', 'L', 'Gyűjtőkategória', '2. lépés: trimmelés – kézi olló és gép külön keresési szándék.', None), (3, 'Trimmelő olló', 'Trimmelés', 'trimmelő olló', 'S', 'Önálló kategória', 'Trimmelő olló 30; Saboten / Easy Snips / AC Infinity.', 'Trimmelő olló'), (3, 'Trimmelő gép, trimmelő tál', 'Trimmelés', 'trimmelő gép', 'L', 'Önálló kategória', 'Trimmelő gép 320 (vegyes).', 'Trimmelő gép, trimmelő tál'), (2, 'Érlelés és tárolás', 'Növényfeldolgozás, afterharvest', 'simítózáras tasak', 'S', 'Gyűjtőkategória', '3. lépés: érlelés és tárolás – páraszabályzás, aroma, légmentes csomagolás.', None), (3, 'Páratartalom-szabályzó tasak', 'Érlelés és tárolás', 'boveda', 'S', 'Önálló kategória', 'Boveda 210, integra boost.', 'Páratartalom-szabályzó tasak'), (3, 'Terpén aromatasak', 'Érlelés és tárolás', 'terpén', 'L', 'Önálló kategória (új)', '9 élő terpén-/aromatasak – saját terméktípus.', 'Terpén aromatasak'), (3, 'Vákuumzsák, simítózáras tasak', 'Érlelés és tárolás', 'simítózáras tasak', 'S', 'Önálló kategória', 'Simítózáras tasak 720, vákuum zsák 90.', 'Vákuumzsák, simítózáras tasak'), (2, 'Kivonatolás: bubble bag, extraktor', 'Növényfeldolgozás, afterharvest', 'kivonatolás', 'L', 'Önálló kategória', '4. lépés: kivonatolás – bubble bag, Secret Box.', 'Kivonatolás: bubble bag, extraktor'), (2, 'Digitális mérleg, zsebmérleg', 'Növényfeldolgozás, afterharvest', 'digitális mérleg', 'S', 'Önálló kategória', 'Digitális mérleg 1600 – a legerősebb termékszó.', 'Digitális mérleg, zsebmérleg'), (2, 'Munkaeszköz: kesztyű, nagyító, grow szemüveg', 'Növényfeldolgozás, afterharvest', 'nitril kesztyű', 'L', 'Kiegészítő kategória', 'Kesztyű, nagyító, szemüveg – kis termékcsoportok együtt.', 'Munkaeszköz: kesztyű, nagyító, grow szemüveg')]
NOT_CATS = [
 ('Fermentáció', 'fermentálás', 'Élelmiszer-fermentálás (6600) – nem a mi szándékunk; a páraszabályzás / érlelés a pontos név.'),
 ('Csomagolás (általános)', 'csomagoló zacskó', 'Túl általános – „Vákuumzsák, simítózáras tasak”.'),
 ('Kesztyű, nagyító külön kategóriában', 'gumikesztyű', 'Kis termékszám – egy „Munkaeszköz” kategóriában.'),
 ('Palántaszállító csomagolás', None, 'A Palántanevelő ágba való.'),
 ('Aszalógép', 'aszalógép', 'Nincs ilyen termék.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A szerkezet csak a főkategória nevéből (a feldolgozás lépései), a termékek típusából és a keresési szándékból készült – a korábbi és a sandbox alkategóriák figyelmen kívül.',
]
TITLE = 'babylon-grow.eu – Növényfeldolgozás, afterharvest kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15/16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: csak a főkategória neve adott; a szerkezet a feldolgozás lépéseit követi: 1. szárítás → 2. trimmelés (olló / gép) → 3. érlelés és tárolás (páraszabályzó tasak, terpén tasak, vákuumzsák) → 4. kivonatolás, mellette mérés és munkaeszköz.',
 'Fő megállapítások: a legerősebb termékszavak: digitális mérleg 1600, simítózáras tasak 720, trimmelő gép 320 (vegyes), boveda 210, szárítóháló 140. A főkategória-névre („afterharvest”) nincs magyar keresés.',
 'Bővítési lehetőség: befőttesüveg / csatos üveg az érleléshez (befőttesüveg 4400) – az Érlelés és tárolás alá.',
 'A nagy általános szavak (fermentálás 6600, gumikesztyű 2900, befőttesüveg 4400, aszalógép 2900) más szándékúak – laza / nem.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a jelenlegi menü, hanem a keresési szándékok csoportosítása a feldolgozás lépései szerint (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Bővítési lehetőségek és nem célzott témák.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO0826 GRO0827 GRO2844 GRO2845 GRO4129 GRO4130 GRO4299 GRO4569 GRO4570', 'Szárítóháló, növényszárító', [], 'Erős', 'Szárítóháló'),
 ('GRO4571 GRO4572', 'Szárítóháló, növényszárító', [], 'Laza', 'Szárítóháló szűrő (tartozék)'),
 ('GRO1109 GRO1140 GRO3843 GRO3844 GRO4146 GRO4204 GRO4205 GRO4206 GRO4245 GRO4246 GRO4275 GRO4276 GRO4277 GRO4278 GRO4602 GRO4603 GRO4605 GRO4606', 'Trimmelő olló', [], 'Erős', 'Trimmelő olló'),
 ('GRO2788 GRO2789 GRO3740 GRO3929 GRO4235 GRO4273 GRO4372 GRO4527 GRO3827', 'Trimmelő gép, trimmelő tál', [], 'Erős', 'Trimmelő tál / gép / zsák'),
 ('GRO4604', 'Trimmelő olló', ['Hasznos kiegészítők'], 'Laza', 'Ollóélező'),
 ('HED1892 HED1893 HED1944 HED2041 HED2198 HED2199 HED2441 HED2442', 'Páratartalom-szabályzó tasak', ['Vákuumzsák, simítózáras tasak'], 'Erős', 'Boveda kétirányú páraszabályzó tasak'),
 ('HED1894 HED1895 HED1896 HED2196 HED2197 HED2287', 'Páratartalom-szabályzó tasak', ['Vákuumzsák, simítózáras tasak'], 'Erős', 'Integra Boost páraszabályzó tasak'),
 ('HED2288 HED2289 HED2329 HED2330 HED2331 GRO4565 GRO4566 GRO4567 GRO4568', 'Terpén aromatasak', ['Páratartalom-szabályzó tasak'], 'Erős', 'Terpén- / aromatasak'),
 ('GRO1542 GRO1805 GRO2822 GRO3264 HED2203', 'Vákuumzsák, simítózáras tasak', [], 'Erős', 'Vasalható vákuumzsák / ziplock tasak'),
 ('GRO4540 GRO4680 GRO4681 GRO4682 GRO4683', 'Palántanevelő ág – palántaszállító csomagolás', [], 'Más főkategória', 'Palántaszállító csomagolás – a Palántanevelő ágban is'),
 ('GRO1253 GRO1254 GRO3263 GRO3728 GRO3729 GRO3791 HED0724', 'Kivonatolás: bubble bag, extraktor', [], 'Erős', 'Secret Icer / Secret Box / shaker'),
 ('HED1397 HED1701 HED1828 HED1836 HED2156 HED2157 HED2341 HED2401 HED2402 HED2403 HED2404 HED2405', 'Digitális mérleg, zsebmérleg', [], 'Erős', 'Digitális zseb- / precíziós mérleg'),
 ('HED0413 HED0414 HED0415 HED1022 HED1489 HED1490', 'Digitális mérleg, zsebmérleg', [], 'Laza', 'Kalibráló súly'),
 ('GRO4279 GRO4557 GRO4558 GRO4559 GRO4560 GRO4562 GRO4641', 'Munkaeszköz: kesztyű, nagyító, grow szemüveg', ['Munkaeszköz: kesztyű, nagyító, grow szemüveg'], 'Erős', 'Egyszer használatos kesztyű'),
 ('GRO0821 GRO4306', 'Munkaeszköz: kesztyű, nagyító, grow szemüveg', ['Munkaeszköz: kesztyű, nagyító, grow szemüveg'], 'Erős', 'Zsebmikroszkóp / LED-es nagyító'),
 ('GRO3829 GRO4203', 'Munkaeszköz: kesztyű, nagyító, grow szemüveg', [], 'Laza', 'Grow- / védőszemüveg'),
]
