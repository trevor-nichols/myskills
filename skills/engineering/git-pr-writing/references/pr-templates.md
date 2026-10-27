# PR Templates

Use the full template for most PRs. Use compact only for truly tiny changes.

## Full template (recommended)

```text
## Summary
- <what changed + user impact>
- <what changed + reviewer should know>
- <risk/flag/migration callout if relevant>

## Context / Why
- Problem: <what was broken/missing>
- Goal: <what “good” looks like>
- Non-goals: <what this PR intentionally does not do>

## Changes
- <Area/Module>: <concrete change>
- <Area/Module>: <concrete change>

## How to Test
1) <manual steps>
2) <edge case / failure case>
3) Commands:
   - `<command>`
   - `<command>`
   - Tests: <exact tests run> OR `Not run (not requested)`

## Screenshots / Demo (if UI)
- Before: <link or image>
- After: <link or image>
- N/A if no UI changes

## Rollout / Backout
- Rollout: <flag/staged deploy/migration order>
- Backout: <safe revert steps>
- Data/Migrations: <additive? destructive? irreversible?>

## Risks / Notes
- Risk: <what could go wrong>
- Mitigation: <monitoring/guards/fallbacks>
- Compatibility: <breaking changes? none?>
- Follow-ups: <what’s next, if anything>

## Checklist
- [ ] Tests added/updated (or N/A)
- [ ] Docs/README updated (or N/A)
- [ ] Logging/metrics added (if needed)
- [ ] Migration/flag plan documented (if needed)
````

## Compact template (tiny PRs only)

```text
## Summary
- <1–2 bullets>

## How to Test
- Tests: <exact tests run> OR `Not run (not requested)`
```

## Examples

### Feature

```text
## Summary
- Adds usage totals API and wires results into the billing dashboard.
- Introduces additive DB table for cached aggregates (TTL cleanup job).

## Context / Why
- Dashboard needed a single source for monthly totals across products.

## Changes
- API: Add `GET /v1/billing/usage-totals`
- Service: Aggregate per product + tenant, return DTO
- UI: Fetch totals + render in billing overview

## How to Test
1) Load Billing → verify totals appear for an active tenant.
2) Validate empty tenant shows 0s (no error).
3) Commands:
   - `pytest -k usage_totals`
   - `pnpm test --filter billing-dashboard`
   - Tests: Not run (not requested)

## Rollout / Backout
- Rollout: enable `billing_totals=true` for 10% → 100%
- Backout: disable flag; API remains additive

## Risks / Notes
- Risk: incorrect aggregation for edge tenants
- Mitigation: counters + dashboard sanity checks
```

### Fix

```text
## Summary
- Fixes refresh-token rotation race to prevent intermittent logouts.
- Adds test coverage for concurrent refresh requests.

## Context / Why
- Parallel refresh calls could invalidate the newest token.

## Changes
- Auth: transactional rotation + single active constraint
- API: consistent error for stale token reuse
- Tests: concurrency regression

## How to Test
1) Simulate 2 parallel refresh calls → one succeeds, one returns expected error.
2) Commands:
   - `pytest -k refresh_race`
   - Tests: Not run (not requested)

## Risks / Notes
- Low risk; change is isolated to refresh flow
```
