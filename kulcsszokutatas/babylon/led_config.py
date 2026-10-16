# Babylon – Növényvilágítás, LED növénylámpa (2026-10-16, 2. változat)
# A jelenlegi éles ÉS sandbox alkategória-elrendezést NEM vettük figyelembe:
# a szerkezet kizárólag az élő termékkínálatból és a kulcsszóadatból készült.
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='LED növénylámpa, termesztőlámpa', sheet='1 LED termesztőlámpa', fo='teljes spektrumú növénynevelő led lámpa',
      area='Teljes spektrumú LED lámpatest growboxba / termesztőtérbe (panel, QB, bar-típusú lámpatest) – 20 W-tól 1000 W-ig',
      place='2. szint – a termékkör magja; teljesítmény (≤100 / 100–400 / 400+ W), márka és lefedett terület = szűrő, nem alkategória',
      note='A termesztői szándék: teljes spektrumú növénynevelő led lámpa 320, full spectrum led 140, növénynevelő led lámpa 140, növénytermesztő lámpa 110, led grow 70. Wattra és modellre csak ~10/hó – ezért a teljesítmény szűrő. A „led panel” (2400) háztartási mennyezeti lámpa – a névben kerülendő.',
      kws='''teljes spektrumú növénynevelő led lámpa|S|F
full spectrum led|S|S
növénynevelő led lámpa|S|S
növénytermesztő lámpa|S|S
teljes spektrumú led|S|S
növénynevelő led|S|E
led grow|S|S
grow led|S|E
led grow lámpa|S|E
grow led lámpa|S|E
growlight|S|E
full spectrum led lámpa|S|E
teljes spektrumú led lámpa|S|E
növénytermesztő led lámpa|S|E
led növénynevelő lámpa|S|E
ledgrow|L|E
led 300w|S|E
600w led|S|E
1000w led|S|E
lumatek zeus 600w|S|G
lumatek ats 300w pro|S|G
led panel|LN|N
led panel lámpa|LN|N
mars hydro ts 600|X|X
mars hydro ts 1000|X|X'''),
 dict(name='Szobanövény-lámpa, LED növénynevelő izzó', sheet='2 Szobanövény-lámpa', fo='növénynevelő lámpa',
      area='Otthoni, dugaszolós növénylámpa: csíptethető / álló lámpa, E27 LED növénynevelő izzó, kis LED – szobanövény, fűszernövény, palánta, orchidea',
      place='2. szint – a legnagyobb keresés ide tartozik (hobbi / otthoni szándék); a palántanevelő lámpa céloldala a Palántanevelő ágban marad',
      note='A „növénynevelő lámpa” (880), „növény lámpa” (720), „növényeknek lámpa” (720), „növény nevelő lámpa” (260) jellemzően otthoni, kis lámpát keres – erre a Sansi csíptethető / álló lámpák és E27 izzók a válasz. Ha a „növénylámpa” (480) a főkategória fő szava, itt a „növénynevelő lámpa” legyen a H1.',
      kws='''növénynevelő lámpa|S|F
növény lámpa|S|S
növény lampa|S|E
növényeknek lámpa|S|S
növény nevelő lámpa|S|S
led növénylámpa|S|S
növény led lámpa|S|E
led növény lámpa|S|E
növény nevelő led lámpa|S|E
ledes növény lámpa|S|E
led lámpa növényeknek|S|E
led lámpa növény|S|E
lámpa növényeknek|S|E
növény megvilágító lámpa|S|E
szobanövény lámpa|S|E
orchidea lámpa|S|E
legjobb növény lámpa|S|E
novenynevelo lampa|S|E
novenylampa|S|E
noveny led|S|E
növénynevelő izzó|S|S
teljes spektrumú led izzó|S|S
növénynevelő led izzó e27|S|E
teljes spektrumú izzó|S|E
teljes spektrumú lámpa|S|E
csíptetős lámpa|L|E
csíptethető lámpa|L|E
növénynevelő lámpa vélemények|S|I
növény lámpa házilag|L|I
palántanevelő lámpa|L|N
e27 led izzó|LN|N
növény lámpa praktiker|X|X
obi növény lámpa|X|X'''),
 dict(name='LED sáv, LED cső növénylámpa', sheet='3 LED sáv', fo='növény led szalag',
      area='Lineáris LED: LED bar / sáv (Cosmorrow, SANlight Stixx / FLEX II, TNoled), LED cső – polcra, alacsony térbe, dugványhoz, kiegészítő világításnak',
      place='2. szint – saját terméktípus (~40 termék), saját keresési szándék',
      note='A keresők „szalagnak” hívják: növény led szalag 90, teljes spektrumú led szalag 40, full spectrum led szalag 20. A „led cső” (320) és a „led bar” (210) általános / autós – LN. A „por és páramentes led lámpatest” (70) a Sylvania START lámpákra laza kötődésű.',
      kws='''növény led szalag|S|F
teljes spektrumú led szalag|S|S
full spectrum led szalag|S|S
por és páramentes led lámpatest|L|E
led cső|LN|N
led bar|LN|N'''),
 dict(name='UV, IR spektrum-kiegészítő', sheet='4 UV IR', fo='uv lámpa növényekhez',
      area='Kiegészítő spektrum fő lámpa mellé: UV-A / UV-B, IR / far-red add-on LED, UV-B T5, zöld fényű munkalámpa a sötét periódushoz',
      place='2. szint – önálló terméktípus (add-on), kis keresés; a fő lámpák lapján kereszt-ajánlás',
      note='Növény-specifikus UV-keresés kicsi (uv lámpa növényekhez 40, uv lámpa növényeknek 40, uvb led 20). Az „uvb lámpa” (390) terráriumos, az „uv led” (210) köröm / általános, az „infravörös lámpa” (390) melegítő – LN.',
      kws='''uv lámpa növényekhez|S|F
uv lámpa növényeknek|S|S
uvb led|S|E
uv b lámpa|L|E
infravörös led|L|E
zöld fényű lámpa|S|E
zöld fényű fejlámpa|S|E
uvb lámpa|LN|N
uv led|LN|N
infravörös lámpa|LN|N
t5 fénycső|LN|N
t5 led fénycső|LN|N'''),
 dict(name='Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', sheet='5 HPS MH CMH', fo='nátrium lámpa',
      area='Hagyományos (HID) növényvilágítás: HPS / MH / CMH izzó, trafó (előtét), reflektor, Cool Tube, foglalat, komplett lámpaszett',
      place='2. szint; 3. szint vagy szűrő: Izzó – Trafó – Reflektor, Cool Tube – Lámpaszett (55 élő termék, csökkenő kereslet)',
      note='Kis, csökkenő keresés: nátrium lámpa 90, e40 foglalat 70, cmh 50, nátriumlámpa 40, fémhalogén izzó 40, hps lámpa 30. A termékek fele már nem élő – nem érdemes tovább bontani, mint 3. szintű szűrő.',
      kws='''nátrium lámpa|S|F
nátriumlámpa|S|S
nátriumgőz lámpa|S|E
nagynyomású nátriumlámpa|S|E
nátrium izzó|S|S
hps lámpa|S|S
fémhalogén izzó|S|S
fémhalogén|S|E
mh lámpa|S|E
cmh|S|S
e40 foglalat|S|S
hps trafó|S|E
elektronikus előtét|L|E
kompakt fénycső|LN|N'''),
 dict(name='Időkapcsoló, világításvezérlő', sheet='6 Időkapcsoló', fo='időzítő kapcsoló',
      area='Fényciklus vezérlése: mechanikus / digitális konnektoros időkapcsoló, többlámpás időzítő doboz, LED dimmer, világításvezérlő panel',
      place='2. szint – az ág legnagyobb keresési klasztere; ugyanaz a termék, amit a keresők keresnek',
      note='Időzítő kapcsoló 1900, időkapcsoló 1000, digitális időkapcsoló 320, időkapcsolós konnektor 260, mechanikus 170, programozható 170. A kültéri / sínre szerelhető időkapcsoló nem a mi termékünk.',
      kws='''időzítő kapcsoló|S|F
időkapcsoló|S|S
digitális időkapcsoló|S|S
mechanikus időkapcsoló|S|S
programozható időkapcsoló|S|S
időkapcsolós konnektor|S|S
időkapcsolós dugalj|S|E
időkapcsoló konnektor|S|E
konnektoros időkapcsoló|S|E
digitális időzítő kapcsoló|S|E
programozható időzítő kapcsoló|S|E
mechanikus időzítő kapcsoló|S|E
mechanikus kapcsolóóra|S|E
időzítős lámpa|L|E
világítás vezérlő|S|E
led dimmer|L|E
digitális időkapcsoló beállítása|S|I
kültéri időzítő kapcsoló|LN|N'''),
 dict(name='Növénylámpa-kiegészítő: tápegység, kábel, függesztő', sheet='7 Lámpa-kiegészítő', fo='lámpa függesztő',
      area='LED tápegység / driver, tápkábel, elosztó, elektromos kábel, Rope Ratchet, lámpafüggesztő, trafótartó',
      place='2. szint (kiegészítő) – pótalkatrészek; a vásárló márka + modell szerint keres',
      note='A lámpafüggesztőre kicsi a keresés (lámpa függesztő 20, lámpa akasztó 10). A „led tápegység” (590) és a „led driver” (260) jórészt LED-szalaghoz – laza.',
      kws='''lámpa függesztő|S|F
lámpa akasztó|S|E
led tápegység|L|S
led driver|L|S'''),
 dict(name='PAR-mérő, fénymérő', sheet='8 PAR-mérő', fo='par mérő',
      area='A fényerő (PPFD) mérése a lámpa beállításához – PAR / quantum mérő',
      place='3. szint a Kiegészítők alatt VAGY a Mérőműszer ágban (pH / EC mellett) – egy céloldal, a másik helyen link',
      note='Kis, de tiszta szándék (par mérő 20). A „fénymérő” (170) és a „luxmérő” (40) fotós / általános – laza; a luxmérő növényekre pontatlan, a leírásban érdemes elmagyarázni.',
      kws='''par mérő|S|F
fénymérő|L|S
luxmérő|L|E'''),
]

OLD_SHEET = 'A fő keresési szándékok'
OLD = [
 ('Főkategória-név', 'A legnagyobb általános szavak: növény lámpa 720, növényeknek lámpa 720, növénylámpa 480; a „led növényvilágítás” (20) és a „növényvilágítás” (50) kicsi. Javasolt menünév: „Növénylámpa, LED növényvilágítás”; H1: „Növénylámpa – LED és nátrium növényvilágítás”.', '''növénylámpa|S
növénylámpa led|S
növényvilágítás|S
növény világítás|S
led növényvilágítás|S'''),
 ('Otthoni / hobbi szándék', '→ Szobanövény-lámpa, LED növénynevelő izzó', '''növénynevelő lámpa|S
növény lámpa|S
növényeknek lámpa|S
növénynevelő izzó|S'''),
 ('Termesztői szándék', '→ LED növénylámpa, termesztőlámpa', '''teljes spektrumú növénynevelő led lámpa|S
full spectrum led|S
led grow|S'''),
 ('Lineáris LED', '→ LED sáv, LED cső növénylámpa', '''növény led szalag|S
teljes spektrumú led szalag|S'''),
 ('Hagyományos (HID) lámpa', '→ Nátrium- és fémhalogén lámpa', '''nátrium lámpa|S
fémhalogén izzó|S
cmh|S'''),
 ('Fényciklus vezérlése', '→ Időkapcsoló, világításvezérlő', '''időzítő kapcsoló|S
időkapcsoló|S'''),
 ('Teljesítmény (watt)', 'Csak szűrő – nincs rá érdemi keresés', '''600w led|S
1000w led|S
led 300w|S'''),
]

EXT = [
 ('Palántanevelő lámpa', 'Céloldala a Palántanevelő ágban (2026-10-09-i döntés) – innen link; a Sansi / kis LED termékek ott is megjelennek', '''palántanevelő lámpa|S
palánta nevelő lámpa|S
palántanevelő led lámpa|S'''),
 ('Beltéri kert, okos virágcserép', 'Urban Garden konyhakert LED-del – Mikrozöld / Palántanevelő hubban; bővíthető termékkör', '''okos virágcserép|L
smart garden|L'''),
 ('Fényvisszaverő fólia', 'Céloldal a Growbox ágban – a lámpák lapján kereszt-ajánlás', '''fényvisszaverő fólia|S'''),
 ('Akvárium- és terráriumvilágítás', 'Rokon LED / UV termék, nem a mi kínálatunk – csak kínálatbővítés esetén', '''akvárium lámpa|L
akváriumi lámpa|L
terrárium lámpa|L
uvb lámpa|L'''),
 ('Versenytárs LED-márkák', 'Nagy márkakeresés, nem forgalmazott márka (Mars Hydro, Spider Farmer)', '''spider farmer|X
mars hydro|X
hydromars|X'''),
 ('Háztartási LED panel', 'Nagy, de nem növényes – a „LED panel” szót ne használjuk kategórianévben', '''led panel|LN
led panel lámpa|LN'''),
 ('Időkapcsoló (általános)', 'A konnektoros időkapcsoló önmagában is jól kereshető – kertészeti / akváriumos vásárló is', '''időzítő kapcsoló|S
időkapcsolós konnektor|S'''),
]

MAKERS = '''sanlight
lumatek
lumatek ats 300w pro
lumatek zeus 600w
sansi
mars hydro
spider farmer'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – Növénylámpa, LED növényvilágítás (csak termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'A jelenlegi éles és sandbox alkategória-elrendezést NEM vettük figyelembe. Kiindulás: az élő termékkínálat (Google Shopping-feed, elmúlt 30 nap) és a Kulcsszótervező adatai. Termékszám = élő termékek, elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'Növénylámpa, LED növényvilágítás'
KI = 'Növénylámpa-kiegészítő: tápegység, kábel, függesztő'
STRUCT = [
 (1, FO, '–', 'növénylámpa', 'S', 'Főkategória', 'Növény lámpa 720, növényeknek lámpa 720, növénylámpa 480 – a LED és a HID is ide tartozik.', None),
 (2, 'LED növénylámpa, termesztőlámpa', FO, 'teljes spektrumú növénynevelő led lámpa', 'S', 'Önálló kategória', 'Termesztői szándék; teljesítmény / márka / terület = szűrő.', 'LED növénylámpa, termesztőlámpa'),
 (2, 'Szobanövény-lámpa, LED növénynevelő izzó', FO, 'növénynevelő lámpa', 'S', 'Önálló kategória', 'A legnagyobb keresés (növénynevelő lámpa 880) – otthoni, kis lámpa.', 'Szobanövény-lámpa, LED növénynevelő izzó'),
 (2, 'LED sáv, LED cső növénylámpa', FO, 'növény led szalag', 'S', 'Önálló kategória', 'Saját terméktípus (bar / sáv / cső).', 'LED sáv, LED cső növénylámpa'),
 (2, 'UV, IR spektrum-kiegészítő', FO, 'uv lámpa növényekhez', 'S', 'Önálló kategória', 'Add-on termékek a fő lámpa mellé.', 'UV, IR spektrum-kiegészítő'),
 (2, 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', FO, 'nátrium lámpa', 'S', 'Önálló kategória (3. szintű szűrő: izzó / trafó / reflektor / szett)', 'Csökkenő kereslet, a termékek fele nem élő.', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)'),
 (2, 'Időkapcsoló, világításvezérlő', FO, 'időzítő kapcsoló', 'S', 'Önálló kategória', 'Az ág legnagyobb klasztere (időzítő kapcsoló 1900).', 'Időkapcsoló, világításvezérlő'),
 (2, KI, FO, 'lámpa függesztő', 'S', 'Kiegészítő kategória', 'Tápegység, kábel, függesztő – pótalkatrész.', KI),
 (3, 'PAR-mérő, fénymérő', KI, 'par mérő', 'S', 'Kis kategória (vagy Mérőműszer ág)', '2 termék; egy céloldal.', 'PAR-mérő, fénymérő'),
]
NOT_CATS = [
 ('Watt szerinti alkategória (0–100 / 100–400 / 400+ W)', '600w led', 'Wattra ~10/hó keresés – szűrő, nem kategória.'),
 ('„LED panel” kategória', 'led panel', 'Háztartási mennyezeti lámpa (2400) – félrevezető név.'),
 ('LED growbox szett', None, 'Céloldala a Growbox ág „Komplett growbox szett” kategóriája – innen csak link / szűrt lista.'),
 ('Palántanevelő lámpa', 'palántanevelő lámpa', 'Céloldala a Palántanevelő ágban.'),
 ('Márka szerinti alkategória (Lumatek, SANlight, Dimlux)', 'lumatek', 'Márkakeresés kicsi (lumatek 30, sanlight 20) – márkaszűrő.'),
 ('Mars Hydro / Spider Farmer', 'spider farmer', 'Nem forgalmazott márka – nem célozni.'),
]
ACTIVE_ONLY = 'az elmúlt 30 napban'
PRODUCT_NOTE = [
 'ÉLŐ KÍNÁLAT ALAPJÁN (2026-10-16): csak azok a termékek kaptak kategóriát, amelyek az elmúlt 30 napban szerepeltek a Babylon Google Shopping-feedben (1525 termék) – ez az éles oldal aktuális kínálata. A korábban hirdetett, de most nem élő termékek „Nem aktív” jelöléssel a lap végén vannak, javasolt kategóriával.',
 'A kategóriaszerkezet a jelenlegi éles és sandbox alkategóriáktól függetlenül, terméktípus és keresési szándék alapján készült. Az éles oldal (babylon-grow.eu) és a Shoprenter API a felhőből nem érhető el.',
 'A teljesítmény (W) a lámpatesteknél szűrő; a ≤ 100 W-os LED lámpatestek másodlagosan a Szobanövény-lámpa kategóriában is szerepelnek.',
]

TITLE = 'babylon-grow.eu – Növénylámpa, LED növényvilágítás kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15/16. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok (a 10-es érték a legkisebb lépcső). Termékek: élő kínálat = Google Shopping-feed, elmúlt 30 nap (1525 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Módszer: a jelenlegi alkategóriákat (éles és sandbox) figyelmen kívül hagytuk – a szerkezet a termékek típusából (lámpatest, sáv, izzó, add-on, HID, vezérlés, kiegészítő) és a keresési szándékból (otthoni vs. termesztői) épül.',
 'Fő megállapítás: a legnagyobb keresés otthoni / hobbi szándékú (növénynevelő lámpa 880, növény lámpa 720, növényeknek lámpa 720) → külön „Szobanövény-lámpa” kategória; a termesztői LED-re kisebb, de vásárlásközeli a keresés (teljes spektrumú növénynevelő led lámpa 320).',
 'A watt szerinti bontásra nincs keresés → szűrő. Az időkapcsoló a legnagyobb klaszter (időzítő kapcsoló 1900) – saját kategóriát érdemel.',
 'A „LED panel” (2400) háztartási mennyezeti lámpa – kategórianévben kerülendő.',
]
OLD_TITLE = 'A fő keresési szándékok és a hozzájuk javasolt kategória'
OLD_SUB = 'Nem a jelenlegi menü, hanem a keresési szándékok csoportosítása (Kulcsszótervező, HU, 12 hó átlag).'
EXT_TITLE = 'Kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Más ágban lévő céloldalak, kereszt-linkek és kínálatbővítési lehetőségek.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO3357 GRO3371 GRO3463 GRO3529 GRO3598 GRO3599 GRO3600 GRO3673 GRO3703 GRO3704 GRO3828 GRO3893 GRO3908 GRO3930 GRO3931 GRO3932 GRO3940 GRO3971 GRO4003 GRO4048 GRO4101 GRO4102 GRO4109 GRO4140 GRO4141 GRO4164 GRO4165 GRO4166 GRO4171 GRO4172 GRO4190 GRO4210 GRO4211 GRO4226 GRO4227 GRO4308 GRO4312 GRO4326 GRO4327 GRO4362 GRO4535 GRO4536 GRO4537 GRO4579 GYUJTO0205 GRO3846 GRO3849 GRO3850 GRO3851 GRO3852 GRO3853 GRO3854 GRO3855 GRO3856 GRO3857 GRO3858 GRO3859', 'LED növénylámpa, termesztőlámpa', [], 'Erős', 'Teljes spektrumú LED lámpatest growboxba / termesztőtérbe (Lumatek, Dimlux, SANlight EVO, AAW Hellion, Agrolite QB, Urban Garden Q / Polaris, LEDMAXECO…) – teljesítmény = szűrő'),
 ('GRO3568 GRO3574 GRO4100 GRO4139', 'LED növénylámpa, termesztőlámpa', ['Szobanövény-lámpa, LED növénynevelő izzó'], 'Erős', 'Kis teljesítményű (≤ 100 W) LED lámpatest – szobanövényhez, palántához is'),
 ('GRO3860 GRO3861 GRO3862 GRO3863 GRO3864', 'LED növénylámpa, termesztőlámpa', ['Növénylámpa-kiegészítő: tápegység, kábel, függesztő'], 'Erős', 'SANlight EVO szett (lámpa + tápegység)'),
 ('GRO3103 GRO3104 GRO3390 GRO3592 GRO3593 GRO3760 GRO3803 GRO3910 GRO3800 GRO3801 GRO3802 GRO3731 GRO3762 GRO3840 GRO3804 GRO3805 GRO4103 GRO4039 GRO4707 GRO4708 GRO4709 GRO4710 GRO4367 GRO4097 GRO4098 GRO4099', 'LED sáv, LED cső növénylámpa', [], 'Erős', 'LED sáv / bar növénylámpa (Cosmorrow, TNoled, SANlight Stixx / FLEX II, Green Force, Agrolite CB, Urban Garden Clone)'),
 ('GRO4597 GRO4598', 'LED sáv, LED cső növénylámpa', ['Szobanövény-lámpa, LED növénynevelő izzó'], 'Erős', 'Sansi LED cső növénylámpa'),
 ('GRO4423 GRO4424 GRO4425 GRO4426 GRO4427 GRO4428', 'LED sáv, LED cső növénylámpa', [], 'Laza', 'Sylvania START vízálló LED lámpatest – általános (por és páramentes) világítás, anyanövény / szárító'),
 ('GRO4585 GRO4586 GRO4587 GRO4588', 'Szobanövény-lámpa, LED növénynevelő izzó', [], 'Erős', 'Sansi LED növénynevelő izzó E27'),
 ('GRO4589 GRO4590 GRO4591 GRO4592 GRO4593 GRO4594 GRO4595 GRO4596 GRO4599', 'Szobanövény-lámpa, LED növénynevelő izzó', [], 'Erős', 'Sansi csíptethető / álló szobanövény-lámpa'),
 ('GRO4419 GRO4420 GRO4422', 'Szobanövény-lámpa, LED növénynevelő izzó', [], 'Laza', 'Sylvania ToLEDo LED izzó E27 – általános fényű'),
 ('GRO3874 GRO3919', 'Szobanövény-lámpa, LED növénynevelő izzó', ['Növénylámpa-kiegészítő: tápegység, kábel, függesztő'], 'Erős', 'E27 foglalat'),
 ('GRO3392 GRO3393 GRO3594 GRO3595 GRO4167 GRO4168 GRO4173 GRO4174 GRO4175 GRO3877', 'UV, IR spektrum-kiegészítő', [], 'Erős', 'UV / IR (NIR) / far-red kiegészítő LED (Cosmorrow, Dimlux, Lumatek)'),
 ('GRO4169 GRO4170 GRO2988', 'UV, IR spektrum-kiegészítő', [], 'Erős', 'UV-B T5 booster, UV-A lámpa'),
 ('GRO1698 GRO2585', 'UV, IR spektrum-kiegészítő', [], 'Laza', 'T5 fénycső (Lightwave reflektorhoz)'),
 ('GRO2369 GRO4510', 'UV, IR spektrum-kiegészítő', [], 'Erős', 'Zöld fényű lámpa a sötét periódushoz'),
 ('GRO3875 GRO3876 GRO3881', 'UV, IR spektrum-kiegészítő', ['Növénylámpa-kiegészítő: tápegység, kábel, függesztő'], 'Erős', 'Lumatek UV bar kábel'),
 ('GRO0001 GRO0002 GRO1175 GRO1176 GRO1279 GRO2271 GRO2520 GRO2757 GRO2876 GRO2877 GRO2879 GRO3154 GRO3155 GRO3156 GRO3157 GRO3219 GRO3265 GRO3269 GRO3325 GRO3573', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', [], 'Erős', 'HPS (nátrium) izzó'),
 ('GRO2521 GRO2880 GRO2881 GRO2882 GRO2883 GRO3267 GRO3268 GRO3688', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', [], 'Erős', 'MH (fémhalogén) izzó'),
 ('GRO3174 GRO3175 GRO3188 GRO3207', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', [], 'Erős', 'CMH (kerámia fémhalogén) izzó'),
 ('GRO1247 GRO3473 GRO3476', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', ['Szobanövény-lámpa, LED növénynevelő izzó'], 'Laza', 'Agrolite CFL (kompakt fénycső) növénynevelő izzó'),
 ('GRO0504 GRO0616 GRO0618 GRO0619 GRO2607 GRO2608 GRO2997 GRO3153 GRO3171 GRO3176 GRO3177 GRO3202 GRO3223 GRO3364 GRO3365 GRO3366 GRO3657 GRO4004', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', [], 'Erős', 'Trafó (mágneses / digitális előtét)'),
 ('GRO1192 GRO1622 GRO1773 GRO1774 GRO3234 GRO3294 GRO3295 GRO3296 GRO3297 GRO3309V GRO3310 GRO3310V GRO3311V GRO3312V GRO3313 GRO3313V GRO3315 GRO3315V GRO3316 GRO3316V GRO3317 GRO3317V GRO3318 GRO3318V GRO3319 GRO3319V GRO3320 GRO3320V GRO3322 GRO3322V GRO3470 GRO3470V GRO3471V GRO3647 GRO3648 GRO3649 GRO3386 GRO3389 GYUJTO0135', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', [], 'Erős', 'Reflektor, Cool Tube (Adjust-A-Wings, Azerwing, Spudnik, Daisy)'),
 ('GRO0506 GRO0835 GRO3298 GRO3682', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', ['Növénylámpa-kiegészítő: tápegység, kábel, függesztő'], 'Erős', 'E40 foglalat, reflektor-kiegészítő'),
 ('GRO3182 GRO3189 GYSZ0005 GYSZ0005V GYSZ0006 GYSZ0006V GYSZ0007 GYSZ0007V GYSZ0023 GYSZ0023V', 'Nátrium- és fémhalogén lámpa (HPS, MH, CMH)', [], 'Erős', 'Komplett HPS / CMH lámpaszett'),
 ('GRO0787 GRO1105 GRO3683 GRO3750 GRO4013 GRO4014 GRO4015 GRO4016 GRO4115', 'Időkapcsoló, világításvezérlő', [], 'Erős', 'Mechanikus / digitális időkapcsoló'),
 ('GRO1201 GRO1350', 'Időkapcsoló, világításvezérlő', ['Nátrium- és fémhalogén lámpa (HPS, MH, CMH)'], 'Erős', 'GSE időzítő kapcsolódoboz több lámpához'),
 ('GRO3651 GRO3652 GRO3179 GRO3410', 'Időkapcsoló, világításvezérlő', ['Növénylámpa-kiegészítő: tápegység, kábel, függesztő'], 'Erős', 'Világításvezérlő, dimmer (SANlight EVO, Lumatek Control Panel)'),
 ('GRO3394 GRO3395 GRO3596 GRO3597 GRO3911 GRO3806 GRO3807 GRO4706 GRO4711 GRO4712', 'Növénylámpa-kiegészítő: tápegység, kábel, függesztő', ['LED sáv, LED cső növénylámpa'], 'Erős', 'LED tápegység (Cosmorrow Power, SANlight wallplug / driver)'),
 ('GRO3148 GRO3287 GRO3290 GRO3650 GRO3816 GRO3820 GRO3821 GRO3873 GRO3659 GRO4282 GRO4283', 'Növénylámpa-kiegészítő: tápegység, kábel, függesztő', [], 'Erős', 'LED tápkábel, összekötő, elosztó'),
 ('GRO1023 GRO1074 GRO1194 GRO1241 GRO2025 GRO2228 GRO2299 GYSZ0061', 'Növénylámpa-kiegészítő: tápegység, kábel, függesztő', [], 'Erős', 'Elektromos kábel trafóhoz, lámpához'),
 ('GRO0770 GRO4270 GRO4122 GRO3398 GRO3723', 'Növénylámpa-kiegészítő: tápegység, kábel, függesztő', ['Growbox ág – Growbox kiegészítő'], 'Erős', 'Rope Ratchet, lámpafüggesztő, trafótartó, kábelakasztó'),
 ('GRO4147 GRO4148', 'PAR-mérő, fénymérő', ['Mérőműszer ág'], 'Erős', 'PAR-mérő (Photobio Quantum, Neptune)'),
 ('GYSZ0054 GYSZ0054V GYSZ0059 GYSZ0059V GYSZ0060 GYSZ0060V GYSZ0062 GYSZ0062V GYSZ0063 GYSZ0063V GYSZ0064 GYSZ0064V GYSZ0065 GYSZ0065V GYSZ0066 GYSZ0066V GYSZ0067 GYSZ0067V GRO4142 GRO4143 GRO4144 GRO4106 GRO4188 GRO4189 GRO4583', 'Growbox ág – Komplett growbox szett', ['LED növénylámpa, termesztőlámpa'], 'Más főkategória', 'LED growbox szett – céloldal a Growbox ágban; innen link / szűrt lista'),
 ('GYSZ0012 GYSZ0013 GYSZ0013V GYSZ0015 GYSZ0015V GYSZ0016 GYSZ0016V GYSZ0018 GYSZ0018V', 'Growbox ág – Komplett growbox szett', ['Nátrium- és fémhalogén lámpa (HPS, MH, CMH)'], 'Más főkategória', 'HPS growbox szett'),
 ('GRO4307 GRO2943 GRO2942', 'Palántanevelő / Mikrozöld ág – beltéri kert, propagátor', ['Szobanövény-lámpa, LED növénynevelő izzó'], 'Más főkategória', 'Propagátor / konyhakert beépített LED-del (okos virágcserép, smart garden)'),
 ('GRO0821 GRO4306', 'Növényfeldolgozás ág – Hasznos kiegészítők', [], 'Más főkategória', 'Mikroszkóp, nagyító LED-del'),
]
