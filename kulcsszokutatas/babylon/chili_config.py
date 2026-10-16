# Babylon – Chillitermesztés (új főkategória, 2026-10-16)
# Csak a FŐKATEGÓRIA NEVE alapján + élő termékkínálat + kulcsszóadat.
# Saját termék csak a chili vetőmag; a többi alkategória más ágak termékeinek szűrt / kereszt-listája
# (hub, mint a Mikrozöld): egy termék, egy URL, több kategória.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

MAG='Chili vetőmag'; PAL='Chili palántanevelés'; TAP='Tápoldat chilihez, paprikához'; CSE='Chili cserépben: föld, cserép'; LED='Chili lakásban: növénylámpa'

CATS = [
 dict(name=MAG, sheet='1 Chili vetőmag', fo='chili paprika mag',
      area='Chili paprika vetőmag fajtánként (Habanero, Jalapeno, Cayenne, Bohócsapka, Etna)',
      place='2. szint – az egyetlen saját termékkör; fajta / csípősség = szűrő',
      note='Chili paprika mag 210, chili mag 170, jalapeno mag 170, carolina reaper mag 260 (nincs ilyen termék – bővítés!), habanero mag 50, chili vetőmag 50. A „chilimag” (210) / „chilimag hu” (110) versenytárs webshop neve – X.',
      kws='''chili paprika mag|S|F
chili mag|S|S
chili vetőmag|S|S
jalapeno mag|S|S
jalapeno paprika mag|S|E
jalapeno vetőmag|S|E
habanero mag|S|S
habanero paprika mag|S|E
cayenne paprika mag|S|E
erős paprika mag|S|E
csípős paprika mag|S|E
chili paprika vetőmag|S|E
chili paprika mag rendelés|S|E
chili paprika mag vásárlás|S|E
carolina reaper mag|S|E
trinidad moruga scorpion mag|S|E
szellem chili mag|S|E
chilimag|X|X
chilimag hu|X|X'''),
 dict(name=PAL, sheet='2 Palántanevelés', fo='chili mag csíráztatás',
      area='Chili magvetés és palántanevelés: propagátor, palántanevelő tálca, Jiffy korong, fűtőlap (a chili 25–30 °C-on csírázik)',
      place='2. szint – szűrt kereszt-lista a Propagátor és a Termesztő közeg ágból; tartalom: csíráztatás lépései',
      note='Paprika mag csíráztatás(a) 140 + 140 (I), paprika mag csíráztatás otthon 90 (I), chili mag csíráztatás 20. A „chili palánta” (170) és „chili paprika palánta” (210) kész palántát keres – nem forgalmazzuk (bővítési lehetőség).',
      kws='''chili mag csíráztatás|S|F
paprika mag csíráztatás|S|I
paprika mag csíráztatása|S|I
paprika mag csíráztatás otthon|S|I
chili paprika mag ültetése|S|I
chili palánta|LN|N
chili paprika palánta|LN|N
jalapeno palánta|LN|N
habanero palánta|LN|N
carolina reaper palánta|LN|N
chili palánta eladó|LN|N'''),
 dict(name=TAP, sheet='3 Tápoldat', fo='paprika tápoldat',
      area='Paprikához / chilihez ajánlott tápoldat: növekedési és virágzási táp, virágzásserkentő, CalMag (a chili kalcium- és magnéziumigényes)',
      place='2. szint – szűrt kereszt-lista a Tápok ágból',
      note='Paprika tápoldat 140, paprika paradicsom tápoldat 90, chili tápoldat 30, chili paprika tápoldat 30, tápoldat paprikához 20. Házilag-keresések (110 / 90) – tartalom.',
      kws='''paprika tápoldat|S|F
paprika paradicsom tápoldat|S|S
chili tápoldat|S|S
chili paprika tápoldat|S|S
tápoldat paprikához|S|E
paprika palánta tápoldatozása|S|I
paprika tápoldat házilag|L|I
paprika palánta tápoldat házilag|L|I'''),
 dict(name=CSE, sheet='4 Föld, cserép', fo='chili paprika cserépben',
      area='Chili termesztése cserépben, balkonon: virágföld (Plagron Allmix, Lightmix, Batmix), szövetcserép',
      place='2. szint – szűrt kereszt-lista a Termesztő közeg és a Cserép ágból',
      note='Chili paprika cserépben 50, chili paprika termesztése cserépben 40; a „virágföld” (2900) céloldala a Termesztő közeg ágban.',
      kws='''chili paprika cserépben|S|F
chili paprika termesztése cserépben|S|I
virágföld|LN|N'''),
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'Chili termesztés 40, chili paprika termesztése 70 – a téma keresése kicsi, a vásárlói szavak a mag (210) és a tápoldat (140). Javasolt menünév: „Chili termesztés” (két szóval, a keresők így írják; a „chillitermesztés” két l-lel nem mért).', '''chili termesztés|S
chili paprika termesztése|S
jalapeno termesztése|S
carolina reaper termesztése|S'''),
 ('Mag', '→ Chili vetőmag', '''chili paprika mag|S
chili mag|S
jalapeno mag|S'''),
 ('Palántanevelés', '→ Chili palántanevelés', '''paprika mag csíráztatása|S
chili palánta|L'''),
 ('Tápanyag', '→ Tápoldat chilihez', '''paprika tápoldat|S
chili tápoldat|S'''),
 ('Fajta, csípősség (tartalom)', 'Blog / fajtaismertető – erős tartalmi kereslet', '''legerősebb paprika|L
világ legerősebb paprikája|L
chili paprika fajtái|L
erős paprika fajták|L
chili fajták|L'''),
]

EXT = [
 ('Fajtaismertető, „legerősebb paprika” (tartalom)', 'Nagy, információs keresés – blog / fajta-oldalak, a vetőmag-kategóriára linkelve', '''legerősebb paprika|L
világ legerősebb paprikája|L
a világ legerősebb paprikája|L
chili paprika fajtái|L
chili paprika fajták képekkel|L
erős paprika fajták|L
legerősebb chili|L'''),
 ('Chili palánta (élő növény)', 'Erős vásárlói szándék, de nem forgalmazzuk – szezonális kínálatbővítési lehetőség', '''chili paprika palánta|L
chili palánta|L
jalapeno palánta|L
carolina reaper palánta|L'''),
 ('Carolina Reaper / szuperforró fajták magja', 'Nincs ilyen vetőmag a kínálatban – bővítés', '''carolina reaper mag|S
trinidad moruga scorpion mag|S'''),
 ('Versenytárs chilimag-webshop', 'Bolt-név keresés – nem célozni', '''chilimag|X
chilimag hu|X'''),
]

MAKERS = '''chilimag
chilimag hu'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Chillitermesztés (csak a főkategória neve + termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Kiindulás: a főkategória neve, az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Saját termék csak a chili vetőmag – a többi alkategória más ágak termékeinek szűrt listája (hub). Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'Chillitermesztés'
STRUCT = [
 (1, FO, '–', 'chili paprika termesztése', 'S', 'Hub főkategória', 'Chili paprika termesztése 70, chili termesztés 40 – hub-leírás + csempék; javasolt menünév: „Chili termesztés”.', None),
 (2, MAG, FO, 'chili paprika mag', 'S', 'Önálló kategória (saját termék)', 'Chili paprika mag 210, chili mag 170, jalapeno mag 170.', MAG),
 (2, PAL, FO, 'chili mag csíráztatás', 'S', 'Szűrt kereszt-lista + tartalom', 'Paprika mag csíráztatása 140 – propagátor, tálca, Jiffy, fűtőlap.', PAL),
 (2, TAP, FO, 'paprika tápoldat', 'S', 'Szűrt kereszt-lista', 'Paprika tápoldat 140.', TAP),
 (2, CSE, FO, 'chili paprika cserépben', 'S', 'Szűrt kereszt-lista', 'Chili paprika cserépben 50 – föld + szövetcserép.', CSE),
 (2, LED, FO, None, '-', 'Navigációs kategória', 'Lakásban termesztéshez kis LED – mérhető keresés nélkül; céloldal a LED ágban.', None),
]
NOT_CATS = [
 ('Fajta szerinti alkategória (Habanero, Jalapeno…)', 'jalapeno mag', '7 vetőmag – szűrő; a fajták tartalmi oldalon.'),
 ('Chili palánta', 'chili palánta', 'Nincs ilyen termék – bővítés (szezonális).'),
 ('Chili szósz, fűszer', 'legerősebb chili szósz', 'Élelmiszer – nem a mi kínálatunk.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak az elmúlt 30 napban a Babylon Google Shopping-feedben szereplő termékek (1525) kaptak kategóriát.',
 'A Chillitermesztés hub: a vetőmag saját kategória; a palántanevelés, tápoldat, föld / cserép és lámpa termékei elsődlegesen a saját águkban vannak („Más főkategória”), ide másodlagosan (szűrt listaként) kerülnek – egy termék, egy URL.',
]
TITLE = 'babylon-grow.eu – Chillitermesztés kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok. Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítások: a termesztésre kicsi a keresés (chili paprika termesztése 70, chili termesztés 40), a vásárlói szavak a mag (chili paprika mag 210, jalapeno mag 170, carolina reaper mag 260) és a tápoldat (paprika tápoldat 140). A legnagyobb a tartalmi kereslet: legerősebb paprika 320, világ legerősebb paprikája 260, chili paprika fajtái 260.',
 'Bővítési lehetőségek: Carolina Reaper / szuperforró vetőmag (260), chili palánta szezonálisan (210 + 170).',
 'Szerkezet: hub főkategória (mint a Mikrozöld) – 1 saját kategória (vetőmag) + szűrt kereszt-listák a meglévő ágakból.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'A keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Tartalom, bővítés és nem célzott témák.'
MAKERS_TITLE = 'Márka- / bolt-keresések'

PRODUCTS = [
 ('GRO4406 GRO4407 GRO4402 GRO4403 GRO4404 GRO4401 GRO4405', MAG, [], 'Erős', 'Chili paprika vetőmag'),
 ('GRO0804 GRO2798 GRO2941 GRO0807 GRO2940 GRO2939', 'Propagátor ág – Propagátor', [PAL], 'Más főkategória', 'Propagátor, fűthető propagátor'),
 ('GRO4635 GRO4633 GRO4634', 'Propagátor ág – Palántanevelő tálca', [PAL], 'Más főkategória', 'Palántanevelő tálca'),
 ('GRO4411 GRO4412 GRO2236 GRO2237', 'Termesztő közeg / Propagátor ág', [PAL], 'Más főkategória', 'Jiffy korong, tőzegcserép'),
 ('GRO4365 GRO1867 GRO4345 GRO4493', 'Propagátor ág – Fűtőlap', [PAL], 'Más főkategória', 'Propagátor fűtőlap'),
 ('GRO1342', 'Tápok ág', [PAL], 'Más főkategória', 'Plagron Seedbooster csíráztató tápoldat'),
 ('GRO0081 GRO0080 GRO0077 GRO0076 GRO0096 GRO0095 GRO0433 GRO0430 GRO0853 GRO0852 GRO0856 GRO0857 GRO0668 GRO0666', 'Tápok ág', [TAP], 'Más főkategória', 'Növekedési / virágzási táp földhöz (kis kiszerelés)'),
 ('GRO3484 GRO3711 GRO3710', 'Tápok ág – CalMag', [TAP], 'Más főkategória', 'CalMag (kalcium + magnézium)'),
 ('GRO1173 GRO1402 GRO1022 GRO1400 GRO0892', 'Termesztő közeg ág – Virágföld', [CSE], 'Más főkategória', 'Plagron földkeverék'),
 ('GRO2492 GRO0822 GRO1110 GRO1111', 'Cserép ág – Szövetcserép', [CSE], 'Más főkategória', 'Szövetcserép 1–10 l'),
 ('GRO4589 GRO4590 GRO4591 GRO4592 GRO4593 GRO4594 GRO4595 GRO4596 GRO4599', 'LED ág – Szobanövény-lámpa', [LED], 'Más főkategória', 'Sansi csíptethető / álló növénylámpa'),
]
