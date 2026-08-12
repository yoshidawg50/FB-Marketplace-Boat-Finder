# CLAUDE.md — SoCal/Baja Fishing Knowledgebase

## Purpose

This repo is the **system of record for fishing KNOWLEDGE**, the way BightSST
(`bightai-api.onrender.com`) is the system of record for **CONDITIONS**. Claude
chat is the primary day-planning surface and consumes **both** at plan time.

Multi-user by design: knowledge notes are **universal**; angler-specific data
lives in `profiles/`. Cameron is the first user, not the subject — anyone should
be able to plan a day with this KB, and recommendations sharpen when they add
their own tackle and boat info.

**Mission:** the KB must be able to guide a brand-new-to-SoCal fisherman through
the full chain: **where** to go, **when** to go, **which techniques** to use and
**when each applies**, **what tackle** goes with each technique, **how to use
their fish finder** to locate fish, and **how to actually fish** each technique.

**Scope:** the KB captures *all* valuable SoCal/Baja-specific fishing knowledge
from the source corpus — every species, technique, lure, rig, and tackle topic
that clears the curation bar — **independent of whether any single user targets,
owns, or has done it**. A user's personal export never bounds what the KB
captures; it merges in as an attributed source and populates that user's profile.

## Gates (process control — do not bypass)

- **GATE A — execution.** No conversational phrasing ("go ahead", "approved to
  execute", etc.) authorizes a build. GATE A unlocks ONLY when Cameron sends a
  message containing exactly **`PLAN APPROVED`** for the current plan document.
  Applying amendments or returning the plan does not unlock it; **any later plan
  amendment re-opens GATE A** and approval must be re-given.
- **GATE B — merge to `main`.** Unlocked ONLY by Cameron's **post-build review**
  of the coverage summary + judgment-calls list, after which he merges. **A
  `PLAN APPROVED` token (GATE A) does NOT satisfy GATE B.** `main` is canonical;
  all consumers (raw fetches, skill builds, future MCP) target `main`, and
  **nothing is canonical until merged.**

## Sources of truth

- **BightSST** — live conditions (SST, chlorophyll, wind/swell/current, break
  detection, upwelling/turnover). Read endpoints open/no-auth. The KB
  *references* BightSST; it does not duplicate it.
- **This KB** — knowledge: seasonal priors, conditions interpretation layers,
  species/technique decision logic, gear implementation, rigging, care.
- **Chat memory** — the live-capture surface for a user's gear changes and new
  observations. Deltas arrive as `memory-export-YYYY-MM-DD.md` files and
  integrate **additively** (see Sync rule). The KB is canonical for knowledge;
  profile files mirror chat memory.

## Repository layout

```
conditions/   interpretation layers: sea-state, moon, tide/slack, current-
              structure, water color/temp, upwelling/turnover, DSL, paddies, birds
seasonal/     month-by-month priors calendar (pattern layer, not current intel)
species/      per-species behavior + decision logic (when/where/why) — the routers
techniques/   how a method works + when to choose it (execution only)
lures/        per-lure / per-class specs, rigging, running params (implementation)
rigging/      knots, leaders, terminal rigs (parameters + judgment; link video)
tackle/       rod/reel/line/hook selection by application; the gear-class lexicon
bait/         making, keeping, and fishing live bait
fish-care/    bleeding, chilling, ikejime, handling
locations/    UNIVERSAL structure/zone knowledge only — no personal coordinates
planning/     day-plan-protocol + search/glassing + electronics + report-reading
profiles/     per-user boat, rods, tackle, lures, spots (cameron/ + _template/)
sources/      raw transcripts, manifest, source registry, extraction log, input docs
skills/       the boat-day skill (built FROM KB notes + a profile)
scripts/      link-maintenance.py, build-skill-resources.py
```

Root `README.md` is the master index (purpose paragraph, branch map, prominent
link to `planning/day-plan-protocol.md`). Every folder's `README.md` is its
auto-generated index.

## Format & linking (native GitHub — non-negotiable)

- **NO `[[wikilinks]]` anywhere.** All cross-references are relative markdown
  links with human text: `[surface iron](../techniques/surface-iron.md)`.
- Indexes ARE `README.md` files (GitHub auto-renders per folder).
- **YAML front matter** stays on every note (machine layer for the skill build
  and any future MCP):

  ```yaml
  ---
  type: species            # species|technique|lure|rig|tackle|bait|fish-care|
                           # conditions|seasonal|location|planning|profile
  tags: [bluefin, trolling, offshore]
  sources: [cameron, XLVUhV8DW64]   # NAMED: cameron | <youtube video_id>
  confidence: high         # high|medium|low
  ---
  ```

- **Sources are NAMED**: `cameron` or the YouTube `video_id` — never
  "personal/owner" — so contributors can be filtered later. Front-matter
  `sources` stay `video_id`s (channel/date live in the manifest, not the note).
- **No `owned` field on general notes.** Ownership lives only in profiles.
  (Supersedes the older memory-export §10 `owned: true` convention.)
- Each note ends with an auto-generated backlinks block:
  `<!-- backlinks:start -->` … `<!-- backlinks:end -->`.

## Confidence rubric (registry-based)

- **high** — repeated doctrine from a source listed in
  `sources/source-registry.md` (seeded: Erik Landesfeind / SoCal Bight Fishing
  Academy, BD Outdoors named captains, `cameron`), OR anything sourced `cameron`.
- **medium** — single credible mention, OR any claim from a channel **not** in
  the registry (unregistered channels cap at medium).
- **low** — sponsored or promotional claim, regardless of channel.
- Cameron promotes a source by editing `sources/source-registry.md`.
- **Cameron nuance:** cameron-sourced *doctrine* is high; cameron-sourced *open
  items* ("open to", "considering", "wants to try") are captured as **attributed
  open items, never asserted as doctrine.**

## Doctrine vs observation

On-the-water / report footage yields **observations, not rules**. Record them
inline under the relevant doctrine as:

```
**Observed** (channel, date, location): <what happened, with conditions>
```

**Observations never change a note's stated doctrine.** A contradicting
observation sits beside the doctrine, attributed — never silently reconciled.

## Species-first routing (the situation → technique map)

The flaw this fixes: species notes and technique notes can each exist while the
**situation→technique mapping lives in neither**. Contract:

1. **Species notes are the entry points and routers.** Mandatory template for
   every species note:
   - **Where & when** — seasonal/geographic pattern, linking `seasonal/` and
     `locations/` notes.
   - **Finding them** — visual sign, bird behavior, and **species-specific sonar
     signatures with depths** (e.g. yellowtail arcs at 5–10 fathoms near
     structure; bluefin sounded to 30–50 fathoms in wind; swordfish in/below the
     DSL), linking `planning/search-and-glassing.md` and
     `planning/electronics-and-sounder.md` for general method.
   - **Situations → techniques** — a table enumerating the scenarios this species
     presents in SoCal; each row: the conditions that produce the scenario, the
     technique(s) that apply (ranked), the gear class, and the link to the
     technique note.
   - **Gear summary** — class terms only, linking `tackle/gear-classes.md`.
   - **Doctrine & conflicts** — attributed, kept side by side.
2. **Technique notes own execution only** — mechanics, retrieves, gear-class
   detail, common failures — plus a short **"Reach for this when"** list. They do
   NOT restate species patterns; the generated `## Linked from` section plus that
   list provides the reverse map.
3. **Decision spin-out notes always live in `species/`.**
   `species/bluefin-trolling.md` is the escape valve, not a special case:
   decision tables live IN the species router by default; spin out a dedicated
   decision note (in `species/`, never `techniques/`) only when the table
   outgrows the section, and the router keeps a summary + link.
4. **Acceptance test per species note:** a new-to-SoCal angler opening
   `species/yellowtail.md` alone learns where to go, when, how to find them
   (including on the meter), which technique per situation, and what gear class —
   with everything deeper exactly one link away. Applied in the finish-step
   review; failures noted in the judgment-calls list.

## Note conventions

- kebab-case filenames; **one concept per note**.
- **Decision logic lives at species/technique level; implementation at gear
  level.** Canonical example: `species/bluefin-tuna.md` holds WHEN to pull the
  Mad Mac vs a spreader bar vs kite vs speed-troll by wind/grade/conditions and
  links each — spinning the table out to `species/bluefin-trolling.md` when it
  grows (NOT `techniques/`); `lures/mad-mac.md` holds specs, rigging, troll
  speed, and links back.
- **Gear described in class terms** (jig-stick class, 40–60 lb class,
  200g-knife-jig class) so profile resolution is a lookup. Universal lure/tackle
  notes cover models beyond any one user's inventory; profiles link the subset
  they own.
- **A user's doctrine MERGES** into knowledge notes as an attributed source
  (Cameron's tern model + Erik's bird doctrine live in one `bird-reading` note).
  **Conflicts are kept side by side, attributed, never silently reconciled.**
  Preserved example: Cameron's "calendar date doesn't matter, water state does"
  (yellowtail) vs the corpus year-anniversary prior (bluefin routes).
- **Preserve specifics exactly** — weights, depths, degrees, line classes, dates.
  Never smooth numbers into generalities.

## Content rules (generalized review corrections)

- **No relative time anywhere.** Use absolute years/dates — never "last year",
  "this season", "next month". A 2021 seminar describing "last year" means 2020;
  write 2020.
- **Region separation.** Every parameter carries its coast/region context.
  Out-of-region technique detail (e.g. East-coast/Gulf Stream numbers) is either
  a **labeled contrast block** or excluded — never sits unlabeled beside SoCal
  doctrine.
- **The router never absorbs execution.** If a species has execution content and
  no technique note to hold it, **create the technique note**; the species note
  keeps routing only (e.g. `techniques/deep-drop-swordfishing.md` holds sword
  execution, `species/swordfish.md` routes to it).
- **Angler self-imposed constraints are profile data,** even when stated with
  conviction (e.g. "manual reels only"). The general note states what the fishery
  does; the constraint lives in `profiles/<user>/`.

## Curation bar

- **Decision knowledge**: when, why, conditions, selection logic.
- **Procedures** (knots, rigging): capture parameters and judgment; link the
  source video URL (in each transcript header) for the visual steps. **Never
  transcribe step-by-step; paraphrase everything** — no copied transcript
  passages.
- SoCal/Baja-specific and hard-won detail earns a note. Generic content
  available anywhere (clothing, bags, "what to bring", out-of-region reports)
  does **not** — skip it and log the reason.

## Hard habit — run before EVERY commit

```
python scripts/link-maintenance.py
```

It (a) validates every relative link resolves — **exits nonzero on dead links**;
(b) regenerates each note's `## Linked from` backlinks section idempotently
between the `backlinks` markers; (c) regenerates each directory's `README.md`
index (between `index` markers, preserving curated prose); (d) adds a Mermaid map
of the branch's note connections to each branch README (between `mermaid`
markers), **capped at 30 nodes** — a branch over the cap renders a "map skipped"
line instead. Never commit with the script failing.

## Planning protocol (the day-plan surface)

`planning/day-plan-protocol.md` is the procedure chat and the boat-day skill
follow: (1) pull conditions — BightSST per-spot SST/chlorophyll +
wind/swell/current, observed AND forecast, per fishing zone and along the
transit route; (2) apply `seasonal/` priors and `conditions/` layers to pick
zones and timing (moon, tide windows), consulting
`planning/report-reading-and-forecasting.md` for report aging + advection;
(3) resolve species + technique via the species routers; (4) resolve gear and
spread against the active profile. It MUST degrade gracefully: no profile →
class-term recommendations; with one → owned gear, boat envelope respected
(range, sea-state, holder geometry). It is written so a session fetching only
that note + the README indexes can navigate the whole KB.

## Profiles

- `profiles/cameron/` — `boat.md`, `rods.md`, `tackle.md`, `trolling-lures.md`,
  `spots.md`. Profile entries link to general notes.
- `profiles/_template/` — same file set, blank, generalized, with a README:
  what a new user provides (boat envelope, rod inventory with line classes, lure
  inventory, home port/range, optional spots) and how recommendations sharpen.
- `locations/` holds universal knowledge only (zone lexicon, search-box sizing,
  island structure) — **no personal coordinates**.

## Repo-visibility / spot-file rule

`spot-lists-PRIVATE-ONLY.md` normally must NOT be committed to a public repo.
**Decision (Cameron, 2026-08-12):** this repo is public and Cameron explicitly
waived the restriction for his spots ("none of these spots are secret"). The
spot data (`sources/spot-lists.md`, renamed from the PRIVATE-ONLY file — that
name is false in a public repo) and `profiles/cameron/spots.md` (with
coordinates) are therefore committed here. For any *future* user's spot file,
re-confirm the waiver or the repo's visibility before committing coordinates;
default to withholding coords on a public repo.

## Sync rule

Cameron's chat memory stays the live-capture surface. Future deltas arrive as
`memory-export-YYYY-MM-DD.md` files and integrate **additively** — merge new
facts into the relevant knowledge/profile notes as attributed sources; never
restart or overwrite the KB. The KB is canonical for knowledge; profile files
mirror chat memory.

## Future ingestion pipeline (process — run per batch, not now)

The corpus will grow. New transcript batches integrate by this pipeline (each
stage logged in `sources/extraction-log.md`):

1. **Land** — new batches go in `sources/transcripts/<channel>/`, with rows
   appended to `_manifest.csv` (columns: `video_id, title, status, caption_type,
   failure_reason, channel, upload_date`).
2. **Dedup pass** — byte-identical files and the same video under a different ID
   are logged `duplicate-of: <id>`; near-duplicate re-uploads are flagged.
3. **Triage pass** — every video is classified in the log BEFORE extraction
   (`tutorial | report | on-the-water | seminar | promo | out-of-region`).
   Extraction depth follows type; skips are logged with a reason.
4. **Extract batch-by-batch** — **amend** existing notes per the merge/conflict
   conventions (never restart), update the log incrementally, run
   `link-maintenance.py` before each commit.
5. **Coverage** — each batch ends with a coverage summary for Cameron — the
   same **GATE B** review as the main build.

A **~400-video multi-channel batch** of mixed tutorials and on-the-water footage
is the expected first use of this pipeline.

## Provenance & logging

`sources/extraction-log.md` maps every `_manifest.csv` video_id AND every
memory-export section to the notes it fed, or `skipped: <reason>`. It is written
**incrementally at each step's commit** (not at the finish) so a dead session
resumes from CLAUDE.md + the log alone; the finish step **verifies**
completeness rather than creating the log. Export sections fan out to **multiple
destinations** — each destination is logged; the accounting is "every source and
every section appears with at least one destination, and every destination is
logged," not "exactly once." Profile files count as destinations (export §5–9 →
profiles + universal splits; §1–4, §10–11 → knowledge notes).
