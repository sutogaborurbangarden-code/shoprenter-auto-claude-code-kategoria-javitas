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
 dict(name='Cserépalátét', sheet='6 Cserépalátét', fo='cserépalátét',
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
 dict(name='Műanyag tálca, árapály asztal', sheet='7 Tálca', fo='nagyméretű műanyag tálca',
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
 ('Önöntöző cserép', 'Nincs önöntöző cserép a kínálatban (csak egy víztartályos alátét) – kategória csak kínálatbővítés esetén', '''önöntöző cserép|L
önöntöző virágcserép|L
cserép öntöző|L
önlocsoló virágcserép|L'''),
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

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Cserép, tálca (termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet, a Google Shopping-feed termékei (1999 db) és a Kulcsszótervező adatai. Termékszám = elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
# (szint, javasolt név, szülő, fő kulcsszó, kötődés-kód, típus, indoklás, CATS-név a klaszterösszeghez)
STRUCT = [
 (1, 'Cserép, tálca', '–', 'virágcserép', 'S', 'Főkategória', 'A főkategória-névre nincs saját keresés („cserép” = tetőcserép); a H1 a virágcserép / cserépalátét / tálca szavakra épüljön.', None),
 (2, 'Virágcserép', 'Cserép, tálca', 'virágcserép', 'S', 'Önálló kategória', 'A főkategória legerősebb klasztere (virágcserép 2400, műanyag virágcserép 590, műanyag cserép 480). Térfogat (liter) és forma szűrővel.', 'Virágcserép'),
 (3, 'Nagy virágcserép', 'Virágcserép', 'nagy virágcserép', 'S', 'Önálló kategória', 'Erős saját klaszter (480 + 320 + 260), és sok 20 literes feletti cserép / konténer van a kínálatban – önálló 3. szint.', 'Nagy virágcserép'),
 (3, 'Szögletes cserép', 'Virágcserép', 'szögletes virágcserép', 'S', 'Szűrő', 'Kis keresési volumen (90 + 70 + 40), de sok szögletes termék van – forma-szűrő; ha a sandbox engedi, 3. szint is lehet.', 'Szögletes cserép'),
 (2, 'Air-Pot cserép', 'Cserép, tálca', 'airpot', 'S', 'Önálló kategória', 'A sandbox „Speciális cserép” helyett: a márkanévre van keresés (airpot 140, air pot 90), a „légmetsző cserép”-re nincs.', 'Air-Pot cserép'),
 (2, 'Szövetcserép, ültetőzsák', 'Cserép, tálca', 'ültetőzsák', 'S', 'Önálló kategória', 'Az „ültetőzsák” (90 + 50) viszi; a szövet / textil cserép, smart pot, grow bag egyenként 20.', 'Szövetcserép, ültetőzsák'),
 (2, 'Cserépalátét', 'Cserép, tálca', 'cserépalátét', 'S', 'Önálló kategória', 'A sandbox „Tálca, alátét” kettébontása: a cserépalátét-klaszter önmagában erős (260 + 260 + 140 + 140 + 110).', 'Cserépalátét'),
 (2, 'Műanyag tálca, árapály asztal', 'Cserép, tálca', 'nagyméretű műanyag tálca', 'L', 'Önálló kategória', 'Gyűjtőtálca sátorba és árapály rendszer (ebb and flow 70, árapály asztal 50). A „gyűjtőtálca” névre nincs keresés.', 'Műanyag tálca, árapály asztal'),
]
NOT_CATS = [
 ('Speciális cserép (sandbox-név)', 'szövetcserép', 'A „speciális cserép” névre nincs mérhető keresés – helyette Air-Pot és Szövetcserép, ültetőzsák.'),
 ('Literes méretek', '20 literes cserép', 'Szűrő (térfogat) a Virágcserép kategóriában, nem kategória.'),
 ('Szaporító / palántanevelő tálca', 'szaporító tálca', 'A Palántanevelő / mini üvegház ág céloldala – itt csak említés (kannibalizáció).'),
 ('Mikrozöld tálca', 'mikrozöld tálca', 'A Mikrozöld termesztés főkategóriáé.'),
 ('Csepptálca, kármentő', 'kármentő tálca', 'Klíma / ipari keresés – nem célozni.'),
 ('Önöntöző cserép', 'önöntöző cserép', 'Van keresés (90), de nincs ilyen termék – csak kínálatbővítés esetén.'),
 ('Palántázó kiscserép (4–12 cm), tőzegcserép', 'palántanevelő cserép', 'A Palántanevelő ág kategóriája – itt legfeljebb másodlagos hozzárendelés.'),
]
PRODUCT_NOTE = [
 'Forrás: a Babylon Google Ads fiók Shopping-termékadatai (termékkód = Shopping item ID, terméknév = feed-cím), 2024-10-01 – 2026-10-14, összesen 1999 termék. A Shoprenter API és az éles oldal a felhőből továbbra sem érhető el.',
 'Figyelem: ez a Google-ben hirdetett termékkör, nem feltétlenül a teljes katalógus – a feedből kimaradt vagy soha nem hirdetett termékek itt nem szerepelnek. A gyártó és a gyűjtőtermék (GYUJTO…) adat a feedben nem érhető el.',
 'A „Más főkategória” sorok cserép / tálca jellegű termékek, amelyeknek a helye egy másik főkategóriában van (Palántanevelő, Mikrozöld, Hidro, Közegek, Esővízgyűjtő).',
]

TITLE = 'babylon-grow.eu – Cserép, tálca főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-12 és 2026-10-14. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok.'
NOTES = [
 'Termékek: 1999 termék a Google Shopping-feedből (2024-10 – 2026-10); ebből a cserép–tálca témájú termékek besorolva – a Termékkínálat lapon és a kategórialapok alján.',
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a virágcserép (2400) és a nagy virágcserép (480) viszi az ágat; a sandbox két gyűjtőnevére („Speciális cserép”, „Tálca, alátét”) nincs vagy félrevezető a keresés – javasolt a kettébontásuk (Kategóriaszerkezet-ajánlás lap).',
 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe; a javaslat a sandbox-tervezetre és a kulcsszóadatra épül.',
 'A „szaporító tálca” / „palántanevelő tálca” céloldala a Palántanevelő ág, a „mikrozöld tálca” a Mikrozöld termesztésé – itt csak említés.',
]
OLD_TITLE = 'A sandbox „Cserép, tálca” menünevei – keresési volumen és javasolt név'
OLD_SUB = 'Sandbox-tervezet: Virágcserép; Speciális cserép, szövetcserép; Tálca, alátét.'
EXT_TITLE = 'Rokon, cserepekhez kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más szándékú vagy más főkategóriába tartozó témák – csak ha van hozzá termék.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'

# Termék–kategória hozzárendelés: (termékkódok, elsődleges kategória, [további kategóriák], illeszkedés, megjegyzés)
PAL_CSEREP = 'Palántanevelő ág – Palántanevelő cserép, tőzegcserép'
PAL_TALCA = 'Palántanevelő ág – Palántanevelő tálca'
PRODUCTS = [
 ('GRO2099 GRO2100 GRO2101 GRO2102 GRO2103 GRO2104 GRO2498', 'Virágcserép', [], 'Erős', 'Kerek fekete műanyag cserép'),
 ('GRO2499 GRO2500', 'Virágcserép', ['Nagy virágcserép'], 'Erős', 'Kerek fekete műanyag cserép, 25–30 l'),
 ('GRO1806 GRO1807 GRO1808 GRO1809 GRO1810 GRO2108', 'Virágcserép', [], 'Erős', 'Lyukacsos kerek, spirálgyökér-gátló'),
 ('GRO2109 GRO2110 GRO2111 GRO2494 GRO2495 GRO2496', 'Virágcserép', ['Nagy virágcserép'], 'Erős', 'Lyukacsos kerek, 20–90 l'),
 ('GRO2501 GRO2502 GRO2503 GRO2504 GRO2505 GRO2506 GRO4644 GRO4645 GRO4646 GRO4647 GRO4648 GRO4649 GRO4652 GRO4653', 'Nagy virágcserép', ['Virágcserép'], 'Erős', 'Konténer, 43–155 l'),
 ('GRO4240 GRO4241', 'Virágcserép', [], 'Erős', 'Gyűjtőcsomag (10 db)'),
 ('GRO2359 GRO2356 GRO0748 GRO1189 GRO1143 GRO0068', 'Virágcserép', ['Szögletes cserép'], 'Erős', 'Görög mintás négyzetes'),
 ('GRO0069 GRO0070', 'Virágcserép', ['Szögletes cserép', 'Nagy virágcserép'], 'Erős', 'Görög mintás négyzetes, 25–30 l'),
 ('GRO1160 GRO1161 GRO1259 GRO1141 GRO0067 GRO1261 GRO2360', 'Virágcserép', ['Szögletes cserép'], 'Erős', 'Szögletes, gyökércsavarodás-gátló'),
 ('GRO2107 GRO2497', 'Virágcserép', ['Szögletes cserép'], 'Erős', 'Lyukacsos szögletes, hidropóniához is'),
 ('GRO4613', 'Virágcserép', [], 'Laza', 'Garland magas falú (tálcaszerű) cserép'),
 ('GRO2900 GRO3232 GRO3233 GRO4623 GRO4624 GRO4625 GRO4626', PAL_CSEREP, ['Szögletes cserép'], 'Laza', 'Palántázó kiscserép (4–9 cm)'),
 ('GRO4621 GRO4622', PAL_CSEREP, ['Virágcserép'], 'Laza', 'Vékonyfalú kerek kiscserép'),
 ('GRO2236 GRO2237 GRO3432 GRO3924 GRO4360 GRO4377 GRO4378 GRO4676 GRO2239 GRO3925 GRO4413 GRO4414 GRO4415', PAL_CSEREP, [], 'Más főkategória', 'Tőzeg- / rostcserép – lebomló'),
 ('GRO1890 GRO1891 GRO1892 GRO1893 GRO1894 GRO1895 GRO3346 GRO3525 GRO3526', 'Air-Pot cserép', [], 'Erős', 'Air-Pot (klón) perforált cserép'),
 ('GRO2571', 'Air-Pot cserép', ['Nagy virágcserép'], 'Erős', 'Air-Pot klón 50 l'),
 ('GRO3348 GRO3349 GRO3350', 'Hidro ág – hidro cserép, hidrokosár', ['Air-Pot cserép'], 'Laza', 'Venti Pot – perforált hidro cserép'),
 ('GRO2492 GRO0822 GRO1110 GRO1111 GRO0823 GRO0824 GRO3225 GRO3226 GRO3227 GRO3228 GRO3229 GRO3664 GRO3665 GRO4131 GRO4132 GRO4297 GRO4324', 'Szövetcserép, ültetőzsák', [], 'Erős', 'Szövet- / textilcserép (Smart Pot típus)'),
 ('GRO2572 GRO3230 GRO3666 GRO3667 GRO3668 GRO3669 GRO3670 GRO3671 GRO3672', 'Szövetcserép, ültetőzsák', [], 'Erős', 'Nagy szövetcserép, 39–550 l'),
 ('GRO4696 GRO4698', 'Közegek – kókuszrost', ['Szövetcserép, ültetőzsák'], 'Laza', 'Kókuszrost ültetőzsák (közeg + edény)'),
 ('GRO1813 GRO1184 GRO1185 GRO1049 GRO2105 GRO1814 GRO2106 GRO1190 GRO1262', 'Cserépalátét', [], 'Erős', 'Szögletes cserépalátét'),
 ('GRO3717 GRO4654 GRO4655 GRO4656 GRO4659', 'Cserépalátét', [], 'Erős', 'Kerek cserépalátét'),
 ('GRO4408', 'Cserépalátét', ['Műanyag tálca, árapály asztal'], 'Erős', 'Univerzális alátéttálca'),
 ('GRO4298', 'Cserépalátét', [], 'Laza', 'Víztartályos (önöntöző) alátét szövetcseréphez'),
 ('GRO1909 GRO1910 GRO3773 GRO3774 GRO3775 GRO3776 GRO1911 GRO3777 GRO1912 GRO1462 GRO1908 GRO3138 GRO1906 GRO1907 GRO1463', 'Műanyag tálca, árapály asztal', ['Cserépalátét'], 'Erős', 'Garland tálca (5–15 cm perem)'),
 ('GRO4667 GRO4668 GRO4669 GRO4670 GRO4671 GRO4672 GRO4673 GRO4674 GRO3124', 'Műanyag tálca, árapály asztal', [], 'Erős', 'Secret Jardin vízgyűjtő tálca termesztősátorba'),
 ('GRO3437 GRO2247 GRO2774 GRO3436', 'Műanyag tálca, árapály asztal', [], 'Erős', 'Nutriculture flexibilis tálca'),
 ('GRO0054 GRO0056 GRO0057 GRO1417', 'Műanyag tálca, árapály asztal', [], 'Erős', 'Dán tálca – apály-dagály (árapály) rendszer'),
 ('GRO1817 GRO3363 GRO4234', 'Műanyag tálca, árapály asztal', [], 'Laza', 'Dán tálca kiegészítő'),
 ('GRO4349 GRO4350 GRO4351 GRO4352 GRO4608 GRO4610 GRO4612 GRO4615 GRO4616', PAL_TALCA, ['Cserépalátét'], 'Laza', 'Garland Seed / Mini tálca – cserépalátétként is'),
 ('GRO4633 GRO4634 GRO4635 GRO4684 GRO4686 GRO2987 GRO2246', PAL_TALCA, [], 'Más főkategória', 'Palántanevelő / propagátor tálca'),
 ('GRO3661 GRO3662 GRO4358 GRO4359 GRO4636 GRO4637', 'Mikrozöld termesztés – mikrozöld tálca', [], 'Más főkategória', 'Mikrozöld tálca'),
 ('GRO0663 GRO1291 GRO4309 GRO3378', 'Hidro ág – hidro cserép, hidrokosár', [], 'Más főkategória', 'Hidrokosár / hidro cserép'),
 ('GRO1812 GRO1958 GRO2244 GRO2637 GRO2638', 'Esővízgyűjtő, víztartály', [], 'Más főkategória', 'Esővízgyűjtő / összecsukható víztartály'),
]
