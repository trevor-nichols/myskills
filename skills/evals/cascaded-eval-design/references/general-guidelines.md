# Cascaded Eval Design Guidelines — General Methodology

**Version:** 2.0 (general-purpose adaptation)  
**Basis:** Adapted from *Cascaded Accounting Eval Design Guidelines*, v1.1 (2026-09-09), incorporating design concepts discussed in Li & Ho, *GeneBench-Pro* (2026).  
**Scope:** Model evaluations involving evidence-dependent expert decisions in any domain.  
**Status:** A methodological guide; an implemented eval still requires source verification, grading checks, and empirical pilots.

## Purpose

Design realistic AI evaluations whose difficulty comes from **dependent expert decisions**, not artificial workload. The solver must recover an analytical or operational path from evidence, revise its working state when facts require it, propagate material judgments, and deliver one consistent result.

> Several initially plausible paths, one evidence-recoverable target (or declared equivalence class), and material downstream consequences for choosing incorrectly.

The principle is portable to scientific inference, software engineering, security, data engineering, legal/contractual analysis, operations, medical research methods, and accounting. Specific expert rules belong in domain-specific profiles. The underlying test is the same: **an early decision changes which later work is valid**.

---

## 1. What “cascaded” means

A **decision point (DP)** is a substantive fork where:

1. Two or more interpretations, analytical paths, or actions look credible before all relevant evidence is assessed.
2. Solver-visible evidence resolves the fork to a defensible outcome, or constrains it to an explicitly acceptable set.
3. The choice changes the later valid scope, population, representation, method, authority, eligibility, rule, branch, or action.
4. A plausible wrong path materially alters a required outcome or observable intermediate artifact.
5. The choice involves professional reasoning rather than mechanical execution.
6. A grader or reviewer can distinguish failure from acceptable variation.

### Parallel work is not a cascade

```text
Solve independent question A ──┐
Solve independent question B ──┼─> Combine answers
Solve independent question C ──┘
```

A pile of hard tasks is still parallel. Repeating a calculation many times does not create new DPs.

### Substantively dependent work is a cascade

```text
DP1: Establish which evidence/state is valid
  ↓ changes eligible records / admissible inputs
DP2: Reconstruct the relevant population
  ↓ changes which rule or estimator applies
DP3: Choose the downstream method
  ↓ changes an action or determination
DP4: Resolve a later condition / reassessment
  ↓ changes selected subsequent work
DP5: Produce and verify the terminal output
```

DP5 counts as a DP only if it contains its own substantive fork; a final reporting operation alone is a terminal step. **The upstream error changes the later task, not only the subtotal.**

### What does not qualify by itself

Opening files; parsing, joins, or data copying; following a prescribed formula; routine refactoring; applying a fixed transformation to a fixed set; formatting; trivial rounding; collecting a known result; generic QA; or splitting one decision into several cosmetic sub-decisions.

A computation can be part of a genuine DP when it supplies an *empirical diagnostic that changes which subsequent method is valid*. The diagnostic's execution alone is not a second DP.

---

## 2. Governing principles

### 2.1 Identifiability before difficulty

The final endpoint must be recoverable **from what the solver is permitted to see and do**. A hidden simulation parameter, private benchmark convention, or desired designer choice is not valid ground truth unless it is identifiable from visible evidence. If multiple expert-valid paths remain, change the evidence/prompt, accept equivalent outcomes, or refrain from assigning a single right answer.

One recoverable answer does not mean an obvious answer. Plausible ambiguity is desirable *before* the evidence is resolved; arbitrary ambiguity is not.

### 2.2 Difficulty from decisions, not inconvenience

Prefer genuine source disagreement, differing time clocks, data-quality diagnostics, omitted/replaced populations, eligibility gates, authoritative specification changes, revision/rollback constraints, hidden selection effects visible through evidence, and model reassessment.

Avoid difficulty primarily from excessive volume, obscure identifiers, incomplete facts, arbitrary thresholds, unrealistic paperwork, tool fragility, and contrived distractions.

### 2.3 Tolerate harmless professional variation

Treat equivalent algorithms, reasonable thresholds that preserve the material outcome, accepted error bounds, different but valid work ordering, equivalent artifacts, and immaterial formatting differences as acceptable where the task allows them.

When the exact method is itself necessary, expose enough constraints to make its selection identifiable. Do not grade an unspoken methodological preference.

### 2.4 Necessary mistakes must be detectable

Fail substantive wrong-state selection, wrong scope/population, wrong controlling source, wrong timing, invalid model choice, incomplete reassessment, missing propagation, overcorrection, and a superficially correct endpoint with materially wrong required components.

### 2.5 Contain the evaluation boundary

Define the solver's role, permitted information, tool/environment capabilities, time of knowledge, domain constraints, outcome contract, and what should happen when the sources are genuinely insufficient. An eval must not require knowledge inaccessible to its solver while calling omission a reasoning failure.

---

## 3. Required development order

```text
Real recurring expert task or documented failure pattern
→ Terminal outcome objects / acceptance contract
→ Qualified decision graph
→ State-setting evidence and causal effects
→ Intended decision path and gold/reference answer
→ Fully propagated wrong-path ablations
→ Solver-facing source-package plan
→ Generate/assemble realistic sources
→ Independent source-only verification
→ Objective or rubric-based grading
→ Pilot runs and validity hardening
→ Verified golden artifact / release certificate
```

**Do not start by generating raw data and then reverse-engineering a story around it.** Data should express a designed reasoning architecture, not accidentally determine it.

Use stage gates: architecture approved; source/gold/ablation verified; empirical validation completed. Never collapse these into a single unqualified “approved” field.

---

## 4. Step 1 — Define the real task, domain, and expert role

Record:

- Domain and specialized subdomain; real working role and authority.
- Recurring real-world workflow or documented type of failure.
- Outcome/decision that a practitioner genuinely needs, not an artificial puzzle objective.
- Scope boundary, relevant date or version, and information-availability assumptions.
- Allowed tool and data access.
- Consequences of wrong work, especially downstream consequences.
- Expected deliverable and why it is auditable/verifiable.
- Source of domain realism: observed cases, practitioner input, literature, technical documentation, or explicitly simulated workflow.

A sophisticated subject is not automatically eval-grade. Find the **first state-setting expert decision** from which later work must follow.

---

## 5. Step 2 — Lock the final output objects

Specify final required outcomes **before** choosing values, records, or source-file layouts.

Possible terminal objects:

- Applicability or eligibility determination; admitted and excluded IDs.
- Corrected population or data representation; classification map.
- Chosen analytical model, estimator, test, or intervention.
- Estimated numerical values with clear units and tolerances.
- Security finding, priority level, remediation choice, patch, or tests.
- Software implementation, dataset transformation, or exact target artifact.
- Contractual consequence, operational action, compliance result, or decision memo.
- Diagnosed cause, status, next action, and effect on other systems.
- Structured JSON output, reproducible notebook, code diff, report, or other deliverable.

The output contract must identify required **components**, not merely their aggregate. Define acceptable equivalent representations and appropriate tolerance semantics (exact IDs, numeric ranges, structural invariants, behavioral tests, or calibrated rubric).

If the target itself cannot be made identifiable, do not force a single scalar answer. Narrow the prompt, expose a decisive constraint, or design an explicit equivalence-class/partially ordered acceptance contract.

---

## 6. Step 3 — Qualify the decision-point architecture

For every candidate DP document:

| Field | Required content |
|---|---|
| DP ID | Stable identifier, e.g. `DP1` |
| Decision | Actual expert fork to resolve |
| Candidate paths | At least two initially plausible options |
| Decisive evidence | Solver-visible evidence that separates options |
| Grounded outcome | Intended conclusion and why |
| Upstream DPs | Prior conclusions on which this DP's applicability depends |
| Changed state | The exact variable, population, representation, or rule updated |
| Downstream effects | Which later DPs/outputs must change |
| Legitimate invariant | What must remain unchanged, with a reason |
| Plausible wrong branch | What a competent but incomplete solver might do |
| Wrong branch consequence | Material output or action difference |
| Grader/verification | Observable check(s) that detect it |

### Six-part DP qualification test

Count a DP only when **all** are yes: plausible alternative; visible decisive evidence; real expert judgment; downstream validity/applicability change; material measurable wrong result; objective or well-defined grading.

### Distinguish graph edge types

- **Causal decision edge:** DP1 selects which cases or rules even enter DP2, or changes which method/source is applicable. Counts toward dependency depth.
- **Computation edge:** DP1 computes an amount used by a fixed formula in DP2 without changing the method, scope, rule, or state. Does **not** count toward dependency depth.
- **Presentation edge:** DP1 flows into a report/format or duplicate output. Does **not** count.
- **Independent edge:** Tasks merely share context; do not claim dependence.

Ask of each claimed causal edge: *If the upstream conclusion flips, must the next expert reconsider which evidence, population, branch, authority, or method is valid?* If not, classify it as arithmetic/presentation rather than a qualified decision dependency.

### Baseline design guidance, not dogma

For a meaningful cascaded eval, a practical starting range is **3–8 substantive DPs**, with multiple genuine dependencies, at least one first-order error that changes a terminal outcome, and enough evidence to distinguish paths. Smaller focused evals can be valuable; larger benchmarks must earn their complexity. Treat fixed DP counts, evidence counts, and file limits as configurable profiles rather than universal laws.

See `difficulty-profiles.md` for nonbinding expert/flagship targets and conditional source/population modules. **Do not split one judgment or invent tasks to hit a quota.**

---

## 7. Step 4 — Construct the dependency graph

Graph the **decisions** separately from mechanical transformations. Annotate every causal edge with its reason:

```text
DP1: Choose the valid event chronology
   | changes which records are eligible at cutoff
   v
DP2: Rebuild the relevant event population
   | changes which analytic assumptions hold
   v
DP3: Select the applicable method
   | changes what follow-up evidence is material
   v
DP4: Reassess the conclusion after a new observation
   | changes correct downstream action
   v
Terminal artifact: decision + measurements + action
```

A valid graph should be acyclic. If a later diagnostic forces reconsidering an earlier result, represent **DP1@initial -> diagnostic -> DP1@revised** or another clear versioned state, not a logic loop.

Record:

- Longest chain of *qualified decision* edges.
- Number and share of DPs with at least one qualified upstream dependency.
- Forks/merges, boundary conditions, and where each output depends on the state.
- Evidence and test that prove each decision edge is substantive.
- Any remaining independent subwork, clearly excluded from depth metrics.

### Cascade strength checks

- Does the upstream fork make a different later analysis or action *valid*?
- Must downstream work be recomputed if the first conclusion changes?
- Could a wrong path still look internally coherent?
- Does the solver have to react to diagnostic evidence rather than only describe it?
- Is there at least one source-supported invariant guarding against overcorrection?
- Is final success possible through a shortcut that bypasses the intended decision sequence? If so, change the output contract/evidence/verification, not just the prompt's prohibition on shortcuts.

---

## 8. Step 5 — Design state-setting facts

**State-setting evidence** establishes or changes which branches, populations, constraints, or actions are valid. Examples across domains:

- Effective, observed, processed, and learned timestamps; versions; release phases.
- Data provenance, source precedence, supersession, and correction notices.
- Eligibility and exclusion criteria; selection/ascertainment processes.
- Calibration, outlier, schema, or QC findings that change method validity.
- Contractual/technical conditions precedent and exceptions.
- Authorization, deployment, ownership, custody, and responsibility mappings.
- Dependencies or features present in an artifact but not reachable at runtime.
- Missingness mechanisms, batch effects, failed diagnostics, conditional models.
- Work completed versus record posted; release/approval state versus physical presence.

For each decisive fact record the exact fact, DP affected, interpretation, wrong reading, source location, source conflict or hierarchy, timestamp/version, and independent consistency checks.

A credible conflict is **locally resolvable**: a careful solver can reconcile it from staged evidence. A misleading record cannot simply be arbitrary falsehood with no discoverable correction.

---

## 9. Step 6 — Lock the intended path and recoverable answer

Solve every substantive decision and calculate, execute, or derive every required outcome **from solver-visible evidence only**. Keep a detailed non-solver-facing reference containing:

- Intended decision/path per DP and decisive evidence.
- Derived scope, IDs, eligibility, and populations at each state.
- Applicable method/rule and parameters.
- Reproducible calculations, transformations, actions, tests, or artifact differences.
- Terminal components and invariants.
- Units, sign/scale conventions, precision, scope/time boundary, and acceptable variation.
- Proof the selected endpoint is observable/recoverable, not hidden designer knowledge.

For simulation, distinguish latent data-generating parameters from finite-sample quantities recoverable by the specified analysis. The latter, not the inaccessible former, should drive grading unless expressly and validly otherwise defined.

Require a defensibility review: can an independent expert produce a different final answer by applying another fully reasonable method? If yes, either extend the accepted outcomes or modify the *solver-visible* evidence and prompt.

---
## 10. Step 7 — Build fully propagated wrong-path ablations

An **ablation** is the actual terminal consequence of replacing one valid upstream decision with an initially plausible wrong decision. It is not merely a list of traps or a verbal guess.

For each material wrong branch record:

1. The earliest mistaken DP and why the wrong path looks reasonable.
2. The missed/misweighted evidence or diagnostic.
3. The incorrect state value and every downstream rule/population/action affected.
4. The resulting full terminal objects, including component-level differences.
5. The invariant objects that correctly remain unchanged.
6. The grader/rubric checks that detect the failure and the margins from tolerances.
7. Whether the wrong artifact still passes shallow checks or internal reconciliations.

### Ablation matrix

| ID | First wrong DP | Plausible shortcut | Decisive evidence missed | Dependent steps redone | Wrong terminal result | Detected by |
|---|---|---|---|---|---|---|
| A1 | DP1 | Wrong source/state |  |  |  |  |
| A2 | DP2 | Wrong population/method |  |  |  |  |
| A3 | DP3 | Wrong timing/threshold |  |  |  |  |
| A4 | DP4 | Notices warning but does not act |  |  |  |  |
| A5 | DP2 | Correct aggregate, wrong components |  |  |  |  |

These are useful archetypes, **not** five mandatory ablations for every task. Select distinct, realistic faults, not five changes to the same record. Flagship packages should normally execute several full-path ablations; see the difficulty profile.

### Representative failure classes

- Wrong source, version, or knowledge state.
- Wrong scope, population, eligibility, or representation.
- Wrong method, rule, policy, architecture, or model.
- Wrong chronology, treatment period, or cutoff.
- Correctly detected anomaly without corresponding action (notice–act gap).
- Partial correction confined to one output, with stale descendants.
- Overcorrection of unaffected populations/components.
- Correct aggregate with materially wrong components, labels, owners, or categories.
- Plausible internally reconciled artifact based on an invalid initial premise.
- Shortcut that gives the same score without demonstrating the target capability.

### Full ablation execution rule

Change the **first wrong state**, rederive all descendant decision states, reconstruct affected populations, rerun applicable analyses or tests, and produce the terminal output. Do not fake separation by manually adjusting a single final value. If two wrong paths accidentally cancel in one aggregate, add component-sensitive checks or reconsider which endpoint is meaningful.

Not every task is numeric. For software, execute the wrong patch and demonstrate failing behavior or incorrect scope. For investigations, show wrong affected-entity sets and required actions. For scientific inference, rerun the estimator on the altered valid set. For document review, derive the wrong contract action and its downstream consequences. If an ablation is not executable, mark the uncertainty and do not claim numerical/executable validation.

### Notice–act and selective-propagation tests

A **notice–act pair** is an observable diagnostic that should change a subsequent decision. Verify a model can fail by describing the evidence correctly but continuing with the invalid analysis. Where appropriate, require two distinct pairs with different downstream effects.

An **invariant** is a source-supported population, decision, or control that must *not* change when the triggering state changes. Record why it stays fixed. Verify both underpropagation and overpropagation; an all-changed answer is not automatically safer than an incompletely changed one.

---

## 11. Step 8 — Design the solver-facing evidence package

Only now decide what files, code, datasets, logs, tool states, or document snippets the solver will see. Every material source should support a decision, establish an invariant, or provide realistic necessary context.

| Source | Real-world owner/origin | Relevant DPs | State-setting facts | Plausible conflict | Join/trace requirement |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Source rules

- Prefer sources reflecting actual workflow ownership and formats.
- Distribute critical facts realistically; do not announce the hidden DP graph.
- Make competing evidence **credible and resolvable**, with provenance and effective-state semantics.
- Include the information the solver needs to choose the right method, even if it must synthesize clues from multiple sources.
- Avoid generic tutorial documents that pre-solve the task.
- Keep sources concise when reality permits; do not impose a universal ten-file limit on domains such as repository-level software tasks.
- Preserve realistic scale when the domain intrinsically demands it. Do not inflate scale to make ordinary data handling masquerade as reasoning depth.
- Maintain a clean separation between solver-visible and author/grader-only materials.

For real documents, verify version and factual accuracy. For simulated documents, create coherent identifiers, authorship, timestamps, system behavior, policies, and contradictions. Do not silently present reconstructed/simulated evidence as a verbatim public case.

---

## 12. Human-authored source guidelines

Human-authored materials might include requirements, contracts, design documents, incident reports, pull-request discussion, review feedback, research notes, study protocols, decision records, operational handoffs, or expert correspondence.

They should have a believable purpose, responsible actor, dates/versions, defined terms, and a realistic amount of context. Put crucial qualifications in the source where an expert would naturally find them. Use apparent conflicts when the actual chain of authority, timing, or applicability resolves the issue.

Keep internal benchmark labels, gold hints, hidden rubrics, ablation names, and meta-instructions out of solver-facing artifacts. The solver should face a credible task, not a puzzle that announces its intended trick.

---

## 13. System-, machine-, and experiment-generated evidence

Machine-origin materials may include code, tests, dependency graphs, CI artifacts, event logs, telemetry, database records, experiment runs, assay readings, reports, simulation outputs, message queues, access audits, and structured extracts.

Use realistic schemas, keys, metadata, IDs, null behavior, legitimate corrections, retries, time shifts, duplicates, and noise proportional to the domain. Distinguish a system-recorded status from the underlying operational state when they differ. Avoid explanatory human commentary inside raw machine exports unless that form genuinely records comments.

Every row, signal, and artifact should have an explainable role. A large dataset can be necessary without being a substantive decision point.

---

## 14. Minimal viable prompt

The solver-facing task should specify:

- Role and operational/scientific context.
- Exactly what decision or output is required.
- Scope/time/version boundary and important legitimate assumptions.
- Available sources, execution environment, and tools where relevant.
- Required output fields and acceptable submission artifacts.
- Numeric units, scales, fixed conventions, and tolerances where necessary for identifiability.

Do not reveal hidden forks, suggest the right method, list the trap locations, expose the reference answer, or prescribe an analytical pipeline when recovering that pipeline is the capability under test.

**A non-prescriptive prompt is not the same as an underspecified prompt.** State any constraint whose omission would permit another equally defensible outcome. If no clean objective target exists, use an evaluated equivalence class or a declared rubric tied to observable task success rather than pretending all experts must agree on an arbitrary method.

---

## 15. Independent verification protocol

Reperform the entire task using *only* the solver-visible sources and capabilities. Ideally, the verifier has not designed the intended answer; an independent expert review is especially valuable in unfamiliar domains.

### 15.1 Evidence/package integrity

Check file inventory, names and renderability, schemas, keys, timezones, versions, source precedence, joins, code/tool dependencies, required package paths, source completeness, solver access, and absence of gold leakage.

### 15.2 Outcome and method integrity

Check every critical scope decision, selected populations, evidence hierarchy, timing, model/algorithm assumptions, executable tests, classification, tolerances, terminal object, and domain-specific invariants. Make explicit what is factual source evidence versus derived analysis.

### 15.3 Decision integrity

For every DP, verify realistic alternative branches, decisive evidence, substantive edges, materially different wrong outcomes, and no defensible alternate gold. Recompute all descendants after source edits. Verify no accidental shortcut and no unearned difficulty from workload or tool instability.

### 15.4 Ablation integrity

Demonstrate wrong-path terminal outcomes from actual re-execution; verify margins versus accepted alternatives; catch wrong-components/right-total; test underpropagation and overcorrection. Every alleged unaffected control must have evidence-backed invariance.

### 15.5 Harness and measurement integrity

Check reproducible tool environment, deterministic grading where feasible, response schema handling, separation of model failures from infrastructure errors, proper comparison against gold/reference source, execution traces when needed, and no leaked labels in training/example data or solver prompts.

For stochastic models, record repeated attempts, versions/settings, and run metadata. Use statistical uncertainty if reporting pass-rate estimates. A zero score from a broken runner is not evidence of expert-level difficulty.

---

## 16. Grading design for cascades

Grade five layers separately where applicable:

1. **Critical upstream conclusions.** The right source, scope, population, or applicability.
2. **Dependency propagation.** The chosen state actually changes every affected descendant output.
3. **Terminal outcome.** Every required field, artifact, result, or action.
4. **Invariants / conservation.** Valid unaffected outputs stay unchanged; no unauthorized expansion of scope.
5. **Execution and deliverable validity.** Tool/application behavior, reproducible tests, schema, required submission.

Use exact tests where the outputs are machine-verifiable. For fuzzy or textual outputs, build bounded rubrics with explicit observable criteria and independently checked examples. Do not grade private hidden reasoning; grade inspectable products and optionally the intermediate diagnostics the task specifically requires.

A final total alone is not enough if a decision-relevant classification, entity membership, or downstream action is required. Likewise, an incidental formatting difference should not fail an otherwise valid solution.

### End-to-end versus diagnostic scores

When the task truly requires *all* critical gates to succeed, use a strict terminal pass/fail as the primary metric, with per-DP diagnostics for insight. Avoid conflating a high rubric score with end-to-end automation. If partial correctness is itself the target capability, state that explicitly and grade accordingly.

---

## 17. Model pilots and hardening

After each run:

1. Grade with the frozen predeclared contract.
2. Identify the earliest *observable* failed decision or state.
3. Trace how descendants followed a wrong yet coherent path.
4. Distinguish not noticing evidence, noticing without acting, partial correction, and overcorrection.
5. Detect shortcuts, leakage, alternate defensible paths, and grader sensitivity to harmless differences.
6. Distinguish domain reasoning failure from tool failure, file corruption, insufficient run budget, and prompt ambiguity.
7. Revise the smallest relevant part of the architecture/evidence/grader, then **revalidate gold and ablations**.
8. Record model/provider/version, sampling/reasoning/tool configuration, attempts, time, and changed artifacts.

### Good hardening

Strengthen a real dependency; add credible evidence conflict with an explicit resolution path; make an existing diagnostic consequential; clarify ambiguous facts; add component-sensitive grading; expose a legitimate invariant; rebuild a population when realistic; require an evidence-driven reassessment.

### Bad hardening

Add unrelated technical topics, inflate records, fragment files pointlessly, bury decisive facts, require unsupported expert guesses, narrow tolerances arbitrarily, exploit flaky tools, or change gold because a strong model disagreed without independently checking validity.

Maintain a genuinely separate held-out evaluation set when optimizing prompts/systems on the benchmark, and report the optimization boundary.

---

## 18. Golden artifact requirements

The golden reference should demonstrate the full intended path, with enough inspection/reproduction information to support audit. Depending on domain it may be a validated code patch, notebook, structured JSON, reference answer and calculations, test matrix, incident action plan, scientific report, or professional deliverable.

Include the state and method decisions, evidence links, output object values, checks/invariants, unresolved qualifications (if any), and a reproducible verification route. A source-specific process profile may require additional outputs (for accounting, entries and reconciliations; for software, tests and expected behavior; for science, estimand/diagnostic details).

Do not assume a spreadsheet is the natural output for every domain.

---

## 19. Blueprint minimum fields

Before generating raw evidence, produce:

```text
Task title:
Domain / expert role:
Real-world workflow / evidence anchor:
Scope date or version:
Solver environment / allowed tools:
Terminal output objects and acceptance semantics:
Difficulty profile: Foundational / Cascaded / Flagship / Custom

For DP1..DPn:
  Decision and initial candidate paths:
  Decisive solver-visible evidence and location:
  Intended conclusion and changed state:
  Substantive upstream dependency (reason for each edge):
  Downstream validity, scope, or method changes:
  Unaffected states / source-supported invariants:
  Plausible wrong interpretation and fully propagated result:
  Grader rules / expected artifacts:

Annotated dependency graph:
State facts / authority / chronology table:
Intended path and gold contract:
Executed/expected ablation matrix and tolerances:
Solver-facing source design:
Known alternative defensible paths and resolution:
Release statuses: architecture / source+gold / empirical:
```

Use `../assets/blueprint-template.md` for a fillable blueprint. For graph-count checks, see the JSON example and validator in `../assets/` and `../scripts/`.

---

## 20. Final quality and release gates

Before claiming architecture approval, verify:

1. Every claimed DP is a substantive and evidence-resolvable choice.
2. Every claimed causal edge changes downstream validity, not only a calculation.
3. The endpoint or equivalence class is identifiable from allowed solver evidence.
4. At least one important wrong path produces a materially different final artifact.
5. Independent realistic alternatives and harmless variation are handled fairly.
6. No secret methodology or hidden data-generating parameter is required to pass.
7. Files and prompts express real expert work without leaking the intended path.
8. Invariants test overcorrection, while affected descendants test missing propagation.
9. The grader actually detects wrong states, wrong components, and failure to act.
10. Difficulty derives from expert decisions, not volume, ambiguity, or runtime friction.

For *release*, further require independently reproduced gold, executed relevant ablations, grader oracle/null tests, working artifacts, and pilots with metadata. For a *flagship* claim, complete the high-difficulty acceptance certificate and any relevant domain profile. A blueprint approved on paper is not an empirically validated benchmark.

---

## 21. Generalized acceptance certificate

Complete `../assets/acceptance-certificate.md` for every released eval. Its stages separate intended architectural properties from demonstrated verification evidence and observed pilot results. If an acceptance field is planned but not tested, mark **PENDING**. Do not turn projected difficulty into claimed failure rates.

---

## Related research and design lineage

This methodology retains the original accounting guideline's ideas of one defensible answer, qualified substantive decision points, source-driven state transitions, wrong-path ablations, selective propagation, and component-level grading. It generalizes the domain of application while preserving those ideas.

GeneBench-Pro (Jeremy Li and Andrew Ho, June 30, 2026) describes domain-specific multi-stage statistical inference, decision points, finite-sample recoverability, carefully controlled data generation, and wrong-path ablations. It reports that models often notice relevant evidence without adjusting downstream methodology. This skill adapts those evaluation-design ideas beyond scientific inference; it is **not** an official OpenAI or GeneBench skill. Reference: https://doi.org/10.64898/2026.06.29.735386.
