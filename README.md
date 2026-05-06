# Iksir (ইকসির)

![Iksir Typography Specimen](documentation/hero.png)

**Iksir (ইকসির)** is a pixel-perfect Bengali and Latin typeface crafted for digital nostalgia. Rooted in 8-bit and 16-bit video game aesthetics, it brings rigid, blocky geometries to the complex curves and conjuncts of Bengali script.

Every glyph is a strict **retro bitmap** adaptation — grid-aligned, aliased, and mathematically precise. Rather than relying on dynamic mark-positioning, Iksir uses an extensive library of **119 manually drawn `akhn` conjunct rules**, ensuring every pixel stays sharp on the grid.

## ✨ Key Features

| Feature | Detail |
|---|---|
| **Style** | Pixel Art / Retro Bitmap |
| **Weights** | Regular, Italic |
| **Scripts** | Bengali (বাংলা), Latin |
| **UPM** | 1000 |
| **Total Glyphs** | 426 per weight |
| **Bengali Conjuncts** | 119 `akhn` rules + 48 `vatu` + 44 `blws` + 13 `half` |
| **Hinting** | Full TrueType (`fpgm`, `prep`, `cvt`) |
| **License** | SIL Open Font License 1.1 |

- **Strictly Monolinear & Aliased** — No sub-pixel blurring. Pure stair-stepped edges.
- **Micro-Engineered Conjuncts** — Every Bengali ligature is hand-drawn onto the pixel grid.
- **Mathematical Italic** — A stepped skew that preserves 8-bit integrity without compromising grid alignment.
- **Zero Composites** — All 426 glyphs drawn independently. No component reuse.

## 📜 License

This Font Software is licensed under the **SIL Open Font License, Version 1.1**.
Available at: [https://openfontlicense.org](https://openfontlicense.org)

## 👤 Author

| | |
|---|---|
| **Designer** | Inan |
| **Web** | [inanxr.me](https://inanxr.me) |
| **Email** | inan@iseer.co |

---

## 🗂️ Repository Structure

```
Iksir/
├── .github/
│   └── workflows/
│       └── fontbakery.yml          # Automated FontBakery QA via GitHub Actions
├── documentation/
│   ├── ARTICLE.en_us.html          # Google Fonts catalog article
│   ├── hero.png                    # Typography specimen image
│   └── images-license.txt          # Image asset license
├── fonts/
│   └── ttf/
│       ├── Iksir-Regular.ttf       # Regular weight binary
│       └── Iksir-Italic.ttf        # Italic weight binary
├── scripts/
│   └── index.html                  # Font preview / test page
├── sources/
│   ├── Iksir-Regular.ufo/          # Regular master source
│   │   ├── glyphs/                 #   └── 426 glyph .glif files
│   │   ├── features.fea            #   └── OpenType feature definitions
│   │   ├── fontinfo.plist           #   └── Font metadata
│   │   ├── groups.plist             #   └── Glyph groups
│   │   ├── kerning.plist            #   └── Kerning data
│   │   ├── layercontents.plist      #   └── Layer registry
│   │   ├── lib.plist                #   └── Font library data
│   │   └── metainfo.plist           #   └── UFO format version
│   └── Iksir-Italic.ufo/           # Italic master source
│       └── (same structure as Regular)
├── .gitignore
├── AUTHORS.txt                     # Authorship documentation
├── build.py                        # Python build script (UFO → TTF)
├── build.sh                        # Shell build script
├── CONTRIBUTORS.txt                # Legacy attributions
├── DESCRIPTION.en_us.html          # Google Fonts catalog description
├── fontbakery-report.md            # Latest FontBakery QA report
├── METADATA.pb                     # Google Fonts protobuf metadata
├── OFL.txt                         # SIL Open Font License
└── README.md
```

## 🔨 Building

```bash
# Install dependencies
pip install defcon ufo2ft fonttools

# Compile TTF binaries from UFO sources
python build.py
```

## 🧪 Quality Assurance

FontBakery validation passes with **0 FAILs**. See [`fontbakery-report.md`](fontbakery-report.md) for the full report.

```bash
fontbakery check-universal fonts/ttf/*.ttf
```
