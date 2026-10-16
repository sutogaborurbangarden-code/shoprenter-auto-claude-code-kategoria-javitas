# Babylon – pH mérő, TDS mérő, refraktométer (2026-10-16)
# Csak a FŐKATEGÓRIA NEVE alapján: a korábbi pH/EC kutatás kategórianevei és szerkezete figyelmen kívül;
# alkategóriák az élő termékkínálat és a kulcsszóadat alapján.
# Kulcsszóadat: friss lekérés (2026-10-16) + a 2026-10-06-i pH/EC kutatás Kulcsszótervező-adatai (ami frissen nem jött vissza).
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

PH='pH mérő'; EC='EC és TDS mérő'; KOMB='Kombinált pH és EC mérő'; TAL='Talajmérő: talaj pH, EC, nedvesség'
MON='pH / EC monitor és szabályozó'; KAL='Kalibráló, tároló és tisztító folyadék'; SZO='pH és EC szonda, csereelektróda'
TES='pH teszt: lakmuszpapír, cseppteszt'; REF='Refraktométer, Brix mérő'; PHF='pH-szabályozó folyadék (pH+ / pH−)'

CATS = [
 dict(name=PH, sheet='1 pH mérő', fo='ph mérő',
      area='Digitális kézi / zseb pH mérő és teszter tápoldathoz, öntözővízhez (Milwaukee, ADWA, Aqua Master, Bluelab, Aquatek)',
      place='2. szint – a termékkör legnagyobb kulcsszava; a főkategória ennek gyűjtőoldala (H1-ben a pH, EC/TDS és refraktométer együtt)',
      note='Ph mérő 1900, digitális ph mérő 480, ph teszter 480, víz ph mérő 260, ph mérő műszer 170. A medencés (480 / 320) és cefre (140) szándék ugyanaz a műszer – laza, felhasználás szerinti szűrő / tartalom. Áruházi keresések (obi, praktiker, lidl) – X.',
      kws='''ph mérő|S|F
ph merő|S|E
digitális ph mérő|S|S
ph teszter|S|S
ph mérő műszer|S|S
víz ph mérő|S|S
ph érték mérő|S|S
ph érték mérés|S|E
elektromos ph mérő|S|E
ph mérő digitális|S|E
ph mérő készülék|S|E
ph szint mérő|S|E
ph mérés|S|I
ph mérése|S|I
ph mérő használata|S|I
cefre ph mérő|L|E
ph mérő cefréhez|L|E
digitális ph mérő cefréhez|L|E
medence ph mérő|L|E
ph mérő medencéhez|L|E
jakuzzi ph mérő|L|E
adwa ph mérő|S|G
milwaukee ph mérő|S|G
hanna ph mérő|X|X
ad12 ph mérő|S|G
ad11 ph mérő|S|G
adwa ad12 ph mérő|S|G
obi ph mérő|X|X
praktiker ph mérő|X|X
ph mérő obi|X|X
lidl ph mérő|X|X'''),
 dict(name=EC, sheet='2 EC TDS mérő', fo='tds mérő',
      area='EC (vezetőképesség) és TDS / ppm mérő a tápoldat töménységéhez (Milwaukee, ADWA, Aqua Master, Bluelab Truncheon, Aquatek)',
      place='2. szint – a főkategória-név második eleme',
      note='Tds mérő 590, ec mérő 210, vezetőképesség mérő 70, ppm mérő 50. A „vízminőség mérő” (260) ivóvizes szándékú is – laza.',
      kws='''tds mérő|S|F
ec mérő|S|S
vezetőképesség mérő|S|S
ppm mérő|S|S
vízminőség mérő|L|S
tds mérő mire jó|S|I
tds mérő használata|S|I'''),
 dict(name=KOMB, sheet='3 Kombinált mérő', fo='ec ph mérő',
      area='Egy készülékben pH + EC / TDS (+ hőmérséklet) – Bluelab OnePen / Combo, Aqua Master P110 / P160 / H600, AC Infinity',
      place='2. szint – sok termék (kezdők legjobb választása), kis keresés',
      note='Ec ph mérő 30, ph ec mérő 30 – a vásárlók külön keresik a pH-t és az EC-t; a kombinált mérő kategória mindkét lapról kereszt-linket kap.',
      kws='''ec ph mérő|S|F
ph ec mérő|S|S
bluelab|S|G
aqua master|S|G'''),
 dict(name=TAL, sheet='4 Talajmérő', fo='talaj ph mérő',
      area='Talajba szúrható pH-, EC- és nedvességmérő, talajteszter (Aquatek 3in1 / 4in1, Aqua Master S300 / E300 / H600 talaj, Bluelab Pulse, AC Infinity)',
      place='2. szint – erős saját szándék (talaj ph mérő 590, talajnedvesség mérő 480)',
      note='Talaj ph mérő 590, talajnedvesség mérő 480, talaj ph mérés 110, föld ph mérő 90, talaj ec mérő 40. A „nedvességmérő” (720) fal / fa nedvessége – LN.',
      kws='''talaj ph mérő|S|F
talajnedvesség mérő|S|S
talaj ph mérés|S|S
föld ph mérő|S|S
talaj nedvesség mérő|S|E
talaj ec mérő|S|S
digitális talajnedvesség mérő|S|E
talaj ph érték mérő|S|E
talajmérő készülék|S|E
talajteszter|S|E
talaj ph mérő tesztcsík|S|E
talaj ph mérő obi|X|X
nedvességmérő|LN|N'''),
 dict(name=MON, sheet='5 Monitor, szabályozó', fo='ph adagoló',
      area='Folyamatos pH / EC monitor, Wi-Fi monitor (Bluelab Guardian), pH szabályozó + adagolópumpa (Milwaukee MC122, Bluelab Pro, Aqua Master C800)',
      place='2. szint – hidro / professzionális vásárlóknak; a Hidropónia ágban kereszt-link',
      note='Kicsi, de vásárlásközeli: ph adagoló 30, ph szabályozó 30, automata ph adagoló 20, ph monitor 10, ph controller 10.',
      kws='''ph adagoló|S|F
ph szabályozó|S|S
automata ph adagoló|S|S
ph monitor|S|E
ph controller|S|E'''),
 dict(name=KAL, sheet='6 Kalibráló folyadék', fo='ph kalibráló folyadék',
      area='pH 4 / 7 / 10 és EC 1413 / 12,88 kalibráló folyadék és por, KCl tároló folyadék, elektródatisztító, karbantartó készlet',
      place='2. szint – sok termék, ismétlődő vásárlás (utánrendelés)',
      note='Ph kalibráló folyadék 70, ph mérő kalibrálás(a) 110 + 110 (kérdés – tartalommal), pufferoldat 50, ph mérő kalibráló folyadék 40.',
      kws='''ph kalibráló folyadék|S|F
ph mérő kalibráló folyadék|S|S
pufferoldat|S|S
kalibráló folyadék|S|E
ph kalibráló por|S|E
kalibráló oldat|S|E
ph mérő kalibrálás|S|I
ph mérő kalibrálása|S|I
digitális ph mérő kalibrálása|S|I'''),
 dict(name=SZO, sheet='7 Szonda', fo='ph szonda',
      area='Csereszonda / elektróda pH és EC mérőkhöz és monitorokhoz (Milwaukee, ADWA, Aqua Master, Bluelab)',
      place='2. szint (kiegészítő) – a mérő típusa szerint szűrve',
      note='Ph szonda 50, ph elektróda 20, ph mérő szonda 10, elektródás ph mérő 10.',
      kws='''ph szonda|S|F
ph elektróda|S|S
ph mérő szonda|S|E
elektródás ph mérő|S|E'''),
 dict(name=TES, sheet='8 pH teszt', fo='lakmuszpapír',
      area='Olcsó, gyors pH-mérés: lakmuszpapír / pH tesztcsík, cseppteszt (Terra Aquatica pH test kit)',
      place='2. szint – a második legnagyobb klaszter (lakmuszpapír 1000, ph teszt 480, ph tesztcsík 480)',
      note='Lakmuszpapír 1000, ph teszt 480, ph tesztcsík 480, lakmusz papir 210, lakmuszpapír hol kapható 170. Az egészségügyi (hüvely ph teszt 210) és a drogériás (ph tesztcsík dm 140) keresés nem ide – LN / X.',
      kws='''lakmuszpapír|S|F
ph teszt|S|S
ph tesztcsík|S|S
lakmusz papir|S|E
lakmuszpapir|S|E
lakmuszpapír hol kapható|S|E
lakmuszpapír vásárlás|S|E
ph mérő papír|S|E
ph mérő tesztcsík|S|E
ph mérő csík|S|E
lakmuszpapír használata|S|I
vízelemző tesztcsík|L|E
medence tesztcsík|LN|N
hüvely ph teszt|LN|N
ph tesztcsík dm|X|X'''),
 dict(name=REF, sheet='9 Refraktométer', fo='refraktométer',
      area='Digitális és optikai refraktométer – Brix (növénynedv, gyümölcs), cefre, méz, alkohol',
      place='2. szint – a főkategória-név harmadik eleme; nagy keresés, kevés termék (bővíthető)',
      note='Refraktométer 1300, brix mérő 170, brix refraktométer 70, alkohol refraktométer 70, digitális refraktométer 50 – a keresés nagy része cefre / bor / méz (laza), de ugyanaz a műszer.',
      kws='''refraktométer|S|F
brix mérő|S|S
brix refraktométer|S|S
refraktométer brix|S|E
digitális refraktométer|S|S
optikai refraktométer|S|E
atc refraktométer|S|E
refraktométer cukortartalom|S|E
refraktométer ár|S|E
refraktométer kalibrálása|S|I
refraktométer kalibráló folyadék|S|E
alkohol refraktométer|L|E
refraktométer alkohol|L|E
cefre refraktométer|L|E
borászati refraktométer|L|E
méz refraktométer|L|E'''),
 dict(name=PHF, sheet='10 pH+ pH−', fo='ph csökkentő',
      area='pH-csökkentő és pH-emelő folyadék a tápoldat beállításához (Plagron pH min / plus, BioNova, Advanced Hydroponics)',
      place='2. szint – a mérés utáni „beavatkozás”; vagy a Tápok ágban (egy céloldal, a másik helyen link)',
      note='Ph csökkentő 260, ph plusz 140, ph csökkentő folyadék 70. A „ph minusz” (210) és a „minuszaph” (40) jórészt medencevegyszer – laza / X.',
      kws='''ph csökkentő|S|F
ph plusz|S|S
ph csökkentő folyadék|S|S
ph minusz|L|E
ph mínusz|L|E
ph emelő|S|E
ph down|S|E
ph up|S|E
ph le|L|E
minuszaph|X|X'''),
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'A menünév jó: a három fő műszer (ph mérő 1900, refraktométer 1300, tds mérő 590). H1-javaslat: „pH mérő, EC / TDS mérő és refraktométer”.', '''ph mérő|S
refraktométer|S
tds mérő|S
ec mérő|S'''),
 ('Folyadék mérése', '→ pH mérő; EC és TDS mérő; Kombinált mérő', '''ph mérő|S
tds mérő|S
ec ph mérő|S'''),
 ('Talaj mérése', '→ Talajmérő', '''talaj ph mérő|S
talajnedvesség mérő|S'''),
 ('Automatizálás', '→ Monitor és szabályozó', '''ph adagoló|S
ph szabályozó|S'''),
 ('Karbantartás', '→ Kalibráló folyadék; Szonda', '''ph kalibráló folyadék|S
ph szonda|S'''),
 ('Olcsó gyorsteszt', '→ pH teszt', '''lakmuszpapír|S
ph tesztcsík|S'''),
 ('Cukortartalom', '→ Refraktométer', '''refraktométer|S
brix mérő|S'''),
 ('pH beállítása', '→ pH-szabályozó folyadék', '''ph csökkentő|S
ph plusz|S'''),
]

EXT = [
 ('Medence (pH, klór)', 'Nagy kereslet, más szándék – a pH mérő lapon felhasználási tartalom; klórmérő csak kínálatbővítéssel', '''medence ph mérő|L
ph mérő medencéhez|L
medence teszter|L
digitális klór és ph mérő|L
ph és klór mérő|L
klór mérő|L
szabad klór mérő|L
medence tesztcsík|LN'''),
 ('Cefre, bor, méz', 'Refraktométer / pH mérő felhasználási tartalom (landing / blog)', '''cefre ph mérő|L
alkohol refraktométer|L
méz refraktométer|L'''),
 ('Ivóvíz, vízminőség', 'Tartalom + a TDS mérő leírásában', '''vízminőség mérő|L
víz ph mérő|S
vízkeménység mérő|LN'''),
 ('Fal / fa nedvessége', 'Nem a mi termékünk', '''nedvességmérő|LN'''),
 ('Egészség (vizelet, hüvely pH)', 'YMYL egészségügyi téma – nem célozni', '''hüvely ph teszt|LN'''),
]

MAKERS = '''adwa ph mérő
milwaukee ph mérő
hanna ph mérő
ad12 ph mérő
ad11 ph mérő
adwa ad12 ph mérő
bluelab
aqua master'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – pH mérő, TDS mérő, refraktométer (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A korábbi pH/EC kutatás kategórianeveit és szerkezetét NEM vettük figyelembe. Kiindulás: a főkategória neve, az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'pH mérő, TDS mérő, refraktométer'
STRUCT = [(1, FO, '–', 'ph mérő műszer', 'S', 'Főkategória (gyűjtőoldal)', 'A „ph mérő” (1900) céloldala a pH mérő alkategória; a főkategória gyűjtőoldal a „ph mérő műszer” (170) / „vízminőség mérő” szavakra.', None)] + [
 (2, PH, FO, 'ph mérő', 'S', 'Önálló kategória', 'Ph mérő 1900 – a legerősebb kulcsszó.', PH),
 (2, EC, FO, 'tds mérő', 'S', 'Önálló kategória', 'Tds mérő 590, ec mérő 210.', EC),
 (2, KOMB, FO, 'ec ph mérő', 'S', 'Önálló kategória', 'Sok termék, kis keresés – kereszt-link a pH és EC lapról.', KOMB),
 (2, TAL, FO, 'talaj ph mérő', 'S', 'Önálló kategória', 'Talaj ph mérő 590, talajnedvesség mérő 480.', TAL),
 (2, MON, FO, 'ph adagoló', 'S', 'Önálló kategória', 'Professzionális / hidro vásárló.', MON),
 (2, KAL, FO, 'ph kalibráló folyadék', 'S', 'Önálló kategória', 'Utánrendelés; kalibrálás-tartalom (110 + 110).', KAL),
 (2, SZO, FO, 'ph szonda', 'S', 'Kiegészítő kategória', 'Csereszonda a mérő típusa szerint.', SZO),
 (2, TES, FO, 'lakmuszpapír', 'S', 'Önálló kategória', 'Lakmuszpapír 1000, ph teszt / tesztcsík 480.', TES),
 (2, REF, FO, 'refraktométer', 'S', 'Önálló kategória', 'Refraktométer 1300 – kevés termék, bővítési lehetőség.', REF),
 (2, PHF, FO, 'ph csökkentő', 'S', 'Önálló kategória vagy Tápok ág', 'Ph csökkentő 260, ph plusz 140.', PHF),
]
NOT_CATS = [
 ('Felhasználás szerinti alkategória (medence, cefre, méz, alkohol pH mérő / refraktométer)', 'medence ph mérő', 'Ugyanaz a műszer – felhasználási szűrő / tartalom, nem külön kategória.'),
 ('Vízkeménység mérő', 'vízkeménység mérő', 'Nincs ilyen termék (720 – háztartási).'),
 ('Nedvességmérő (fal, fa)', 'nedvességmérő', 'Építőipari szándék.'),
 ('Márka szerinti alkategória', 'adwa ph mérő', 'Kis márkakeresés – márkaszűrő.'),
 ('Hő- és páratartalom-mérő', None, 'A Légtechnika ágban (Klíma) – itt link.'),
 ('PAR-mérő', None, 'A LED ágban – itt link.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A szerkezet csak a főkategória nevéből, a termékek típusából és a keresési szándékból készült – a korábbi pH/EC kutatás kategórianevei figyelmen kívül.',
 'Kombinált pH + EC mérők elsődlegesen a Kombinált mérő kategóriában, másodlagosan a pH és az EC kategóriában is.',
]
TITLE = 'babylon-grow.eu – pH mérő, TDS mérő, refraktométer kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), friss lekérés: 2026-10-16; ahol a friss lekérés nem adott értéket, a 2026-10-06-i pH/EC kutatás Kulcsszótervező-adata. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: csak a főkategória neve adott; az alkategóriák a mért jellemző (pH, EC / TDS, kombinált, talaj, Brix), a felhasználás módja (kézi mérő, monitor / szabályozó, gyorsteszt) és a kiegészítők (kalibráló folyadék, szonda, pH+ / pH−) szerint épülnek.',
 'Fő megállapítások: ph mérő 1900, refraktométer 1300, lakmuszpapír 1000, talaj ph mérő 590, tds mérő 590 – a menünév három eleme valóban a három legnagyobb műszer-keresés. A talajmérő és a pH teszt (lakmuszpapír) erős önálló szándék.',
 'Refraktométerből csak 1 élő termék van, a keresés viszont 1300 – kínálatbővítési lehetőség (optikai Brix-refraktométer).',
 'A medence- (ph mérő medencéhez 320, medence teszter 210) és cefre-szándék ugyanaz a műszer – felhasználási tartalommal, nem külön kategóriával.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a korábbi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más felhasználási területek: tartalom, kínálatbővítés vagy kizárás.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO2086 GRO2093 GRO2092 GRO1016 GRO2181 GRO2948 GRO3954 GRO4318 GRO3957 GRO4219 GRO1857 GRO1428 GRO4546 GRO1426 GRO3151 GRO3282 GRO4311 GRO4520', PH, [], 'Erős', 'Digitális pH mérő / teszter'),
 ('GRO4550', PH, [], 'Laza', 'Milwaukee FOOD PRO+ élelmiszer pH mérő'),
 ('GRO2174 GRO2196 GRO3374 GRO3955 GRO4317 GRO2935 GRO3336 GRO3281 GRO3152 GRO1427 GRO4506 GRO1429 GRO2129', EC, [], 'Erős', 'EC / TDS / ppm mérő'),
 ('GRO3959 GRO3956 GRO4319 GRO4248 GRO3961 GRO3531 GRO4006 GRO4005', KOMB, [PH, EC], 'Erős', 'Kombinált pH + EC (+ TDS, hőmérséklet) mérő, starter pack'),
 ('GRO3960 GRO3958 GRO4573 GRO2466 GRO2467 GRO4341 GRO3462', TAL, [], 'Erős', 'Talaj pH / EC / nedvesség mérő, talajteszter'),
 ('GRO4281', TAL, [], 'Laza', '9V elem a talajteszterhez'),
 ('GRO1015 GRO1026 GRO3900 GRO4007 GRO4008 GRO4009 GRO3373 GRO1551 GRO2514 GRO4262 GRO3744', MON, [], 'Erős', 'pH / EC monitor, Wi-Fi monitor, pH szabályozó (szett)'),
 ('GRO2515 GRO4263 GRO4264 GRO4265', 'Hidropónia ág – Tápoldat-adagoló pumpa', [MON], 'Más főkategória', 'Perisztaltikus adagolópumpa – céloldal a Hidropónia ágban'),
 ('GRO4249 GRO4251 GRO4252 GRO3964 GRO3965 GRO3969 GRO4256 GRO4257 GRO4258 GRO4255 GRO4253 GRO4254 GRO3967 GRO3966 GRO3933 GRO3934 GRO3935 GRO3678 GRO3679 GRO3449 GRO1145 GRO2095 GRO0609 GRO2096 GRO0600 GRO2636 GRO0602 GRO2062 GRO0601 GRO2063 GRO3575 GRO2934', KAL, [], 'Erős', 'pH / EC kalibráló folyadék, kalibráló por'),
 ('GRO3968 GRO4259 GRO4260 GRO1554 GRO4261 GRO1553 GRO2097 GRO3450 GRO3451', KAL, [], 'Erős', 'Tároló folyadék, elektródatisztító, karbantartó készlet'),
 ('GRO2274 GRO3923 GRO3963 GRO3962 GRO3826 GRO1552 GRO2790 GRO2180 GRO2098', SZO, [], 'Erős', 'pH / EC csereszonda, elektróda'),
 ('GRO3905 GRO4225 GRO0154 GRO3273', TES, [], 'Erős', 'Lakmuszpapír, pH tesztcsík, cseppteszt'),
 ('GRO4547', REF, [], 'Erős', 'Milwaukee MA871 digitális refraktométer'),
 ('GRO3899 GRO3898 GRO3897 GRO3918 GRO3915 GRO3917 GRO3916 GRO3914 GRO0724 GRO0725 GRO2371 GRO0680 GRO0634 GRO1012 GRO0632', PHF, ['Tápok ág'], 'Erős', 'pH+ / pH− folyadék'),
 ('GRO4549 GRO4548', 'Bővítés – klórmérő, hőmérő', [EC], 'Laza', 'Milwaukee szabadklór fotométer, digitális hőmérő'),
 ('GRO0795 GRO0796 GRO3565 GRO4271 GRO4125 GRO4126 GRO4127', 'Légtechnika ág – Hő- és páratartalom-mérő', [], 'Más főkategória', 'Hő- és páratartalom-mérő'),
 ('GRO4147 GRO4148', 'LED ág – PAR-mérő', [], 'Más főkategória', 'PAR-mérő'),
]
