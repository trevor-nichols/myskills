---
name: cascaded-eval-design
description: Design, audit, and harden rigorous AI evaluations built from dependent expert decisions, where an upstream evidence-based choice changes the valid downstream population, method, state, or action. Use for benchmark creation, adversarial eval design, expert reasoning tests, multistage workflows, causal decision graphs, gold-answer construction, wrong-path ablations, grader design, or debugging evals that are too easy, ambiguous, or artificially difficult. Works across accounting, science, software engineering, security, operations, and other domains.
metadata:
  version: "1.0.0"
---

# Cascaded Eval Design

Build **decision-dependent evaluations**, not long checklists of independent tasks. The defining property is:

> **An upstream error changes what downstream work is valid, not merely a number passed into a fixed computation.**

Several paths may be plausible at first. Evidence available to the solver must resolve the important forks. A valid solution propagates that state through every affected output and leaves genuinely unaffected outputs unchanged.

## Choose the working mode

Infer the mode from the user's task; ask only for an essential missing constraint.

| Mode | Use when | Deliver |
|---|---|---|
| **Design** | Creating a new cascaded benchmark | Blueprint, graph, evidence plan, gold contract, ablation plan, grader plan |
| **Convert** | Turning an existing task or eval into a cascade | Before/after dependency graph, redesigned gates, required changes |
| **Audit** | Checking an existing evaluation | Qualified DP inventory, failed gates, ambiguity/shortcut findings, fixes |
| **Build** | User explicitly requests a complete runnable eval | Solver prompt/data, non-solver gold, ablations, grader, verification, run instructions |
| **Harden** | An eval exists but under-tests models | Earliest observed failure, stronger *legitimate* dependencies, new ablations, revalidation |

Read `references/general-guidelines.md` for the full methodology. Read `references/difficulty-profiles.md` when assigning a difficulty profile. Read `references/domain-examples.md` for examples outside accounting. If working in accounting, also read `references/accounting-profile.md`. Use templates in `assets/` rather than improvising file contracts.

## Nonnegotiable invariants

1. **Substantive decision points (DPs).** A DP is a genuine fork between initially plausible interpretations or expert actions. Source evidence must distinguish them. The choice must change later *valid* data, applicability, population, method, state, or action and materially change an assessable result.
2. **Substantive edges.** A graph edge counts as a *decision dependency* only if the upstream conclusion changes which downstream branch, rule, evidence, or population applies. Pure arithmetic propagation, file joins, implementation steps, formatting, and repeated computations do not count.
3. **Recoverable outcome.** The solver-visible problem must identify the requested result and contain enough evidence for a defensible answer or an explicitly defined equivalence class of acceptable answers. Do not grade a hidden simulation parameter that cannot be recovered from the visible evidence.
4. **Notice -> act -> propagate.** Include opportunities where evidence invalidates an initial state. A model must not receive full credit for mentioning the warning without revising the downstream work.
5. **Selective propagation.** Identify what must change *and what must remain unchanged*. Test undercorrection, overcorrection, and plausible internally consistent wrong paths.
6. **Ablation proof.** Re-execute major plausible wrong branches to their terminal outputs. A wrong-path description without a tested outcome is only a hypothesis.
7. **Measurement integrity.** Separate reasoning failures from missing inputs, runtime/tool failures, grader defects, and defensible alternative methods. Pilot results are empirical evidence; graph size is not a model pass-rate prediction.

## Workflow: design backwards from the real outcome

Follow this order; **do not generate raw source data before the architecture and gold contract are approved**.

1. **Ground the task.** Identify the real expert role, recurring workflow, decision-relevant endpoint, consequences of getting it wrong, operating context, and time/reference boundary. Start from real workflows or documented failure patterns when available; label synthetic illustrations as synthetic.
2. **Lock the terminal output contract.** Specify precise final objects to grade: decisions, entities, selected records, classifications, predictions, code/test artifacts, measured quantities, actions, reports, or combinations. Specify tolerances and harmless variation.
3. **Invent no decorative gates.** Propose candidate DPs, test each against the qualification checklist, reject mechanical work, and draw a directed acyclic decision graph. If reassessment is real, use versioned/dated states rather than a cycle.
4. **Identify state-setting evidence.** For each fork, record candidate conclusions, decisive solver-visible evidence, provenance, conflicts, timestamps/versions, and what a plausible wrong interpretation would do.
5. **Derive the intended path.** Solve from only the information the solver will receive. Record gold values, methods, identifiers, causal state changes, provenance, and accepted equivalents; have an independent reviewer or reproduction if feasible.
6. **Execute wrong-path ablations.** For each strategically chosen wrong decision, propagate the alternative all the way to the deliverable; report changed terminal objects, preserved invariants, and separation from acceptable answers. Rework all descendants, not just one cell.
7. **Design solver-facing sources.** Place facts in realistic documents, datasets, logs, codebases, or tools. Make conflicts credible and resolvable. Do not leak the decision graph, grader, gold solution, or ablation targets into solver-facing instructions.
8. **Create the minimal viable prompt.** State role/context, exact requested endpoint, timeframe/scope, available sources, output schema, and allowable conventions. Do **not** prescribe the hidden decision sequence. Add clarifying constraints if otherwise several expert approaches would legitimately diverge.
9. **Verify independently.** Reproduce the solution from solver-only materials. Validate source integrity, dependency graph, ablations, tolerances, grading rules, environmental reproducibility, and no accidental shortcut.
10. **Pilot and harden.** Record model, version, reasoning/tool settings, date, attempts, grades, and observed failures. Locate the earliest failed DP; distinguish failure to notice from failure to act and underpropagation from overpropagation. Revise and revalidate. Do not tune arbitrary thresholds just to lower scores.
11. **Package and release.** Keep solver-visible and author/grader material isolated. Record architecture approval, source/gold validation, and empirical validation as **separate statuses**.

## Qualify each decision and edge

For every claimed decision point, demand six yes/no answers:

- Are at least two paths initially plausible to a competent solver?
- Can the correct path be recovered from solver-visible evidence?
- Is expert reasoning, rather than routine mechanics, needed to resolve it?
- Does the choice change downstream *validity or applicability*, not just a numerical value?
- Does a realistic wrong choice materially alter a graded outcome or required intermediate artifact?
- Can objective grading or a well-specified rubric identify the failure without penalizing a defensible equivalent?

Reject a DP if any answer is no; redesign or downgrade difficulty. For each graph edge, ask: **If I flip the upstream conclusion, would a downstream expert need to reconsider the population, source authority, decision rule, or method?** If only a subtotal changes, mark a `calculation` edge and do not count it toward causal depth.

Use the decision table and graph in `assets/blueprint-template.md`. For JSON graph records, use `assets/blueprint.example.json` and run `python scripts/validate_blueprint.py path/to/blueprint.json` to compute **structural** metrics. The script does not certify substantive validity; that requires evidence review.

## Select difficulty without gaming the metric

- **Foundational:** One or two genuine forks; useful for a focused capability check but generally not a deep cascade.
- **Cascaded / Expert:** Several meaningful forks with a causal chain, identifiable endpoint, and demonstrated wrong-path separation.
- **Flagship:** Sustained decision dependency, multiple state transitions, distinct downstream consequences, full ablations, selective propagation, and empirical validation. Use the configurable gates in `references/difficulty-profiles.md`; do not impose accounting-specific requirements on unrelated domains.

Do not infer difficulty from file count, row count, technical jargon, human hours, or mere DP count. Reject artificial complexity added just to satisfy a threshold.

## Grade the effect of decisions, not private thoughts

A robust grading contract covers **terminal correctness**, **critical intermediate artifacts if required**, **propagation consistency**, **invariants**, and **execution quality**. Use observable outputs, artifacts, and tool traces; do not demand hidden chain-of-thought or a single prescribed internal reasoning style. A model reaching the right total with materially wrong components must not automatically pass a component-sensitive task. A model using a different defensible method must not automatically fail.

Where useful, report both a strict all-critical-outputs pass/fail measure and diagnostic stage-level scores; do not substitute partial credit for an explicitly end-to-end success requirement.

## Working and release rules

- Prefer an existing user's sources, grader, harness, and templates to unnecessary replacements.
- Never label an **unverified** gold answer, ablation, or model pass rate as verified.
- If a missing real-world fact or underspecified target admits multiple defensible outcomes, request a minimal clarification, add a solver-visible constraint, broaden the acceptance set, or withhold release. Never assume a private preferred interpretation.
- If the task naturally supports only a short cascade, say so instead of inventing unrelated branches.
- If only an architecture is requested, create the architecture; do not imply a complete runnable benchmark exists.
- Keep proprietary/domain-specific rules in an optional profile and keep this core domain-neutral.

## Expected deliverables

In **Design/Convert**, provide a filled blueprint, graph with substantive annotated edges, evidence plan, reference answer contract, ablation matrix, and qualification risks. In **Audit**, provide a pass/hold assessment with exact failed DP/edge IDs and targeted changes. In **Build**, add solver-facing files, non-solver solution/verification/graders, and reproducible test instructions. In **Harden**, provide before/after graph and revalidated ablations.

Use `assets/acceptance-certificate.md` as the review artifact. Cite the user's actual evidence; mark planned checks as **pending**, not passing.
