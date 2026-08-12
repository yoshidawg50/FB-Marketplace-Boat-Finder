---
type: planning
tags: [day-plan, protocol, workflow]
sources: [cameron]
confidence: high
---

# Day-Plan Protocol

The procedure chat and the boat-day skill follow to turn **conditions** +
**priors** into a gear'd-up plan. It degrades gracefully: with no profile it
returns class-term recommendations; with a profile it returns owned gear and
respects the boat envelope (range, sea-state, holder geometry). A session that
fetches only this note plus the folder [README](../README.md) indexes can
navigate the whole KB.

## The four steps

1. **Pull conditions.** From [BightSST](https://bightai-api.onrender.com), per
   fishing zone and along the transit route, observed **and** forecast: per-spot
   SST + chlorophyll, wind/swell/current. (BightSST read endpoints are open /
   no-auth; expect Render free-tier cold starts of 30–60 s.)
2. **Apply priors + interpretation layers.** Weight zones and set timing (moon,
   tide windows) using the [seasonal priors](../seasonal/) calendar and the
   [conditions layers](../conditions/) — especially
   [sea-state](../conditions/sea-state.md), [moon](../conditions/moon.md),
   [tide & slack](../conditions/tide-and-slack.md),
   [current-structure](../conditions/current-structure.md), and
   [water color](../conditions/water-color.md) /
   [temperature](../conditions/water-temperature.md). Age the intel with
   [report reading & forecasting](report-reading-and-forecasting.md) (report
   aging, advection, coverage bias).
3. **Resolve species + technique.** Enter through the [species routers](../species/):
   each maps the day's situation → ranked technique(s) → gear class.
4. **Resolve gear + spread** against the active [profile](../profiles/). No
   profile → class terms; with one → owned gear within the boat envelope.

## Conditions sources (BightSST)

- **Role:** BightSST is the system of record for *conditions*; this KB
  *references* it and never duplicates it.
- **Endpoints:** read endpoints open/no-auth; admin behind a Bearer key.
- **Cold-start caveat:** Render free tier, 30–60 s cold starts.
- **Doctrine — distrust single-source SST extremes; cross-check models.** A
  known `goes_west_composite` window discrepancy and a cloud-contaminated NRT
  max (96.6 °F) mean single-source SST outliers are treated with suspicion.

## Supporting notes

- [Search & glassing](search-and-glassing.md) — how to run the day and read sign.
- [Electronics & sounder](electronics-and-sounder.md) — finding fish on the meter.
- [Report reading & forecasting](report-reading-and-forecasting.md) — aging
  reports, advection, coverage bias.
- [Species routers](../species/) — enter here to map situation → technique → gear.


<!-- backlinks:start -->
## Linked from

- [<Your Boat>](../profiles/_template/boat.md)
- [<Your> Spots](../profiles/_template/spots.md)
- [April](../seasonal/april.md)
- [August](../seasonal/august.md)
- [Current Diagnostics](../conditions/current-diagnostics.md)
- [Current Structure](../conditions/current-structure.md)
- [Electronics and Sounder](electronics-and-sounder.md)
- [February–March](../seasonal/february-march.md)
- [June–July](../seasonal/june-july.md)
- [May](../seasonal/may.md)
- [Moon](../conditions/moon.md)
- [November–December](../seasonal/november-december.md)
- [October](../seasonal/october.md)
- [Report Reading and Forecasting](report-reading-and-forecasting.md)
- [Sea State](../conditions/sea-state.md)
- [Search and Glassing](search-and-glassing.md)
- [September](../seasonal/september.md)
- [Tide and Slack](../conditions/tide-and-slack.md)
- [Water Color](../conditions/water-color.md)
- [Water Temperature](../conditions/water-temperature.md)
- [Year-Anniversary Prior](../seasonal/year-anniversary-prior.md)
<!-- backlinks:end -->
