---
type: profile
tags: [cameron, spots, coordinates, coronados, la-jolla, bola, catalina]
sources: [cameron]
confidence: high
---

# Cameron's Spots

Cameron's spot library. **Repo public; Cameron waived the private-only
restriction (2026-08-12) — "none of these spots are secret,"** so coordinates
are committed here. The **complete coordinate library** (391 waypoints, N→S by
region) is [`sources/spot-lists.md`](../../sources/spot-lists.md) — this note is
the curated profile view: home waters, the modeling anchors, and the naming
rules, with everything linked to the universal [locations](../../locations/)
knowledge (which holds no coordinates).

## Home base & range

- **Home port / launch:** Dana Landing, Mission Bay (San Diego). Also trailers
  for Catalina (weighs a shorter tow vs a longer crossing).
- **Home waters:** Coronado Islands, La Jolla, San Diego offshore banks.
- **Baja program:** regular trips, especially **Bahía de los Ángeles (BOLA)** —
  major multi-day trip May 2026; next BOLA trip September 2026.
- Boat envelope (range, sea-state, holder geometry) is in [boat](boat.md).

## Region index (full coords in the library)

Grouped as in [`sources/spot-lists.md`](../../sources/spot-lists.md); structure
knowledge is in [locations](../../locations/):
Offshore banks (N→S) · La Jolla · San Diego artificial reefs · Point Loma ·
Imperial Beach · International artificial reef · Coronado Islands (+ nearby
rockfish) · Northern Baja · Finger Bank rockfish · Ensenada · Punta Banda /
Santo Tomás · Colonet · San Quintín · Crystal Cove · Dana Point · Oceanside /
North County (+ artificial reefs) · Santa Barbara Island · San Nicolas Island ·
Catalina (backside / front side / rockfish) · San Clemente (front / back).

See [zone lexicon](../../locations/zone-lexicon.md) for how these group into
search boxes, and [island structure](../../locations/island-structure.md) for
how each island's contours fish.

## BightSST eval / modeling anchors

The spots his upwelling-turnover model evaluates (names in
[BightSST eval targets](../../locations/bightsst-eval-targets.md); model in
[upwelling & turnover](../../conditions/upwelling-and-turnover.md)). Original 8,
expanding to ~14 by splitting the 6 Coronado spots:

| Anchor | Coordinates (from the library) |
| --- | --- |
| 14 Mile Bank | 33 23.833 / 118 00.000 |
| North 9 Mile Bank | 32 38.000 / 117 26.000 |
| South 9 Mile Bank | 32 32.000 / 117 21.000 |
| 302 (Kidney Bank) | 32 26.333 / 117 34.750 |
| Cortes Bank | 32 26.417 / 119 07.833 |
| La Jolla NW Corner | 32 50.630 / 117 18.460 |
| Coronado Islands (6 spots) | see library — each split out individually |
| Mexican Rockpile · Pyramid Cove (SCI) | see library |

The **~125-bank list** is the training universe for the model.

## Naming & housekeeping (Cameron's rules)

- **Collision rule:** prefix with the closest landmass — "Catalina - X",
  "Baja - X", "San Diego - X". Exception: the two "400" banks are **East 400 /
  West 400** (both Baja offshore, ~44 km apart E–W at the same latitude).
- **Not collisions** (distinct, just similar): "475" vs "475 Knuckle"; "300" vs
  "Bell Bank (300)" vs "300 (The Rampart)"; "179" vs "Tuna Hole (179)"; "220" vs
  "Double 220"; "Kidney Bank (63)" vs "302 (Kidney Bank)".
- **UNRESOLVED (open item):** "The Slide" ×2 — one Catalina front-side shoreline
  spot, one offshore bank ~6 km away; both closest to Catalina, the landmass
  rule can't separate them. Awaiting Cameron.
- **Sub-pixel clusters** (collapse to ~1 MUR pixel for modeling; keep distinct
  waypoints for navigation): Carlsbad AR 1–12, Oceanside AR 1A–1H/2A–2L,
  Pendleton 1–7, International Reef A–F, Torrey Pines 1–2.
- Coordinate format: `deg min.mmm`, all latitudes N, all longitudes W; decimal =
  `deg + min/60` (negate longitude).


<!-- backlinks:start -->
## Linked from

- [BightSST Eval Targets](../../locations/bightsst-eval-targets.md)
- [Cameron's Boat — Panga Marine Marquesas 22](boat.md)
- [Island Structure](../../locations/island-structure.md)
- [Upwelling and Turnover](../../conditions/upwelling-and-turnover.md)
- [Zone Lexicon](../../locations/zone-lexicon.md)
<!-- backlinks:end -->
