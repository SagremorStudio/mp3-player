# 🎵 Neon MP3 Lejátszó

Egy retro-neon dizájnú, böngészőben futó MP3 lejátszó, mappa-alapú navigációval, spektrum-vizualizációval és Python háttérszerverrel.

![verzió](https://img.shields.io/badge/verzi%C3%B3-0.07--FIXED-00bfff)
![licenc](https://img.shields.io/badge/licenc-saját%20haszn%C3%A1latra-lightgrey)


<img width="1898" height="908" alt="sagplayer" src="https://github.com/user-attachments/assets/c0e1da97-4f2a-4dda-be3c-1a883b2d857f" />




## ✨ Funkciók

- **Mappa-alapú böngészés** – az `mp3/` könyvtár almappái szerint csoportosított, lenyíló listás fájlböngésző
- **Lejátszásvezérlés** – lejátszás/szünet, előző/következő szám, ±10/20/30 másodperces ugrás
- **Autoplay** – a lista automatikus továbbjátszása a szám végén (ki/be kapcsolható)
- **Élő spektrumanalizátor** – Web Audio API-val hajtott VU-meter csíkok és pulzáló "hangjegy" animáció
- **Állapot-visszaállítás** – a böngésző újratöltése után is emlékszik a legutóbb lejátszott számra és a nyitott mappákra (`localStorage`)
- **Memóriakezelés** – automatikus és manuális memóriatisztítás hosszú futásidejű (pl. kioszk módú) használathoz
- **Élő státusz sáv** – memóriahasználat, lejátszási állapot és tisztítási státusz valós időben
- **Automatikus lista-frissítés** – 30 másodpercenként újralekéri a mappastruktúrát a szerverről

## 📁 Projektstruktúra

```
.
├── index.html          # A lejátszó felhasználói felülete (ez a repó tartalma)
├── server.py           # Python háttérszerver (statikus kiszolgálás + /list végpont)
└── mp3/                # A lejátszandó MP3 fájlok mappái
    ├── Album 1/
    │   ├── 01 - szam.mp3
    │   └── 02 - szam.mp3
    └── Album 2/
        └── ...
```

## ⚙️ Hogyan működik

A frontend egyetlen statikus `index.html` fájl, ami két dologra támaszkodik a szerver felől:

1. **`GET /list`** – JSON választ vár, ami a mappaneveket a bennük lévő fájlnevek listájára képezi le:

   ```json
   {
     "Album 1": ["01 - szam.mp3", "02 - szam.mp3"],
     "Album 2": ["intro.mp3"],
     "": ["gyoker_szam.mp3"]
   }
   ```

2. **Statikus fájlkiszolgálás** az `mp3/` mappából, mivel a lejátszó a számokra `mp3/<mappa>/<fájlnév>` relatív URL-eken hivatkozik.

A háttérszerver feladata tehát mindössze ennyi: egy egyszerű HTTP szerver, ami kiszolgálja az `index.html`-t, a statikus `mp3/` könyvtárat, és biztosít egy `/list` végpontot, ami bejárja az `mp3/` mappát és visszaadja a fenti JSON struktúrát.

## 🚀 Telepítés és futtatás

### Előfeltételek

- Python 3.8+
- Modern böngésző (Chrome, Firefox, Edge – Web Audio API támogatással)

### Lépések

1. Klónozd a repót:
   ```bash
   git clone https://github.com/<felhasznalonev>/<repo-nev>.git
   cd <repo-nev>
   ```

2. Másold az MP3 fájljaidat mappánként az `mp3/` könyvtárba.

3. Indítsd el a szervert:
   ```bash
   python server.py
   ```

4. Nyisd meg a böngészőben:
   ```
   http://localhost:8000
   ```

> 💡 A pontos indítási parancs és port a `server.py`-ban használt keretrendszertől (pl. `http.server`, Flask) függően eltérhet – szükség esetén igazítsd a fenti lépéseket a saját szerver implementációdhoz.

## 🎛️ Használat

| Vezérlő | Funkció |
|---|---|
| ▶ / ⏸ | Lejátszás / szünet |
| ⏮ / ⏭ | Előző / következő szám |
| 🔙 / 🔜 | Ugrás -30/-20/-10s ill. +10/+20/+30s |
| 🔊 csúszka | Hangerő |
| 🔁 Autoplay | Automatikus továbbjátszás ki/be |
| 🗑️ Memória tisztítás | Kattintás: normál tisztítás • Dupla kattintás: agresszív tisztítás (AudioContext újraindítása) |

A mappalista fejlécére kattintva nyitható/csukható az adott mappa tartalma, a beállítás a böngésző `localStorage`-ában megmarad.

## 🧠 Memóriakezelés

Mivel a lejátszót tartós (pl. iskolai kijelzőn futó) használatra tervezték, beépített memóriakezelést tartalmaz:

- **Automatikus tisztítás** dalváltáskor, illetve 3 percenként, ha a lejátszás szünetel
- **Manuális tisztítás** a 🗑️ gombbal, dupla kattintásra agresszív módban (az `AudioContext` teljes újraindításával)
- **Élő memóriakijelzés** a lábléc státuszsávjában (`performance.memory` API, ha a böngésző támogatja)

## 🛠️ Testreszabás

A színpaletta a `:root` CSS változóiban módosítható:

```css
:root {
  --bg: #0a0f16;
  --panel: #1c2a3a;
  --accent: #00bfff;
  --accent2: #63f588;
  --accent3: #c2f563;
  --text: #e3f2ff;
}
```

---

*2025 | Verzió: 0.07-FIXED*

