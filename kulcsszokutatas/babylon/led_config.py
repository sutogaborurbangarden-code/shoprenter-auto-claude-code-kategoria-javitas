# Babylon – LED növényvilágítás (sandbox-főkategória, 2026-10-15)
# kulcsszó | kötődés-kód (S/L/LN/X) | felhasználás-kód (F/S/E/I/N/X/G)

CATS = [
 dict(name='LED növénylámpa 0–100 W', sheet='1 LED 0-100W', fo='növénynevelő lámpa',
      area='Kis teljesítményű LED növénylámpa – szobanövény, palánta, dugvány, kis growbox (≤ 100 W)',
      place='2. szint – menünév marad, H1 / title: „Kis teljesítményű LED növénylámpa, növénynevelő lámpa” (a 2026-10-09-i döntés szerint)',
      note='A „növénynevelő lámpa” (880), „növény lámpa” (720), „növényeknek lámpa” (720) jórészt hobbi / szobanövény szándék = kis lámpa. A palántanevelő lámpa (390) céloldala a Palántanevelő ágban van – itt csak link.',
      kws='''növénynevelő lámpa|S|F
növény lámpa|S|S
növény lampa|S|E
növényeknek lámpa|S|S
növény nevelő lámpa|S|S
növénynevelő led lámpa|S|S
növénynevelő led|S|E
led növénylámpa|S|S
led növénynevelő lámpa|S|E
növény led lámpa|S|E
led növény lámpa|S|E
növény nevelő led lámpa|S|E
ledes növény lámpa|S|E
led lámpa növényeknek|S|E
led lámpa növény|S|E
lámpa növényeknek|S|E
növény megvilágító lámpa|S|E
szobanövény lámpa|S|E
legjobb növény lámpa|S|E
novenynevelo lampa|S|E
novenylampa|S|E
noveny led|S|E
növénynevelő lámpa vélemények|S|I
növény lámpa házilag|L|I
palántanevelő lámpa|L|N
por és páramentes led lámpatest|L|E
növény lámpa praktiker|X|X
obi növény lámpa|X|X'''),
 dict(name='LED növénylámpa 100–400 W', sheet='2 LED 100-400W', fo='teljes spektrumú növénynevelő led lámpa',
      area='Közepes teljesítményű, teljes spektrumú LED – 60×60 … 120×120 cm-es growboxhoz',
      place='2. szint – menünév marad; H1: „Teljes spektrumú LED növénylámpa 100–400 W”',
      note='A „teljes spektrumú növénynevelő led lámpa” (320) és a „full spectrum led” (140) a termesztői szándék. Mars Hydro (TS 600: 90, TS 1000: 70) és Spider Farmer (480) versenytárs-márka, nem forgalmazzuk – nem célozni.',
      kws='''teljes spektrumú növénynevelő led lámpa|S|F
full spectrum led|S|S
teljes spektrumú led|S|S
full spectrum led lámpa|S|E
teljes spektrumú led lámpa|S|E
teljes spektrumú lámpa|S|E
növénytermesztő lámpa|S|S
növénytermesztő led lámpa|S|E
led 300w|S|E
lumatek ats 300w pro|S|G
mars hydro ts 600|X|X
mars hydro ts 1000|X|X'''),
 dict(name='LED növénylámpa 400 W felett', sheet='3 LED 400W+', fo='led grow',
      area='Nagy teljesítményű professzionális LED (Lumatek ZEUS, Dimlux, SANlight EVO, AAW Hellion) – 120×120 cm-től',
      place='2. szint – menünév: „LED növénylámpa 400 W felett” (a „400+W” jelölés helyett)',
      note='Kis, szakmai keresés: led grow 70, grow led 40, ledgrow 210 (részben webshopnév). Wattra (600w led, 1000w led) és modellre (lumatek zeus 600w) 10/hó. Márka- és modellszűrő fontos.',
      kws='''led grow|S|F
grow led|S|S
led grow lámpa|S|E
grow led lámpa|S|E
growlight|S|E
ledgrow|L|E
600w led|S|E
1000w led|S|E
lumatek zeus 600w|S|G
lumatek 600w|S|G'''),
 dict(name='HPS, MH, CMH izzó, trafó, reflektor', sheet='4 HPS MH CMH', fo='nátrium lámpa',
      area='Hagyományos (HID) növényvilágítás – nátrium, fémhalogén, CMH izzó, trafó (előtét), reflektor, Cool Tube, lámpaszett',
      place='2. szint (sandbox: „Növénylámpa izzók – HPS, MH, CMH”) – a trafó és a reflektor is ide kerüljön (eddig nincs helye a fában)',
      note='Csökkenő, kis keresés: nátrium lámpa 90, e40 foglalat 70, cmh 50, nátriumlámpa 40, fémhalogén izzó 40. A HID-termékek száma viszont nagy (~120) – 3. szintű bontás javasolt: Izzó; Trafó; Reflektor, Cool Tube; Lámpaszett.',
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
 dict(name='UV, IR és kiegészítő LED', sheet='5 UV IR kieg LED', fo='uv lámpa növényekhez',
      area='Spektrum-kiegészítés: UV-A / UV-B, IR (far-red) add-on LED, T5, zöld fényű munkalámpa',
      place='2. szint (sandbox: „Speciális LED növényvilágítás”) – a „speciális” szóra nincs keresés; javasolt: „UV, IR és kiegészítő LED”',
      note='Növény-specifikus UV keresés kicsi (uv lámpa növényekhez 40, uv lámpa növényeknek 40, uvb led 20). Az „uvb lámpa” (390) hüllő-terrárium, az „uv led” (210) köröm / általános – laza. A „t5 fénycső” (260) általános világítás.',
      kws='''uv lámpa növényekhez|S|F
uv lámpa növényeknek|S|S
uv b lámpa|L|E
uvb led|S|E
uvb lámpa|LN|N
uv led|LN|N
infravörös led|L|E
infravörös lámpa|LN|N
t5 fénycső|LN|N
t5 led fénycső|LN|N
led bar|LN|N
zöld fényű lámpa|S|E
zöld fényű fejlámpa|S|E'''),
 dict(name='LED növénynevelő izzó, csíptethető lámpa', sheet='6 LED izzó', fo='növénynevelő izzó',
      area='E27 foglalatú LED növénynevelő izzó és csíptethető / álló növénylámpa (Sansi) – szobanövényhez, palántához',
      place='Új 2. szintű kategória (a „Speciális” helyett / mellett); a Sansi csíptethető lámpák a 0–100 W kategóriában is',
      note='Saját szándékú, kis klaszter (növénynevelő izzó 50, teljes spektrumú led izzó 40, növénynevelő led izzó e27 20). Az „e27 led izzó” (1900) általános háztartási – LN.',
      kws='''növénynevelő izzó|S|F
teljes spektrumú led izzó|S|S
növénynevelő led izzó e27|S|S
teljes spektrumú izzó|S|E
csíptetős lámpa|L|E
csíptethető lámpa|L|E
orchidea lámpa|S|E
növény led szalag|S|E
teljes spektrumú led szalag|S|E
full spectrum led szalag|S|E
e27 led izzó|LN|N'''),
 dict(name='LED tápegység, kábel, vezérlő', sheet='7 Tápegység, vezérlő', fo='led tápegység',
      area='LED driver / tápegység, tápkábel, elosztó, dimmer, világításvezérlő (Lumatek Control Panel, SANlight), elektromos kábel',
      place='Új 2. szintű kiegészítő kategória – eddig nincs helye a sandboxban',
      note='A „led tápegység” (590), „led driver” (260), „led dimmer” (210) LED-szalaghoz is keresett – laza; a mi termékeink lámpa-specifikus pótalkatrészek, a vásárlók márka + modell szerint keresik.',
      kws='''led tápegység|L|F
led driver|L|S
led dimmer|L|S
világítás vezérlő|S|E'''),
 dict(name='Lámpafüggesztő, időkapcsoló', sheet='8 Függesztő, időkapcsoló', fo='időzítő kapcsoló',
      area='Mechanikus / digitális időkapcsoló, többlámpás időzítő doboz (GSE), Rope Ratchet, lámpafüggesztő',
      place='2. szint (sandbox: „Növénylámpa függesztők és időzítők”) – javasolt: „Lámpafüggesztő, időkapcsoló” (a keresők „időkapcsolót” írnak)',
      note='Az időkapcsoló-klaszter nagy (időzítő kapcsoló 1900, időkapcsoló 1000, digitális 320, időkapcsolós konnektor 260) és a mi termékünk is ugyanaz a konnektoros időkapcsoló. A kültéri / sínre szerelhető változat nem a mi termékünk. A függesztőre kicsi (lámpa függesztő 20).',
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
digitális időkapcsoló beállítása|S|I
lámpa függesztő|S|S
lámpa akasztó|S|E
kültéri időzítő kapcsoló|LN|N'''),
 dict(name='LED growbox szett', sheet='9 LED growbox szett', fo='grow box szett',
      area='Sátor + LED + szellőzés egy csomagban – navigációs belépő a LED ágból',
      place='2. szint – navigációs (szűrt lista / link); a céloldal a Growbox ág „Komplett growbox szett” kategóriája (kannibalizáció!)',
      note='Kis keresés (grow box szett 20, grow box led 10, növénytermesztő sátor szett 40 – ez utóbbi a Growbox ág fő kulcsszava). Itt ne legyen saját title / H1 a szett-kulcsszavakra.',
      kws='''grow box szett|S|F
grow box led|S|E
növénytermesztő sátor szett|S|N'''),
]

OLD_SHEET = 'Sandbox menünevek'
OLD = [
 ('LED növényvilágítás (főkategória)', 'A „led növényvilágítás” (20) és a „növényvilágítás” (50) kicsi; a fő szavak a „növénylámpa” (480), „növény lámpa” (720), „növénynevelő lámpa” (880). Javasolt H1: „LED növénylámpa, növényvilágítás”.', '''led növényvilágítás|S
növényvilágítás|S
növény világítás|S
növénylámpa|S
növénylámpa led|S'''),
 ('LED növénylámpa 0-100W', 'Marad (navigációs + „Kis teljesítményű LED növénylámpa” H1).', '''növénynevelő lámpa|S
led növénylámpa|S'''),
 ('LED növénylámpa 100-400W', 'Marad.', '''teljes spektrumú növénynevelő led lámpa|S
full spectrum led|S'''),
 ('LED növénylámpa 400+W', 'Marad; menünévben „400 W felett”.', '''led grow|S
600w led|S'''),
 ('Növénylámpa izzók - HPS, MH, CMH', '→ „HPS, MH, CMH izzó, trafó, reflektor” – a trafónak és a reflektornak sincs más helye.', '''nátrium lámpa|S
fémhalogén izzó|S
cmh|S'''),
 ('Speciális LED növényvilágítás', '→ „UV, IR és kiegészítő LED” + új „LED növénynevelő izzó, csíptethető lámpa”.', '''uv lámpa növényekhez|S
növénynevelő izzó|S'''),
 ('Növénylámpa függesztők és időzítők', '→ „Lámpafüggesztő, időkapcsoló”.', '''időkapcsoló|S
időzítő kapcsoló|S
lámpa függesztő|S'''),
 ('LED growbox szettek', 'Navigációs; céloldal a Growbox ágban.', '''grow box szett|S
grow box led|S'''),
]

EXT = [
 ('Versenytárs LED-márkák (Mars Hydro, Spider Farmer)', 'Nagy márkakeresés, de nem forgalmazott márka – csak ha bekerül a kínálatba', '''spider farmer|X
mars hydro|X
hydromars|X
spiderfarmer eu|X'''),
 ('Akváriumvilágítás', 'Rokon LED-termék, nem a mi kínálatunk', '''növényes akvárium led világítás|LN'''),
 ('UV lámpa (köröm, terrárium, fertőtlenítés)', 'Nagy, de nem növényes szándék', '''uvb lámpa|LN
uv led|LN'''),
 ('Kompakt fénycső, T5 általános világítás', 'Csökkenő, háztartási', '''kompakt fénycső|LN
t5 fénycső|L'''),
]

MAKERS = '''sanlight
lumatek
lumatek ats 300w pro
lumatek zeus 600w
sansi
mars hydro
spider farmer'''

STRUCT_TITLE = 'Kategóriaszerkezet-ajánlás – LED növényvilágítás (termékkínálat + kulcsszóadat alapján)'
STRUCT_SUB = 'Az éles oldal jelenlegi kategóriáit nem vettük figyelembe. Kiindulás: a sandbox-tervezet, a Google Shopping-feed termékei (1999 db) és a Kulcsszótervező adatai. Termékszám = elsődleges + másodlagos hozzárendelés.'
PRODUCT_COUNT_TEXT = 'termékexport szükséges'
FO = 'LED növényvilágítás'
HID = 'HPS, MH, CMH izzó, trafó, reflektor'
STRUCT = [
 (1, FO, '–', 'növénylámpa', 'S', 'Főkategória', 'Fő szavak: növénylámpa 480, növény lámpa 720 – H1: „LED növénylámpa, növényvilágítás”. A HID-termékek is ide tartoznak, ezért a főkategória-név tágabb is lehet: „Növényvilágítás, LED növénylámpa”.', None),
 (2, 'LED növénylámpa 0–100 W', FO, 'növénynevelő lámpa', 'S', 'Önálló kategória', 'Növénynevelő lámpa 880 – a legnagyobb termékkulcsszó.', 'LED növénylámpa 0–100 W'),
 (2, 'LED növénylámpa 100–400 W', FO, 'teljes spektrumú növénynevelő led lámpa', 'S', 'Önálló kategória', 'Teljes spektrumú növénynevelő led lámpa 320, full spectrum led 140.', 'LED növénylámpa 100–400 W'),
 (2, 'LED növénylámpa 400 W felett', FO, 'led grow', 'S', 'Önálló kategória', 'Szakmai, kis keresés; márka / modell szűrő.', 'LED növénylámpa 400 W felett'),
 (2, HID, FO, 'nátrium lámpa', 'S', 'Gyűjtőkategória', 'Sok termék, kis keresés – 3. szint: Izzó / Trafó / Reflektor, Cool Tube / Lámpaszett (szűrőként is működhet).', HID),
 (2, 'UV, IR és kiegészítő LED', FO, 'uv lámpa növényekhez', 'S', 'Önálló kategória', 'Sandbox: „Speciális LED növényvilágítás”.', 'UV, IR és kiegészítő LED'),
 (2, 'LED növénynevelő izzó, csíptethető lámpa', FO, 'növénynevelő izzó', 'S', 'Önálló kategória (új)', 'Sansi E27 izzó és csíptethető lámpák.', 'LED növénynevelő izzó, csíptethető lámpa'),
 (2, 'Lámpafüggesztő, időkapcsoló', FO, 'időzítő kapcsoló', 'S', 'Önálló kategória', 'Időzítő kapcsoló 1900, időkapcsoló 1000 – az ág legnagyobb klasztere.', 'Lámpafüggesztő, időkapcsoló'),
 (2, 'LED tápegység, kábel, vezérlő', FO, 'led tápegység', 'L', 'Kiegészítő kategória (új)', 'Pótalkatrészek, vezérlők – eddig nincs helye.', 'LED tápegység, kábel, vezérlő'),
 (2, 'LED growbox szett', FO, 'grow box szett', 'S', 'Navigációs kategória', 'Céloldal: Growbox ág – Komplett growbox szett.', 'LED growbox szett'),
]
NOT_CATS = [
 ('Mars Hydro / Spider Farmer márkakategória', 'spider farmer', 'Nem forgalmazott márka – nem célozni.'),
 ('Palántanevelő LED lámpa', 'palántanevelő lámpa', 'Céloldala a Palántanevelő ágban (2026-10-09-i döntés) – itt link.'),
 ('UV lámpa (általános)', 'uvb lámpa', 'Hüllő-terrárium / köröm – nem növényes szándék.'),
 ('E27 LED izzó (általános)', 'e27 led izzó', 'Háztartási izzó – csak a növénynevelő izzó ide.'),
 ('Kompakt fénycső', 'kompakt fénycső', 'Csak 3 Agrolite CFL – a HID-ágban, szűrőként.'),
]
PRODUCT_NOTE = [
 'Forrás: a Babylon Google Ads fiók Shopping-termékadatai (termékkód = Shopping item ID, terméknév = feed-cím), 2024-10-01 – 2026-10-14, összesen 1999 termék. A Shoprenter API és az éles oldal a felhőből nem érhető el.',
 'Figyelem: ez a Google-ben hirdetett termékkör, nem feltétlenül a teljes katalógus. A gyártó és a gyűjtőtermék (GYUJTO…) adat a feedben nem érhető el.',
 'Teljesítmény szerinti besorolás a terméknévben szereplő watt alapján (0–100 W / 100–400 W / 400 W felett). Ahol a névben nincs watt (SANlight EVO 1.5 lámpák és szettek, hortiONE, Cosmorrow készletek), becsült érték – ellenőrizendő; GRO3357 és GRO3846 teljesítménye ismeretlen.',
 'A LED growbox szettek elsődlegesen itt (navigációs), másodlagosan a Growbox ág „Komplett growbox szett” kategóriájában – a céloldal ott van.',
]

TITLE = 'babylon-grow.eu – LED növényvilágítás főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
SOURCE = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-15. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok (a 10-es érték a legkisebb lépcső). Termékek: Google Shopping-feed (1999 termék).'
NOTES = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a keresők nem wattban, hanem „növénynevelő lámpa” (880), „növény lámpa” (720), „növényeknek lámpa” (720), „növénylámpa” (480) formában keresnek – ez a kis / hobbi lámpa szándéka. A nagy teljesítményű LED-re kicsi a keresés (led grow 70), a watt-szerinti bontás navigációs.',
 'A „Speciális LED” névre nincs keresés → „UV, IR és kiegészítő LED” + új „LED növénynevelő izzó, csíptethető lámpa”.',
 'Az időkapcsoló a legnagyobb klaszter az ágban (időzítő kapcsoló 1900, időkapcsoló 1000) – a „Növénylámpa függesztők és időzítők” helyett „Lámpafüggesztő, időkapcsoló”.',
 'A HID-ág (HPS, MH, CMH) termékszáma nagy, keresése kicsi – a trafó és a reflektor ide kerüljön (a sandboxban nincs helyük).',
 'A Mars Hydro (320) és a Spider Farmer (480) versenytárs-márka – nem forgalmazzuk.',
]
OLD_TITLE = 'A sandbox „LED növényvilágítás” menünevei – keresési volumen és javaslat'
OLD_SUB = 'Sandbox-tervezet: LED növénylámpa 0-100W / 100-400W / 400+W; Növénylámpa izzók - HPS, MH, CMH; Speciális LED növényvilágítás; Növénylámpa függesztők és időzítők; LED growbox szettek.'
EXT_TITLE = 'Rokon területek (Kulcsszótervező, HU, 12 hó átlag)'
EXT_SUB = 'Nagy volumenű, de nem forgalmazott vagy nem növényes szándékú témák.'
MAKERS_TITLE = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő kérdéséhez)'

PRODUCTS = [
 ('GRO3103 GRO3104 GRO3357 GRO3568 GRO3574 GRO4039 GRO4097 GRO4098 GRO4099 GRO4100 GRO4139 GRO4367 GRO4707 GRO4708 GRO4709 GRO3804 GRO3805 GRO4103 GRO3731 GRO3762 GRO3840 GRO3390 GRO3592 GRO3593 GRO3760 GRO3803 GRO3910 GRO3800 GRO3801 GRO3849 GRO3860', 'LED növénylámpa 0–100 W', [], 'Erős', 'LED növénylámpa ≤ 100 W (Cosmorrow, TNoled, SANlight FLEX / Stixx, Clone, Agrolite, Green Force LED sáv…). GRO3357 teljesítménye ellenőrizendő'),
 ('GRO3463 GRO3598 GRO3599 GRO3828 GRO3931 GRO3932 GRO3971 GRO4101 GRO4102 GRO4109 GRO4140 GRO4141 GRO4190 GRO4210 GRO4211 GRO4308 GRO4312 GRO4326 GRO4535 GRO4579 GRO4710 GRO3802 GRO3850 GRO3851 GRO3852 GRO3853 GRO3854 GRO3855 GRO3856 GRO3857 GRO3858 GRO3861 GRO3862 GRO3863 GRO3864', 'LED növénylámpa 100–400 W', [], 'Erős', 'LED növénylámpa 100–400 W (Lumatek ATS, Urban Garden Q / Polaris, LEDMAXECO, SANlight EVO 1.5 – EVO-teljesítmény becsült, hortiONE becsült)'),
 ('GRO3371 GRO3529 GRO3600 GRO3673 GRO3703 GRO3704 GRO3893 GRO3908 GRO3930 GRO3940 GRO4003 GRO4048 GRO4164 GRO4165 GRO4166 GRO4171 GRO4172 GRO4226 GRO4227 GRO4327 GRO4362 GRO4536 GRO4537 GYUJTO0205 GRO3859', 'LED növénylámpa 400 W felett', [], 'Erős', 'LED növénylámpa > 400 W (Lumatek ZEUS, Dimlux, AAW Hellion, Agrolite QB, Lumen-King, Fortis, SANlight EVO S1W)'),
 ('GRO3846', 'LED növénylámpa 100–400 W', [], 'Laza', 'Spektra Master Full Spectrum LED – teljesítmény a névben nincs, ellenőrizendő'),
 ('GRO4419 GRO4420 GRO4422', 'LED növénynevelő izzó, csíptethető lámpa', [], 'Laza', 'Sylvania ToLEDo LED izzó E27 – általános fényű, anyanövény / szobanövény'),
 ('GRO4423 GRO4424 GRO4425 GRO4426 GRO4427 GRO4428', 'LED növénylámpa 0–100 W', [], 'Laza', 'Sylvania START vízálló LED lámpatest – általános (por és páramentes) világítás'),
 ('GRO4585 GRO4586 GRO4587 GRO4588 GRO3874 GRO3919', 'LED növénynevelő izzó, csíptethető lámpa', [], 'Erős', 'Sansi LED növénynevelő izzó E27, E27 foglalat'),
 ('GRO4589 GRO4590 GRO4591 GRO4592 GRO4593 GRO4594 GRO4595 GRO4596 GRO4599', 'LED növénynevelő izzó, csíptethető lámpa', ['LED növénylámpa 0–100 W'], 'Erős', 'Sansi csíptethető / álló növénylámpa E27 izzóval'),
 ('GRO3392 GRO3393 GRO3594 GRO3595 GRO4167 GRO4168 GRO4173 GRO4174 GRO4175 GRO3877', 'UV, IR és kiegészítő LED', [], 'Erős', 'UV / IR (NIR) / far-red kiegészítő LED (Cosmorrow, Dimlux, Lumatek)'),
 ('GRO4169 GRO4170 GRO2988', 'UV, IR és kiegészítő LED', [], 'Erős', 'UV-B T5 booster, UV-A lámpa'),
 ('GRO1698 GRO2585 GRO4597 GRO4598', 'UV, IR és kiegészítő LED', [], 'Laza', 'T5 fénycső, LED cső (Sansi)'),
 ('GRO2369 GRO4510', 'UV, IR és kiegészítő LED', [], 'Erős', 'Zöld fényű lámpa a sötét periódushoz (fejlámpa, AC Infinity IONBEAM)'),
 ('GRO3875 GRO3876 GRO3881', 'UV, IR és kiegészítő LED', ['LED tápegység, kábel, vezérlő'], 'Erős', 'Lumatek UV bar kábel'),
 ('GRO0001 GRO0002 GRO1175 GRO1176 GRO1279 GRO2271 GRO2520 GRO2757 GRO2876 GRO2877 GRO2879 GRO3154 GRO3155 GRO3156 GRO3157 GRO3219 GRO3265 GRO3269 GRO3325 GRO3573', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'HPS (nátrium) izzó'),
 ('GRO2521 GRO2880 GRO2881 GRO2882 GRO2883 GRO3267 GRO3268 GRO3688', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'MH (fémhalogén) izzó'),
 ('GRO3174 GRO3175 GRO3188 GRO3207', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'CMH (kerámia fémhalogén) izzó'),
 ('GRO1247 GRO3473 GRO3476', 'HPS, MH, CMH izzó, trafó, reflektor', ['LED növénynevelő izzó, csíptethető lámpa'], 'Laza', 'Agrolite CFL (kompakt fénycső) növénynevelő izzó'),
 ('GRO0504 GRO0616 GRO0618 GRO0619 GRO2607 GRO2608 GRO2997 GRO3153 GRO3171 GRO3176 GRO3177 GRO3202 GRO3223 GRO3364 GRO3365 GRO3366 GRO3657 GRO4004', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'Trafó (mágneses / digitális előtét) HPS, MH, CMH izzóhoz'),
 ('GRO1192 GRO1622 GRO1773 GRO1774 GRO3234 GRO3294 GRO3295 GRO3296 GRO3297 GRO3309V GRO3310 GRO3310V GRO3311V GRO3312V GRO3313 GRO3313V GRO3315 GRO3315V GRO3316 GRO3316V GRO3317 GRO3317V GRO3318 GRO3318V GRO3319 GRO3319V GRO3320 GRO3320V GRO3322 GRO3322V GRO3470 GRO3470V GRO3471V GRO3647 GRO3648 GRO3649 GRO3386 GRO3389 GYUJTO0135', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'Reflektor, Cool Tube, Adjust-A-Wings, Azerwing, Daisy'),
 ('GRO0506 GRO0835 GRO3298 GRO3682', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'E40 foglalat, reflektor-kiegészítő'),
 ('GRO3182 GRO3189 GYSZ0005 GYSZ0005V GYSZ0006 GYSZ0006V GYSZ0007 GYSZ0007V GYSZ0023 GYSZ0023V', 'HPS, MH, CMH izzó, trafó, reflektor', [], 'Erős', 'Komplett HPS / CMH lámpaszett (izzó + trafó + reflektor)'),
 ('GRO3394 GRO3395 GRO3596 GRO3597 GRO3911 GRO3806 GRO3807 GRO4706 GRO4711 GRO4712', 'LED tápegység, kábel, vezérlő', [], 'Erős', 'LED tápegység (Cosmorrow Power, SANlight wallplug / driver)'),
 ('GRO3148 GRO3287 GRO3290 GRO3650 GRO3816 GRO3820 GRO3821 GRO3873 GRO3659 GRO4282 GRO4283', 'LED tápegység, kábel, vezérlő', [], 'Erős', 'LED tápkábel, összekötő, elosztó (SANlight, Lumatek, Dimlux)'),
 ('GRO3651 GRO3652 GRO3179 GRO3410', 'LED tápegység, kábel, vezérlő', ['Lámpafüggesztő, időkapcsoló'], 'Erős', 'Világításvezérlő, dimmer (SANlight EVO, Lumatek Control Panel)'),
 ('GRO1023 GRO1074 GRO1194 GRO1241 GRO2025 GRO2228 GRO2299 GYSZ0061', 'LED tápegység, kábel, vezérlő', ['HPS, MH, CMH izzó, trafó, reflektor'], 'Erős', 'Elektromos kábel trafóhoz, lámpához'),
 ('GRO0787 GRO1105 GRO3683 GRO3750 GRO4013 GRO4014 GRO4015 GRO4016 GRO4115', 'Lámpafüggesztő, időkapcsoló', [], 'Erős', 'Mechanikus / digitális időkapcsoló (TBOX, Garden Highpro)'),
 ('GRO1201 GRO1350', 'Lámpafüggesztő, időkapcsoló', ['HPS, MH, CMH izzó, trafó, reflektor'], 'Erős', 'GSE időzítő kapcsolódoboz több lámpához'),
 ('GRO0770 GRO4270 GRO4122 GRO3398 GRO3723', 'Lámpafüggesztő, időkapcsoló', ['Growbox ág – Growbox kiegészítő'], 'Erős', 'Rope Ratchet, lámpafüggesztő készlet, trafótartó, kábelakasztó'),
 ('GYSZ0054 GYSZ0054V GYSZ0059 GYSZ0059V GYSZ0060 GYSZ0060V GYSZ0062 GYSZ0062V GYSZ0063 GYSZ0063V GYSZ0064 GYSZ0064V GYSZ0065 GYSZ0065V GYSZ0066 GYSZ0066V GYSZ0067 GYSZ0067V GRO4142 GRO4143 GRO4144 GRO4106 GRO4188 GRO4189 GRO4583', 'LED growbox szett', ['Growbox ág – Komplett growbox szett'], 'Erős', 'LED growbox szett – céloldal a Growbox ágban, itt navigációs'),
 ('GYSZ0012 GYSZ0013 GYSZ0013V GYSZ0015 GYSZ0015V GYSZ0016 GYSZ0016V GYSZ0018 GYSZ0018V', 'Growbox ág – Komplett growbox szett', [], 'Más főkategória', 'HPS growbox szett – nem LED'),
 ('GRO4307 GRO2943', 'Palántanevelő ág – Propagátor / mini üvegház', ['LED növénylámpa 0–100 W'], 'Más főkategória', 'Propagátor / konyhakert beépített LED-del'),
 ('GRO0821 GRO4306', 'Növényfeldolgozás ág – Hasznos kiegészítők', [], 'Más főkategória', 'Mikroszkóp, nagyító LED-del'),
]
