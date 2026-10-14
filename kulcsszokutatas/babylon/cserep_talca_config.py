# Babylon – Cserép, tálca (sandbox-főkategória, 2026-10-14)
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='Virágcserép', sheet='1 Virágcserép', fo='virágcserép',
      area='Termesztő cserép – műanyag, kerek, literes méretek',
      place='2. szint – „Virágcserép” (sandbox-név marad); H1 / SEO title: „Műanyag virágcserép”; szűrők: térfogat (liter), átmérő, forma',
      note='A literes keresések kicsik (20 literes 50, 10 literes 30, 50 literes 30, 30 literes 20, 15 literes 20) – a térfogat legyen szűrő, ne kategória. A „cserép” (2900) önmagában tetőcserép, a „műanyag vödör” (590) a Bővítés lapon van.',
      kws='''virágcserép|S|F
műanyag virágcserép|S|S
műanyag virág cserép|S|E
műanyag cserép|S|S
műanyagcserép|S|E
virágcserép műanyag|S|E
könnyű cserepek|S|E
olcsó műanyag virágcserép|S|E
virágcserepek|S|E
műanyag cserép nagykereskedés|S|E
virágcserép méretek|S|I
cserepek|S|E
olcsó virágcserép|S|E
műanyag virágcserép 40 cm|S|E
20 literes cserép|S|E
kerti cserép|L|E
10 literes cserép|S|E
50 literes cserép|S|E
virágcserép 30 cm|S|E
30 literes cserép|S|E
15 literes cserép|S|E
műanyag virágcserepek|S|E
virágcserép olcsón|S|E
kerek virágcserép|S|E
virágcserép webáruház|S|E
konténer cserép|S|E
5 literes cserép|S|E
műanyag palántázó cserép|S|E
obi virágcserép|X|X
praktiker virágcserép|X|X'''),
 dict(name='Nagy virágcserép', sheet='2 Nagy virágcserép', fo='nagy virágcserép',
      area='Nagy térfogatú cserép – 20–100 literes termesztés, kültér',
      place='3. szint a Virágcserép alatt – csak ha legalább 3–4 nagy (kb. 20 l feletti) cserép van a kínálatban; különben a Virágcserép másodlagos kulcsszava',
      note='Erős klaszter (nagy virágcserép 480, nagyméretű műanyag virágcserép 320, virágcserép nagy 260). A „műanyag virágcserép 100 cm” (390) / „60 cm” (320) főleg dekor balkon- és teraszcserép.',
      kws='''nagy virágcserép|S|F
nagyméretű műanyag virágcserép|S|S
virágcserép nagy|S|S
nagy cserép|S|S
nagy méretű virágcserép|S|E
nagyméretű cserép|S|E
nagy virágcserép olcsón|S|E
nagy műanyag cserép|S|E
nagy műanyag virágcserép|S|E
nagyméretű műanyag cserép|S|E
xxl cserép|L|E
50 literes virágcserép|S|E
műanyag virágcserép 100 cm|LN|N
műanyag virágcserép 60 cm|LN|N'''),
 dict(name='Szögletes cserép', sheet='3 Szögletes cserép', fo='szögletes virágcserép',
      area='Helytakarékos termesztés sátorban / polcon',
      place='Szűrő a Virágcserép kategóriában (forma: kerek / szögletes) – önálló kategóriának kevés',
      note='A „négyzetes cserép” kifejezésre nincs mérhető keresés – a „szögletes” a vásárlói szó.',
      kws='''szögletes virágcserép|S|F
magas cserép|S|S
szögletes cserép|S|S
szögletes műanyag cserép|S|S
magas műanyag virágcserép|S|E
négyszögletes virágcserép|S|E
négyzet alakú virágcserép|S|E
négyszögletes műanyag cserép|S|E
mély cserép|S|E'''),
 dict(name='Air-Pot cserép', sheet='4 Air-Pot', fo='airpot',
      area='Gyökérlégzés, gyökérmetszés – termesztés konténerben',
      place='2. szint – a „Speciális cserép, szövetcserép” helyett vagy alatta; a menünévben a márkanév legyen',
      note='A „légmetsző / légmetszéses / gyökérlégző cserép” kifejezésekre nincs mérhető keresés – a vásárlók a márkanevet keresik.',
      kws='''airpot|S|F
air pot|S|S
air pot 50l|S|G
air pot hydro|S|G
air pot 9l|S|G'''),
 dict(name='Szövetcserép, ültetőzsák', sheet='5 Szövetcserép', fo='ültetőzsák',
      area='Szövet / textil / filc cserép, ültető- és termesztőzsák',
      place='2. szint – a „Speciális cserép, szövetcserép” utódja; menünév: „Szövetcserép, ültetőzsák”',
      note='A „szövetcserép” egybeírva csak 10; a „szövet cserép”, „textil cserép”, „textil virágcserép”, „smart pot”, „grow bag” egyenként 20. A legerősebb az „ültetőzsák” (90 + ékezet nélkül 50), de ennek egy része burgonyás zsák.',
      kws='''ültetőzsák|S|F
szövet cserép|S|S
textil cserép|S|S
textil virágcserép|S|S
smart pot|S|E
grow bag|S|E
szövetcserép|S|E
ultetozsak|S|E
burgonya ültető zsák|L|E
krumpli ültető zsák|L|E
krumpli termesztő zsák|L|E
growbag|S|E
termesztőzsák|S|E
növénynevelő zsák|S|E
root pouch|S|G
smarpot|S|E'''),
 dict(name='Önöntöző cserép', sheet='6 Önöntöző cserép', fo='önöntöző cserép',
      area='Víztartályos, önöntöző cserép – szobanövény, fűszer',
      place='Opcionális 2. szint – csak ha van önöntöző kínálat; különben kimarad',
      note='Kis, de tiszta szándékú klaszter.',
      kws='''önöntöző cserép|L|F
önöntöző virágcserép|L|S
cserép öntöző|L|E
önlocsoló virágcserép|L|E
önöntözős virágcserép|L|E
intelligens virágcserép|L|E'''),
 dict(name='Cserépalátét', sheet='7 Cserépalátét', fo='cserépalátét',
      area='Cserép alá – vízfelfogás, gurulós alátét',
      place='2. szint – a „Tálca, alátét” kettébontásával; az „alátét” szó önmagában csavaralátét',
      note='A „cserépalátét” és a „cserép alátét” egyenként 260; a „virágcserép alátéttel” (140) a cseréppel együtt vásárlót jelenti – a Virágcserép kategóriában is említendő.',
      kws='''cserépalátét|S|F
cserép alátét|S|S
virágcserép alátét|S|S
műanyag cserépalátét|S|S
virágcserép alátéttel|S|E
gurulós virágtartó|L|E
gurulós virágállvány|L|E
virágcserép alátét 60 cm|S|E
cserépalátét 80 cm|S|E
cserépalátét 60 cm|S|E
cserépalátét 50 cm|S|E
virágcserép alátét 50 cm|S|E
gurulós alátét|L|E
guruló virágtartó|L|E
műanyag virágcserép alátét|S|E
cserépalátét 70 cm|S|E
műanyag virágláda alátét|S|E
gurulós virágcserép alátét|S|E
virágcserép alátét méretek|S|I
kerámia cserépalátét|LN|N
agyag cserépalátét|LN|N
alátét|LN|N
obi cserépalátét|X|X'''),
 dict(name='Műanyag tálca, árapály asztal', sheet='8 Tálca', fo='nagyméretű műanyag tálca',
      area='Gyűjtőtálca termesztősátorba, árapály (ebb & flow) rendszer',
      place='2. szint – a „Tálca, alátét” kettébontásával',
      note='A „gyűjtőtálca”, „növénytálca”, „cserép tálca” kifejezésekre nincs mérhető keresés. A „tálcák” (1000) konyhai, a „csepptálca” (210) és a „kármentő tálca” (480) klíma / ipari. A „szaporító / palántanevelő tálca” a Palántanevelő ágé, a „mikrozöld tálca” a Mikrozöld termesztésé.',
      kws='''nagyméretű műanyag tálca|L|F
műanyag tálca|L|S
ebb and flow|S|S
árapály asztal|S|S
nagy műanyag tálca|L|E
árapály asztal eladó|S|E
műanyag csepegtető tálca|L|E
műanyag kármentő tálca|L|E
kármentő tálca műanyag|L|E
termesztő tálca|S|E
fekete műanyag tálca|L|E
kerek műanyag tálca|L|E
növény tálca|S|E
vízgyűjtő tálca|S|E
csepegtető tálca műanyag|L|E
kerti tálca|S|E
tálcák|LN|N
kármentő tálca|LN|N
csepptálca|LN|N
szaporító tálca|LN|N
műanyag tálca obi|X|X'''),
]

# A sandbox (új) menünevek saját keresése – a javaslathoz az éles kategóriákat nem használjuk
OLD_SHEET = 'Sandbox menünevek'
OLD = [
 ('Cserép, tálca (főkategória)', 'A „cserép” (2900) tetőcserép, a „cserép tálca” / „cserép és tálca” kifejezésre nincs mérhető keresés. Menünévnek jó, a H1 / SEO title legyen: „Virágcserép, cserépalátét, tálca”.', '''cserép|LN
virágcserép|S
cserépalátét|S'''),
 ('Virágcserép', 'Marad; H1: „Műanyag virágcserép”, szűrők: liter, átmérő, forma', '''virágcserép|S
műanyag virágcserép|S'''),
 ('Speciális cserép, szövetcserép', 'A „speciális cserép” névre nincs keresés, a „szövetcserép”-re 10. Javaslat: két önálló alkategória – „Air-Pot cserép” és „Szövetcserép, ültetőzsák”.', '''szövetcserép|S
szövet cserép|S
airpot|S
ültetőzsák|S'''),
 ('Tálca, alátét', 'Az „alátét” (720) csavaralátét, a „tálcák” (1000) konyhai. Javaslat: kettébontás – „Cserépalátét” és „Műanyag tálca, árapály asztal”.', '''alátét|LN
tálcák|LN
cserépalátét|S
cserép alátét|S
nagyméretű műanyag tálca|L'''),
]

EXT = [
 ('Műanyag vödör', 'Csak ha van vödör (pl. DWC / hidro vödör) – akkor a Hidro ágba vagy szűrőként', '''műanyag vödör|L
műanyagvödör|L
olcsó műanyag vödör|L
műanyag vödör fedővel|L'''),
 ('Hidrokultúrás cserép, hálós kosár', 'A Hidro főkategóriába (ha van); innen kereszt-link', '''hidrokultúrás cserép|L
hálós kosár|L
hidroponikus cserép|L
hidro cserép|L
net pot|L'''),
 ('Orchidea és átlátszó cserép', 'Csak ha van ilyen termék – különben szűrő / említés', '''orchidea cserép|L
átlátszó cserép|L
orchidea cserép átlátszó|L
átlátszó orchidea cserép|L'''),
 ('Kaspó, virágláda, dekor cserép', 'Nem growshop-téma – csak ha forgalmazod', '''kaspó|LN
virágláda|LN
virágtartó|LN
agyag cserép|LN
kerámia cserép|LN'''),
]

MAKERS = '''airpot
air pot
air pot 50l
air pot hydro
smart pot
smarpot
root pouch'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Cserép, tálca (kulcsszóadat alapján; a termékszám termékexport után kerül be)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet (Virágcserép; Speciális cserép, szövetcserép; Tálca, alátét) és a Kulcsszótervező adatai.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
# (szint, javasolt név, szülő, fő kulcsszó, kötődés-kód, típus, indoklás, CATS-név a klaszterösszeghez)
STRUCT = [
 (1, 'Cserép, tálca', '–', 'virágcserép', 'S', 'Főkategória', 'A főkategória-névre nincs saját keresés („cserép” = tetőcserép); a H1 a virágcserép / cserépalátét / tálca szavakra épüljön.', None),
 (2, 'Virágcserép', 'Cserép, tálca', 'virágcserép', 'S', 'Önálló kategória', 'A főkategória legerősebb klasztere (virágcserép 2400, műanyag virágcserép 590, műanyag cserép 480). Térfogat (liter) és forma szűrővel.', 'Virágcserép'),
 (3, 'Nagy virágcserép', 'Virágcserép', 'nagy virágcserép', 'S', 'Önálló kategória (feltételes)', 'Erős saját klaszter (480 + 320 + 260). Csak akkor önálló, ha legalább 3–4 nagy cserép van; különben a Virágcserép másodlagos kulcsszava.', 'Nagy virágcserép'),
 (3, 'Szögletes cserép', 'Virágcserép', 'szögletes virágcserép', 'S', 'Szűrő', 'Kis volumen (90 + 70 + 40) – forma-szűrőként elég.', 'Szögletes cserép'),
 (2, 'Air-Pot cserép', 'Cserép, tálca', 'airpot', 'S', 'Önálló kategória', 'A sandbox „Speciális cserép” helyett: a márkanévre van keresés (airpot 140, air pot 90), a „légmetsző cserép”-re nincs.', 'Air-Pot cserép'),
 (2, 'Szövetcserép, ültetőzsák', 'Cserép, tálca', 'ültetőzsák', 'S', 'Önálló kategória', 'Az „ültetőzsák” (90 + 50) viszi; a szövet / textil cserép, smart pot, grow bag egyenként 20.', 'Szövetcserép, ültetőzsák'),
 (2, 'Önöntöző cserép', 'Cserép, tálca', 'önöntöző cserép', 'L', 'Opcionális kategória', 'Csak ha van önöntöző kínálat (önöntöző cserép 90).', 'Önöntöző cserép'),
 (2, 'Cserépalátét', 'Cserép, tálca', 'cserépalátét', 'S', 'Önálló kategória', 'A sandbox „Tálca, alátét” kettébontása: a cserépalátét-klaszter önmagában erős (260 + 260 + 140 + 140 + 110).', 'Cserépalátét'),
 (2, 'Műanyag tálca, árapály asztal', 'Cserép, tálca', 'nagyméretű műanyag tálca', 'L', 'Önálló kategória', 'Gyűjtőtálca sátorba és árapály rendszer (ebb and flow 70, árapály asztal 50). A „gyűjtőtálca” névre nincs keresés.', 'Műanyag tálca, árapály asztal'),
]
NOT_CATS = [
 ('Speciális cserép (sandbox-név)', 'szövetcserép', 'A „speciális cserép” névre nincs mérhető keresés – helyette Air-Pot és Szövetcserép, ültetőzsák.'),
 ('Literes méretek', '20 literes cserép', 'Szűrő (térfogat) a Virágcserép kategóriában, nem kategória.'),
 ('Szaporító / palántanevelő tálca', 'szaporító tálca', 'A Palántanevelő / mini üvegház ág céloldala – itt csak említés (kannibalizáció).'),
 ('Mikrozöld tálca', 'mikrozöld tálca', 'A Mikrozöld termesztés főkategóriáé.'),
 ('Csepptálca, kármentő', 'kármentő tálca', 'Klíma / ipari keresés – nem célozni.'),
]
PRODUCT_NOTE = [
 'A termékexport ebben a munkamenetben még nem állt rendelkezésre (a felhőből az éles bolt nem érhető el), ezért a termékek itt és a kategórialapokon még nem szerepelnek.',
 'Kérjük a teljes termékexportot CSV-ben (termékkód, terméknév, gyártó, gyűjtőtermék) – utána minden kategóriához kigyűjtjük az odaillő termékeket (egy termék több kategóriában is lehet).',
]

TITLE = 'babylon-grow.eu – Cserép, tálca főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-12 és 2026-10-14. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok.'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a virágcserép (2400) és a nagy virágcserép (480) viszi az ágat; a sandbox két gyűjtőnevére („Speciális cserép”, „Tálca, alátét”) nincs vagy félrevezető a keresés – javasolt a kettébontásuk (Kategóriaszerkezet-ajánlás lap).',
 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe; a javaslat a sandbox-tervezetre és a kulcsszóadatra épül.',
 'A „szaporító tálca” / „palántanevelő tálca” céloldala a Palántanevelő ág, a „mikrozöld tálca” a Mikrozöld termesztésé – itt csak említés.',
 'Termékkínálat: a termékexport még hiányzik – a termékszámok és a kategórialapok termékblokkja az export után kerül be.',
]
OLD_TITLE = 'A sandbox „Cserép, tálca” menünevei – keresési volumen és javasolt név'
OLD_SUB = 'Sandbox-tervezet: Virágcserép; Speciális cserép, szövetcserép; Tálca, alátét.'
EXT_TITLE = 'Rokon, cserepekhez kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más szándékú vagy más főkategóriába tartozó témák – csak ha van hozzá termék.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'
