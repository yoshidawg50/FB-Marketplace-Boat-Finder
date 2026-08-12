# Conditions


<!-- index:start -->
## Index

- [Bird Reading](bird-reading.md) — Birds are the fastest long-range fish detector on the water.
- [Current Diagnostics](current-diagnostics.md) — This is the observables note: how to read current strength and direction off things you can actually see on the water, so you can pick and adjust presentation i
- [Current Structure](current-structure.md) — This is the mechanism note: how moving water plus bottom structure builds a food chain, and where on a bank or island that chain concentrates.
- [Deep Scattering Layer](deep-scattering-layer.md) — The deep scattering layer (DSL) is a dense band of small organisms — hake, small rockfish, squid, myctophids, zooplankton — that sits 600+ ft down by day and ri
- [Kelp Paddies](kelp-paddies.md) — Drifting kelp paddies are floating structure — they hold bait, shade, and gamefish (yellowtail, dorado, paddy bluefin, tripletail, bycatch) out over open water.
- [Moon](moon.md) — The moon phase is a probability adjustment, never a gate.
- [Sea State](sea-state.md) — A raw wind + swell pull (height, period, direction) is not a fishability read on its own.
- [Tide and Slack](tide-and-slack.md) — Tidal phase decides when to be where.
- [Upwelling and Turnover](upwelling-and-turnover.md) — Chlorophyll is not a yes/no signal — it has an age.
- [Water Color](water-color.md) — Water color / chlorophyll is the second axis alongside SST.
- [Water Temperature](water-temperature.md) — SST is one axis of a two-axis read (temperature and water color / chlorophyll).
<!-- index:end -->


<!-- mermaid:start -->
## Map

```mermaid
graph LR
  n0["Bird Reading"]
  n1["Current Diagnostics"]
  n2["Current Structure"]
  n3["Deep Scattering Layer"]
  n4["Kelp Paddies"]
  n5["Moon"]
  n6["Sea State"]
  n7["Tide and Slack"]
  n8["Upwelling and Turnover"]
  n9["Water Color"]
  n10["Water Temperature"]
  n0 --> n4
  n1 --> n2
  n1 --> n6
  n1 --> n7
  n1 --> n9
  n10 --> n2
  n10 --> n8
  n10 --> n9
  n2 --> n1
  n2 --> n10
  n2 --> n3
  n2 --> n4
  n2 --> n6
  n2 --> n7
  n2 --> n8
  n2 --> n9
  n3 --> n2
  n4 --> n0
  n4 --> n2
  n4 --> n5
  n5 --> n4
  n5 --> n7
  n6 --> n1
  n6 --> n2
  n7 --> n1
  n7 --> n2
  n7 --> n5
  n7 --> n9
  n8 --> n10
  n8 --> n2
  n8 --> n9
  n9 --> n1
  n9 --> n10
  n9 --> n2
  n9 --> n7
  n9 --> n8
```
<!-- mermaid:end -->
