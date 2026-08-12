---
type: location
tags: [bightsst, eval-spots, upwelling, turnover, modeling]
sources: [cameron]
confidence: high
---

# BightSST Eval Targets

The **named** evaluation spots Cameron's [BightSST](https://bightai-api.onrender.com)
platform uses to test its upwelling / turnover detection — a fixed, small set of
locations the model is scored against. This note holds the **names only** (no
coordinates) so the KB can reference the eval set; the live conditions and model
output are BightSST's job, not the KB's. The mechanism these spots test —
upwelling, the sharp SST drop and chlorophyll spike, and the approach to
turnover — is in [upwelling and turnover](../conditions/upwelling-and-turnover.md).

## The original 8 eval spots

The upwelling/turnover model started on 8 eval spots (Cameron, memory §10):

1. La Jolla NW Corner
2. 302 Bank
3. Coronado Islands
4. Mexican Rockpile
5. Pyramid Cove
6. 9 Mile Bank (San Diego)
7. 14 Mile Bank (LA)
8. Cortes Bank

## Expanding to ~14

The **Coronado Islands** entry is being split into **each of the 6 Coronado
Islands spots individually**, because conditions vary a lot across that group —
one averaged reading hides the spread. That expansion takes the set from 8 to
**~14** eval locations. In the spot-file the split is recorded as: 14 Mile Bank,
North + South 9 Mile Bank, Cortes Bank, 302, La Jolla NW Corner, Rockpile,
Pyramid Cove, and each of the 6 Coronado Islands spots.

## The training universe

Behind the eval set sits a **~125-bank list** — the training universe of SoCal
banks and structures the model draws on. The eval spots are the scored subset;
the 125-bank list is the full population. Cameron holds ~13 years of local SST,
chlorophyll, tide, wind, swell, and historical fish-count data for this modeling
(memory §10).

Cameron's turnover doctrine, which these evals are built to serve: **fishing is
best right before turnover** — the sharp SST drop plus chlorophyll spike — so the
key model output is **time-to-turnover / the approach**, not the turnover event
itself. This is captured as doctrine in
[upwelling and turnover](../conditions/upwelling-and-turnover.md).


<!-- backlinks:start -->
## Linked from

- [Cameron's Spots](../profiles/cameron/spots.md)
- [Deep Scattering Layer](../conditions/deep-scattering-layer.md)
- [Upwelling and Turnover](../conditions/upwelling-and-turnover.md)
- [Zone Lexicon](zone-lexicon.md)
<!-- backlinks:end -->
