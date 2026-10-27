# Domain Examples: Genuine Cascades vs. Parallel Work

These are **illustrative synthetic blueprints**, not released, independently verified benchmark packages. The examples show what a design must *eventually verify with actual staged evidence*. Their claimed DPs must pass the six-part qualification test before being counted.

## Example A: Software security — Vulnerable release triage

**Expert role:** Application security / release engineer.  
**End task:** Determine which deployed environments are actually exposed, apply an appropriate mitigation without breaking compatibility, and provide a verified remediation map.  
**Operational evidence:** Artifact digest manifest, release tags, signed deployment audit, software bill of materials, runtime call graph, rollout log, schema-migration manifest, and test results.

### Miniature controlled facts (synthetic)

- A security advisory applies to `parsekit` **version 1.8** when its `decodeRemote()` function is reachable from an untrusted ingress.
- `web-prod`: running digest `D21`, contains `parsekit` 1.8, exposed ingress reaches `decodeRemote()`.
- `web-eu-canary`: running digest `D21`, same exposure.
- `admin-prod`: running digest `A21`, contains `parsekit` 1.8, but the vulnerable function is not reachable from untrusted ingress.
- `worker-prod`: running digest `W20`, contains `parsekit` 1.7, not affected by this advisory.
- A human-maintained release-tag table is stale about what the canary runs; the signed deployment audit resolves it.
- A newer database migration prevents safe rollback of the web service to the prior application release; the compatible mitigation is a patched forward build that updates `parsekit` while preserving the schema version.

### Intended substantive decision chain

```text
DP1: Which source identifies each *running* artifact? (tag vs signed digest audit)
     ↓ establishes authoritative deployed versions
DP2: Which live artifacts contain the advisory-matched dependency?
     ↓ changes which binaries are candidates for exploitability review
DP3: In which candidates is the vulnerable function reachable from ingress?
     ↓ changes the actual exposed environment population
DP4: Which deployment environments need intervention?
     ↓ changes applicable remediation and test population
DP5: Is rollback valid given the schema migration, or is forward patch required?
     ↓ changes deployable mitigation
DP6: Which environments require regression verification, and which remain untouched?
     ↓ terminal patch/deployment map + invariant checks
```

**Proposed terminal objects:** `exposed_environments = {web-prod, web-eu-canary}`; `not_exposed = {admin-prod, worker-prod}`; `mitigation = compatible patched forward build on both web environments`; `no_restarts = {admin-prod, worker-prod}`; plus executable tests showing patched ingress behavior and preserved DB compatibility.

### Ablations to implement and test

| Wrong path | First wrong decision | Material expected consequence | Guard |
|---|---|---|---|
| A1 | Trust stale release tags over signed deployed digests | Misses the EU canary, so a vulnerable environment remains unpatched | Deploy audit / canary test |
| A2 | Treat component presence as exploitability without reachability | Needlessly targets admin-prod and misstates actual exposure | Runtime call-graph evidence |
| A3 | Select rollback without checking schema compatibility | Rollback artifact fails migration-compatibility test | Migration guard |
| A4 | Note canary exposure but patch only production | Accurate diagnosis, incomplete propagation | Verify both deployed digests |
| A5 | Report `2` exposed environments but substitute admin-prod for EU canary | Correct count, wrong components; dangerous incomplete remediation | Exact membership and unchanged-environment checks |

This example requires **real simulated staged files and runnable checks** to become a validated eval. The sketch alone is not evidence that six qualified DPs exist or that all downstream choices are distinct; source review must exclude any branch that becomes mechanical once an earlier decision is made.

## Example B: Scientific statistics — Time-dependent intervention analysis

**Expert role:** Applied statistician.  
**End task:** Estimate a well-defined intervention effect from observational data and report a decision-relevant estimate with diagnostics.

Potential causal chain:

```text
DP1: Recover which observations correspond to the target sampling population
  ↓ selects valid observation units
DP2: Determine whether entry/selection introduces a conditional population
  ↓ changes eligible follow-up and estimand
DP3: Reconstruct intervention timing versus outcome-risk intervals
  ↓ changes whether exposure is time-varying
DP4: Diagnose whether evolving patient/subject state confounds intervention timing
  ↓ changes estimator class and assumptions
DP5: Choose/validate method against observed diagnostics
  ↓ changes admissible weighting/model and uncertainty
Terminal: recoverable estimand, estimate, intervals, and method validity
```

A candidate ablation is to use a fixed-exposure model where intervention is time varying, which can introduce immortal-time bias. Another is to use only tested or complete-case records when the target is the full eligible population. A third is to notice confounder feedback but fit an estimator whose assumptions remain invalid. Do not prescribe a single estimator without showing the data and assumptions that make alternatives untenable; grades must permit scientifically defensible equivalents.

**Important:** The correct target should be the quantity identifiable from the observed finite sample under declared assumptions, not the hidden parameter used to synthesize the sample. This is a central methodological lesson from GeneBench-Pro.

## Example C: Supply-chain operations — Product eligibility and delivery action

**Expert role:** Quality and logistics lead.  
**End task:** Determine which lots can legally/operationally ship by a defined cutoff, which customers are affected, and what replenishment actions are required.

Potential chain:

```text
DP1: Choose authoritative quality-rejection state across test, retest, and release approval
  ↓ changes releasable lot IDs
DP2: Distinguish repacked/replaced lots from duplicate legacy lot records
  ↓ changes true available inventory population
DP3: Apply destination-specific eligibility and temperature-history rules
  ↓ changes which orders each lot can satisfy
DP4: Reconstruct loaded/arrived timestamps relative to holds and customer cutoff
  ↓ changes shipments that must be redirected versus left alone
DP5: Recompute service commitments from corrected eligible/ship-to populations
  ↓ changes replenishment priority and notice obligations
Terminal: lot/order allocations, held shipments, notices, and unchanged controls
```

**Important test:** Correct total inventory is not sufficient if the lot IDs are wrong or if the solver moves inventory that belongs to an unaffected customer. A valid invariant might be a fully released lot delivered before a later hold that does not apply retroactively. The rule and dates must be supported by staged sources, not imagined after the fact.

## Example D: What looks complex but is not a deep cascade

A prompt requiring an agent to (1) parse 20 documents, (2) run the same formula for each document, (3) produce a table, (4) sum the table, and (5) format a slide deck has **zero or very few qualified decision forks** even if it takes hours. Its length measures processing burden, not cascaded expert judgment.

Compare a shorter task that requires choosing an authoritative document version, rebuilding a population, reselecting a valid analysis method, interpreting a new diagnostic, and propagating a changed state into a distinct follow-on decision. That second task measures the targeted capability.

## How to use these examples

Translate the same architecture into a domain's *natural objects*:

| Generic abstraction | Science | Software/security | Operations | Accounting |
|---|---|---|---|---|
| State-setting evidence | QC, cohort metadata | Digests, traces, migrations | Status, approval, telemetry | Contract, legal/effective date |
| Valid population | Samples/subjects | Deployed artifacts/environments | Lots/orders | Transactions/entities |
| Model applicability | Estimator/causal assumptions | Remediation/deployment strategy | Eligibility/allocation rule | Recognition/measurement basis |
| Second-order consequence | Translational decision | Rollout/testing constraint | Customer commitment | Contractual/regulatory test |
| Invariant | Excluded controls | Unaffected service | Unaffected order | Unaffected balance/account |
| Terminal artifact | Estimate + diagnostics | Patch + verification | Action/allocations | Workpaper + report |

Do not force unnatural objects across domains. The defining mechanism is **causal decision dependence**, not similarity of vocabulary.
