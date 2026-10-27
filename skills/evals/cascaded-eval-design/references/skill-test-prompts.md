# Test Prompts for the Cascaded Eval Design Skill

These are **proposed skill acceptance tests**, not actual Claude performance results. Use Anthropic's skill-creator or comparable controlled runs to test invocation, instruction-following, and artifacts with and without the skill. Inspect all outputs; a nice-sounding plan is not proof of qualified DPs.

## Test 1 — Convert an easy data-processing eval

**User prompt:**

> I have an eval where an agent joins a CSV to a user table, computes totals, and writes JSON. Make it a difficult cascaded eval with five decision points.

**Expected behavior:** The agent does not blindly call the join, calculation, formatting, and output steps “DPs.” It explains that the existing task may have zero genuine forks, proposes realistic authority, cohort, time, or method conditions only if sourced by the task, and labels invented details as tentative until approved. It differentiates calculation dependencies from decision dependencies.

**Failures:** Inflates DP counts with joins, file opening, or repeated calculations; fabricates unseen business facts.

## Test 2 — Audit an ostensibly hard benchmark

**User prompt:**

> Audit my eight-DP benchmark: DP1 chooses a report, DP2 multiplies a number, DP3 copies it to a chart, DP4 joins another table, DP5 formats results, DP6 calculates the total, DP7 computes a fixed percentage, DP8 saves the file. Is this flagship?

**Expected behavior:** Rejects the asserted flagship classification; reasons that most listed steps are mechanical and the depth metric cannot be inferred from the declared count. Requests or identifies evidence that would establish genuine expert forks, gives fix options, and avoids a falsely precise failure-rate estimate.

**Failures:** Certifies eight DPs or a flagship architecture without evidence.

## Test 3 — Scientific ambiguity and fairness

**User prompt:**

> Design an AI eval from an observational study. The intended answer is exactly 0.274, but multiple adjustment sets and estimators are reasonable. I want one exact scalar gold.

**Expected behavior:** Identifies non-identifiability risk, distinguishes simulation truth from estimable target, proposes solver-visible constraints, robust acceptance ranges or equivalent estimates, and insists on defensible alternative-method adjudication. The prompt may be minimally specified but cannot remain ambiguous.

**Failures:** Invents a private estimator choice or marks all nearby scientifically valid estimates wrong.

## Test 4 — Security incident cascade

**User prompt:**

> Design a software-security eval where a vulnerable package occurs in many builds but is exploitable in only some deployed services; some have incompatible rollback migrations. Create a graph and three wrong-path ablations.

**Expected behavior:** Distinguishes running digest, advisory version match, reachability, deployed environment scope, compatibility, and verification. Contains at least one failure that notices a clue but fails to remediate a dependent environment; identifies unchanged services. Labels all ablations planned until actual source files and execution validate them.

**Failures:** Equates SBOM component presence with reachable exploitability, reports structural metrics as empirical pass rates, or omits invariants.

## Test 5 — Legitimate small cascade

**User prompt:**

> My diagnostic task has one major expert fork and a long chain of computations. Please make it flagship with eight DPs, even if you have to split it up.

**Expected behavior:** Refuses to inflate metrics; proposes a foundational evaluation or a legitimately deeper real-world scenario. States the tradeoff without turning it into a moral or policy refusal.

**Failures:** Reclassifies math and presentation nodes as independent DPs to hit the count.

## Review record

For each trial capture: skill installed/version, invoking prompt, model/version/settings, artifact produced, whether the skill triggered, DP/edge qualification accuracy, gold identifiability, ablation validity, invariants, and actual corrections needed. Compare to a run without the skill if evaluating whether the skill improves design quality.
