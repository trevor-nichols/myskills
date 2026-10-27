# Cascaded Eval Blueprint — Fillable Template

**Task:** [Working title]  
**Domain / expert role:**  
**Real-world workflow or documented problem class:**  
**What decision/action depends on the result?**  
**Scope, time/version, and source authority:**  
**Solver's available evidence and tools:**  
**Difficulty profile:** Foundational / Expert / Flagship / Custom  
**Profile overrides / domain requirements:**  
**Status:** DRAFT / ARCHITECTURE APPROVED / GOLD VERIFIED / EMPIRICALLY VALIDATED

## A. Terminal output contract

| Output ID | Object to deliver | Units / exact IDs / artifact format | Acceptable equivalent outcomes | Verification check |
|---|---|---|---|---|
| O1 |  |  |  |  |
| O2 |  |  |  |  |

**Decisiveness:** Explain why these outputs affect a real downstream decision rather than only benchmarking a calculation.

**Boundary:** Record what is out of scope and how the solver should respond to genuinely insufficient evidence.

## B. Decision inventory

Copy one section per qualified decision point.

### DP1 — [Substantive decision]

- **Initial alternatives:**
- **Solver-visible decisive evidence:** [source, line/table/key/commit, timestamp, provenance]
- **Authoritative hierarchy / reconciliation rule:**
- **Intended grounded conclusion:**
- **Why another path initially looks credible:**
- **Changed state and its exact scope:**
- **Substantive upstream dependencies:** [IDs and *why* they change applicability]
- **Downstream DPs and terminal outputs impacted:**
- **Source-supported invariant/unaffected objects:**
- **Plausible wrong choice and its downstream result:**
- **Grader/evidence check:**
- **Six-part qualification:** plausible Y/N; evidence Y/N; expert judgment Y/N; validity-changing Y/N; material output Y/N; objectively graded Y/N.

### DP2 — [Repeat full DP1 fields]

## C. Annotated causal decision graph

```text
DP1 --[evidence hierarchy changes admissible population]--> DP2
DP2 --[population changes applicable method]--> DP3
DP3 --[method changes decision threshold]--> DP4
DP4 --[requires intervention to affect deployment]--> O1
```

**Non-counting computation/presentation links:**  
**Versioned reassessment (if any):**  
**Qualified DP count:**  
**Dependent DP count/density:**  
**Longest qualified path (edges / decisions):**  
**Independently solved tasks excluded from graph depth:**

## D. State-setting evidence map

| Fact ID | Source + version/time | State established/changed | DP affected | Misleading alternative | Reason conflict is resolvable |
|---|---|---|---|---|---|
| F1 |  |  |  |  |  |

**Chronology (only if material):** economic/effective; observed; processed; knowledge-available.  
**Eligibility and population keys (if material):**  
**Distinct downstream systems/rules (if material):**

## E. Complete intended path and gold/reference answer

| DP | Correct state | Why visible evidence supports it | Derived population/rule/action | Outputs affected |
|---|---|---|---|---|
| DP1 |  |  |  |  |

**Terminal results, full component level:**  
**Reference execution/calculations:**  
**Acceptable method/result variation and tolerances:**  
**Alternative defensible interpretations reviewed:**  
**Source-only independent reproduction:** PENDING / DONE [evidence]

## F. Ablations — full downstream recomputations

| Ablation | First wrong DP | Why credible | Entire recomputed path / evidence | Wrong terminal objects | Invariants preserved | Grader detection | Status |
|---|---|---|---|---|---|---|---|
| A1 |  |  |  |  |  |  | PLANNED / EXECUTED |

**Notice–act gaps:**  
**Undercorrection case:**  
**Overcorrection case:**  
**Correct-total/wrong-components or analogous case:**  
**Internally coherent wrong artifact:**  
**Distance from accepted outcomes:**

## G. Solver-facing sources and minimal prompt

| Source | Real-world owner/origin | Relevant DPs | Decisive facts | Realistic misleading facts | Integrity verification |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

**Solver-facing prompt:** [Role, objective, timeframe/scope, outputs, sources, tools; **not** the hidden DP sequence.]  
**Author-only files kept private:**  
**Allowed tools and environment specification:**

## H. Grading and release

| Check | Observable condition | Type (exact/test/rubric) | Consequence of failure | Gold or oracle test |
|---|---|---|---|---|
|  |  |  |  |  |

**Independent domain review:**  
**Source, schema, and path validation:**  
**Oracle/null grader tests:**  
**Pilot model/version/settings/repetitions:**  
**Earliest observed failed DP and propagation pattern:**  
**Reasoning vs. tool/harness failure distinguished:**  
**Release decisions:** Architecture [APPROVE/HOLD]; Source+Gold [VERIFY/HOLD]; Empirical [VALIDATE/PENDING].

Use `../scripts/validate_blueprint.py` to check declared JSON graph structure. This Markdown blueprint requires substantive human review.
