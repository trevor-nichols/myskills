# Difficulty Profiles for Cascaded Evals

Use these profiles to **calibrate design ambition**. A count is a structural proxy, not proof of expert difficulty or empirical model performance. The core skill works with any domain; apply only conditions that belong to the underlying professional task.

## Levels

| Level | Typical shape | Release interpretation |
|---|---|---|
| **Foundational** | One or two substantive forks followed by mechanical steps or a fixed method | A useful focused evaluation, not a substantial cascade |
| **Cascaded / Expert** | Several qualified DPs, at least a meaningful dependent chain, source-supported branch resolution, terminal separation | A defensible multistage reasoning eval |
| **Flagship / Deep cascade** | Sustained causal depth, multiple state changes, multi-system/decision interactions, ablation proof, invariant checks, empirical validation | High-difficulty *candidate*, validated only after pilot evidence |

Treat the following as **recommended default design targets**, not arbitrary hard laws. If the real task cannot sustain them naturally, label it honestly or choose a task with a stronger architecture. Never split one decision merely to inflate counts.

## Recommended flagship structural profile

| Dimension | Recommended target | What to count |
|---|---|---|
| Qualified decisions | Approximately 6–8 or more genuine forks | Evidence-resolvable, outcome-material expert decisions |
| Substantive dependency | 4+ DPs with qualifying upstream dependencies; roughly >=60% of all DPs | Count dependent DPs once; exclude arithmetic-only edges |
| Causal path | A longest chain of >=4 causal decision edges connecting >=5 qualified DPs | Only edges that change downstream applicability/state/method |
| Distinct state changes | >=2 transitions in genuinely different variables | Not two copies of one correction |
| Decision-driven second-order consequence | >=1 downstream system with **its own** eligibility/threshold/method/decision criteria | Not copied totals, reporting, or formatting |
| Wrong-path evidence | Multiple substantively distinct executed ablations, ideally 3–5 | Rerun descendants and preserve unaffected controls |
| Balanced/confident wrong path | >=1 credible incorrect solution that passes superficial internal checks | Must fail a material decision outcome |
| Notice–act gap | >=2 opportunities to diagnose and then change course; verify >=1 full wrong-path failure | Recognition alone is not propagation |
| Selective propagation | >=1 source-supported invariant and >=1 correction with multiple affected descendants | Test over- as well as undercorrection |
| Fair grading | Graded outcomes separate material errors from harmless alternatives | Stable tolerance/equivalence contract |
| Independent review | Source-only reproduction and expert validity review | No assumption that a designer's initial answer is always right |
| Empirical validation | Pilots across appropriate model settings and repeated attempts | Track scores, error taxonomy, uncertainty; no guessed pass rates |

### Conditional modules — only if natural to the task

**Evidence reconciliation module** (document/system-heavy domains): Target multiple evidence-state types, at least two resolvable conflicts, and explicit source authority/recency. Do not invent paperwork for an algorithmic task that naturally uses a single artifact.

**Population reconstruction module** (statistics, analytics, finance, compliance, entity scope): Rebuild included/excluded/replaced records from raw evidence. Where multiple distinct purpose-specific populations exist, propagate changes differently into each and reconcile their relationship. Do not make two identical subsets merely to claim two populations.

**Chronology module** (events, regulations, experiments, incidents, release systems): Distinguish event effectiveness, processing, availability, and observation when those clocks actually affect outcomes. Do not manufacture extra clocks for a timeless proof or algorithm.

**Component-conservation module** (multi-component endpoints): Require at least one plausible right-total/wrong-components result and conservation/invariant checks. If a task has no meaningful aggregate, replace this with the domain's analogous **apparently passing surface metric / materially wrong underlying behavior**.

**Executable artifact module** (coding/security/data pipelines): Require an executable regression, behavior difference, or deployment/configuration constraint—not fake balances or unnecessary reports.

**Scientific inference module** (model selection/estimation): Require identifiable estimands, robustness to nearby valid analysis choices, adequate QC controls, and separation from plausible wrong estimators.

### Architecture versus evidence

A certificate records actual findings. Label separately:

1. **Architecture approved**: Qualified graph, evidence/state map, identifiable target, ablation plan, and plausible intended computations are coherent.
2. **Source and gold verified**: Sources exist, independent solver-only solution reproduces gold, ablations have been executed, and grader/harness tests pass.
3. **Empirically validated**: Pilots genuinely tested reasoning under specified model/version/tool settings and acceptance criteria.

An architecture with six nodes but no executed wrong paths is **not** a validated flagship eval. An eval with three exceptionally hard dependencies may be more discriminating than one with ten shallow forks, but its structural classification should be explicit rather than retroactively redefined.

## Original accounting high-difficulty profile

The provided accounting guidelines (v1.1, 2026-09-09) used a stricter **accounting-specific** flagship acceptance certificate:

- At least 6 substantive DPs; at least 4 dependent and at least 60% dependent; >=4-edge/5-DP causal path.
- Full population rebuild affecting at least two purpose-specific populations, with reconciliation rather than forced equality.
- Two distinct material state transitions, three evidence-state types, and two locally resolvable source conflicts.
- A relevant economic/effective versus processing/cash/information chronology split.
- A genuinely different second-order accounting, contractual, regulatory, reimbursement, or settlement model.
- Three to five full ablations (five preferred), balanced wrong result, correct-total/wrong-components case, two notice–act opportunities, and selective propagation.
- A maximum of ten model-facing files and domain-specific numerical, financial-reporting, grading, and workbook checks.

Keep those **when designing an accounting flagship eval** if the governing project requires them. Do **not** impose accounting journal entries, reconciliations, source limits, or a particular numeric representation on all domains.

## Structural metric definitions

With DP set `V` and substantiated decision edges `E`:

- `qualified_dp_count = |V|` after rejecting mechanical pseudo-decisions.
- `dependent_dp_count = count(v in V with >=1 incoming substantive DP edge)`.
- `dependency_density = dependent_dp_count / qualified_dp_count` (zero for no qualified DPs).
- `longest_causal_path_edges = max number of substantive edges along a directed path`.
- `longest_causal_path_nodes = longest_causal_path_edges + 1` if there is at least one DP.

Ignore pure calculation/format links in those metrics. Use `../scripts/validate_blueprint.py` to check declared structure only. The script cannot know whether an asserted edge is truly substantive; an expert must adjudicate it.

## Audit heuristics

- **Too easy:** A user-provided final population, preselected estimator/algorithm, or prescriptive prompt collapses the chain to a formula.
- **Hard for the wrong reason:** An incomplete file, vague objective, broken dependency, or multiple plausible gold outcomes lowers scores spuriously.
- **Overfitted:** Each new pilot failure produces an arbitrary exception aimed at that one model.
- **Credibly difficult:** A wrong initial decision can create an internally coherent analysis or artifact, while independent source evidence makes the intended path uniquely recoverable, and the grader reliably distinguishes the paths.
