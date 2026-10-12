# Babylon – Propagátor, propagátor kiegészítő (2026-10-09)
CATS = [
 dict(name='Propagátor, palántanevelő', sheet='1 Propagátor', fo='palántanevelő',
      area='Palántanevelés, magvetés, dugványozás – beltér',
      place='1. Propagátor (2. szint) – menünév: „Propagátor, palántanevelő”',
      note='A „propagátor” szót csak havi 70-en keresik, a „palántanevelő” (880) a vásárlói nyelv. A régi „Propagátorok” és „Palántanevelés” név ide olvad.',
      kws='''palántanevelő|S|F
propagátor|S|S
palanta nevelo|S|S
palantanevelo|S|E
szaporítóláda|S|S
palántanevelés|S|I
palántanevelés lakásban|S|I
propagator|S|E
palántanevelő láda|S|E
palántanevelő házilag|LN|N
palántanevelés házilag|S|I
palántanevelő szett|S|E
palántanevelő edény|S|E
palántanevelő üvegház|S|E
palántanevelő doboz|S|E
propagátor eladó|S|E
palántanevelés eszközei|S|I
szaporítóláda használata|S|I
palántanevelés üvegházban|LN|N
palántanevelés árak|S|E
lidl palántanevelő|X|X'''),
 dict(name='Fűthető propagátor', sheet='2 Fűthető propagátor', fo='fűthető palántanevelő',
      area='Palántanevelés – fűtött alsó hő (paprika, chili, paradicsom)',
      place='1. Propagátor alatt 3. szint vagy szűrő („fűthető: igen/nem”)',
      note='Kis volumen, de erős vásárlási szándék. Valószínűleg elég szűrőként / termékcímben kezelni.',
      kws='''fűthető palántanevelő|S|F
fűthető propagátor|S|S
fűthető mini üvegház|S|S
propagátor fűtés|S|E
mini üvegház fűtése|S|I
fűtött palántanevelő|S|E'''),
 dict(name='Mini üvegház, mini melegház', sheet='3 Mini üvegház', fo='mini üvegház',
      area='Palántanevelés – erkély, ablakpárkány, szoba',
      place='1. Propagátor alatt 3. szint, vagy a propagátor kategória másodlagos kulcsszava',
      note='A „melegház” (1000) és a „növényház” (140) kerti (polikarbonát/fólia) melegházat jelent – nem a propagátor-kínálat, csak említés.',
      kws='''mini üvegház|S|F
mini melegház|S|S
mini üvegház erkélyre|S|S
üvegház mini|S|E
melegház erkélyre|L|E
szobai mini üvegház|S|E
mini növényház|S|E
kis melegház|L|E
polcos melegház|L|E
mini üvegház használata|S|I
mini melegház házilag|LN|N
melegház|LN|N
növényház|LN|N
obi mini üvegház|X|X
mini melegház lidl|X|X'''),
 dict(name='Palántanevelő tálca, szaporító tálca', sheet='4 Palántanevelő tálca', fo='palántanevelő tálca',
      area='Magvetés, palántázás, dugványozás – tálcák, multitálcák',
      place='2. Propagátor kiegészítő alatt 3. szint (a kiegészítő ág legerősebb klasztere)',
      note='Három ~1000-es kulcsszó (palántanevelő / palántázó / palánta tálca) – a Google külön mutatja, de valószínűleg egy klaszter, ezért az összeg felülbecsül.',
      kws='''palántanevelő tálca|S|F
palántázó tálca|S|S
palánta tálca|S|S
szaporító tálca|S|S
szaporítótálca|S|E
vetőtálca|S|E
palanta nevelo talca|S|E
palántázó tálca tetővel|S|E
palánta nevelő tálca|S|E
műanyag palántanevelő tálca|S|E
gyökereztető tálca|S|E
növény szaporító tálca|S|E
palánta ültető tálca|S|E
nikecell palántanevelő tálca|S|E
palántanevelő tálca használata|S|I
mikrozöld tálca|L|E
használt palántanevelő tálca eladó|X|X
palántázó tálca lidl|X|X
palántázó tálca aldi|X|X'''),
 dict(name='Palántanevelő cserép, tőzegcserép', sheet='5 Palántanevelő cserép', fo='palántanevelő cserép',
      area='Palántázás, tűzdelés – cserepek, poharak',
      place='2. Propagátor kiegészítő alatt 3. szint, vagy a tálca-kategóriával összevonva',
      note='',
      kws='''palántanevelő cserép|S|F
palánta cserép|S|S
tőzegcserép|S|S
tőzeg cserép|S|E
palántanevelő pohár|S|E
szaporító cserép|S|E
kókuszrost cserép|S|E
tőzegcserép használata|S|I
palánta cserép obi|X|X'''),
 dict(name='Gyökereztető kocka, tőzegtabletta', sheet='6 Gyökereztető kocka', fo='tápkocka',
      area='Magvetés, dugványozás – kocka, tabletta, plug',
      place='2. Propagátor kiegészítő alatt 3. szint (a régi „Palánta közegek” egy része)',
      note='A „kőzetgyapot” (5400) szinte teljesen építőipari szigetelés – csak a „kőzetgyapot kocka” releváns. A „jiffy” márkanév, de így keresik a tőzegtablettát.',
      kws='''tápkocka|S|F
jiffy|S|S
kőzetgyapot kocka|S|S
tőzegtabletta|S|S
palántanevelő kocka|S|E
palánta tápkocka|S|E
grodan|S|G
root riot|S|G
gyökereztető kocka|S|E
jiffy 7|S|G
grodan kocka|S|G
kőzetgyapot termesztő kocka|S|E
dehidratált tőzegtabletta|S|E
kézi tápkocka nyomó|S|E
tápkocka készítés házilag|S|I
tőzegtabletta obi|X|X
kőzetgyapot|LN|N'''),
 dict(name='Fűtőlap, fűtőszőnyeg palántákhoz', sheet='7 Fűtőlap', fo='fűtőlap',
      area='Propagátor / palántatálca alsó fűtése',
      place='2. Propagátor kiegészítő, propagátor fűtőlap – a menünévben a „fűtőlap” maradjon',
      note='A „fűtőszőnyeg” (1300) és az „elektromos fűtőszőnyeg” (590) padlófűtést jelent; a „terrárium fűtőlap” (140) állattartás – ugyanaz a termék, más vevő. A „palánta fűtőszőnyeg” (90) a pontos kulcsszó.',
      kws='''fűtőlap|S|F
palánta fűtőszőnyeg|S|S
heat mat|S|S
fűtőlap termosztáttal|S|S
palánta fűtőlap|S|E
fűtő lap|S|E
futolap|S|E
terrárium fűtőlap|L|E
fűtőlap terrárium|L|E
fűtőszőnyeg|LN|N
elektromos fűtőszőnyeg|LN|N
fűtő szőnyeg|LN|N
kisállat fűtőszőnyeg|LN|N
kutyaház fűtőlap|LN|N'''),
 dict(name='Termosztát fűtőlaphoz', sheet='8 Termosztát', fo='termosztátos konnektor',
      area='Fűtőlap / propagátor hőfokszabályzás',
      place='2. Propagátor kiegészítő alatt 3. szint vagy a fűtőlap kategóriában szűrő',
      note='A „termosztát” (5400) szobatermosztátot / kazánt jelent – nem célozni. A konnektoros (dugaljas) termosztát az, ami a fűtőlaphoz kell.',
      kws='''termosztátos konnektor|S|F
termosztát konnektor|S|S
konnektoros termosztát|S|S
termosztátos dugalj|S|S
konnektor termosztát|S|E
fűtőszőnyeg termosztát|S|E
termosztát dugalj|S|E
dugalj termosztát|S|E
keltető termosztát|L|E
konnektorba dugható termosztát|S|E
wifi konnektor termosztát|S|E
digitális konnektoros termosztát|S|E
digitális termosztát|LN|N
termosztát|LN|N
konnektoros termosztát praktiker|X|X
konnektoros termosztát obi|X|X'''),
 dict(name='Palántanevelő lámpa', sheet='9 Palántanevelő lámpa', fo='palántanevelő lámpa',
      area='Palántanevelés kiegészítő világítás (ablak, polc)',
      place='2. Propagátor kiegészítő alatt 3. szint, vagy a Világítás főkategóriában – kereszt-linkkel',
      note='Ha a lámpák a Világítás főkategóriában lesznek, itt elég egy „Palántanevelő lámpa” al-/kereszt-kategória a kis teljesítményű LED-ekkel.',
      kws='''palántanevelő lámpa|S|F
palánta nevelő lámpa|S|S
palánta lámpa|S|S
palántanevelő led lámpa|S|S
palanta nevelo lampa|S|E
palánta világítás|S|E
palántanevelő led|S|E
palánta nevelő led|S|E
palántanevelő led szalag|S|E
palántanevelő led izzó|S|E
palántanevelő fénycső|S|E
palánta led|S|E
növény palántanevelő led lámpa|S|E
palántanevelő lámpa használata|S|I
palántanevelő lámpa obi|X|X'''),
 dict(name='Páratartalom mérő, higrométer', sheet='10 Páratartalom mérő', fo='páratartalom mérő',
      area='Propagátor / nevelőtér klíma ellenőrzése',
      place='Elsősorban a mérők (pH/EC) vagy klíma főkategóriába; itt kereszt-link / ajánlott termék',
      note='Nagy volumen, de a keresők többsége lakás-páratartalmat mér. Termékhez kötve érdemes, külön propagátor-alkategóriának nem.',
      kws='''páratartalom mérő|L|F
páratartalommérő|L|S
higrométer|L|S
hő és páratartalom mérő|L|S
hőmérséklet és páratartalom mérő|L|E
digitális hő és páratartalom mérő|L|E
digitális páratartalom mérő|L|E
digitális hőmérő és páratartalom mérő|L|E
hőmérő páratartalom mérő|L|E
levegő páratartalom mérő|L|E
hőmérséklet páratartalom mérő|L|E
szobai páratartalom mérő|LN|N
higrométer működése|L|I
páratartalom mérő media markt|X|X'''),
 dict(name='Permetező flakon, párásító', sheet='11 Permetező flakon', fo='permetező flakon',
      area='Palánták, dugványok párásítása',
      place='2. Propagátor kiegészítő – termékszint, külön kategória nem kell',
      note='A „párásító” (5400) szobai párásító készülék – nem célozni.',
      kws='''permetező flakon|S|F
virágpermetező flakon|S|S
kézi párásító|LN|N
párásító|LN|N'''),
]

# Régi kategóriák (Palántanevelés ág) – hova kerül
OLD = [
 ('Palántanevelés (régi főkategória)', 'Az új „Propagátor, propagátor kiegészítő” főkategória váltja; a „palántanevelő” szó maradjon a menünévben vagy SEO title-ben.', '''palántanevelő|S
palántanevelés|S
paprika palántanevelés|L
paradicsom palántanevelés|L
palántanevelés lakásban|S
tálcás palántanevelés|S
tápkockás palántanevelés|S
chili paprika palánta nevelés|L'''),
 ('Propagátorok (régi)', '→ 1. Propagátor (új)', '''propagátor|S
fűthető palántanevelő|S
mini üvegház|S
szaporítóláda|S'''),
 ('Propagátor kiegészítők (régi)', '→ 2. Propagátor kiegészítő, propagátor fűtőlap (új)', '''palántanevelő tálca|S
palántázó tálca|S
fűtőlap|S
palánta fűtőszőnyeg|S
palántanevelő lámpa|S
palántanevelő cserép|S'''),
 ('Palánta közegek (régi)', 'A föld-típusú közegek a Közegek / földkeverékek főkategóriába; a kocka/tabletta jellegűek az új 2. Propagátor kiegészítő ágba (6. lap).', '''palántaföld|S
palánta föld|S
palántaföld 50l|S
legjobb palántaföld|S
bio palántaföld|S
palántanevelő föld|S
vetőföld|S
palántanevelő tőzeg|S
kókuszrost|L
kókuszföld|L
tápkocka|S
jiffy|S
kőzetgyapot kocka|S
tőzegtabletta|S
palántaföld házilag|LN
obi palántaföld|X
praktiker palántaföld|X'''),
 ('Palánta tápok (régi)', 'A Tápok / adalékok főkategóriába (gyökereztetők, starter tápok); innen kereszt-link elég.', '''gyökereztető por|S
palánta tápoldat|S
gyökereztető hormon por|S
clonex|S
clonex gel|S
gyökereztető|S
palánta tápoldat házilag|LN
paprika palánta tápoldat házilag|LN
paradicsom palánta tápoldat|S
radix gyökereztető|S
palánta gyökér erősítő|S
gyökereztető folyadék|S
palántanevelő tápoldat|S
gyökereztető szer|S
clonex gyökereztető gél|S
plagron power roots|S
palánta táp|S
gyökereztető gél|S
gyökereztető hormon házilag|LN
obi gyökereztető hormon|X'''),
 ('Vetőmagok (régi)', 'Önálló főkategória vagy megszüntetés – a growshop-releváns rész a zöldség/chili/mikrozöld; a szántóföldi (lucerna, kukorica, búza) nem célpiac.', '''vetőmag|L
vetőmagok|L
vetőmag rendelés|L
paradicsom vetőmag|L
chili paprika mag|L
zöldség vetőmag|L
vetőmag webshop|L
bio vetőmagok|L
chili mag|L
mikrozöld mag|L
paprika vetőmag|L
fűszernövény magok|L
chili vetőmag|L
uborka vetőmag|L
bazsalikom vetőmag|L
lucerna vetőmag|LN
kukorica vetőmag|LN
obi vetőmag|X'''),
]

EXT = [
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


TITLE = 'babylon-grow.eu – Propagátor, propagátor kiegészítő főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-09. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok.'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a „propagátor” szóra havi 70 keresés jut, a „palántanevelő”-re 880, a „palántanevelő tálca / palántázó tálca / palánta tálca” mindegyikére 1000. A menünévben érdemes a „palántanevelő” szót is szerepeltetni.',
 'A fűtőlap-ágban a „fűtőszőnyeg” és a „termosztát” nagy számai padlófűtésre / szobatermosztátra vonatkoznak – ezek nem a mi vevőink (Laza / Nem).',
 'A régi Palántanevelés-ág kategóriáinak keresései a „Régi kategóriák” lapon vannak, javaslattal, hova kerüljenek az új fában.',
 'Termékkínálat: az éles bolt terméklistáját ebből a környezetből nem értem el (a Shoprenter API-t és a babylon-grow.eu-t a hálózati szabály tiltja), ezért az „Érdemes” oszlop a keresési szándékon alapul – termékexport alapján finomítandó.',
]
OLD_TITLE = 'A régi „Palántanevelés” ág kategórianevei – keresési volumen és javasolt helyük az új fában'
OLD_SUB = 'Régi fa: Palántanevelés → Palánta közegek, Palánta tápok, Propagátor kiegészítők, Propagátorok, Vetőmagok.'
EXT_TITLE = 'Rokon, palántaneveléshez kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Nagy volumenű, de nem propagátor-vásárlási szándékú témák – blog, GYIK vagy külön kategória, ha van hozzá termék.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'
