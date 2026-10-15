# Babylon – Termesztő közeg (sandbox-főkategória, 2026-10-15)
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='Virágföld, termesztőföld', sheet='1 Virágföld', fo='virágföld',
      area='Előtrágyázott és szerves földkeverék (Plagron Allmix, Growmix, Batmix, Royal Mix, Promix, Lightmix)',
      place='2. szint – ÚJ (a sandboxban nincs): a kínálat nagy része földkeverék, a „virágföld” (2900) a fő vásárlói szó',
      note='A sandboxban csak „Palántaföld” van, de a földek többsége nem palántaföld. A „termőföld” (2400) kerti ömlesztett föld, a „tőzeg” (2400) tiszta tőzeg – nem célozni.',
      kws='''virágföld|S|F
virágföld 50l|S|S
tőzeges föld|S|S
tőzeg föld|S|E
50 l virágföld|S|E
általános virágföld|L|E
viragfold|S|E
tőzeges virágföld|S|S
virágföld rendelés|S|E
ültetőföld|S|E
perlit virágföld|S|E
perlites virágföld|S|E
virágföld nagy tételben|S|E
humuszos virágföld|S|E
általános földkeverék|S|E
plagron lightmix|S|G
jó minőségű virágföld|S|E
legjobb virágföld|S|E
virágföld 100l|S|E
bio virágföld|S|E
biobizz light mix|L|G
tőzegmentes virágföld|L|E
bio föld|S|E
minőségi virágföld|S|E
plagron föld|S|G
virágföld nagy kiszerelés|S|E
plagron allmix|S|G
allmix plagron|S|G
biobizz all mix|L|G
virágföld típusok|S|I
termőföld|LN|N
tőzeg|LN|N
obi virágföld|X|X
praktiker virágföld|X|X'''),
 dict(name='Palántaföld', sheet='2 Palántaföld', fo='palántaföld',
      area='Magvetéshez, palántázáshoz – könnyű, gyengén trágyázott föld',
      place='Sandbox „Palántaföld” – a kínálatban csak a Plagron Lightmix illik ide: 3. szint / szűrő a Virágföld alatt, vagy közös kategória „Virágföld, palántaföld” néven',
      note='Erős kulcsszó (palántaföld 1300, palántaföld 50l 260), de kevés termék (2 db Lightmix) – vékony oldal. A tőzegkorongok a Palántanevelő ágé.',
      kws='''palántaföld|S|F
palántaföld 50l|S|S
palánta föld|S|S
palantafold|S|E
magvető föld|S|S
legjobb palántaföld|S|E
bio palántaföld|S|E
vetőföld|S|E
palántanevelő tőzeg|S|E
palántaföld vagy virágföld|S|I
palántaföld házilag|L|I
palántaföld obi|X|X'''),
 dict(name='Kertészeti kókuszrost, kókusztégla', sheet='3 Kókuszrost', fo='kókuszrost',
      area='Kókusz termesztőközeg – zsákos, préselt tégla, paplan',
      place='2. szint – a sandbox-név jó; H1: „Kertészeti kókuszrost, kókusztégla”',
      note='Erős klaszter: kókuszrost 1000, kókuszrost tégla 720, kókusztégla 320, kertészeti kókuszrost 170. A „kókuszrost korong” a Palántanevelő ágé.',
      kws='''kókuszrost|S|F
kókuszrost tégla|S|S
kókusztégla|S|S
kertészeti kókuszrost|S|S
kokuszrost|S|E
kókuszföld|S|S
kókusz rost|S|E
kókusztégla 5 kg|S|E
kókusztégla ár|S|E
kókuszpaplan|S|E
kókusz tégla|S|E
kókuszrost ültetőközeg vásárlás|S|E
kókuszrost ültetőközeg|S|E
kókuszrost föld|S|E
kokusz rost|S|E
kókusz rost tégla|S|E
kókuszrost virágföld|S|E
kókuszrost paplan|S|E
kókuszrost termesztőközeg|S|E
préselt kókuszrost|S|E
canna coco|S|G
plagron cocos|S|G
biobizz coco mix|S|G
cocos premium|S|G
kókuszrost tégla használata|S|I
kókusztégla használata|S|I
kókuszrost használata|S|I
mire jó a kókuszrost tégla|S|I
kókuszföld használata|S|I
kókuszrost praktiker|X|X
kókuszrost tégla obi|X|X'''),
 dict(name='Kertészeti kőzetgyapot', sheet='4 Kőzetgyapot', fo='kőzetgyapot kocka',
      area='Kőzetgyapot termesztőkocka és -tábla (Grodan, Agra-Wool)',
      place='2. szint – a sandbox-név jó (a „kertészeti” előtag kell, mert a „kőzetgyapot” szigetelés)',
      note='A „kőzetgyapot” (5400) szinte teljesen építőipari szigetelés. A kertészeti keresés kicsi (kőzetgyapot kocka 40, kertészeti kőzetgyapot 20, Grodan 20) – a márkanév fontos.',
      kws='''kőzetgyapot kocka|S|F
kertészeti kőzetgyapot|S|S
grodan|S|S
grodan kőzetgyapot|S|S
grodan kocka|S|G
grodan delta|S|G
grodan paplan|S|G
grodan growcube|S|G
agra wool|S|G
kőzetgyapot termesztő kocka|S|E
kőzetgyapot palánta|S|E
kertészeti kőzetgyapot árlista|S|E
kőzetgyapot|LN|N'''),
 dict(name='Kertészeti perlit, vermikulit, agyaggolyó', sheet='5 Perlit, agyaggolyó', fo='kertészeti perlit',
      area='Talajlazító és vízmegtartó adalék – perlit, vermikulit, agyaggolyó (agyaggranulátum)',
      place='2. szint – a sandbox-név jó. Az agyaggolyó céloldala INNEN legyen (a Hidro ágban csak hidrokosár) – egy céloldal',
      note='A „perlit” (4400) jórészt építőipari (perlitbeton, vakolat) – laza. A „vermikulit” (1600) is vegyes. Az „agyaggranulátum” (590) az agyaggolyó szinonimája – a menünévbe / H1-be érdemes.',
      kws='''kertészeti perlit|S|F
perlit|LN|N
vermikulit|L|S
agyaggolyó|S|S
agyaggranulátum|S|S
kertészeti perlit ár|S|E
perlit kertészeti|S|E
duzzasztott perlit|L|E
agyaggolyó növényekhez|S|E
kertészeti perlit 100l|S|E
perlit virágföldbe|S|E
kertészeti vermikulit|S|E
perlit 100 l|S|E
agyaggolyók|S|E
kertészeti agyaggolyó|S|E
vermikulit vásárlás|S|E
perlit vásárlás|S|E
agyaggolyó 50l|S|E
hidrogolyó|S|E
agyaggolyó orchidea|L|E
orchidea agyaggolyó|L|E
perlit mire jó|S|I
kertészeti perlit használata|S|I
agyaggolyó használata|S|I
perlit használata|S|I
vermikulit használata|S|I
perlitbeton|LN|N
zeolit|LN|N
kertészeti perlit obi|X|X
perlit obi|X|X
obi agyaggolyó|X|X'''),
 dict(name='Talajjavító, gilisztahumusz', sheet='6 Talajjavító', fo='gilisztahumusz',
      area='Szerves talajjavító adalék – gilisztahumusz, denevérguanó',
      place='2. szint – ÚJ javaslat (a sandboxban nincs); vagy a Tápok főkategória szerves adalék ágában',
      note='Gilisztahumusz 320, talajjavító 210, guanó 110. A „mikorrhiza gomba” (2900) és a „trichoderma” (480) nagy keresés, de nincs ilyen termék (Bővítés lap).',
      kws='''gilisztahumusz|S|F
talajjavító|L|S
guanó|S|S
talajjavító granulátum|L|E
huminsav talajjavító|L|E
talajjavító anyagok|L|E
talajjavító szer|L|E
humusz giliszta eladó|S|E
gilisztahumusz eladó|S|E
talajjavítók|L|E
humusz giliszta|S|E'''),
]

OLD_SHEET = 'Sandbox menünevek'
OLD = [
 ('Termesztő közeg (főkategória)', 'A „termesztő közeg” (30) kicsi; az „ültetőközeg” (140) és a „szubsztrát” (140) is gyenge. Menünévnek jó, de a H1 / SEO title a keresett szavakra épüljön (virágföld, kókuszrost, perlit).', '''termesztő közeg|S
ültetőközeg|S
szubsztrát|L
közeg|LN'''),
 ('Palántaföld', 'Erős kulcsszó, de csak 2 termék (Lightmix) – javasolt: „Virágföld, palántaföld” közös kategória, vagy 3. szint', '''palántaföld|S
virágföld|S'''),
 ('Kertészeti Kókuszrost, kókusztégla', 'Marad', '''kókuszrost|S
kókusztégla|S
kókuszrost tégla|S'''),
 ('Kertészeti kőzetgyapot', 'Marad (a „kertészeti” előtag fontos)', '''kertészeti kőzetgyapot|S
kőzetgyapot kocka|S
kőzetgyapot|LN'''),
 ('Kertészeti perlit, vermikulit, agyaggolyó', 'Marad; H1-be érdemes az „agyaggranulátum” is', '''kertészeti perlit|S
vermikulit|L
agyaggolyó|S
agyaggranulátum|S'''),
]

EXT = [
 ('Mikorrhiza, trichoderma (talajélet)', 'Nagy keresés, nincs termék – kínálatbővítési lehetőség', '''mikorrhiza gomba|L
mikorrhiza|L
trichoderma|L'''),
 ('Zeolit, bioszén', 'Talajjavító ásvány / szén – csak kínálatbővítés esetén', '''zeolit|L
bioszén|L'''),
 ('Termőföld, tőzeg (ömlesztett, kerti)', 'Kerti / ömlesztett föld – nem growshop-termék', '''termőföld|LN
tőzeg|LN'''),
 ('Tőzegkorong (palántanevelés)', 'A Palántanevelő ágba – itt legfeljebb kereszt-link', '''tőzegkorong|L
jiffy tőzegkorong|L
tőzegtabletta|L'''),
]

MAKERS = '''plagron lightmix
plagron allmix
plagron föld
plagron cocos
canna coco
biobizz coco mix
biobizz light mix
biobizz all mix
grodan
agra wool'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Termesztő közeg (termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet, a Google Shopping-feed termékei (1999 db) és a Kulcsszótervező adatai. Termékszám = elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [
 (1, 'Termesztő közeg', '–', 'ültetőközeg', 'S', 'Főkategória', 'A főkategória-névre kicsi a keresés (termesztő közeg 30, ültetőközeg 140) – navigációs név; a H1 a keresett szavakra épüljön.', None),
 (2, 'Virágföld, termesztőföld', 'Termesztő közeg', 'virágföld', 'S', 'Önálló kategória (ÚJ)', 'A sandboxból hiányzik, pedig a földkeverékek (Plagron) a kínálat jelentős része, és a „virágföld” (2900) a legerősebb kulcsszó.', 'Virágföld, termesztőföld'),
 (3, 'Palántaföld', 'Virágföld, termesztőföld', 'palántaföld', 'S', 'Szűrő / 3. szint (vagy közös név)', 'Palántaföld 1300 – erős, de csak 2 termék (Lightmix). Javaslat: „Virágföld, palántaföld” közös kategória, a palántaföld H1-ben / leírásban.', 'Palántaföld'),
 (2, 'Kertészeti kókuszrost, kókusztégla', 'Termesztő közeg', 'kókuszrost', 'S', 'Önálló kategória', 'Kókuszrost 1000, kókuszrost tégla 720 – erős klaszter, sok termék.', 'Kertészeti kókuszrost, kókusztégla'),
 (2, 'Kertészeti kőzetgyapot', 'Termesztő közeg', 'kőzetgyapot kocka', 'S', 'Önálló kategória', 'Kis keresés, de egyértelmű termékkör (Grodan, Agra-Wool).', 'Kertészeti kőzetgyapot'),
 (2, 'Kertészeti perlit, vermikulit, agyaggolyó', 'Termesztő közeg', 'kertészeti perlit', 'S', 'Önálló kategória', 'Kertészeti perlit 720, agyaggolyó 880, agyaggranulátum 590, vermikulit 1600 (vegyes).', 'Kertészeti perlit, vermikulit, agyaggolyó'),
 (2, 'Talajjavító, gilisztahumusz', 'Termesztő közeg', 'gilisztahumusz', 'S', 'Önálló kategória (ÚJ, kicsi)', 'Gilisztahumusz 320, talajjavító 210, guanó 110 – 5 termék (Mega Worm, Bat Guano); a Tápok ágban is elhelyezhető.', 'Talajjavító, gilisztahumusz'),
]
NOT_CATS = [
 ('Termőföld', 'termőföld', 'Kerti ömlesztett föld – nem célozni.'),
 ('Tőzeg', 'tőzeg', 'Tiszta tőzegünk nincs (csak tőzegkorong / tőzeges föld) – a virágföld leírásában említés.'),
 ('Mikorrhiza gomba', 'mikorrhiza gomba', 'Nagy keresés, de nincs termék – kínálatbővítés.'),
 ('Tőzegkorong, magvető kocka', 'tőzegkorong', 'A Palántanevelő ág kategóriája – itt csak másodlagos hozzárendelés.'),
 ('Enzimes közegjavító (Cannazym, PowerZyme…)', None, 'A Tápok / adalékok főkategóriába valók.'),
]
PRODUCT_NOTE = [
 'Forrás: a Babylon Google Ads fiók Shopping-termékadatai (termékkód = Shopping item ID, terméknév = feed-cím), 2024-10-01 – 2026-10-14, összesen 1999 termék. A Shoprenter API és az éles oldal a felhőből nem érhető el.',
 'Figyelem: ez a Google-ben hirdetett termékkör, nem feltétlenül a teljes katalógus. A gyártó és a gyűjtőtermék (GYUJTO…) adat a feedben nem érhető el.',
 'A lapon a teljes termékkínálat szerepel: elöl a Termesztő közeg kategóriákba sorolt termékek (Erős, Laza), majd a más főkategóriába tartozók, végül „Nem tartozik ide” jelöléssel az összes többi.',
]

TITLE = 'babylon-grow.eu – Termesztő közeg főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15 (a „kőzetgyapot” értéke 2026-10-09). Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: Google Shopping-feed (1999 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a sandboxból hiányzik a „Virágföld” kategória – a földkeverékek (Plagron) nem palántaföldek, és a „virágföld” (2900) a főkategória legerősebb kulcsszava. A „Palántaföld” (1300) erős szó, de csak a Lightmix illik hozzá.',
 'Félrevezető nagy számok: „kőzetgyapot” 5400 és „perlit” 4400 (építőipar), „termőföld” 2400 (kerti föld), „tőzeg” 2400.',
 'Az agyaggolyó céloldala ez az ág legyen (a sandboxban itt van a nevében); a Hidro ágban csak hidrokosár / kereszt-link – kannibalizáció elkerülése.',
 'Javasolt új alkategória: Talajjavító, gilisztahumusz (Mega Worm, Bat Guano).',
]
OLD_TITLE = 'A sandbox „Termesztő közeg” menünevei – keresési volumen és javaslat'
OLD_SUB = 'Sandbox-tervezet: Palántaföld; Kertészeti Kókuszrost, kókusztégla; Kertészeti kőzetgyapot; Kertészeti perlit, vermikulit, agyaggolyó.'
EXT_TITLE = 'Rokon, közegekhez kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Nem kínált vagy más ágba tartozó témák – csak kínálatbővítés esetén.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'

PAL = 'Palántanevelő ág – Gyökereztető kocka, tőzegtabletta'
PRODUCTS = [
 ('GRO1021 GRO1401 GRO1022 GRO1402 GRO1173 GRO1399 GRO1403 GRO1404', 'Virágföld, termesztőföld', [], 'Erős', 'Plagron földkeverék'),
 ('GRO0892 GRO1400', 'Palántaföld', ['Virágföld, termesztőföld'], 'Erős', 'Plagron Lightmix – könnyű, palántához is'),
 ('GRO0385 GRO2234 GRO2235 GRO2415 GRO2416 GRO2417 GRO4411 GRO4412 GRO4411/1 GRO4412/1', PAL, ['Palántaföld'], 'Laza', 'Jiffy tőzeg- / kókuszkorong'),
 ('GRO0418 GRO1405 GRO2912 GRO3246 GRO3518 GRO4693', 'Kertészeti kókuszrost, kókusztégla', [], 'Erős', 'Zsákos kókusz termesztőközeg'),
 ('GRO0848 GRO2273 GRO2892 GRO3209 GRO4113 GRO4114 GRO4320 GRO4321 GRO4689 GRO4694', 'Kertészeti kókuszrost, kókusztégla', [], 'Erős', 'Préselt kókusztégla / -blokk'),
 ('GRO4701 GRO4696 GRO4698', 'Kertészeti kókuszrost, kókusztégla', [], 'Erős', 'Kókuszpaplan, kókusz ültetőzsák'),
 ('GRO2707 GRO2708 GRO2709 GRO2710 GRO2711 GRO2712 GRO2794 GRO2795 GRO4363 GRO4371 GRO4416 GRO4417 GRO4675', PAL, ['Kertészeti kókuszrost, kókusztégla'], 'Laza', 'Kókusz magvető kocka / korong'),
 ('GRO0388 GRO1325 GRO1326 GRO1327 GRO1343 GRO1348 GRO3257 GRO3759 GRO4380 GRO4464', 'Kertészeti kőzetgyapot', [], 'Erős', 'Grodan kőzetgyapot'),
 ('GRO4751 GRO4752 GRO4753 GRO4754 GRO4755 GRO4757', 'Kertészeti kőzetgyapot', [], 'Erős', 'Agra-Wool kőzetgyapot'),
 ('GRO1466 GRO2471 GRO2224 GRO2225 GRO2226', 'Kertészeti perlit, vermikulit, agyaggolyó', [], 'Erős', 'Kertészeti perlit'),
 ('GRO3748 GRO3890', 'Kertészeti perlit, vermikulit, agyaggolyó', [], 'Erős', 'Vermikulit'),
 ('GRO1406 GRO2349 GRO2850 GYUJTO0319', 'Kertészeti perlit, vermikulit, agyaggolyó', [], 'Erős', 'Agyaggolyó – a Hidro ágban kereszt-link'),
 ('GRO1174 GRO2011 GRO3883', 'Talajjavító, gilisztahumusz', [], 'Erős', 'Plagron Mega Worm (gilisztahumusz)'),
 ('GRO1767 GRO3445', 'Talajjavító, gilisztahumusz', [], 'Laza', 'Plagron Bat Guano – a Tápok ágban is'),
 ('GRO4463/1', 'Mikrozöld termesztés – mikrozöld közeg', [], 'Más főkategória', 'Mikrozöld kókuszszőnyeg'),
]
