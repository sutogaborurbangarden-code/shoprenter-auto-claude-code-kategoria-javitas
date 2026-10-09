# Kategóriafa- és kulcsszókutató ügynök — munkajegyzet

Ez a repó a webshopok **kategóriafa-struktúrájának megtervezésére és
kulcsszókutatásra** szolgáló dedikált munkamenet közös memóriája. Minden új
munkamenet először ezt olvassa el, és ide vezeti fel a döntéseket.

## Webshopok (eddigi munkamenetekből ismert)

- **urbangardenshop.hu** — Shoprenter, aldomain: `urbangardenshop`
  (API: `urbangardenshop.api.myshoprenter.hu`). Termesztés / growshop:
  közegek, tápok, világítás, szellőzés, hidro.
- **Babylon**, **Gomoa** — további boltok (termékfeltöltési munkamenetekből
  ismertek, részletek még nincsenek rögzítve).
- A meglévő automatizációs scriptek a felhasználó Windows gépén:
  `C:\shoprenter-auto\` (itt vannak a Shoprenter API-hitelesítések is).
- A felhőkonténer **nem éri el** a Shoprenter API-t (egress proxy tiltja),
  ezért élő adatot exportként (CSV) kell ide hozni, vagy a scriptet helyben
  futtatni.

## Rögzített szabályok

- **Gyűjtőtermék-elv:** a `GYUJTO…` SKU-jú gyűjtőtermék és az összes
  gyereke (változata) pontosan **ugyanazt a kategóriakészletet** kapja.
- Egy termék jellemzően két párhuzamos ágban is szerepel: **márka-ág**
  (pl. Plagron) és **termékkategória-ág** (pl. földkeverékek). Több
  kategória-ID duplán létezik (pl. 6574 és 6829 = Plagron; 6699 és 6821 =
  földkeverékek) — ez a két (vagy kétnyelvű / két fa alatti) ág jele, nem
  hiba, de a kategóriafa újratervezésénél tisztázandó.
- Shoprenter azonosítók: base64(`category-6574`) alak; exportban és a
  jegyzetekben a sima számot használjuk.

## Ismert kategória-ID-k (urbangardenshop, 2026-09 export alapján)

| ID | Megnevezés | ID | Megnevezés |
|---|---|---|---|
| 6551 | árva (1 termék) | 6687 | Integra Boost |
| 6560 | BioBizz | 6697, 6819 | perlit / agyaggolyó |
| 6565 | Canna | 6699, 6821 | földkeverékek |
| 6574, 6829 | Plagron | 6704 | szellőzés / szűrő |
| 6576, 6817 | Terra Aquatica | 6706 | klipsz / padló ventilátor |
| 6591 | növénytartó háló | 6710 | csőventilátor |
| 6600 | fűtött szaporító | 6731 | hidro rendszer |
| 6608 | szaporítóláda | 6744 | mérlegek |
| 6627 | LED lámpák | 6786 | rejtekhely / tárolás |
| 6630 | kábelek / tápegységek | 6666 | kalibráló folyadékok |
| 6644 | Secret Jardin kiegészítők | 6667 | pH mérők |
| 6661 | nem beazonosított (GYUJTO0086 csoport) | 6669 | pH teszt |

## Előzmény: kategória-javítás (2026-09-16)

`claude-code-kategoria-javitas.md` alapján egy Python script készült
(branch: `claude/lucid-thompson-38go7y`, **nem került pusholásra**, a
munkamenet megszakadt): 61 termék kategóriáinak szinkronizálása (76
hozzáadás, 11 törlés, 22 gyűjtő), 2 termék leválasztása rossz szülőről
(HED0118 ← GYUJTO0240, GRO2251 ← GYUJTO0226), majd ellenőrzés.

## Nyitott kérdések / következő lépések

- [ ] A kategóriafa-tervezésről és kulcsszókutatásról folytatott korábbi
      (claude.ai chat) beszélgetés tartalma — ide kell felvezetni.
- [ ] Aktuális teljes kategóriafa-export (ID, név, szülő, URL, termékszám)
      boltonként.
- [ ] Kulcsszó-adatforrás: Google Search Console (Windsor.ai-n át elérhető
      lehet), Google Ads Keyword Planner export.
