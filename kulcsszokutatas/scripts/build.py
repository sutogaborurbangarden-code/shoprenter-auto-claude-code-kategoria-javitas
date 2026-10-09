import json, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

KP, OUT = sys.argv[1], sys.argv[2]
VOL = json.load(open(KP + '/all.json', encoding='utf8'))

def vol(k):
    if k not in VOL:
        raise SystemExit('HIÁNYZÓ KULCSSZÓ: ' + k)
    return VOL[k][0]

KOT = {'S': ('Szoros', 'Igen'), 'L': ('Laza', 'Igen'), 'LN': ('Laza', 'Nem'),
       'X': ('Nincs (áruházi / nem vásárlási szándék)', 'Nem – kizárandó')}
USE = {'F': 'Kategórianév + H1 + SEO title (fő kulcsszó)',
       'S': 'SEO title / H1 / bevezető (másodlagos)',
       'E': 'Kategórialeírás (természetes említés)',
       'I': 'Leírás alsó része, GYIK vagy blog',
       'N': 'Nem célozni külön oldallal (max. említés)',
       'X': 'Nem használni (áruházi/nem vásárlási szándék)',
       'G': 'Gyártóoldal / szűrő / termékoldal'}
FILL = {'S': 'FFE8F5E9', 'L': 'FFFFF8E1', 'LN': 'FFF3F4F6', 'X': 'FFFDECEA'}
GREEN = 'FF2E7D32'

# kulcsszó | kötődés-kód | felhasználás-kód
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

hdr_font = Font(bold=True, color='FFFFFFFF', size=10)
hdr_fill = PatternFill('solid', fgColor=GREEN)
title_font = Font(bold=True, size=13, color=GREEN)
f10 = Font(size=10)
bold10 = Font(bold=True, size=10)

def header(ws, row, labels):
    for i, l in enumerate(labels, 1):
        c = ws.cell(row, i, l)
        c.font, c.fill = hdr_font, hdr_fill
        c.alignment = Alignment(wrap_text=True, vertical='center')

def widths(ws, ws_w):
    for i, w in enumerate(ws_w, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def parse(block):
    out = []
    for line in block.strip().splitlines():
        p = line.split('|')
        out.append((p[0], p[1] if len(p) > 1 else 'S', p[2] if len(p) > 2 else None))
    return out

def fillrow(ws, row, ncols, code):
    for c in range(1, ncols + 1):
        ws.cell(row, c).fill = PatternFill('solid', fgColor=FILL[code])

wb = Workbook()
summ = wb.active
summ.title = 'Összefoglaló'
ext = wb.create_sheet('Bővítés – rokon területek')
old = wb.create_sheet('Régi kategóriák')
allws = wb.create_sheet('Összes kulcsszó')

# --- kategória-lapok + összes kulcsszó sorok
all_rows = []
for cat in CATS:
    kws = parse(cat['kws'])
    rows = []
    for k, code, use in kws:
        if code == 'X': use = 'X'
        elif code == 'LN' and use is None: use = 'N'
        rows.append((k, vol(k), code, use or 'E'))
    assert rows[0][0] == cat['fo'], cat['name']
    fo = rows[0]
    rest = sorted(rows[1:], key=lambda r: -r[1])
    rows = [fo] + rest
    ws = wb.create_sheet(cat['sheet'])
    ws['A1'] = f"{cat['name']}  –  fő kulcsszó: „{cat['fo']}”"; ws['A1'].font = title_font
    ws['A2'] = f"Felhasználási terület: {cat['area']}"
    ws['A3'] = f"Megjegyzés: {cat['note']}" if cat['note'] else 'Megjegyzés: –'
    ws['A4'] = f"Felvett releváns kulcsszavak: {len(rows)} (a Kulcsszótervező > 0 keresésű ötleteiből válogatva; a teljes nyers lista a CSV-ben)"
    for r in range(2, 5): ws.cell(r, 1).font = f10
    header(ws, 6, ['#', 'Kulcsszó', 'Havi keresés', 'Kötődés a webshophoz', 'Érdemes rá kategória/oldal?', 'Felhasználási terület', 'Javasolt felhasználás'])
    for i, (k, v, code, use) in enumerate(rows, 1):
        r = 6 + i
        kot, erd = KOT[code]
        vals = [i, k, v, kot, erd, cat['area'], USE[use]]
        for c, val in enumerate(vals, 1):
            cell = ws.cell(r, c, val); cell.font = f10
        ws.cell(r, 3).number_format = '#,##0'
        fillrow(ws, r, 7, code)
        all_rows.append((cat['name'], i, k, v, kot, erd, cat['area'], USE[use], code))
    last = 6 + len(rows)
    ws.cell(last + 1, 2, 'Összesen (érdemes rá oldal = Igen):').font = bold10
    c = ws.cell(last + 1, 3, f'=SUMIFS(C7:C{last},E7:E{last},"Igen")'); c.font = bold10; c.number_format = '#,##0'
    widths(ws, [5, 38, 12, 22, 16, 30, 40])
    ws.freeze_panes = 'A7'

# --- Összes kulcsszó
header(allws, 1, ['Kategória', '#', 'Kulcsszó', 'Megjegyzés (szint)', 'Havi keresés', 'Kötődés a webshophoz', 'Érdemes rá kategória/oldal?', 'Felhasználási terület', 'Javasolt felhasználás'])
for j, (cn, i, k, v, kot, erd, area, use, code) in enumerate(sorted(all_rows, key=lambda r: -r[3]), 2):
    for c, val in enumerate([cn, i, k, None, v, kot, erd, area, use], 1):
        allws.cell(j, c, val).font = f10
    allws.cell(j, 5).number_format = '#,##0'
    fillrow(allws, j, 9, code)
n_all = len(all_rows) + 1
allws.auto_filter.ref = f'A1:I{n_all}'
allws.freeze_panes = 'A2'
widths(allws, [30, 5, 38, 22, 12, 22, 16, 30, 40])

# --- Összefoglaló
summ['A1'] = 'babylon-grow.eu – Propagátor, propagátor kiegészítő főkategória kulcsszókutatás (Google Ads Kulcsszótervező, HU, magyar, 12 hó átlag)'
summ['A1'].font = title_font
summ['A2'] = 'Forrás: Babylon Adwords fiók (867-850-6485) Kulcsszótervező (Windsor.ai-on át), lekérdezve: 2026-10-09. Hely: Magyarország, nyelv: magyar, hálózat: Google Keresés. A számok kerekített lépcsős havi átlagok.'
summ['A2'].font = f10
header(summ, 4, ['Kategória (menünév)', 'Fő kulcsszó', 'Fő kulcsszó havi', 'Klaszter összesen (érdemes = Igen)', 'Kötődés a webshophoz', 'Érdemes rá kategória?', 'Felhasználási terület', 'Javasolt hely az új fában'])
summ.row_dimensions[4].height = 30
for i, cat in enumerate(CATS, 5):
    fo_code = parse(cat['kws'])[0][1]
    kot, erd = KOT[fo_code]
    vals = [cat['name'], cat['fo'],
            f"=SUMIFS('Összes kulcsszó'!$E:$E,'Összes kulcsszó'!$A:$A,A{i},'Összes kulcsszó'!$C:$C,B{i})",
            f"=SUMIFS('Összes kulcsszó'!$E:$E,'Összes kulcsszó'!$A:$A,A{i},'Összes kulcsszó'!$G:$G,\"Igen\")",
            kot, erd, cat['area'], cat['place']]
    for c, val in enumerate(vals, 1):
        summ.cell(i, c, val).font = f10
    summ.cell(i, 3).number_format = summ.cell(i, 4).number_format = '#,##0'
    summ.cell(i, 8).alignment = Alignment(wrap_text=True, vertical='top')
    fillrow(summ, i, 8, fo_code)
r = 5 + len(CATS) + 1
summ.cell(r, 1, 'Jelmagyarázat').font = bold10
for j, (code, txt) in enumerate([('S', 'Szoros kötődés · érdemes: Igen'), ('L', 'Laza kötődés · érdemes: Igen'),
                                 ('LN', 'Laza kötődés · érdemes: Nem'), ('X', 'Nincs (áruházi / nem vásárlási szándék) kötődés · érdemes: Nem – kizárandó')], 1):
    c = summ.cell(r + j, 1, txt); c.font = f10; c.fill = PatternFill('solid', fgColor=FILL[code])
notes = [
 'Megjegyzés: a klaszter-összeg átfedéseket tartalmazhat (pl. elírt és ékezet nélküli változatok, amelyeket a Google külön sorban is mutat).',
 'Fő megállapítás: a „propagátor” szóra havi 70 keresés jut, a „palántanevelő”-re 880, a „palántanevelő tálca / palántázó tálca / palánta tálca” mindegyikére 1000. A menünévben érdemes a „palántanevelő” szót is szerepeltetni.',
 'A fűtőlap-ágban a „fűtőszőnyeg” és a „termosztát” nagy számai padlófűtésre / szobatermosztátra vonatkoznak – ezek nem a mi vevőink (Laza / Nem).',
 'A régi Palántanevelés-ág kategóriáinak keresései a „Régi kategóriák” lapon vannak, javaslattal, hova kerüljenek az új fában.',
 'Termékkínálat: az éles bolt terméklistáját ebből a környezetből nem értem el (a Shoprenter API-t és a babylon-grow.eu-t a hálózati szabály tiltja), ezért az „Érdemes” oszlop a keresési szándékon alapul – termékexport alapján finomítandó.',
]
for j, t in enumerate(notes):
    c = summ.cell(r + 6 + j, 1, t); c.font = f10
widths(summ, [34, 26, 16, 22, 16, 18, 46, 60])
summ.freeze_panes = 'A5'

# --- Régi kategóriák
old['A1'] = 'A régi „Palántanevelés” ág kategórianevei – keresési volumen és javasolt helyük az új fában'
old['A1'].font = title_font
old['A2'] = 'Régi fa: Palántanevelés → Palánta közegek, Palánta tápok, Propagátor kiegészítők, Propagátorok, Vetőmagok.'
old['A2'].font = f10
header(old, 4, ['Régi kategória', 'Javaslat (hova kerüljön)', 'Releváns keresés (Szoros+Laza)'])
start = 5 + len(OLD) + 2
header(old, start, ['Régi kategória', 'Kulcsszó', 'Havi keresés', 'Kötődés a webshophoz', 'Érdemes rá oldal?', 'Javasolt felhasználás'])
rr = start + 1
for name, adv, block in OLD:
    rows = sorted([(k, vol(k), code) for k, code, _ in parse(block)], key=lambda x: -x[1])
    for k, v, code in rows:
        kot, erd = KOT[code]
        use = USE['X'] if code == 'X' else USE['N'] if code == 'LN' else 'Az új kategória leírásában / átirányítás (301) a régi URL-ről'
        for c, val in enumerate([name, k, v, kot, erd, use], 1):
            old.cell(rr, c, val).font = f10
        old.cell(rr, 3).number_format = '#,##0'
        fillrow(old, rr, 6, code)
        rr += 1
end = rr - 1
for i, (name, adv, _) in enumerate(OLD, 5):
    old.cell(i, 1, name).font = f10
    old.cell(i, 2, adv).font = f10
    old.cell(i, 2).alignment = Alignment(wrap_text=True, vertical='top')
    c = old.cell(i, 3, f'=SUMIFS(C{start+1}:C{end},A{start+1}:A{end},A{i},E{start+1}:E{end},"Igen")'); c.font = f10; c.number_format = '#,##0'
widths(old, [34, 60, 16, 22, 16, 52])

# --- Bővítés
ext['A1'] = 'Rokon, palántaneveléshez kapcsolódó területek (Kulcsszótervező, HU, 12 hó átlag)'
ext['A1'].font = title_font
ext['A2'] = 'Nagy volumenű, de nem propagátor-vásárlási szándékú témák – blog, GYIK vagy külön kategória, ha van hozzá termék.'
ext['A2'].font = f10
header(ext, 4, ['Terület', 'Javaslat', 'Releváns keresés (Szoros+Laza)'])
start = 5 + len(EXT) + 2
header(ext, start, ['Terület', 'Kulcsszó', 'Havi keresés', 'Kötődés a webshophoz', 'Érdemes rá oldal?', 'Javasolt felhasználás'])
rr = start + 1
for name, adv, block in EXT:
    rows = sorted([(k, vol(k), code) for k, code, _ in parse(block)], key=lambda x: -x[1])
    for k, v, code in rows:
        kot, erd = KOT[code]
        for c, val in enumerate([name, k, v, kot, erd, adv], 1):
            ext.cell(rr, c, val).font = f10
        ext.cell(rr, 3).number_format = '#,##0'
        fillrow(ext, rr, 6, code)
        rr += 1
end = rr - 1
for i, (name, adv, _) in enumerate(EXT, 5):
    ext.cell(i, 1, name).font = f10; ext.cell(i, 2, adv).font = f10
    c = ext.cell(i, 3, f'=SUMIFS(C{start+1}:C{end},A{start+1}:A{end},A{i},E{start+1}:E{end},"<>Nem")'); c.font = f10; c.number_format = '#,##0'
widths(ext, [38, 44, 16, 20, 16, 52])

# --- Gyártói
mk = wb.create_sheet('Gyártói kulcsszavak')
mk['A1'] = 'Gyártó- és márkanevekre érkező keresések (a gyártó szerinti szűrő / alkategória kérdéséhez)'
mk['A1'].font = title_font
header(mk, 3, ['Kulcsszó', 'Havi keresés'])
for i, (k, v) in enumerate(sorted([(k, vol(k)) for k in MAKERS.split('\n')], key=lambda x: -x[1]), 4):
    mk.cell(i, 1, k).font = f10; mk.cell(i, 2, v).font = f10
widths(mk, [38, 14])

# lapsorrend: Összefoglaló, Bővítés, Régi, Összes, kategória-lapok, Gyártói
wb.save(OUT)
print('OK', len(all_rows), 'kulcsszó a kategórialapokon')
