import json, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

KP, OUT, CFG = sys.argv[1], sys.argv[2], sys.argv[3]  # CFG: kategória-konfiguráció (.py)
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
# CATS, OLD, EXT, MAKERS és a lapcímek a konfigurációs fájlból jönnek
exec(open(CFG, encoding='utf8').read())

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
old = wb.create_sheet(globals().get('OLD_SHEET', 'Régi kategóriák'))
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
summ['A1'] = TITLE
summ['A1'].font = title_font
summ['A2'] = SOURCE
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
notes = NOTES
for j, t in enumerate(notes):
    c = summ.cell(r + 6 + j, 1, t); c.font = f10
widths(summ, [34, 26, 16, 22, 16, 18, 46, 60])
summ.freeze_panes = 'A5'

# --- Régi kategóriák
old['A1'] = OLD_TITLE
old['A1'].font = title_font
old['A2'] = OLD_SUB
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
ext['A1'] = EXT_TITLE
ext['A1'].font = title_font
ext['A2'] = EXT_SUB
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
mk['A1'] = MAKERS_TITLE
mk['A1'].font = title_font
header(mk, 3, ['Kulcsszó', 'Havi keresés'])
for i, (k, v) in enumerate(sorted([(k, vol(k)) for k in MAKERS.split('\n')], key=lambda x: -x[1]), 4):
    mk.cell(i, 1, k).font = f10; mk.cell(i, 2, v).font = f10
widths(mk, [38, 14])

# lapsorrend: Összefoglaló, Bővítés, Régi, Összes, kategória-lapok, Gyártói
wb.save(OUT)
print('OK', len(all_rows), 'kulcsszó a kategórialapokon')
