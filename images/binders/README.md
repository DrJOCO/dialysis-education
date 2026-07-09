# Binder pill photos

The dialysis pages show an accurate **inline illustration** of each binder.
This avoids broken image requests on the live site and keeps the handouts
usable even without real pill photos.

If real photos are added later, update `templates/dialysis-unit.html`, then run
`python3 generate_units.py` so every dialysis unit page is regenerated.

## Filenames (must match exactly)

| Binder (generic / brand)            | File name              |
|-------------------------------------|------------------------|
| Calcium acetate (PhosLo)            | `calcium-acetate.jpg`  |
| Sevelamer (Renvela)                 | `sevelamer.jpg`        |
| Lanthanum (Fosrenol)                | `lanthanum.jpg`        |
| Sucroferric oxyhydroxide (Velphoro) | `sucroferric.jpg`      |
| Ferric citrate (Auryxia)            | `ferric-citrate.jpg`   |
| Tenapanor (Xphozah)                 | `tenapanor.jpg`        |

## Photo tips

- Shoot the pill on a plain white background, lit evenly, filling most of the frame.
- Square-ish crop works best (the card area is roughly square).
- Keep files small (under ~300 KB each) so the page loads fast on phones.
- `.jpg` is suggested. If you use `.png`, make sure the template uses the same extension.

Note: generics vary by manufacturer, so a photo may not match every patient's
exact pill. The shape, color, and how-to-take instructions are what matter most.
