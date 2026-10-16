# Babylon – Hidropónia, öntözés (2026-10-16, 2. változat)
# Csak a FŐKATEGÓRIA NEVE alapján: a korábbi / sandbox alkategória-nevek és -szerkezet figyelmen kívül;
# alkategóriák az élő termékkínálat és a kulcsszóadat alapján.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 {'name': 'Hidropóniás rendszer', 'sheet': '1 Hidro rendszer', 'fo': 'hidropóniás rendszer', 'area': 'Komplett hidropóniás rendszer: DWC (mélyvizes), aeropónia, csepegtető (Wilma), árasztásos (ebb & flow, dán tálca)', 'place': '2. szint; technika (DWC / aeropónia / csepegtető / árasztásos) = szűrő', 'note': 'A „hidropónia” (210) a főkategória szava; itt a rendszerek: hidropóniás rendszer 40, dwc 90, ebb and flow 70, hidroponika 140. Az árasztásos dán tálca a Cserép ágban is (egy céloldal: itt).', 'kws': 'hidropóniás rendszer|S|F\nhidropónia webshop|S|S\nhidroponika|S|S\nhidropónia rendszer|S|E\ndwc|L|E\nhidropóniás termesztés|S|I\naeropónia|S|E\ndwc rendszer|S|E\nhidropónia otthon|S|E\nhidroponika otthon|S|E\nnutripot|S|G\nvízkultúra|L|E\nhidropónia hátrányai|S|I\nikea hidroponia|X|X\nebb and flow|S|S\ndán tálca|S|E\nhidroponikus termesztés|S|E'},
 {'name': 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép', 'sheet': '2 Hidrokultúra', 'fo': 'hidrokultúra', 'area': 'Hidro közeg és ültetőedény: agyaggolyó, hidrokosár (hálós kosár), neoprén korong, Venti Pot és lyukacsos hidro cserép', 'place': '2. szint – a „hidrokultúra” (90) szobanövényes és termesztői szándékot is lefed; az „agyaggolyó” (880) céloldala a Termesztő közeg ágban (itt H2 + link)', 'note': 'Hidrokultúra 90, agyaggolyó 880 (közeg-ág céloldal), hálós kosár 20, hidrogolyó 20.', 'kws': 'hidrokultúra|S|F\nhidrokultúra házilag|L|I\nagyaggolyó|S|N\nagyaggolyó növényekhez|S|S\nkertészeti agyaggolyó|S|S\nagyaggolyók|S|E\nagyaggolyó 50l|S|E\nhidrogolyó|S|S\nhálós kosár|S|S\nkomplement hálós kosár|S|E\nagyaggolyó orchidea|L|E\norchidea agyaggolyó|L|E\nagyaggolyó használata|S|I\nobi agyaggolyó|X|X'},
 {'name': 'Levegőztetés: légpumpa, porlasztókő', 'sheet': '3 Levegőztetés', 'fo': 'légpumpa', 'area': 'Tápoldat oxigénellátása: membrános légpumpa, porlasztókő (rúd, korong, gyűrű), levegőztető cső, elosztó', 'place': '2. szint', 'note': 'A keresők jó része akváriumos – laza kötődés, de ugyanaz a termék (Hailea, Neptune).', 'kws': 'légpumpa|S|F\nakvárium légpumpa|L|S\nlevegőztető pumpa|S|S\nporlasztókő|S|S\nlevegőztető kő|S|E\nlégpumpa akvárium|L|E\nlevegőpumpa akváriumba|L|E\nakvárium levegőztető pumpa|L|E\nakvárium porlasztókő|L|E\nlevegőztető cső|S|E\nhailea légpumpa|S|G\nporlasztó kő|S|E\nlevegőztető kő használata|S|I\nakvárium levegőztető kő|L|E'},
 {'name': 'Tápoldat-adagoló pumpa, vízhűtő', 'sheet': '4 Adagoló, vízhűtő', 'fo': 'tápoldat adagoló', 'area': 'Hidro automatizálás: perisztaltikus adagoló pumpa (Aqua Master, Milwaukee), tápoldathűtő (chiller)', 'place': '2. szint (kicsi, ~6 termék) – vagy a Hidropóniás rendszer alatt 3. szinten', 'note': 'Tápoldat adagoló 140, perisztaltikus pumpa 110, adagoló pumpa 50.', 'kws': 'tápoldat adagoló|S|F\nadagoló pumpa|S|S\nadagolópumpa|S|S\nfolyékony tápoldat adagoló|S|E\ncsepegtető tápoldat adagoló|S|E\nöntözőrendszer tápoldat adagoló|L|E\nakvárium hűtő|L|S\nakvárium vízhűtő|L|E\ntápoldat adagoló házilag|L|I\nchiller|LN|N\npumpás adagoló|LN|N\nperisztaltikus pumpa|S|S'},
 {'name': 'Vízpumpa, tápoldattartály', 'sheet': '5 Vízpumpa, tartály', 'fo': 'vízpumpa', 'area': 'Merülő keringető szivattyú és összecsukható tápoldattartály (FlexiTank)', 'place': '2. szint – a két terméktípus együtt (kevés élő termék, közös felhasználás)', 'note': 'Vízpumpa 720, víztartály 1300 (vegyes), összecsukható víztartály 50. A „búvárszivattyú” (8100) kútszivattyú – LN.', 'kws': 'vízpumpa|S|F\nmerülő szivattyú|L|S\nszökőkút szivattyú|L|S\nakvárium szivattyú|L|S\ncsobogó szivattyú|L|E\nvizpumpa|S|E\nmerülőszivattyú|L|E\nelektromos vízpumpa|S|E\nakvárium pumpa|L|E\nakvárium keringető szivattyú|L|E\n12v vízpumpa|L|E\nbúvárszivattyú|LN|N\nvíztartály|L|S\nműanyag víztartály|L|S\nösszecsukható víztartály|S|S\n1000 literes víztartály|L|E\nviz tartály|L|E\nviztartaly|L|E\nösszecsukható esővízgyűjtő|L|E'},
 {'name': 'Automata öntözés, önöntöző', 'sheet': '6 Öntözés', 'fo': 'automata öntözőrendszer', 'area': 'Beltéri automata öntözés tartályból, időzítővel; önöntöző alátét / cserép', 'place': '2. szint – a főkategória „öntözés” felének céloldala', 'note': 'Automata öntözőrendszer 880, önöntöző cserép 90. Az „öntözés” (1900), „öntözőrendszer” (4400), „csepegtető cső” (3600) kerti szándék – LN.', 'kws': 'automata öntözőrendszer|S|F\nöntözőrendszer|LN|N\ncsepegtető rendszer|LN|N\ncsepegtető öntözés|LN|N\ncsepegtető öntözőrendszer|LN|N\nöntözés időzítő|S|S\nlocsolás időzítő|L|E\nautomata öntöző|S|E\ncsepegtető öntözés tartályból|S|E\nöntözőrendszer szett|S|E\nöntöző automata|S|E\ncsepegtető öntözés szivattyúval|S|E\nautomata csepegtető rendszer|S|E\ncsapra szerelhető öntöző automata|L|E\nmikro öntözés|S|E\nautopot|S|G\nblumat|S|G\nautomata növény öntöző|S|E\nbalkon öntözőrendszer|L|E\nöntöző szett|S|E\nszobanövény öntöző|S|E\nnyaralás alatti öntözés|S|I\ncsepegtető rendszer házilag|L|I\ngravitációs csepegtető öntözés házilag|L|I\nöntözőrendszer házilag|L|I\ncsepegtető cső|LN|N\nöntözés|LN|N\nkerti öntöző|LN|N\nönöntöző cserép|S|S\ncsepegtető öntöző szett|S|E\nkapilláris cső öntözés|S|E'},
 {'name': 'Kézi és pumpás permetező', 'sheet': '7 Permetező', 'fo': 'kézi permetező', 'area': 'Kézi és pumpás permetező, elektromos porlasztófej – tápoldat, levéltrágya, növényvédő szer kijuttatására', 'place': '2. szint – erős saját kulcsszó (kézi permetező 1300)', 'note': 'Kézi permetező 1300, pumpás permetező 260, 5 literes permetező 480. A háti / akkus permetező (1600 / 2400) mezőgazdasági – LN.', 'kws': 'kézi permetező|S|F\npumpás permetező|S|S\n5 literes permetező|S|S\nkézi permetező 5l|S|E\nkézi permetező 2l|S|E\nelektromos permetező|L|E\npermetező|LN|N\nakkus permetező|LN|N'},
 {'name': 'Víztisztító, fordított ozmózis', 'sheet': '8 Víztisztító', 'fo': 'fordított ozmózisos víztisztító', 'area': 'Öntöző- és tápoldatvíz tisztítása: fordított ozmózis (RO), üledék- és aktívszén-szűrő, RO membrán', 'place': '2. szint', 'note': 'A „vízszűrő” (6600) és a „víztisztító” (5400) nagy, de kancsós / ivóvíz-szándék is. A „vízszűrő kancsó” (5400), a „vízlágyító” (2900) és a „vízszűrő betét” (1300) nem a mi termékünk.', 'kws': 'fordított ozmózisos víztisztító|S|F\ncsapra szerelhető víztisztító|S|S\nro víztisztító|S|S\nreverse osmosis víztisztító|S|S\nvíztisztító ro|S|E\ncsapra szerelhető vízszűrő|S|E\nfordított ozmózis|S|S\nozmózis víztisztító|S|E\nozmózisos víztisztító|S|E\nozmozisos vízszűrő|S|E\nro vízszűrő|S|E\nfordított ozmózis vízszűrő|S|E\nozmózis szűrő|S|E\nozmózis vízszűrő|S|E\nozmózisos vízszűrő|S|E\nozmózis membrán|S|E\nüledékszűrő|S|E\naktívszén szűrő|L|E\naktív szén szűrőbetét|L|E\nvíztisztító szűrő|L|E\nvízszűrő patron|L|E\nklórmentesítő|L|E\nvízszűrő rendszer|L|E\nvízszűrő berendezés|LN|N\nvíztisztító berendezés|LN|N\nvízszűrő csapra|LN|N\nvízszűrő|LN|N\nvíztisztító|LN|N\nvízszűrő kancsó|LN|N\nvízlágyító|LN|N'},
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'A „hidropónia” (210) és az „öntözés” (1900, főleg kerti) – a menünév „Hidropónia, öntözés” jó; H1: „Hidropónia és beltéri öntözés”.', '''hidropónia|S
hidroponika|S
öntözés|LN'''),
 ('Rendszer vásárlása', '→ Hidropóniás rendszer', '''hidropóniás rendszer|S
dwc|L
ebb and flow|S'''),
 ('Hidrokultúra (szobanövény is)', '→ Hidrokultúra', '''hidrokultúra|S
agyaggolyó|S'''),
 ('Oxigén, tápoldat', '→ Levegőztetés; Tápoldat-adagoló', '''légpumpa|S
tápoldat adagoló|S
perisztaltikus pumpa|S'''),
 ('Víz mozgatása, tárolása', '→ Vízpumpa, tápoldattartály', '''vízpumpa|S
víztartály|L'''),
 ('Öntözés', '→ Automata öntözés; Permetező', '''automata öntözőrendszer|S
kézi permetező|S'''),
 ('Víz tisztítása', '→ Víztisztító, fordított ozmózis', '''fordított ozmózisos víztisztító|S'''),
]

EXT = [
 ('Kerti öntözés (csepegtető cső, szórófej)', 'Nagy volumen, de kerti öntözéstechnika – csak kínálatbővítés esetén', '''öntözőrendszer|L
csepegtető cső|L
csepegtető rendszer|L
kerti öntöző|L'''),
 ('Kútszivattyú, búvárszivattyú', 'Nem growshop-téma', '''búvárszivattyú|LN
merülő szivattyú|L'''),
 ('Vízszűrő kancsó, vízlágyító', 'Háztartási ivóvíz-szűrés – nem a mi termékünk', '''vízszűrő kancsó|LN
vízlágyító|LN'''),
 ('Háti / akkus permetező', 'Mezőgazdasági permetező – csak kínálatbővítés esetén', '''permetező|L
akkus permetező|L'''),
]

MAKERS = '''nutripot
autopot
blumat
hailea légpumpa'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Hidropónia, öntözés (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A korábbi és a sandbox alkategória-neveket és -szerkezetet NEM vettük figyelembe. Kiindulás: a főkategória neve, az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [(1, 'Hidropónia, öntözés', '–', 'hidropónia', 'S', 'Főkategória', 'Hidropónia 210 + öntözés 1900 (kerti, LN) – a menünév jó.', None), (2, 'Hidropóniás rendszer', 'Hidropónia, öntözés', 'hidropóniás rendszer', 'S', 'Önálló kategória', 'DWC, aeropónia, Wilma, dán tálca – technika = szűrő.', 'Hidropóniás rendszer'), (2, 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép', 'Hidropónia, öntözés', 'hidrokultúra', 'S', 'Önálló kategória', 'Hidrokultúra 90; agyaggolyó céloldala a Közeg ágban.', 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép'), (2, 'Levegőztetés: légpumpa, porlasztókő', 'Hidropónia, öntözés', 'légpumpa', 'S', 'Önálló kategória', 'Légpumpa 110, porlasztókő 70.', 'Levegőztetés: légpumpa, porlasztókő'), (2, 'Tápoldat-adagoló pumpa, vízhűtő', 'Hidropónia, öntözés', 'tápoldat adagoló', 'S', 'Önálló kategória', 'Tápoldat adagoló 140, perisztaltikus pumpa 110.', 'Tápoldat-adagoló pumpa, vízhűtő'), (2, 'Vízpumpa, tápoldattartály', 'Hidropónia, öntözés', 'vízpumpa', 'S', 'Önálló kategória', 'Vízpumpa 720, víztartály 1300 (vegyes).', 'Vízpumpa, tápoldattartály'), (2, 'Automata öntözés, önöntöző', 'Hidropónia, öntözés', 'automata öntözőrendszer', 'S', 'Önálló kategória', 'Automata öntözőrendszer 880, önöntöző cserép 90.', 'Automata öntözés, önöntöző'), (2, 'Kézi és pumpás permetező', 'Hidropónia, öntözés', 'kézi permetező', 'S', 'Önálló kategória', 'Kézi permetező 1300.', 'Kézi és pumpás permetező'), (2, 'Víztisztító, fordított ozmózis', 'Hidropónia, öntözés', 'fordított ozmózisos víztisztító', 'S', 'Önálló kategória', 'Fordított ozmózisos víztisztító 880.', 'Víztisztító, fordított ozmózis')]
NOT_CATS = [
 ('Hidro / öntözés gyűjtőkategóriák (2 szintű bontás)', None, 'Kevés élő termék (~60) – lapos, egyszintű bontás áttekinthetőbb.'),
 ('Agyaggolyó önálló kategória', 'agyaggolyó', 'Céloldala a Termesztő közeg ágban – itt a Hidrokultúra része.'),
 ('Kerti öntözés (csepegtető cső, szórófej)', 'csepegtető cső', 'Nincs ilyen termék.'),
 ('Búvárszivattyú', 'búvárszivattyú', 'Kútszivattyú – nem a mi termékünk.'),
 ('Vízszűrő kancsó', 'vízszűrő kancsó', 'Háztartási ivóvíz – nem célozni.'),
 ('Hidro tápok (CANNA Hydro, Aqua…)', None, 'A Tápok főkategóriába valók.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A szerkezet csak a főkategória nevéből, a termékek funkciójából és a keresési szándékból készült – a korábbi és a sandbox alkategóriák figyelmen kívül.',
]
TITLE = 'babylon-grow.eu – Hidropónia, öntözés kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15/16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: csak a főkategória neve („Hidropónia, öntözés”) adott; az alkategóriák a termékek funkciójából (rendszer, közeg / edény, levegőztetés, adagolás, víz mozgatása / tárolása, öntözés, permetezés, víztisztítás) és a keresési szándékból épülnek, lapos (2 szintű) szerkezetben.',
 'Fő megállapítások: a legerősebb termékszavak: kézi permetező 1300, víztartály 1300 (vegyes), automata öntözőrendszer 880, fordított ozmózisos víztisztító 880, vízpumpa 720; maga a „hidropónia” csak 210. A „hidrokultúra” (90) jó gyűjtőnév az agyaggolyó + hidrokosár + hidro cserép körnek.',
 'Új a besorolásban: a dán tálca (ebb & flow 70) és az önöntöző alátét (önöntöző cserép 90) is ide tartozik.',
 'A nagy általános szavak (búvárszivattyú 8100, vízszűrő 6600, öntözőrendszer 4400, akkus permetező 2400) kerti / háztartási szándékúak – LN.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a jelenlegi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Kerti / háztartási vagy nem kínált témák – csak kínálatbővítés esetén.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO1106 GRO1219 GYSZ0029 GYSZ0029V GYSZ0033 GYSZ0034', 'Hidropóniás rendszer', [], 'Erős', 'DWC / aeropóniás rendszer, hidro szett'),
 ('GRO1679 GRO1680 GRO1681 GRO1682 GRO1683 GRO1685 GRO3765 GRO3766 GRO3767', 'Hidropóniás rendszer', ['Automata öntözés, önöntöző'], 'Erős', 'Wilma / Flo-Gro csepegtető rendszer'),
 ('GRO1222 GRO1757', 'Palántanevelő ág – Propagátor', ['Hidropóniás rendszer'], 'Laza', 'X-Stream aeropóniás propagátor'),
 ('GRO0054 GRO0056 GRO0057 GRO1417', 'Hidropóniás rendszer', ['Cserép, tálca ág – Műanyag tálca, árapály asztal'], 'Erős', 'Dán tálca – árasztásos (ebb & flow) hidrorendszer'),
 ('GRO1841 GRO1845 GRO1847 GRO1848 GRO1990 GRO4369 GRO4370', 'Levegőztetés: légpumpa, porlasztókő', [], 'Erős', 'Légpumpa'),
 ('GRO1628 GRO1629 GRO1851 GRO1853 GRO1854 GRO1855 GRO2365 GRO2366 GRO2631', 'Levegőztetés: légpumpa, porlasztókő', [], 'Erős', 'Porlasztókő'),
 ('GRO1084 GRO1736 GRO2630 GRO2625 GRO2628 GRO1763', 'Levegőztetés: légpumpa, porlasztókő', [], 'Laza', 'Levegőztető cső, elosztó, idom'),
 ('GRO1406 GRO2349 GRO2850 GYUJTO0319', 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép', [], 'Erős', 'Agyaggolyó – a Közegek ágban is'),
 ('GRO0663 GRO1291 GRO4309 GRO3378 GRO0801 GRO2584', 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép', [], 'Erős', 'Hidrokosár, neoprén korong'),
 ('GRO3348 GRO3349 GRO3350', 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép', [], 'Laza', 'Venti Pot hidro cserép'),
 ('GRO2107 GRO2497', 'Hidrokultúra: agyaggolyó, hidrokosár, hidro cserép', ['Cserép, tálca ág – Virágcserép'], 'Laza', 'Lyukacsos szögletes cserép, hidropóniához is'),
 ('GRO2515 GRO4263 GRO4264 GRO4265 GRO4269 GRO3746', 'Tápoldat-adagoló pumpa, vízhűtő', [], 'Erős', 'Perisztaltikus adagoló, hidro vezérlő'),
 ('GRO2624 GRO1992 GRO1993', 'Tápoldat-adagoló pumpa, vízhűtő', [], 'Erős', 'Hailea vízhűtő (chiller)'),
 ('GRO0810 GRO1408', 'Automata öntözés, önöntöző', [], 'Erős', 'Automata öntözőrendszer, öntözési időzítő'),
 ('GRO2939', 'Palántanevelő ág – Propagátor', ['Automata öntözés, önöntöző'], 'Laza', 'Önöntöző propagátor'),
 ('GRO1252 GRO1328 GRO1329 GRO1330 GRO1331 GRO1332 GRO1849 GRO1850 GRO1994', 'Vízpumpa, tápoldattartály', [], 'Erős', 'Merülő keringető szivattyú'),
 ('GRO1958 GRO2244 GRO2637 GRO2638', 'Vízpumpa, tápoldattartály', [], 'Erős', 'FlexiTank összecsukható víztartály'),
 ('GRO1812', 'Vízpumpa, tápoldattartály', [], 'Laza', 'Esővízgyűjtő tartály'),
 ('GRO0811 GRO0812 GRO0813 GRO4128 GRO4576', 'Kézi és pumpás permetező', [], 'Erős', 'Kézi / pumpás permetező, porlasztófej'),
 ('GRO0798 GRO1248 GRO2395 GRO2396 GRO2397', 'Víztisztító, fordított ozmózis', [], 'Erős', 'Fordított ozmózisos víztisztító'),
 ('GRO1249 GRO1250 GRO2777', 'Víztisztító, fordított ozmózis', [], 'Erős', 'Szűrőbetét, RO membrán'),
 ('GRO4298', 'Automata öntözés, önöntöző', ['Cserép, tálca ág'], 'Erős', 'AC Infinity víztartályos (önöntöző) alátét'),
 ('GRO0424 GRO0427 GRO1530 GRO1531', 'Tápok ág – hidro táp', [], 'Más főkategória', 'CANNA Hydro táp – a Tápok ágba'),
]
