# Babylon – Hidropónia, öntözés (sandbox-főkategória, 2026-10-15)
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='Hidropóniás rendszer', sheet='1 Hidro rendszer', fo='hidropónia',
      area='DWC, aeropónia, csepegtető hidro – komplett rendszerek',
      place='3. szint a „Hidropóniás rendszer, kiegészítő” alatt (vagy 2. szint, ha a kiegészítők külön ágat kapnak)',
      note='Kis, de tiszta szándékú klaszter (hidropónia 210, hidropónia webshop 70). A „hidrokultúra” (90) inkább szobanövény-hidrokultúra. A „dwc” (90) vegyes (porszívó-modellnév is).',
      kws='''hidropónia|S|F
hidropónia webshop|S|S
hidroponika|S|S
hidropóniás rendszer|S|S
hidropónia rendszer|S|E
hidrokultúra|L|E
dwc|L|E
hidropóniás termesztés|S|I
aeropónia|S|E
dwc rendszer|S|E
hidropónia otthon|S|E
hidroponika otthon|S|E
nutripot|S|G
vízkultúra|L|E
hidrokultúra házilag|L|I
hidropónia hátrányai|S|I
ikea hidroponia|X|X'''),
 dict(name='Levegőztető pumpa, porlasztókő', sheet='2 Levegőztetés', fo='légpumpa',
      area='Tápoldat oxigénellátása – légpumpa, porlasztókő, levegőztető cső',
      place='3. szint a „Hidropóniás rendszer, kiegészítő” alatt',
      note='A keresők jó része akváriumos – laza kötődés, de ugyanaz a termék (Hailea, Neptune).',
      kws='''légpumpa|S|F
akvárium légpumpa|L|S
levegőztető pumpa|S|S
porlasztókő|S|S
levegőztető kő|S|E
légpumpa akvárium|L|E
levegőpumpa akváriumba|L|E
akvárium levegőztető pumpa|L|E
akvárium porlasztókő|L|E
levegőztető cső|S|E
hailea légpumpa|S|G
porlasztó kő|S|E
levegőztető kő használata|S|I'''),
 dict(name='Agyaggolyó, hidrokosár', sheet='3 Agyaggolyó', fo='agyaggolyó',
      area='Hidro közeg és ültetőedény – agyaggolyó, hálós kosár, neoprén korong',
      place='3. szint a „Hidropóniás rendszer, kiegészítő” alatt; az agyaggolyó a Közegek ágban is (kannibalizáció: egy céloldal!)',
      note='Az „agyaggolyó” (880) erős, de jórészt orchidea / szobanövény célú. Ha a Közegek főkategóriában is lesz agyaggolyó kategória, a fő kulcsszó céloldala csak az egyik lehet – itt a hidrokosár legyen a hangsúly.',
      kws='''agyaggolyó|S|F
agyaggolyó növényekhez|S|S
kertészeti agyaggolyó|S|S
agyaggolyók|S|E
agyaggolyó 50l|S|E
hidrogolyó|S|S
hálós kosár|S|S
komplement hálós kosár|S|E
agyaggolyó orchidea|L|E
orchidea agyaggolyó|L|E
agyaggolyó használata|S|I
obi agyaggolyó|X|X'''),
 dict(name='Tápoldat-adagoló, vízhűtő', sheet='4 Adagoló, hűtő', fo='tápoldat adagoló',
      area='Hidro automatizálás – perisztaltikus adagoló pumpa, tápoldathűtő (chiller)',
      place='3. szint a „Hidropóniás rendszer, kiegészítő” alatt, vagy szűrő a kiegészítők között',
      note='A „chiller” (170) ipari / klíma keresés, az „akvárium hűtő” (210) akváriumos – laza. A „pumpás adagoló” (140) szappanadagoló.',
      kws='''tápoldat adagoló|S|F
adagoló pumpa|S|S
adagolópumpa|S|S
folyékony tápoldat adagoló|S|E
csepegtető tápoldat adagoló|S|E
öntözőrendszer tápoldat adagoló|L|E
akvárium hűtő|L|S
akvárium vízhűtő|L|E
tápoldat adagoló házilag|L|I
chiller|LN|N
pumpás adagoló|LN|N'''),
 dict(name='Automata öntözőrendszer', sheet='5 Öntözőrendszer', fo='automata öntözőrendszer',
      area='Cserepes / beltéri csepegtető öntözés tartályból, időzítővel',
      place='3. szint az „Öntözés, vízpumpa, tartály” alatt',
      note='Az „öntözőrendszer” (4400), „csepegtető rendszer” (1900), „csepegtető cső” (3600) főleg kerti, földbe telepített öntözés – laza. A mi termékeink a tartályból, szivattyúval / időzítővel működő beltéri rendszerek (csepegtető öntözés tartályból 210).',
      kws='''automata öntözőrendszer|S|F
öntözőrendszer|LN|N
csepegtető rendszer|LN|N
csepegtető öntözés|LN|N
csepegtető öntözőrendszer|LN|N
öntözés időzítő|S|S
locsolás időzítő|L|E
automata öntöző|S|E
csepegtető öntözés tartályból|S|E
öntözőrendszer szett|S|E
öntöző automata|S|E
csepegtető öntözés szivattyúval|S|E
automata csepegtető rendszer|S|E
csapra szerelhető öntöző automata|L|E
mikro öntözés|S|E
autopot|S|G
blumat|S|G
automata növény öntöző|S|E
balkon öntözőrendszer|L|E
öntöző szett|S|E
szobanövény öntöző|S|E
nyaralás alatti öntözés|S|I
csepegtető rendszer házilag|L|I
gravitációs csepegtető öntözés házilag|L|I
öntözőrendszer házilag|L|I
csepegtető cső|LN|N
öntözés|LN|N
kerti öntöző|LN|N'''),
 dict(name='Vízpumpa, keringető szivattyú', sheet='6 Vízpumpa', fo='vízpumpa',
      area='Merülő keringető szivattyú hidro rendszerhez, tápoldat-tartályhoz',
      place='3. szint az „Öntözés, vízpumpa, tartály” alatt',
      note='A „búvárszivattyú” (8100) kútszivattyú – nem a mi termékünk. A „merülő szivattyú” (1000) vegyes, a „szökőkút szivattyú” (390) és az „akvárium szivattyú” (260) ugyanaz a termékkör.',
      kws='''vízpumpa|S|F
merülő szivattyú|L|S
szökőkút szivattyú|L|S
akvárium szivattyú|L|S
csobogó szivattyú|L|E
vizpumpa|S|E
merülőszivattyú|L|E
elektromos vízpumpa|S|E
akvárium pumpa|L|E
akvárium keringető szivattyú|L|E
12v vízpumpa|L|E
búvárszivattyú|LN|N'''),
 dict(name='Víztartály, tápoldattartály', sheet='7 Víztartály', fo='víztartály',
      area='Tápoldat és öntözővíz tárolása – összecsukható (flexi) tartály',
      place='3. szint az „Öntözés, vízpumpa, tartály” alatt; az esővízgyűjtő külön',
      note='A „víztartály” (1300) vegyes (ivóvíz, kerti). Az összecsukható tartály a mi termékünk (összecsukható víztartály 50).',
      kws='''víztartály|L|F
műanyag víztartály|L|S
összecsukható víztartály|S|S
1000 literes víztartály|L|E
viz tartály|L|E
viztartaly|L|E'''),
 dict(name='Kézi és pumpás permetező', sheet='8 Permetező', fo='pumpás permetező',
      area='Növényvédő szer, levéltrágya kijuttatása – kézi és pumpás permetező',
      place='3. szint az „Öntözés…” alatt, vagy a Növényvédelem főkategóriában (ha lesz)',
      note='A „permetező” (2900) és az „akkus permetező” (2400) főleg háti / mezőgazdasági permetező. A mi termékeink 1–5 literes kézi / pumpás permetezők.',
      kws='''pumpás permetező|S|F
kézi permetező|S|S
5 literes permetező|S|S
kézi permetező 5l|S|E
kézi permetező 2l|S|E
elektromos permetező|L|E
permetező|LN|N
akkus permetező|LN|N'''),
 dict(name='Vízszűrő, fordított ozmózis', sheet='9 Vízszűrő', fo='fordított ozmózisos víztisztító',
      area='Öntöző- és tápoldatvíz tisztítása – RO (fordított ozmózis), üledék- és aktívszén szűrő',
      place='2. szint – a sandbox-név jó; a H1 / SEO title: „Fordított ozmózisos vízszűrő, víztisztító”',
      note='A „vízszűrő” (6600) és a „víztisztító” (5400) nagy, de kancsós / ivóvíz-szándék is. A „vízszűrő kancsó” (5400), a „vízlágyító” (2900) és a „vízszűrő betét” (1300) nem a mi termékünk.',
      kws='''fordított ozmózisos víztisztító|S|F
csapra szerelhető víztisztító|S|S
ro víztisztító|S|S
reverse osmosis víztisztító|S|S
víztisztító ro|S|E
csapra szerelhető vízszűrő|S|E
fordított ozmózis|S|S
ozmózis víztisztító|S|E
ozmózisos víztisztító|S|E
ozmozisos vízszűrő|S|E
ro vízszűrő|S|E
fordított ozmózis vízszűrő|S|E
ozmózis szűrő|S|E
ozmózis vízszűrő|S|E
ozmózisos vízszűrő|S|E
ozmózis membrán|S|E
üledékszűrő|S|E
aktívszén szűrő|L|E
aktív szén szűrőbetét|L|E
víztisztító szűrő|L|E
vízszűrő patron|L|E
klórmentesítő|L|E
vízszűrő rendszer|L|E
vízszűrő berendezés|LN|N
víztisztító berendezés|LN|N
vízszűrő csapra|LN|N
vízszűrő|LN|N
víztisztító|LN|N
vízszűrő kancsó|LN|N
vízlágyító|LN|N'''),
]

OLD_SHEET = 'Sandbox menünevek'
OLD = [
 ('Hidropónia, öntözés (főkategória)', 'A „hidropónia” (210) és az „öntözés” (1900, főleg kerti) a főkategória-név két fele – jó menünév.', '''hidropónia|S
öntözés|LN'''),
 ('Hidropóniás rendszer, kiegészítő', 'Marad; alatta 3. szinten: Hidropóniás rendszer; Levegőztető pumpa, porlasztókő; Agyaggolyó, hidrokosár; Tápoldat-adagoló, vízhűtő', '''hidropónia|S
hidropóniás rendszer|S
légpumpa|S
agyaggolyó|S'''),
 ('Öntözés, vízpumpa, tartály', 'Marad; alatta 3. szinten: Automata öntözőrendszer; Vízpumpa, keringető szivattyú; Víztartály; (Permetező)', '''automata öntözőrendszer|S
vízpumpa|S
víztartály|L'''),
 ('Vízszűrő, fordított ozmózis', 'Marad; H1: „Fordított ozmózisos vízszűrő, víztisztító”', '''vízszűrő|L
fordított ozmózis|S
fordított ozmózisos víztisztító|S'''),
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

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Hidropónia, öntözés (termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet, a Google Shopping-feed termékei (1999 db) és a Kulcsszótervező adatai. Termékszám = elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
HIDRO = 'Hidropóniás rendszer, kiegészítő'
ONT = 'Öntözés, vízpumpa, tartály'
STRUCT = [
 (1, 'Hidropónia, öntözés', '–', 'hidropónia', 'S', 'Főkategória', 'Jó főkategória-név: a „hidropónia” (210) és az „öntözés” (1900) is keresett.', None),
 (2, HIDRO, 'Hidropónia, öntözés', 'hidropónia', 'S', 'Gyűjtőkategória', 'A sandbox-név jó; a kiegészítők 3. szintre bontva.', None),
 (3, 'Hidropóniás rendszer', HIDRO, 'hidropónia', 'S', 'Önálló kategória', 'DWC, aeropónia, Wilma csepegtető rendszerek.', 'Hidropóniás rendszer'),
 (3, 'Levegőztető pumpa, porlasztókő', HIDRO, 'légpumpa', 'S', 'Önálló kategória', 'Sok termék (Hailea, Neptune pumpák, porlasztókövek, cső, elosztó).', 'Levegőztető pumpa, porlasztókő'),
 (3, 'Agyaggolyó, hidrokosár', HIDRO, 'agyaggolyó', 'S', 'Önálló kategória', 'Erős klaszter (agyaggolyó 880); egyeztetni a Közegek ággal (egy céloldal).', 'Agyaggolyó, hidrokosár'),
 (3, 'Tápoldat-adagoló, vízhűtő', HIDRO, 'tápoldat adagoló', 'S', 'Önálló kategória (kicsi)', 'Perisztaltikus adagoló pumpák, Hailea chiller – kis keresés, navigációs szerep.', 'Tápoldat-adagoló, vízhűtő'),
 (2, ONT, 'Hidropónia, öntözés', 'automata öntözőrendszer', 'S', 'Gyűjtőkategória', 'A sandbox-név jó (öntözés, vízpumpa, tartály) – 3. szintre bontva.', None),
 (3, 'Automata öntözőrendszer', ONT, 'automata öntözőrendszer', 'S', 'Önálló kategória', 'Automata öntözőrendszer 880; a beltéri, tartályos rendszerek.', 'Automata öntözőrendszer'),
 (3, 'Vízpumpa, keringető szivattyú', ONT, 'vízpumpa', 'S', 'Önálló kategória', 'Vízpumpa 720, szökőkút / akvárium szivattyú (laza) – sok Neptune / Hailea pumpa.', 'Vízpumpa, keringető szivattyú'),
 (3, 'Víztartály, tápoldattartály', ONT, 'víztartály', 'L', 'Önálló kategória (kicsi)', 'Víztartály 1300 (vegyes); 4 FlexiTank + esővízgyűjtő.', 'Víztartály, tápoldattartály'),
 (3, 'Kézi és pumpás permetező', ONT, 'pumpás permetező', 'S', 'Önálló kategória vagy Növényvédelem ág', 'Kézi permetező 1300, pumpás permetező 260 – 5 termék.', 'Kézi és pumpás permetező'),
 (2, 'Vízszűrő, fordított ozmózis', 'Hidropónia, öntözés', 'fordított ozmózisos víztisztító', 'S', 'Önálló kategória', 'Fordított ozmózisos víztisztító 880, csapra szerelhető víztisztító 880, RO víztisztító 480.', 'Vízszűrő, fordított ozmózis'),
]
NOT_CATS = [
 ('Kerti öntözés', 'csepegtető cső', 'Kerti csepegtető cső / szórófej – nincs ilyen termék.'),
 ('Búvárszivattyú', 'búvárszivattyú', 'Kútszivattyú – nem a mi termékünk.'),
 ('Vízszűrő kancsó, vízlágyító', 'vízszűrő kancsó', 'Háztartási ivóvíz – nem célozni.'),
 ('Hidro tápok (Canna Aqua / Hydro, Dutch Formula …)', None, 'A Tápok főkategóriába valók, nem ide.'),
 ('Hydro Shoot termesztősátor', None, 'A név ellenére termesztősátor – a Sátor ágba.'),
]
PRODUCT_NOTE = [
 'Forrás: a Babylon Google Ads fiók Shopping-termékadatai (termékkód = Shopping item ID, terméknév = feed-cím), 2024-10-01 – 2026-10-14, összesen 1999 termék. A Shoprenter API és az éles oldal a felhőből nem érhető el.',
 'Figyelem: ez a Google-ben hirdetett termékkör, nem feltétlenül a teljes katalógus. A gyártó és a gyűjtőtermék (GYUJTO…) adat a feedben nem érhető el.',
 'A lapon a teljes termékkínálat szerepel: elöl a Hidropónia, öntözés kategóriákba sorolt termékek (Erős, Laza), majd a más főkategóriába tartozók, végül „Nem tartozik ide” jelöléssel az összes többi.',
]

TITLE = 'babylon-grow.eu – Hidropónia, öntözés főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: Google Shopping-feed (1999 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a sandbox három alkategória-neve jó, de mindhárom gyűjtőnév – a forgalmat a konkrét termékszavak hozzák (fordított ozmózisos víztisztító 880, automata öntözőrendszer 880, agyaggolyó 880, vízpumpa 720, hidropónia 210, légpumpa 110). Javasolt 3. szintű bontás a Kategóriaszerkezet-ajánlás lapon.',
 'A nagy általános szavak (öntözőrendszer 4400, csepegtető cső 3600, búvárszivattyú 8100, vízszűrő 6600, vízszűrő kancsó 5400) főleg kerti / háztartási szándékúak – laza kötődés vagy kizárás.',
 'Az agyaggolyó a Közegek ágban is előfordulhat: a fő kulcsszónak csak egy céloldala legyen (kannibalizáció).',
]
OLD_TITLE = 'A sandbox „Hidropónia, öntözés” menünevei – keresési volumen és javaslat'
OLD_SUB = 'Sandbox-tervezet: Hidropóniás rendszer, kiegészítő; Öntözés, vízpumpa, tartály; Vízszűrő, fordított ozmózis.'
EXT_TITLE = 'Rokon, vízzel kapcsolatos területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Nagy volumenű, de kerti / háztartási vagy nem kínált témák – csak kínálatbővítés esetén.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'

PRODUCTS = [
 ('GRO1106 GRO1219 GYSZ0029 GYSZ0029V GYSZ0033 GYSZ0034', 'Hidropóniás rendszer', [], 'Erős', 'DWC / aeropóniás rendszer, hidro szett'),
 ('GRO1679 GRO1680 GRO1681 GRO1682 GRO1683 GRO1685 GRO3765 GRO3766 GRO3767', 'Hidropóniás rendszer', ['Automata öntözőrendszer'], 'Erős', 'Wilma / Flo-Gro csepegtető rendszer'),
 ('GRO1222 GRO1757', 'Palántanevelő ág – Propagátor', ['Hidropóniás rendszer'], 'Laza', 'X-Stream aeropóniás propagátor'),
 ('GRO0054 GRO0056 GRO0057 GRO1417', 'Cserép, tálca ág – Műanyag tálca, árapály asztal', ['Hidropóniás rendszer'], 'Laza', 'Dán tálca – árasztásos (ebb & flow) rendszer'),
 ('GRO1841 GRO1845 GRO1847 GRO1848 GRO1990 GRO4369 GRO4370', 'Levegőztető pumpa, porlasztókő', [], 'Erős', 'Légpumpa'),
 ('GRO1628 GRO1629 GRO1851 GRO1853 GRO1854 GRO1855 GRO2365 GRO2366 GRO2631', 'Levegőztető pumpa, porlasztókő', [], 'Erős', 'Porlasztókő'),
 ('GRO1084 GRO1736 GRO2630 GRO2625 GRO2628 GRO1763', 'Levegőztető pumpa, porlasztókő', [], 'Laza', 'Levegőztető cső, elosztó, idom'),
 ('GRO1406 GRO2349 GRO2850 GYUJTO0319', 'Agyaggolyó, hidrokosár', [], 'Erős', 'Agyaggolyó – a Közegek ágban is'),
 ('GRO0663 GRO1291 GRO4309 GRO3378 GRO0801 GRO2584', 'Agyaggolyó, hidrokosár', [], 'Erős', 'Hidrokosár, neoprén korong'),
 ('GRO3348 GRO3349 GRO3350', 'Agyaggolyó, hidrokosár', [], 'Laza', 'Venti Pot hidro cserép'),
 ('GRO2107 GRO2497', 'Cserép, tálca ág – Virágcserép', ['Agyaggolyó, hidrokosár'], 'Laza', 'Lyukacsos szögletes cserép, hidropóniához is'),
 ('GRO2515 GRO4263 GRO4264 GRO4265 GRO4269 GRO3746', 'Tápoldat-adagoló, vízhűtő', [], 'Erős', 'Perisztaltikus adagoló, hidro vezérlő'),
 ('GRO2624 GRO1992 GRO1993', 'Tápoldat-adagoló, vízhűtő', [], 'Erős', 'Hailea vízhűtő (chiller)'),
 ('GRO0810 GRO1408', 'Automata öntözőrendszer', [], 'Erős', 'Automata öntözőrendszer, öntözési időzítő'),
 ('GRO2939', 'Palántanevelő ág – Propagátor', ['Automata öntözőrendszer'], 'Laza', 'Önöntöző propagátor'),
 ('GRO1252 GRO1328 GRO1329 GRO1330 GRO1331 GRO1332 GRO1849 GRO1850 GRO1994', 'Vízpumpa, keringető szivattyú', [], 'Erős', 'Merülő keringető szivattyú'),
 ('GRO1958 GRO2244 GRO2637 GRO2638', 'Víztartály, tápoldattartály', [], 'Erős', 'FlexiTank összecsukható víztartály'),
 ('GRO1812', 'Víztartály, tápoldattartály', [], 'Laza', 'Esővízgyűjtő tartály'),
 ('GRO0811 GRO0812 GRO0813 GRO4128 GRO4576', 'Kézi és pumpás permetező', [], 'Erős', 'Kézi / pumpás permetező, porlasztófej'),
 ('GRO0798 GRO1248 GRO2395 GRO2396 GRO2397', 'Vízszűrő, fordított ozmózis', [], 'Erős', 'Fordított ozmózisos víztisztító'),
 ('GRO1249 GRO1250 GRO2777', 'Vízszűrő, fordított ozmózis', [], 'Erős', 'Szűrőbetét, RO membrán'),
]
