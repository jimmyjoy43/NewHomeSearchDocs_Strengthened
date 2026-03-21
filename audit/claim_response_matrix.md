# Claim-by-Claim Response Matrix

This file addresses the two uploaded critique documents directly and records what changed in the strengthened repo.

Disposition labels:
- **Agree**: the critique was substantially right
- **Partly agree**: the critique identified a real weakness but overstated or misstated part of it
- **Disagree**: the critique does not fit the provided snapshot
- **Unverified from snapshot**: plausible in the original repo, but not observable from the uploaded files alone

---

## Audit 1: "Project Autopsy and Adversarial Review"

### Finding 1: Duplicate folders causing drift
**Disposition:** Partly agree  
**Response:** The drift risk is real, but the uploaded working snapshot did not include an active duplicate `housing/` tree. The strengthened repo avoids duplicate canonicals entirely and keeps one authoritative layout.  
**Implemented change:** single canonical tree only; no mirror directory.

### Finding 2: Mixed building-level and unit-level data in `buildings.csv`
**Disposition:** Agree  
**Response:** This was the highest-leverage structural fix.  
**Implemented change:** `data/buildings.csv` and `data/units.csv` are now separate, with IDs and cross-file validation.

### Finding 3: Arbitrary score thresholds and lack of weights
**Disposition:** Agree  
**Response:** The old scoring logic had anchors but not a real decision model.  
**Implemented change:** weighted utility model, confidence penalty, documented thresholds, and configurable hard stops in `config/decision_config.json` and `docs/09_scoring_rubric.md`.

### Finding 4: Review-site bias treated too casually
**Disposition:** Agree  
**Response:** Review sites are useful signals, not sufficient evidence.  
**Implemented change:** source hierarchy, evidence classes, and provenance capture in `docs/12_research_methodology.md` and `data/evidence.csv`.

### Finding 5: Overreliance on LLMs for extraction without guardrails
**Disposition:** Mostly agree  
**Response:** LLMs can help, but raw CSV generation plus web scraping assumptions were brittle.  
**Implemented change:** prompts now request JSON, repo scripts do deterministic validation, and cost calculations are handled by code rather than by model arithmetic.

### Finding 6: Missing treatment of uncertainty and missing data
**Disposition:** Agree  
**Response:** Blank previously meant too many different things.  
**Implemented change:** tri-state booleans (`yes`, `no`, `unknown`), confidence labels, evidence counts, and explicit unknown handling.

### Finding 7: Fair-housing / discriminator risk in `adult_vibe_score`
**Disposition:** Agree  
**Response:** The goal was operational stability, but the label and examples were unnecessarily risky.  
**Implemented change:** replaced with `community_stability_score`, plus a legal-guardrails doc and revised tour questions.

### Finding 8: Non-robust net-effective-rent calculation
**Disposition:** Agree  
**Response:** Derived pricing should be deterministic and should incorporate recurring fees.  
**Implemented change:** `units.csv` now separates base rent, concession value, and recurring costs; the repo scripts own the derived monthly-cost math.

### Finding 9: Missing cross-row integrity checks
**Disposition:** Agree  
**Response:** The old validator mainly checked row shape.  
**Implemented change:** new validator checks IDs, duplicates, cross-file references, and obvious cost inconsistencies.

### Finding 10: Missing automation documentation
**Disposition:** Partly agree  
**Response:** The README described workflows that were not visible in the uploaded file set.  
**Implemented change:** added actual workflow files and `docs/14_automation.md`.

### Finding 11: Timeline outdated and rigid
**Disposition:** Partly agree  
**Response:** On the snapshot date the timeline was still current, so "outdated" was too strong. The rigidity critique was valid.  
**Implemented change:** retained the current plan but added anchor-date logic and recalculation guidance.

### Finding 12: Over-optimistic trust in Notion integration
**Disposition:** Agree  
**Response:** External sync should be explicit, not automatic by default.  
**Implemented change:** Notion sync is now optional, dry-run by default, and manual-dispatch only.

### Finding 13: Weak evidence provenance
**Disposition:** Agree  
**Response:** Durable claims need URLs and dates.  
**Implemented change:** `data/evidence.csv` plus packet requirements that preserve source URLs and retrieval dates.

### Finding 14: Missing domain-expert / legal framing
**Disposition:** Partly agree  
**Response:** The repo is still a personal decision-support tool, not professional advice, but it needed legal and operational guardrails.  
**Implemented change:** added `docs/11_legal_and_fair_housing.md`, stronger source hierarchy, and explicit notes on when to verify with staff or counsel.

### Finding 15: Incomplete or missing documentation and placeholders
**Disposition:** Partly disagree  
**Response:** Several supposedly missing docs do exist in the uploaded snapshot. The critique was right, however, that some files were thin and the decision log was effectively empty.  
**Implemented change:** expanded docs, auto-generated decision log, and rebuilt unit-comparison/report flow.

### Finding 16: Oversimplified representation of noise risk
**Disposition:** Agree  
**Response:** One quietness score was not enough.  
**Implemented change:** added `structural_noise_risk` and `location_noise_risk` fields alongside the overall quietness score.

### Finding 17: Weak conflicting-evidence instructions
**Disposition:** Agree  
**Response:** The scoring rules needed a conflict protocol.  
**Implemented change:** explicit conflict handling in `docs/09_scoring_rubric.md` and `docs/12_research_methodology.md`.

### Finding 18: Hard stop rule too narrow
**Disposition:** Agree  
**Response:** The original hard stop caught only one bad combination.  
**Implemented change:** configurable hard-stop rules now also cover approval speed and severe security risk, with room to extend further.

### Finding 19: Prompts assumed ChatGPT could read the repo directly
**Disposition:** Agree  
**Response:** That assumption was too optimistic.  
**Implemented change:** prompts now require actual uploaded or pasted files and explicitly reject imaginary repo access.

### Finding 20: Missing safety/fairness instructions in prompts
**Disposition:** Agree  
**Response:** This was a real omission.  
**Implemented change:** every prompt now instructs the model not to guess, not to use demographic proxies, and to keep unknowns explicit.

---

## Audit 2: "Repo Audit and Improvement Plan"

### Claim: Core docs were missing
**Disposition:** Disagree for the uploaded snapshot  
**Response:** `04`, `05`, `08`, and `09` are present in the uploaded files. The critique still usefully highlighted that the docs were too thin or inconsistent.  
**Implemented change:** rewritten docs with stronger methodology and clearer path references.

### Claim: Duplicate `housing/` directory causes drift
**Disposition:** Partly agree  
**Response:** Sensible engineering concern, though the duplicate tree was not present in the upload set itself.  
**Implemented change:** single canonical structure only.

### Claim: GitHub Actions were missing at the repo root
**Disposition:** Unverified from snapshot, but directionally valid  
**Response:** The uploaded file set did not include root workflows.  
**Implemented change:** added root workflow files.

### Claim: Data model conflates building- and unit-level facts
**Disposition:** Agree  
**Implemented change:** normalized tables and referential checks.

### Claim: Unknown versus false versus not-checked are conflated
**Disposition:** Agree  
**Implemented change:** tri-state enums and separate confidence metadata.

### Claim: The scoring rubric was missing
**Disposition:** Disagree for the uploaded snapshot  
**Response:** The file exists. The better critique is that the rubric was too thin and risky in places.  
**Implemented change:** rewritten scoring rubric with weights, utility mapping, uncertainty, and safer terminology.

### Claim: Research triangulation is too weak
**Disposition:** Agree  
**Implemented change:** source-tier rules, evidence logging, and required provenance.

### Claim: Building-level risk categories are not separated cleanly
**Disposition:** Agree  
**Implemented change:** separate fields for structural noise, location noise, security risk, and pricing risk.

### Claim: Scripts are duplicated under an archive tree
**Disposition:** Unverified from snapshot, but plausible  
**Response:** The strengthened repo avoids this by design.  
**Implemented change:** one script location only.

### Claim: No dedupe logic or stable IDs
**Disposition:** Agree  
**Implemented change:** `building_id`, `unit_id`, `decision_id`, and `evidence_id` are all explicit and validated.

### Claim: Prompts are long but not skeptical enough
**Disposition:** Agree  
**Implemented change:** shorter stage prompts, JSON outputs, fair-housing guardrails, and explicit "do not guess" instructions.

### Claim: `docs/07_decision_log.md` is empty
**Disposition:** Agree  
**Response:** This was a real gap because decision rationale was scattered in narrative notes.  
**Implemented change:** seeded `data/decisions.csv` from the existing breadth scan and auto-generated the markdown decision log.

---

## Repeated themes from both critiques that are now addressed structurally

### 1. The repo needed a stronger evidence backbone
**Implemented:** `data/evidence.csv`, provenance rules, and packet requirements.

### 2. The repo needed a safer model interaction pattern
**Implemented:** JSON-first prompts plus deterministic merge and validation scripts.

### 3. The repo needed a real decision model
**Implemented:** weighted utility, uncertainty handling, and confidence-aware triage.

### 4. The repo needed clearer operational and legal guardrails
**Implemented:** fair-housing rewrite, objective question set, and stronger QA checklist.

### 5. The repo needed immediate usefulness, not just a blank redesign
**Implemented:** existing breadth-scan conclusions were migrated into normalized `buildings.csv` and `decisions.csv` so the strengthened version starts with real state.
