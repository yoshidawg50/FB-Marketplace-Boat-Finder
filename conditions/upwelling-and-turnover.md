---
type: conditions
tags: [upwelling, turnover, chlorophyll, bloom-age, bightsst, SST]
sources: [h3PTupup17I, cameron]
confidence: high
---

# Upwelling and Turnover

Chlorophyll is not a yes/no signal — it has an **age**. This note is about
reading that age: telling **fresh cold upwelled water** (bad now, productive
later) from a **mature bloom edge** (fish now), and about **turnover** — the
sharp regime flip that Cameron's model treats as the single most useful thing to
forecast.

## Bloom age — the freshness interpretation

Upwelling is the front end of the food chain (mechanism in
[current structure](current-structure.md)): current forced over structure lifts
cold, nutrient-rich water, which greens up as phytoplankton bloom. But it takes
time to climb the chain to gamefish, so **freshly upwelled water is cold, green,
and bad *now*** (Landesfeind, Academy Ep. 1):

- **New cold bloom → avoid.** An overnight ~5 °F drop plus green water after an
  afternoon NW wind is a local upwelling event. Short-term negative — but **mark
  it for the recovery**, because that same water will be productive once the
  chain catches up.
- **Mature bloom edge → fish.** The edges of an established bloom, where green
  meets blue, are where the bait (and the gamefish on it) have stacked up.

So every chlorophyll pull needs the age question attached: *is this a new bloom
(post-wind, cold, freshly green — leave it) or a mature bloom edge (fish it)?*
Pair with [water color](water-color.md) and
[water temperature](water-temperature.md).

## Turnover — Cameron's doctrine (source `cameron`)

Cameron's turnover model, built from his BightSST work, sharpens the timing:

> **Fishing is best right *before* turnover** — the point where you get the sharp
> SST drop and the chlorophyll spike. **The key model output is
> time-to-turnover / the approach to it — not the turnover event itself.**

In other words, the value is in forecasting *when* a spot is about to flip and
being there in the window just ahead of it, rather than reacting after the SST
has already crashed and the water has gone green. This runs in the same direction
as the corpus bloom-age rule — the pre-turnover window is the mature-edge
opportunity just before the water resets to a fresh cold bloom — and states it
as a **timing target** the plan can aim at.

### Cameron's BightSST upwelling / turnover model (reference, do not duplicate)

His platform ([BightSST](../locations/bightsst-eval-targets.md),
`bightai-api.onrender.com`) is the system of record for the live signal — this KB
references it, it does not reproduce it:

- **Automated upwelling detection** and break detection (Canny/Sobel) on NOAA
  satellite SST, with multi-model SST per spot and frontness-vs-daily-stats.
- **Eval spots:** originally **8** (La Jolla NW corner, 302 Bank, Coronado
  Islands, Mexican rockpile, Pyramid Cove, 9 Mile Bank SD, 14 Mile Bank LA,
  Cortes Bank), **expanding to ~14** by splitting each of the 6 Coronado spots
  into its own eval location (conditions vary a lot across the group). A ~125-bank
  list is the training universe.
- **Known data quirk (`goes_west`):** a composite-window discrepancy
  (self-reported ~23 h vs. stated 12 h) and a cloud-contaminated `goes_west` NRT
  max (96.6 °F) — **treat single-source SST extremes with suspicion.** This is an
  open data-quality item Cameron flagged, not settled doctrine.

Pull the live upwelling/turnover state from BightSST at plan time; use *this*
note for how to interpret bloom age and how to aim for the pre-turnover window.


<!-- backlinks:start -->
## Linked from

- [<Your> Spots](../profiles/_template/spots.md)
- [April](../seasonal/april.md)
- [Bight Geography](../locations/bight-geography.md)
- [BightSST Eval Targets](../locations/bightsst-eval-targets.md)
- [Cameron's Spots](../profiles/cameron/spots.md)
- [Current Structure](current-structure.md)
- [June–July](../seasonal/june-july.md)
- [Report Reading and Forecasting](../planning/report-reading-and-forecasting.md)
- [Water Color](water-color.md)
- [Water Temperature](water-temperature.md)
- [Year-Anniversary Prior](../seasonal/year-anniversary-prior.md)
<!-- backlinks:end -->
