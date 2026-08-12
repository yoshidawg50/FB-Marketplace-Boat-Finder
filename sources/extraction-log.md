# Extraction Log

Maps **every** `_manifest.csv` `video_id` and **every** `memory-export.md`
section to the note(s) it fed, or `skipped: <reason>`. Maintained
**incrementally** — updated at each build step's commit so a dead session
resumes from [CLAUDE.md](../CLAUDE.md) + this log alone. The finish step
**verifies** completeness (it does not build the log).

Accounting rule: every source and every export section appears with **at least
one** destination, and **every** destination is logged (sections fan out to
multiple notes). Not "exactly once."

## Corpus reconciliation

- Manifest rows + transcript files both reconcile to **128** (the kickoff said
  ~129). No missing transcripts.
- **Not a duplicate:** `vqsD0qpwcJA` ("Slow Pitch Jigging // Yellowtail LA Bay
  Baja", 2022-04-06) and `Jtf-bU4aM-c` ("Does SLOW PITCH JIGGING work for
  YELLOWTAIL?!", 2022-06-27) are **distinct** videos (different md5, titles,
  dates, bodies). Both extracted separately; topic overlaps — not `duplicate-of`.

## Known dispositions (seeded step 0; confirmed as steps run)

| video_id | title | disposition |
| --- | --- | --- |
| j2NhAD2An4s | How to Catch Kingfish | `skipped: out-of-region` (FL king mackerel, Port Canaveral) |
| gBAu56Uw8Fk | East Florida Fishing Report | `skipped: out-of-region` (East Florida) |

**Thin areas (absent from both inputs — recorded, not skipped):** mako shark,
thresher shark.

## Transcript video_id → notes

_Filled incrementally per step. Format: `video_id — note(s) | skipped: reason`._

<!-- log:transcripts:start -->
**Step 1 (conditions / seasonal / locations / planning / swordfish) — consumed:**

| video_id | note(s) fed |
| --- | --- |
| zKmZ4zql2ws | conditions/sea-state |
| DnSqw4r7A1s | conditions/sea-state, tide-and-slack, kelp-paddies; planning/search-and-glassing; seasonal/june-july |
| S2L3KLSQ6Is | conditions/sea-state; seasonal/may |
| OYOda6T3f-8 | conditions/sea-state, water-temperature, bird-reading; seasonal/october, november-december |
| Z3rZqy2Pi8E | conditions/sea-state; seasonal/november-december |
| HzE4FHHcvTk | conditions/sea-state, tide-and-slack, kelp-paddies, bird-reading; seasonal/august; locations/bight-geography; planning/report-reading-and-forecasting |
| XLVUhV8DW64 | conditions/moon, water-temperature; seasonal/october, year-anniversary-prior; planning/report-reading-and-forecasting |
| -JZpyWLdKlk | conditions/moon, kelp-paddies; seasonal/august |
| HnqiE05vdXs | conditions/moon, current-diagnostics, current-structure; seasonal/august; locations/island-structure |
| 5D1vx29LVpI | conditions/moon; seasonal/november-december |
| LEiyB9QNzHY | conditions/moon |
| 6TBxHnkYXI0 | conditions/tide-and-slack, current-diagnostics, water-color; locations/island-structure; planning/search-and-glassing |
| 5to3Q5P7w90 | conditions/tide-and-slack, water-temperature; seasonal/september, october |
| h3PTupup17I | conditions/water-color, current-structure, upwelling-and-turnover |
| Blh2BA-7Ono | conditions/bird-reading; seasonal/june-july; locations/zone-lexicon; planning/report-reading-and-forecasting |
| yMiBtZ7k8-w | conditions/deep-scattering-layer; planning/electronics-and-sounder; species/swordfish |
| KuVwmfF6RAo | species/swordfish |
| nRFFM8DT-og | conditions/deep-scattering-layer |
| yLpDI8jnizU | conditions/deep-scattering-layer, bird-reading; planning/electronics-and-sounder |
| 0KQ--N5TjqE | conditions/current-structure; locations/island-structure, bass-structure |
| Kf5wk_TFgTc | seasonal/february-march |
| pcwcRdmWmLc | seasonal/february-march |
| CMQkHQMxbXM | seasonal/august |
| 5p6gu14ZC4w | planning/report-reading-and-forecasting |
| YZtX1MiT0y8 | seasonal/april |
| YgqXf9iICyg | locations/bays-and-harbors |
| kwMIgkCtFUE | locations/bass-structure |
| bydQzE3F9yM | locations/breakwalls-jetties-riprap; conditions/bird-reading |
| jTXIr9O6zYk | locations/breakwalls-jetties-riprap |
| E4vKwRaRueA | planning/search-and-glassing (glassing); (dorado species pending step 2) |
| 4xzK7YaXK5s | conditions/kelp-paddies |
| 11npFUPOJKU | planning/electronics-and-sounder |

**Step 2 (species routers) — consumed (species videos; dated reports re-mined
for species behavior, adding species destinations to the step-1 report rows):**

| video_id | note(s) fed |
| --- | --- |
| HWx1jDTGsng | species/bluefin-tuna |
| HtuLTv1NlL0 | species/bluefin-tuna |
| EyB98RuKfeQ | species/bluefin-tuna |
| z1CmWHqe9uk | species/bluefin-trolling |
| YsiHziY_PWw | species/bluefin-trolling |
| VgpgJ8IAyJo | species/bluefin-trolling, yellowfin-tuna, dorado, striped-marlin |
| 8M4QhL-Qb7E | species/yellowfin-tuna |
| lxFNVdDhMy4 | species/yellowfin-tuna, skipjack-tuna |
| sYrsPGXiYhI | species/bluefin-tuna (concept; full rig → rigging/rubber-band-deep-rig, step 4) |
| D5DR7Kx42_A | species/yellowtail |
| Jtf-bU4aM-c | species/yellowtail |
| vqsD0qpwcJA | species/yellowtail |
| E4vKwRaRueA | species/dorado (also planning/search-and-glassing, step 1) |
| YIABTTYXeqc | species/calico-bass |
| n6PTy8g3pb0 | species/calico-bass |
| Rwy4MqeXCIU | species/calico-bass |
| P2OzCf2CwXI | species/sand-bass |
| 9br4Z4sfcNI | species/sand-bass (double swimbait rig; also techniques/swimbaits, step 3) |
| GVP3IChsmRQ | species/spotted-bay-bass |
| um5MAeCjNDg | species/spotted-bay-bass (also techniques/ned-rig, step 3) |
| lm7D9Tlc7Po | species/barracuda (also rigging/haywire-twist, step 4) |
| O5aQkex0qGg | species/rockfish-lingcod, ocean-whitefish |
| 6-8KfjEg0x8 | species/rockfish-lingcod, ocean-whitefish |
| AqW_Z9pFcHU | species/rockfish-lingcod |
| OpcKQPA3vAI | species/california-halibut, white-seabass |
| a5u8BaYzw8c | species/california-halibut |
| Xr4nURK-Z48 | species/white-seabass (also rigging/leadhead-mods, step 4) |
| b19_AJjYCok | species/california-spiny-lobster; techniques/hoop-netting |

Dated reports (YZtX1MiT0y8, S2L3KLSQ6Is, DnSqw4r7A1s, Blh2BA-7Ono, CMQkHQMxbXM,
-JZpyWLdKlk, HzE4FHHcvTk, HnqiE05vdXs, 5to3Q5P7w90, XLVUhV8DW64, OYOda6T3f-8,
Z3rZqy2Pi8E, 5D1vx29LVpI) were re-mined for species behavior — destinations
added to bluefin-tuna, yellowfin-tuna, yellowtail, calico-bass, sand-bass,
white-seabass, barracuda, bonito, striped-marlin as applicable.

**New technique note this step:** `techniques/deep-drop-swordfishing.md` and
`techniques/hoop-netting.md` (created per rule C2 — router never absorbs
execution).

**Step 3 (techniques) — consumed:**

| video_id | technique note(s) |
| --- | --- |
| HTssdpnUGMo | surface-iron |
| PRNMGpLj7Pw, dLj0sW_l-_A, OHxbPovgvgc | slow-pitch-jigging |
| j37zxs33gws | knife-jigging (also nRFFM8DT-og, reused) |
| YsiHziY_PWw | kite-fishing |
| z1CmWHqe9uk | speed-trolling |
| HtuLTv1NlL0 | foamer-casting (+ HzE4FHHcvTk, HnqiE05vdXs reused, cameron) |
| T3p1mrqNjIo, mscHk0qiXnk, raUPkuaFXpw, SluBXkT3cuw, 8YvmROeVL-0 | flyline |
| mUrihh0V59M | dropper-loop |
| apyGy3XKlss | sliding-sinker |
| E4vKwRaRueA | chunking (dorado-on-paddy application; chunking mechanics from proposal §4.5/§6.7 — medium confidence, flagged) |
| — (cameron §6 + HzE4FHHcvTk) | trolling (rod-tip elevation rule + 4-factor framework, attributed cameron) |
| YIABTTYXeqc, n6PTy8g3pb0, 9br4Z4sfcNI | swimbaits |
| um5MAeCjNDg | ned-rig |
| k4mD2d6C81k, 1enjjFVcDG0 | drop-shot |
| O5aQkex0qGg, 11npFUPOJKU, 6-8KfjEg0x8, AqW_Z9pFcHU | rockfish-deep-dropping |

**Step 4 (lures + rigging) — consumed:**

| video_id | note(s) |
| --- | --- |
| VgpgJ8IAyJo | lures/mad-mac, dtx-minnow, tuna-feathers-and-skirts |
| AJMjWDKsdRg, j1YZ_9IMUVY | lures/tuna-poppers-and-stickbaits |
| _KE9InIHx8M, zkSKgP2bq10 | rigging/wind-on-leader |
| CIMTyepgonk, NXtvXkqpT9w | rigging/fg-and-albright |
| SwXh9Cwi4e0, hF4dFlSB12s | rigging/essential-knots (Palomar, San Diego jam, RP, uni-to-uni) |
| _w8KNSgGPVE, yr6z3DmWY4s | rigging/hollow-splice-and-serving |
| kO_BqzUYayc | rigging/bite-leaders |
| GqcVaTIlyg0 | rigging/flying-fish-harness |
| UrEymGvZx00 | rigging/double-trouble-rig |
| sYrsPGXiYhI | rigging/rubber-band-deep-rig (concept; captions garbled) |
| qIKGJSEE2aY | rigging/trap-rig |
| RXb0HvVwqO4, Xr4nURK-Z48, F-vOTerdulU | rigging/leadhead-mods |
| lm7D9Tlc7Po | rigging/haywire-twist |
| CWVPLM6NheY | rigging/tuna-feather-rig; lures/tuna-feathers-and-skirts |

Lure class notes (iron-jigs, knife-jigs, soft-plastic-swimbaits, bay-bass-plastics)
draw specs from cameron §8/§9 + technique-note sources already logged (XLVUhV8DW64,
HnqiE05vdXs, OHxbPovgvgc, YIABTTYXeqc, n6PTy8g3pb0, um5MAeCjNDg, k4mD2d6C81k).

**Step 5 (tackle) — consumed:**

| video_id | note(s) |
| --- | --- |
| aXF0bxAFtU0, GoVI7CtN6L8, evhJMzJ7Dz0, YrvQZojc1q0, 0EpILTF0yvE | tackle/line-and-leader (sponsored superiority claims kept low-confidence) |
| xPFm_ZV2PZU | tackle/rod-and-reel-selection, gear-classes, line-and-leader |
| ONH1K2MOp7Q, 8tTVMOV2arE, gOAOyMNG3Ug, qSgIwLX2FWw | tackle/rod-and-reel-selection |
| sWRSYCmt4Tw, HIXTFWlwnM0, m2q22sPPkEM | tackle/hooks |
| EyB98RuKfeQ | tackle/line-and-leader, hooks (also species/bluefin-tuna, step 2) |
| 5yfA5XAaLLY | tackle/reel-maintenance |
| dMJJbowNb40 | topic covered by rigging/essential-knots (uni-to-uni knot demo); Gold Label preference covered from stronger sources |

**Step 6 (bait + fish-care) — consumed:**

| video_id | note(s) |
| --- | --- |
| 1QWstxUibDA | bait/bait-tanks (East vs West tank design) |
| T3p1mrqNjIo, mscHk0qiXnk, raUPkuaFXpw, SluBXkT3cuw, 8YvmROeVL-0 | bait/fishing-live-bait (live-bait tip videos; also techniques/flyline, step 3) |
| lxFNVdDhMy4 | bait/fishing-live-bait (also species/yellowfin-tuna, skipjack-tuna, step 2) |
| JeexIvtUkZc, w6DDCSLu8vM | fish-care/tuna-care (gill-gut + gaffing) |
| WzT0RSHpaQc | fish-care/ikejime |
| E4vKwRaRueA | fish-care/dorado-and-general (also step 1 search-and-glassing, step 3 chunking) |

Content notes are complete after step 6. **Remaining unmapped video_ids** (weekly
sportboat roundups, gear roundups, and pure filler) are reconciled at the finish
step (mostly `skipped: thin sportboat roundup — superseded by the dated Bight
reports` or `skipped: generic filler / out-of-region`).
<!-- log:transcripts:end -->

## memory-export.md section → destinations

_Sections fan out; every destination logged._

<!-- log:memory:start -->
Sections fan out; every destination logged. `(→ step N)` marks a destination
that lands in a later step.

| § | destinations (step 1 landed unless marked) |
| --- | --- |
| §1 Angler profile & programs | profiles/cameron/README, boat, rods, spots (context); seeds species interests — species/swordfish (open item), yellowtail BOLA (→ step 2) |
| §2 Personal doctrine & observations | conditions/tide-and-slack (slack/bait-rise), water-color (chlorophyll≥SST doctrine), sea-state (SD Bay swell 160–186°), upwelling-and-turnover (turnover model); profiles/cameron/boat (Garmin 840xs, data capture). **Deferred:** fleet-intelligence practices (AIS sportboat tracking, Everingham bait boats, VHF ch72) — see thin-areas below |
| §3 Bird-reading model | conditions/bird-reading (merged, attributed) |
| §4 Bait operation | profiles/cameron/boat (30-gal tank); bait/making-bait, bait-tanks (→ step 6); sabiki setup (→ step 6) |
| §5 Boat platform | profiles/cameron/boat |
| §6 Trolling platform | profiles/cameron/boat (platform facts); techniques/trolling (universal doctrine: rod-tip elevation rule, 4-factor framework — → step 3) |
| §7 Rods (8 setups) | profiles/cameron/rods |
| §8 Hard baits / casting / jigging | profiles/cameron/tackle; lures/iron-jigs, tuna-poppers-and-stickbaits, etc. (→ step 4) |
| §9 Trolling lures + specs | profiles/cameron/trolling-lures; lures/mad-mac, dtx-minnow, halco-laser-pro, rapala-husky-magnum, cedar-plug, tuna-feathers-and-skirts, spreader-bar (spec backbone — → step 4) |
| §10 BightSST platform | planning/day-plan-protocol (conditions-sources section); conditions/upwelling-and-turnover; locations/bightsst-eval-targets |
| §11 Sync & canonical | CLAUDE.md (sync rule, gates, provenance) |

**Deferred/thin (flag):** §2 fleet-intelligence practices are not yet in a
dedicated note — candidate destination planning/search-and-glassing or a future
`planning/fleet-intelligence.md`. Logged so it is not silently dropped.
<!-- log:memory:end -->

## Build decisions logged

- Spot input retained, renamed `sources/spot-lists-PRIVATE-ONLY.md` →
  `sources/spot-lists.md` (repo public; Cameron waived privacy 2026-08-12).
- Manifest augmented with `channel` + `upload_date` columns (from transcript
  headers) per amendment V3-1.
- `sources/source-registry.md` seeded per amendment V3-1.
- Ocean whitefish → its own note `species/ocean-whitefish.md` (tilefish
  relative, not a rockfish); rationale per amendment V3/A3.

### Review corrections (swordfish, C1–C4) — generalized to all species notes

- **C1 Region separation:** `species/swordfish.md` parameters labeled SoCal;
  East-coast/Gulf Stream detail moved to a labeled "East-coast contrast" block in
  the technique note. General rule added to CLAUDE.md.
- **C2 Router never absorbs execution:** created
  `techniques/deep-drop-swordfishing.md` and moved sword execution (deployment
  sequence/timing, drift-setup up-current, bite handling incl. don't-touch-the-rod
  with attribution, lead/leader rigging) there; `species/swordfish.md` keeps
  routing. General rule added to CLAUDE.md (create a technique note rather than let
  a router hold execution).
- **C3 Angler constraint → profile:** "manual reels only" reframed as Cameron's
  profile constraint (already in `profiles/cameron/rods.md`); the species note
  states the fishery uses both electric-assist and manual. General rule added.
- **C4 No relative time:** swordfish seminar pinned to Feb 2021 / seasons
  2019–2020; relative time banned KB-wide (CLAUDE.md). Enforced in the step-2
  review of all species notes.

### Step 7 (skills + template + build script)

- No `*.skill` package was provided → `skills/boat-day/` is a scaffold + build
  plan; `scripts/build-skill-resources.py` generates the deployable skill FROM
  the KB decision layer (planning + conditions + seasonal + locations + species
  routers + gear-classes) plus a named profile. Verified working with
  `profiles/cameron`, `--no-profile` (generic), and `profiles/_template`
  (56 notes bundled each).
- Generated skill artifacts (`skills/boat-day/resources/`, `SKILL.md`) are
  git-ignored and excluded from `link-maintenance.py` — regenerable, never
  committed.
- `profiles/_template/` completed (boat, rods, tackle, trolling-lures, spots +
  README): blank/generalized with fill-in prompts and a public-repo coordinate
  caution.
- Fixed a stale exclusion in `link-maintenance.py` (`spot-lists-PRIVATE-ONLY.md`
  → `spot-lists.md`) so the renamed raw spot file is treated as a raw input.

## Finish reconciliation — full 128 accounting

The 17 video_ids not consumed as a primary source in steps 1–6, accounted for
here (no silent drops):

| video_id | title | disposition |
| --- | --- | --- |
| aBnpfNKAN_g | Tackle & gear storage bags | `skipped: generic filler` (not SoCal-specific) |
| VK2By1vTKBc | Clothing options for sportboats | `skipped: generic filler` |
| Dixn41OzeSE | What to bring offshore | `skipped: generic filler` |
| gC7dxSmiip8 | SD sportboat roundup 1/27/22 | `skipped: thin weekly roundup` — current intel superseded by the 17 dated Bight reports; pattern layer lives in `seasonal/` |
| 9emFjXt89N4 | SD sportboat roundup 2/3/22 | `skipped: thin weekly roundup` |
| NeYxQT-w42o | SD sportboat roundup 2/10/22 | `skipped: thin weekly roundup` |
| UDkKa2PU_4c | SD sportboat roundup 3/3/22 | `skipped: thin weekly roundup` |
| _a1e7-7Mbjw | SD fishing tips roundup 5/19/22 | `skipped: thin weekly roundup` |
| F1omCfmMsCU | SD report & tackle tips 5/26/22 | `skipped: thin weekly roundup` |
| nTLweGNuHKw | SD report & tips 6/17/22 | `skipped: thin weekly roundup` |
| _9um-TZOUgE | Tackle tips roundup 11/10/22 | `covered`: uni-knot/tackle content captured in `rigging/essential-knots` + `tackle/` |
| tyG2wBr0m8Q | Bluefin gear roundup 12/02/22 | `covered`: captured in `species/bluefin-tuna`, `bluefin-trolling`, `tackle/line-and-leader` |
| KVdnRJYq4jU | SoCal bays fall tips | `covered`: captured in `species/spotted-bay-bass` + `locations/bays-and-harbors` |
| 3tur7-VCM2g | Academy Ep8 — structure setup | `covered`: structure-setup doctrine captured via Ep5/Ep14 in `locations/bass-structure`, `species/calico-bass`, `sand-bass` |
| -eaaWPN5Fxk | Academy Ep7 — calico/sand tackle | `covered`: bass tackle captured in `species/calico-bass`, `sand-bass`, `tackle/gear-classes`, `lures/soft-plastic-swimbaits` |
| gH8JWhlqYqw | Academy Ep4 — spotty tackle | `covered`: captured via Ep3 in `species/spotted-bay-bass` + `lures/bay-bass-plastics` |
| 3txdqaQdBd4 | How Do You Gulp — Lenny Rudow | `covered`: gulp/plastic doctrine captured via `AqW_Z9pFcHU` in `species/rockfish-lingcod` |

Plus the two out-of-region skips logged at the top (`j2NhAD2An4s` FL king
mackerel, `gBAu56Uw8Fk` East Florida). **All 128 `_manifest.csv` video_ids are
now accounted** — a destination, `covered`, or an explicit `skipped: <reason>`.

## Coverage summary

- **128** transcripts, **all** accounted (destinations, `covered`, or `skipped`).
- **~110 knowledge notes** across conditions (11), seasonal (9), species (18
  routers + 1 decision spin-out), techniques (18 incl. deep-drop-swordfishing +
  hoop-netting), lures (12), rigging (12), tackle (5), bait (3), fish-care (3),
  locations (7), planning (4). Plus Cameron's profile (5 + README), the
  `_template` profile, and the boat-day skill scaffold + generator.
- **All 11 memory-export sections** mapped (multi-destination — see the memory
  table).
- `link-maintenance.py`: **0 dead links**, idempotent, Mermaid cap 30.
- `build-skill-resources.py`: works with `profiles/cameron`, `--no-profile`, and
  `profiles/_template` (56 notes bundled each).
- **Species acceptance test: 18/18 pass** (each router answers where / when /
  how-to-find incl. a sonar-depth signature / technique-per-situation / gear class).

## Judgment calls (for Cameron's review)

**Structure / scoping**
- `profiles/cameron/spots.md` curates home-water anchors + BightSST eval targets
  with coords and **links the full 391-waypoint library** in
  `sources/spot-lists.md` rather than duplicating 391 lines across two files.
- Ocean whitefish gets **its own note** (tilefish relative), not folded into
  rockfish-lingcod (per amendment A3).
- **Two technique notes created per rule C2** (router never absorbs execution):
  `deep-drop-swordfishing`, `hoop-netting`.
- Weekly SD sportboat roundups **skipped as thin** (7-day-cutoff current intel;
  the pattern layer is the 17 dated Bight reports in `seasonal/`).

**Correction to an amendment's premise**
- The "byte-identical duplicate" claim for `vqsD0qpwcJA` / `Jtf-bU4aM-c` **does
  not hold** — verified distinct (titles, upload dates 2022-04-06 vs 2022-06-27,
  md5s, bodies). Both extracted separately; topic overlap noted. (One step-3/step-4
  subagent repeated the "identical" claim in its report — not carried into any
  note.)

**Conflicts kept side by side, attributed (never reconciled)**
- Yellowtail **water-state-over-calendar** (cameron) vs the **year-anniversary
  prior** (corpus, bluefin) — in `species/yellowtail.md` + `seasonal/year-anniversary-prior.md`.
- **Parallel current** prior vs the **into-the-island late-fall/off-color**
  exception (both Landesfeind) — in `conditions/current-structure.md`, `seasonal/november-december.md`.
- Moon **leading-days-strongest** vs **7-days-before-and-after** — in `conditions/moon.md`.

**Thin / low-confidence areas**
- **Mako, thresher:** absent from both inputs — recorded as a thin area, not
  skipped (no source to skip).
- **Pacific crevalle jack (toro):** zero corpus mentions — built from general
  SoCal/Baja knowledge + Cameron's interest; `confidence: low`, sonar read marked
  inferred.
- **Barracuda, bonito:** report-bycatch mentions only — `confidence: medium`,
  technique tables inferred.
- **Chunking mechanics:** the mapped dorado video doesn't detail chunking; note
  kept lean at `confidence: medium`, mechanics from proposal §4.5/§6.7.
- **Fish-care §9 numbers** (slurry/chill) have no video_id in the corpus —
  attributed in prose to the seminar/report context, not in front matter.

**Deferred (flagged, not dropped)**
- Memory §2 **fleet-intelligence practices** (AIS sportboat tracking, Everingham
  bait boats, VHF ch72) have no dedicated note yet — candidate:
  `planning/fleet-intelligence.md` or a section in `planning/search-and-glassing.md`.
- **Lobster regs** stated from a 2019 source — flagged in-note to verify with
  current CDFW rules.

**Caption-garble corrections (flagged)**
- `leadhead-mods` (F-vOTerdulU): caption "8 oz → 1 oz" rendered as the plausible
  1/8–1 oz; `rubber-band-deep-rig` (sYrsPGXiYhI): concept only, no shaky numbers.

**Cameron open items preserved (attributed, not doctrine)**
- SPJ/speed-jig setup shopping; 10 ft jig-stick yellowtail reps; kite (no helium/
  no tank room) + foamer (no-bait run-and-gun) constraints; dedicated sabiki-rod
  build; cast net for Mexico; striped-marlin deployment-trigger learning; toro
  target; drill-powered retrieve; Fathom 80 respool-to-bulk-spool; Yo-Zuri Hydro
  Minnow "LC 205" size to verify; dad's unidentified skirt bag; Tranx braid
  pending respool.
