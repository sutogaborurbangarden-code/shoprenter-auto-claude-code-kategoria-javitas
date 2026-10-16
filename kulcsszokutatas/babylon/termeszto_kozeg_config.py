# Babylon – Termesztő közeg (2026-10-16, 2. változat)
# Csak a FŐKATEGÓRIA NEVE alapján: a korábbi / sandbox alkategória-nevek és -szerkezet figyelmen kívül;
# alkategóriák az élő termékkínálat és a kulcsszóadat alapján.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 {'name': 'Virágföld, palántaföld', 'sheet': '1 Virágföld, palántaföld', 'fo': 'virágföld', 'area': 'Zsákos virágföld / földkeverék és könnyű palánta- / magvető föld (Plagron Allmix, Lightmix, Batmix, Royalmix…)', 'place': '2. szint – a legerősebb közeg-kulcsszó (virágföld 2900); a palántaföld (1300) ugyanazon a lapon, H2-ként / szűrőként (kevés palántaföld termék)', 'note': 'A sandboxban csak „Palántaföld” van, de a földek többsége nem palántaföld. A „termőföld” (2400) kerti ömlesztett föld, a „tőzeg” (2400) tiszta tőzeg – nem célozni.', 'kws': 'virágföld|S|F\nvirágföld 50l|S|S\ntőzeges föld|S|S\ntőzeg föld|S|E\n50 l virágföld|S|E\náltalános virágföld|L|E\nviragfold|S|E\ntőzeges virágföld|S|S\nvirágföld rendelés|S|E\nültetőföld|S|E\nperlit virágföld|S|E\nperlites virágföld|S|E\nvirágföld nagy tételben|S|E\nhumuszos virágföld|S|E\náltalános földkeverék|S|E\nplagron lightmix|S|G\njó minőségű virágföld|S|E\nlegjobb virágföld|S|E\nvirágföld 100l|S|E\nbio virágföld|S|E\nbiobizz light mix|L|G\ntőzegmentes virágföld|L|E\nbio föld|S|E\nminőségi virágföld|S|E\nplagron föld|S|G\nvirágföld nagy kiszerelés|S|E\nplagron allmix|S|G\nallmix plagron|S|G\nbiobizz all mix|L|G\nvirágföld típusok|S|I\ntermőföld|LN|N\ntőzeg|LN|N\nobi virágföld|X|X\npraktiker virágföld|X|X\npalántaföld|S|S\npalántaföld 50l|S|S\npalánta föld|S|S\npalantafold|S|E\nmagvető föld|S|S\nlegjobb palántaföld|S|E\nbio palántaföld|S|E\nvetőföld|S|E\npalántanevelő tőzeg|S|E\npalántaföld vagy virágföld|S|I\npalántaföld házilag|L|I\npalántaföld obi|X|X'},
 {'name': 'Kókuszrost, kókusztégla', 'sheet': '2 Kókuszrost', 'fo': 'kókuszrost', 'area': 'Zsákos kókusz termesztőközeg, préselt kókusztégla / -blokk, kókuszpaplan', 'place': '2. szint', 'note': 'Erős klaszter: kókuszrost 1000, kókuszrost tégla 720, kókusztégla 320, kertészeti kókuszrost 170. A „kókuszrost korong” a Palántanevelő ágé.', 'kws': 'kókuszrost|S|F\nkókuszrost tégla|S|S\nkókusztégla|S|S\nkertészeti kókuszrost|S|S\nkokuszrost|S|E\nkókuszföld|S|S\nkókusz rost|S|E\nkókusztégla 5 kg|S|E\nkókusztégla ár|S|E\nkókuszpaplan|S|E\nkókusz tégla|S|E\nkókuszrost ültetőközeg vásárlás|S|E\nkókuszrost ültetőközeg|S|E\nkókuszrost föld|S|E\nkokusz rost|S|E\nkókusz rost tégla|S|E\nkókuszrost virágföld|S|E\nkókuszrost paplan|S|E\nkókuszrost termesztőközeg|S|E\npréselt kókuszrost|S|E\ncanna coco|S|G\nplagron cocos|S|G\nbiobizz coco mix|S|G\ncocos premium|S|G\nkókuszrost tégla használata|S|I\nkókusztégla használata|S|I\nkókuszrost használata|S|I\nmire jó a kókuszrost tégla|S|I\nkókuszföld használata|S|I\nkókuszrost praktiker|X|X\nkókuszrost tégla obi|X|X'},
 {'name': 'Kőzetgyapot: kocka, paplan', 'sheet': '3 Kőzetgyapot', 'fo': 'kőzetgyapot kocka', 'area': 'Grodan és Agra-Wool kőzetgyapot kocka, blokk, paplan (slab)', 'place': '2. szint', 'note': 'A „kőzetgyapot” (5400) szinte teljesen építőipari szigetelés. A kertészeti keresés kicsi (kőzetgyapot kocka 40, kertészeti kőzetgyapot 20, Grodan 20) – a márkanév fontos.', 'kws': 'kőzetgyapot kocka|S|F\nkertészeti kőzetgyapot|S|S\ngrodan|S|S\ngrodan kőzetgyapot|S|S\ngrodan kocka|S|G\ngrodan delta|S|G\ngrodan paplan|S|G\ngrodan growcube|S|G\nagra wool|S|G\nkőzetgyapot termesztő kocka|S|E\nkőzetgyapot palánta|S|E\nkertészeti kőzetgyapot árlista|S|E\nkőzetgyapot|LN|N'},
 {'name': 'Gyökereztető kocka, tőzeg- és kókuszkorong', 'sheet': '4 Gyökereztető kocka', 'fo': 'jiffy', 'area': 'Magvető és dugványozó közeg: Jiffy tőzeg- / kókuszkorong, Eazy Plug és kókusz magvető kocka, kőzetgyapot magvető kocka (lap)', 'place': '2. szint – ÚJ ebben az ágban: közeg, ezért a céloldal itt; a Propagátor ágból (Dugványozás) link', 'note': 'Jiffy 90, tápkocka 70, kókuszrost korong 50, tőzegkorong 40, jiffy tőzegkorong 40, palántanevelő kocka 20 – kis, de tiszta szándék, sok termék (~19 élő).', 'kws': 'jiffy|S|F\ntápkocka|S|S\nkókuszrost korong|S|S\ntőzegkorong|S|S\njiffy tőzegkorong|S|E\ntőzegtabletta|S|E\npalántanevelő kocka|S|E\npalánta tápkocka|S|E\ngyökereztető kocka|S|E\njiffy 7|S|G\ndehidratált tőzegtabletta|S|E'},
 {'name': 'Perlit, vermikulit', 'sheet': '5 Perlit, vermikulit', 'fo': 'kertészeti perlit', 'area': 'Kertészeti (duzzasztott) perlit és vermikulit – lazító, vízmegtartó adalék', 'place': '2. szint', 'note': 'Kertészeti perlit 720, vermikulit 1600 (vegyes – építőipari is). A „perlit” (4400) jórészt építőipari – LN.', 'kws': 'kertészeti perlit|S|F\nperlit|LN|N\nvermikulit|L|S\nkertészeti perlit ár|S|E\nperlit kertészeti|S|E\nduzzasztott perlit|L|E\nkertészeti perlit 100l|S|E\nperlit virágföldbe|S|E\nkertészeti vermikulit|S|E\nperlit 100 l|S|E\nvermikulit vásárlás|S|E\nperlit vásárlás|S|E\nperlit mire jó|S|I\nkertészeti perlit használata|S|I\nperlit használata|S|I\nvermikulit használata|S|I\nperlitbeton|LN|N\nzeolit|LN|N\nkertészeti perlit obi|X|X\nperlit obi|X|X'},
 {'name': 'Agyaggolyó', 'sheet': '6 Agyaggolyó', 'fo': 'agyaggolyó', 'area': 'Égetett agyaggolyó (Plagron Euro Pebbles, CANNA Aqua Clay Pebbles) – hidrokultúra, drénréteg, orchidea', 'place': '2. szint – ÖNÁLLÓ: az „agyaggolyó” (880) céloldala ez (a Hidropónia ág „Hidrokultúra” kategóriája ide linkel)', 'note': 'Agyaggolyó 880, agyaggranulátum 590, agyaggolyó orchidea 140 (laza).', 'kws': 'agyaggolyó|S|F\nagyaggranulátum|S|S\nagyaggolyó növényekhez|S|E\nagyaggolyók|S|E\nkertészeti agyaggolyó|S|E\nagyaggolyó 50l|S|E\nhidrogolyó|S|E\nagyaggolyó orchidea|L|E\norchidea agyaggolyó|L|E\nagyaggolyó használata|S|I\nobi agyaggolyó|X|X'},
 {'name': 'Talaj- és közegjavító: guanó, gilisztahumusz, enzim', 'sheet': '7 Talajjavító', 'fo': 'talajjavító', 'area': 'Szerves talajadalék (guanó, gilisztahumusz) és enzimes közegjavító (Pure Zym, PowerZyme, Cannazym, BioNova Zym)', 'place': '2. szint – a közeg „élete”; az enzimek a Tápok ágban is (egy céloldal: Tápok, itt szűrt lista)', 'note': 'Talajjavító 210, gilisztahumusz 320 (termék most nem élő), guanó 110. A „mikorrhiza” (720) és „mikorrhiza gomba” (2900) nagy, de nincs ilyen termék – bővítés.', 'kws': 'talajjavító|S|F\ngilisztahumusz|S|S\nguanó|S|S\ntalajjavító granulátum|L|E\nhuminsav talajjavító|L|E\ntalajjavító anyagok|L|E\ntalajjavító szer|L|E\nhumusz giliszta eladó|S|E\ngilisztahumusz eladó|S|E\ntalajjavítók|L|E\nhumusz giliszta|S|E'},
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'Ültetőközeg 140, termesztő közeg 30, közeg 70 – a vásárlók a konkrét közeget keresik.', '''ültetőközeg|S
termesztő közeg|S
közeg|L'''),
 ('Föld', '→ Virágföld, palántaföld', '''virágföld|S
palántaföld|S'''),
 ('Föld nélküli közeg', '→ Kókuszrost; Kőzetgyapot; Agyaggolyó', '''kókuszrost|S
kőzetgyapot kocka|S
agyaggolyó|S'''),
 ('Vetés, dugványozás', '→ Gyökereztető kocka, tőzeg- és kókuszkorong', '''jiffy|S
tápkocka|S'''),
 ('Adalék', '→ Perlit, vermikulit; Talajjavító', '''kertészeti perlit|S
vermikulit|L
talajjavító|S'''),
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

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Termesztő közeg (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A korábbi és a sandbox alkategória-neveket és -szerkezetet NEM vettük figyelembe. Kiindulás: a főkategória neve, az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
STRUCT = [(1, 'Termesztő közeg', '–', 'ültetőközeg', 'S', 'Főkategória', 'Ültetőközeg 140, termesztő közeg 30 – a menünév jó; H1: „Termesztő közeg, virágföld, kókuszrost”.', None), (2, 'Virágföld, palántaföld', 'Termesztő közeg', 'virágföld', 'S', 'Önálló kategória', 'Virágföld 2900, palántaföld 1300.', 'Virágföld, palántaföld'), (2, 'Kókuszrost, kókusztégla', 'Termesztő közeg', 'kókuszrost', 'S', 'Önálló kategória', 'Kókuszrost 1000, kókuszrost tégla 720.', 'Kókuszrost, kókusztégla'), (2, 'Kőzetgyapot: kocka, paplan', 'Termesztő közeg', 'kőzetgyapot kocka', 'S', 'Önálló kategória', 'Kőzetgyapot kocka 40 (a „kőzetgyapot” 5400 építőipari).', 'Kőzetgyapot: kocka, paplan'), (2, 'Gyökereztető kocka, tőzeg- és kókuszkorong', 'Termesztő közeg', 'jiffy', 'S', 'Önálló kategória', 'Jiffy 90, tápkocka 70 – ÚJ itt (közeg).', 'Gyökereztető kocka, tőzeg- és kókuszkorong'), (2, 'Perlit, vermikulit', 'Termesztő közeg', 'kertészeti perlit', 'S', 'Önálló kategória', 'Kertészeti perlit 720, vermikulit 1600.', 'Perlit, vermikulit'), (2, 'Agyaggolyó', 'Termesztő közeg', 'agyaggolyó', 'S', 'Önálló kategória', 'Agyaggolyó 880 – önálló céloldal.', 'Agyaggolyó'), (2, 'Talaj- és közegjavító: guanó, gilisztahumusz, enzim', 'Termesztő közeg', 'talajjavító', 'S', 'Önálló kategória', 'Talajjavító 210, gilisztahumusz 320.', 'Talaj- és közegjavító: guanó, gilisztahumusz, enzim')]
NOT_CATS = [
 ('Külön palántaföld kategória', 'palántaföld', 'Csak 2 termék (Plagron Lightmix) – a Virágföld lapon H2 / szűrő.'),
 ('Perlit + agyaggolyó egy kategóriában', 'agyaggolyó', 'Az agyaggolyó (880) önálló, erős szó – külön céloldal.'),
 ('Mikorrhiza, trichoderma', 'mikorrhiza', 'Nincs termék – kínálatbővítés.'),
 ('Termőföld, tőzeg (ömlesztett)', 'termőföld', 'Kerti, ömlesztett – nem growshop-termék.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát – ez az éles oldal aktuális kínálata. A most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak.',
 'A szerkezet csak a főkategória nevéből, a közegek anyagából / felhasználásából és a keresési szándékból készült – a korábbi és a sandbox alkategóriák figyelmen kívül.',
]
TITLE = 'babylon-grow.eu – Termesztő közeg kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15/16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: csak a főkategória neve adott; az alkategóriák a közeg anyaga (föld, kókusz, kőzetgyapot, agyag, perlit / vermikulit), a felhasználás (vetés / dugványozás) és az adalékok (talajjavító) szerint épülnek, lapos szerkezetben.',
 'Fő megállapítások: virágföld 2900, vermikulit 1600, palántaföld 1300, kókuszrost 1000, agyaggolyó 880, kertészeti perlit 720. Változás: az agyaggolyó önálló kategória (céloldal), és a gyökereztető kocka / tőzegkorong ide került (közeg).',
 'Bővítés: mikorrhiza (2900 / 720), trichoderma (480), gilisztahumusz (320 – a Plagron Mega Worm most nem élő).',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a korábbi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Kínálatbővítés és nem célzott témák.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO1021 GRO1401 GRO1022 GRO1402 GRO1173 GRO1399 GRO1403 GRO1404', 'Virágföld, palántaföld', [], 'Erős', 'Plagron földkeverék'),
 ('GRO0892 GRO1400', 'Virágföld, palántaföld', [], 'Erős', 'Plagron Lightmix – könnyű, palántához is'),
 ('GRO0385 GRO2234 GRO2235 GRO2415 GRO2416 GRO2417 GRO4411 GRO4412 GRO4411/1 GRO4412/1', 'Gyökereztető kocka, tőzeg- és kókuszkorong', ['Propagátor ág – Dugványozás'], 'Erős', 'Jiffy tőzeg- / kókuszkorong'),
 ('GRO0418 GRO1405 GRO2912 GRO3246 GRO3518 GRO4693', 'Kókuszrost, kókusztégla', [], 'Erős', 'Zsákos kókusz termesztőközeg'),
 ('GRO0848 GRO2273 GRO2892 GRO3209 GRO4113 GRO4114 GRO4320 GRO4321 GRO4689 GRO4694', 'Kókuszrost, kókusztégla', [], 'Erős', 'Préselt kókusztégla / -blokk'),
 ('GRO4701 GRO4696 GRO4698', 'Kókuszrost, kókusztégla', [], 'Erős', 'Kókuszpaplan, kókusz ültetőzsák'),
 ('GRO2707 GRO2708 GRO2709 GRO2710 GRO2711 GRO2712 GRO2794 GRO2795 GRO4363 GRO4371 GRO4416 GRO4417 GRO4675', 'Gyökereztető kocka, tőzeg- és kókuszkorong', ['Propagátor ág – Dugványozás'], 'Erős', 'Kókusz magvető kocka / korong'),
 ('GRO0388 GRO1325 GRO1326 GRO1327 GRO1343 GRO1348 GRO3257 GRO3759 GRO4380 GRO4464', 'Kőzetgyapot: kocka, paplan', [], 'Erős', 'Grodan kőzetgyapot'),
 ('GRO4751 GRO4752 GRO4753 GRO4754 GRO4755 GRO4757', 'Kőzetgyapot: kocka, paplan', [], 'Erős', 'Agra-Wool kőzetgyapot'),
 ('GRO1466 GRO2471 GRO2224 GRO2225 GRO2226', 'Perlit, vermikulit', [], 'Erős', 'Kertészeti perlit'),
 ('GRO3748 GRO3890', 'Perlit, vermikulit', [], 'Erős', 'Vermikulit'),
 ('GRO1406 GRO2349 GRO2850 GYUJTO0319', 'Agyaggolyó', ['Hidropónia ág – Hidrokultúra'], 'Erős', 'Agyaggolyó'),
 ('GRO1174 GRO2011 GRO3883', 'Talaj- és közegjavító: guanó, gilisztahumusz, enzim', [], 'Erős', 'Plagron Mega Worm (gilisztahumusz)'),
 ('GRO1767 GRO3445', 'Talaj- és közegjavító: guanó, gilisztahumusz, enzim', [], 'Laza', 'Plagron Bat Guano – a Tápok ágban is'),
 ('GRO4463/1', 'Mikrozöld termesztés – mikrozöld közeg', [], 'Más főkategória', 'Mikrozöld kókuszszőnyeg'),
 ('GRO0671 GRO0868 GRO0870 GRO0670 GRO0231 GRO0234 GRO0233 GRO0230 GRO0460 GRO1537 GRO1859 GRO0461 GRO0459 GRO0723 GRO2512', 'Tápok ág – enzim, adalék', ['Talaj- és közegjavító: guanó, gilisztahumusz, enzim'], 'Más főkategória', 'Enzimes közegjavító – céloldal a Tápok ágban, itt szűrt lista'),
]
