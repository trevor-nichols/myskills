# Commit Templates

Use the structured format for non-trivial changes. Use minimal only for tiny edits.

## Structured format (recommended)

```text
<type>(<scope>): <imperative summary>

Why
- <what problem or need triggered this change?>

What changed
- <bullet 1: concrete change>
- <bullet 2>
- <bullet 3>

Impact
- <user-visible behavior change, API change, perf change, or "No user-visible change">

Tests
- <exact tests run / commands> (or "Not run (not requested)")

Notes
- <migrations, rollout steps, backward compatibility, risks, flags, config, etc.> (use `- None` if not applicable)

Refs
- <ticket/issue/milestone IDs, PR link>
```

## Minimal format (tiny commits only)

```text
<type>(<scope>): <imperative summary>
```

## Types

- feat (new user-facing behavior or capability)
- fix (bug fix)
- refactor (behavior same, code improved)
- perf (performance improvement)
- test (tests only)
- docs (docs only)
- chore (maintenance, tooling, deps)
- ci (CI pipeline changes)
- build (build tooling)
- revert (reverting a prior commit)

## Scope

Short area name: api, frontend, auth, billing, db, workers, infra, deps, etc.

## Examples

### Feature

```text
feat(billing): add usage totals endpoint and wire into dashboard

Why
- UI needed a single source for monthly totals across products.

What changed
- Added GET /v1/billing/usage-totals
- Implemented service aggregation + response DTO
- Updated dashboard to fetch and render totals

Impact
- Dashboard now shows accurate totals; no breaking API changes.

Tests
- pytest apps/api-service/tests/test_billing_usage_totals.py
- pnpm test --filter billing-dashboard

Refs
- #139, BE-007
```

### Fix

```text
fix(auth): prevent refresh token rotation race on concurrent requests

Why
- Parallel refresh requests could invalidate the newest token.

What changed
- Added transactional token rotation with single "active" constraint
- Returned consistent error on stale token reuse

Impact
- Fewer unexpected logouts under concurrency.

Tests
- pytest apps/api-service/tests/test_auth_refresh_race.py

Refs
- BUG-214
```

### Refactor

```text
refactor(frontend): centralize API error mapping for consistent toasts

Why
- Multiple components handled errors inconsistently.

What changed
- Introduced apiErrorToMessage() utility
- Removed duplicated inline mapping in 6 components

Impact
- No functional change; UX messaging is now consistent.

Tests
- pnpm test
- pnpm lint

Refs
- FE-016
```
