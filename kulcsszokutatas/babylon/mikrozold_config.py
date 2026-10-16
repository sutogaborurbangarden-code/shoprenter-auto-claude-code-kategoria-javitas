# Babylon – Mikrozöld termesztés (új főkategória, 2026-10-16)
# Csak a FŐKATEGÓRIA NEVE alapján + élő termékkínálat + kulcsszóadat.
# Döntés (2026-10-09): Mikrozöld = hub főkategória (rövid + hosszú leírás, csempék);
# valódi alkategória ott, ahol saját keresés van.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

MAG='Mikrozöld mag, csíramag'; BRO='Brokkoli csíramag'; RET='Retek csíramag'; BOR='Borsó és napraforgó mikrozöld mag'; ZSA='Zsázsa mag'
CSI='Csíráztató: üveg, tál, torony'; TAL='Mikrozöld tálca'; LAP='Termesztőlap: juta, kenderrost, kókusz'
LED='Mikrozöld LED lámpa'

CATS = [
 dict(name=MAG, sheet='1 Mikrozöld mag', fo='mikrozöld mag',
      area='Csíráztatásra és mikrozöld nevelésre szánt mag (200 g-os és bio kiszerelés): retek, brokkoli, borsó, napraforgó, zsázsa, lucerna, mustár, cékla, vöröskáposzta…',
      place='2. szint – a hub legnagyobb termékköre (~45 élő termék); fajta = 3. szint, ahol van saját keresés, a többi szűrő',
      note='Csíra magok 320, mikrozöld mag 170, mikrozöld magok 170, csíráztató mag 170, csíra mag 90. A „lucerna vetőmag” (1300) és a „bíborhere” (1900) mezőgazdasági vetőmag / takarmány – LN.',
      kws='''mikrozöld mag|S|F
mikrozöld magok|S|S
csíra magok|S|S
csíráztató mag|S|S
csíráztató magok|S|S
csíra mag|S|E
csíramag vásárlás|S|E
csíra vásárlás|S|E
bio csíra|S|E
csíra fajták|S|I
lucerna csíra|S|E
lucerna mag|L|E
bíborhere csíra|S|E
bíborhere mag|L|E
mungóbab csíra|S|E
póréhagyma csíra|S|E
cékla csíra|S|E
cékla mikrozöld|S|E
mustármag csíra|S|E
petrezselyem csíra|S|E
lucerna csíra hatása|L|I
mungóbab csíra hatásai|L|I
lucerna vetőmag|LN|N
bíborhere|LN|N
dm csíra|X|X'''),
 dict(name=BRO, sheet='2 Brokkoli', fo='brokkoli csíra', area='Brokkoli csíramag (bio és 200 g)', place='3. szint a „Mikrozöld mag” alatt – erős saját keresés',
      note='Brokkoli csíra 720, brokkoli csira 170, brokkolicsira 170, brokkoli mag 140 (vegyes – kerti vetőmag is).',
      kws='''brokkoli csíra|S|F
brokkoli csira|S|E
brokkolicsira|S|E
brokkoli csíráztatás|S|E
brokkoli mikrozöld|S|E
brokkoli mag|L|E'''),
 dict(name=RET, sheet='3 Retek', fo='retek csíra', area='Retek csíramag (retek, fekete retek, vörös korall, sango)', place='3. szint a „Mikrozöld mag” alatt',
      note='Retek csíra 590, retekcsira 590, retek csíra hatása 140 (I), retekmag csíra 70, retek mikrozöld 30. A „retek mag” (110) kerti vetőmag is – laza.',
      kws='''retek csíra|S|F
retekcsira|S|S
retekmag csíra|S|E
retek mikrozöld|S|E
retek csíra hatása|L|I
retek mag|L|E'''),
 dict(name=BOR, sheet='4 Borsó, napraforgó', fo='borsó csíra', area='Salátaborsó, zöldborsó, napraforgó mikrozöld mag – „hajtás” típusú mikrozöld', place='3. szint a „Mikrozöld mag” alatt',
      note='Borsó csíra 260, zöldborsó csíra 90, napraforgó csíra 70, borsó mikrozöld 40, napraforgó mikrozöld 20.',
      kws='''borsó csíra|S|F
zöldborsó csíra|S|S
napraforgó csíra|S|S
borsó mikrozöld|S|E
napraforgó mikrozöld|S|E'''),
 dict(name=ZSA, sheet='5 Zsázsa', fo='kerti zsázsa', area='Zsázsa (kerti zsázsa) mag – bio és 200 g', place='3. szint a „Mikrozöld mag” alatt',
      note='Kerti zsázsa 480, kerti zsázsa mag 50. A „zsázsa” (1600) a növény / recept – laza.',
      kws='''kerti zsázsa|S|F
kerti zsázsa mag|S|S
zsázsa|L|S'''),
 dict(name=CSI, sheet='6 Csíráztató', fo='csíráztató',
      area='Csíráztató üveg szűrős tetővel, csíráztató tál, többemeletes csíráztató torony',
      place='2. szint – a hub legerősebb termékszava (csíráztató 1300, csíráztató edény 1000)',
      note='Csíráztató 1300, csíráztató edény 1000, csíráztató edények 1000, csíráztató üveg 720, csíráztató tál 390, csiraztato 320, csíráztató szett 110. Csíráztatás-tartalom: csíráztatás 880, csíráztatás otthon 260.',
      kws='''csíráztató|S|F
csíráztató edény|S|S
csíráztató edények|S|S
csíráztató üveg|S|S
csíráztató tál|S|S
csiraztato|S|E
csíráztató szett|S|S
csíráztató üveg szett|S|E
mikrozöldség csíráztató|S|E
üveg csíráztató|S|E
csíráztató gép|S|E
csíráztatás|S|I
csíráztatás otthon|S|I
csíráztatás házilag|S|I
csíráztatás folyamata|S|I
mag csíráztatás|S|I
magok csíráztatása|S|I
csíráztató edény házilag|L|I
ikea csíráztató|X|X'''),
 dict(name=TAL, sheet='7 Mikrozöld tálca', fo='mikrozöld tálca',
      area='Lyukas és lyuk nélküli mikrozöld (dupla) tálca – Garland Microgreens, magvető tálca',
      place='2. szint', note='Mikrozöld tálca 70 – kicsi, de tiszta szándék. Fedél / propagátor: a Propagátor ágban (link).',
      kws='''mikrozöld tálca|S|F'''),
 dict(name=LAP, sheet='8 Termesztőlap', fo='kenderrost lap',
      area='Föld nélküli mikrozöld közeg: juta lap / háló, kenderrost termesztőlap, kókuszrost szőnyeg, Jiffy kókusz szaporítólap, szilikon háló',
      place='2. szint – a mikrozöld saját „közege” (a Termesztő közeg ágból link)',
      note='Kenderrost lap 70; a többi lap-típusra nincs mérhető keresés – a kategória fő szava a „kenderrost lap”, leírásban juta / kókusz.',
      kws='''kenderrost lap|S|F'''),
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'Mikrozöld 880, mikrozöldek 320, mikrozöld termesztés 210, microgreens 170 – a „Mikrozöld termesztés” menünév jó; H1: „Mikrozöld termesztés – mag, csíráztató, tálca”.', '''mikrozöld|S
mikrozöldek|S
mikrozöld termesztés|S
microgreens|S
mikrozold|S
mikrozöldek termesztése|S'''),
 ('Mag', '→ Mikrozöld mag (3. szint: brokkoli, retek, borsó / napraforgó, zsázsa)', '''mikrozöld mag|S
csíra magok|S
brokkoli csíra|S
retek csíra|S'''),
 ('Eszköz', '→ Csíráztató; Mikrozöld tálca; Termesztőlap', '''csíráztató|S
csíráztató üveg|S
mikrozöld tálca|S
kenderrost lap|S'''),
 ('Tudás (tartalom)', 'Hub-leírás, blog: csíráztatás lépései', '''csíráztatás|S
csíra|S
csíráztatás otthon|S'''),
]

EXT = [
 ('Búzafű (egészség, étrend-kiegészítő)', 'Nagy, de táplálékkiegészítő szándék (kapszula, por) – csak a búzafű mag / termesztés tartalom', '''búzafű|L
búzafű mire jó|LN
búzafű kapszula|LN
búzafű mag|S
búzafű termesztése|S'''),
 ('Paprika / paradicsom mag csíráztatása', 'Palántanevelési szándék – a Chillitermesztés és a Propagátor ág tartalma', '''paprika mag csíráztatása|L
paradicsom mag csíráztatása|L'''),
 ('Mezőgazdasági vetőmag (lucerna, bíborhere)', 'Takarmány / zöldtrágya – nem célozni', '''lucerna vetőmag|LN
bíborhere|LN'''),
 ('Beltéri kert, okos virágcserép', 'Urban Garden konyhakert – rokon termékkör, bővítés', '''okos virágcserép|L
smart garden|L'''),
 ('Mikrozöld fény, propagátor', 'Céloldal a LED / Propagátor ágban – a hubról csempe-link', '''palántanevelő lámpa|L
mini üvegház|L'''),
]

MAKERS = '''ikea csíráztató
dm csíra'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Mikrozöld termesztés (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Kiindulás: a főkategória neve („Mikrozöld termesztés”), az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. A 2026-10-09-i döntés szerint hub főkategória. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'Mikrozöld termesztés'
STRUCT = [
 (1, FO, '–', 'mikrozöld', 'S', 'Hub főkategória', 'Mikrozöld 880 – rövid + hosszú leírás, csempék a 2. szintű kategóriákra.', None),
 (2, MAG, FO, 'mikrozöld mag', 'S', 'Önálló kategória', 'A legtöbb termék; fajta = 3. szint / szűrő.', MAG),
 (3, BRO, MAG, 'brokkoli csíra', 'S', 'Önálló kategória', 'Brokkoli csíra 720.', BRO),
 (3, RET, MAG, 'retek csíra', 'S', 'Önálló kategória', 'Retek csíra 590, retekcsira 590.', RET),
 (3, BOR, MAG, 'borsó csíra', 'S', 'Önálló kategória', 'Borsó csíra 260, napraforgó csíra 70.', BOR),
 (3, ZSA, MAG, 'kerti zsázsa', 'S', 'Önálló kategória', 'Kerti zsázsa 480.', ZSA),
 (2, CSI, FO, 'csíráztató', 'S', 'Önálló kategória', 'Csíráztató 1300, csíráztató edény 1000.', CSI),
 (2, TAL, FO, 'mikrozöld tálca', 'S', 'Önálló kategória', 'Mikrozöld tálca 70.', TAL),
 (2, LAP, FO, 'kenderrost lap', 'S', 'Önálló kategória', 'Föld nélküli mikrozöld közeg.', LAP),
 (2, LED, FO, None, '-', 'Navigációs kategória (szűrt lista)', 'A „mikrozöld lámpa” keresés 20 alatti – a 2026-10-09-i döntés szerint navigációs; céloldal a LED / Propagátor ágban.', None),
]
NOT_CATS = [
 ('Minden magfajta külön kategóriában', 'lucerna csíra', 'Csak ahol saját keresés van (brokkoli, retek, borsó / napraforgó, zsázsa) – a többi fajta szűrő.'),
 ('Búzafű kategória', 'búzafű', 'Egészség / étrend-kiegészítő szándék; a búzafű mag a Mikrozöld mag alatt.'),
 ('Mikrozöld LED önálló SEO-oldallal', None, 'Nincs mérhető keresés – navigációs szűrt lista.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A fajta szerinti 3. szintű kategóriák termékei elsődlegesen a fajta-kategóriában, másodlagosan a „Mikrozöld mag” kategóriában is szerepelnek.',
]
TITLE = 'babylon-grow.eu – Mikrozöld termesztés kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítások: a téma erős – mikrozöld 880, csíráztató 1300, csíráztató edény 1000, csíra 1000, csíráztatás 880, brokkoli csíra 720, retek csíra 590, kerti zsázsa 480. A „Mikrozöld termesztés” menünév jó (mikrozöld termesztés 210).',
 'Szerkezet: hub főkategória (döntés 2026-10-09), 2. szint: Mag, Csíráztató, Tálca, Termesztőlap (+ navigációs LED); 3. szint csak a saját kereséssel rendelkező magfajtáknak.',
 'A „búzafű” (720) és a „csíra” (1000) jórészt egészség / étkezés szándék – a hub-leírásban és blogban kiszolgálandó, nem kategóriával.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'A keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Tartalom, kereszt-linkek, bővítés és nem célzott témák.'
MAKERS_TITLE = 'Márka- / bolt-keresések'

PRODUCTS = [
 ('GRO4433 GRO4390 GRO4399', BRO, [MAG], 'Erős', 'Brokkoli csíramag'),
 ('GRO4447 GRO4446 GRO4394 GRO4398 GRO4449 GRO4448', RET, [MAG], 'Erős', 'Retek csíramag (retek, fekete, vörös korall, sango)'),
 ('GRO4395 GRO4396 GRO4456 GRO4443 GRO4387', BOR, [MAG], 'Erős', 'Borsó, napraforgó mikrozöld mag'),
 ('GRO4457 GRO4400 GRO4385', ZSA, [MAG], 'Erős', 'Zsázsa mag'),
 ('GRO4440 GRO4431 GRO4432 GRO4397 GRO4389 GRO4434 GRO4439 GRO4392 GRO4442 GRO4388 GRO4444 GRO4393 GRO4445 GRO4450 GRO4451 GRO4441 GRO4391 GRO4452 GRO4386 GRO4453 GRO4454 GRO4455', MAG, [], 'Erős', 'Mikrozöld mag (egyéb fajták: lucerna, búza, cékla, mustár, rukkola, lencse…)'),
 ('GRO4435 GRO4436 GRO4437 GRO4382 GRO4383 GRO4438 GRO4384', CSI, [], 'Erős', 'Csíráztató üveg, tál, torony'),
 ('GRO3661 GRO3662 GRO4358 GRO4359 GRO4636 GRO4637', TAL, [], 'Erős', 'Mikrozöld tálca, magvető tálca'),
 ('GRO4356 GRO4357 GRO4460 GRO4746 GRO4463/1 GRO4675 GRO4504', LAP, [], 'Erős', 'Juta, kenderrost, kókusz termesztőlap, szilikon háló'),
 ('GRO4589 GRO4590 GRO4591 GRO4592 GRO4593 GRO4594 GRO4596 GRO4597 GRO4598', 'LED ág – Szobanövény-lámpa / LED sáv', [LED], 'Más főkategória', 'Kis LED mikrozöld polcra – céloldal a LED ágban'),
 ('GRO4097 GRO4098', 'Propagátor ág – Palántanevelő LED lámpa', [LED], 'Más főkategória', 'Urban Garden Clone LED'),
 ('GRO0804 GRO2798 GRO3262', 'Propagátor ág – Propagátor, mini üvegház', [TAL], 'Más főkategória', 'Fűtés nélküli propagátor csíráztatáshoz'),
 ('GRO2943', 'Beltéri kert', [LED], 'Más főkategória', 'Urban Garden konyhakert LED-del'),
]
