---
name: git-pr-writing
description: Draft a professional Pull Request (PR) title and description from the current branch’s changes vs the base branch (default - repo default branch, usually main), then create or update the GitHub PR by default. Use when asked to write, improve, standardize, or generate a PR description, or to create/update a PR. Always compute the merge-base against upstream default branch, summarize changes, include testing instructions/status, and call out risks/rollout/migrations when relevant. Do not ask follow-up questions.
---

# Git PR Writing
## Overview

Generate a professional PR title and a review-ready PR description from the current branch changes compared to the base branch, then publish it via `gh` by default. Optimize for reviewer speed: clear intent, concrete change list, how to test, and risk/rollout notes.

## Default behavior (no questions)

- Always compare **current HEAD** to the **merge-base** with the repo default branch (usually `main`).
- Always include a **How to Test** section.
- Always include a **Risk / Rollout / Backout** section (use “N/A” or “Low risk” when appropriate).
- If tests are unknown, write exactly: `Not run (not requested)`.
- If the repo has a PR template, follow it (fill it, don’t fight it).
- Include references (tickets/IDs) **only if the user already provided them** in the conversation.
- Always create or update the GitHub PR via `gh` after drafting title/body, unless the user explicitly asks for draft text only.

## Workflow

### 1) Collect context (always)

Run:

- `git status -sb`
- Optional: `scripts/collect_pr_context.sh --show-template` (preferred for consistent snapshots)
- Determine base branch (prefer repo default branch):
  - `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'` (preferred)
  - Fallback: `git remote show origin | sed -n '/HEAD branch/s/.*: //p'`
  - Fallback: assume `main`
- Fetch base:
  - `git fetch origin <base_branch>`
- Compute merge base:
  - `BASE_REF=origin/<base_branch>`
  - `MB=$(git merge-base HEAD "$BASE_REF")`
- Range summary:
  - `git log --oneline --decorate --no-merges "$MB..HEAD"`
  - `git diff --name-status "$MB..HEAD"`
  - `git diff "$MB..HEAD"`
  - Optional: `git diff --stat "$MB..HEAD"`

If available, also detect a PR template:

- Check common locations:
  - `.github/pull_request_template.md`
  - `.github/PULL_REQUEST_TEMPLATE.md`
  - `.github/PULL_REQUEST_TEMPLATE/*.md`
- If found, use it as the output skeleton.

### 2) Synthesize intent and reviewer-relevant impact

- Identify the primary goal: feature / fix / refactor / perf / docs / chores.
- Call out user-visible behavior changes, API changes, config/migrations, and operational impact.
- If multiple areas changed, keep the title scoped to the dominant area; describe the rest in the body.

### 3) Write the PR title

Preferred format (consistent with your commit skill):

- Conventional Commits style: `<type>(<scope>): <imperative summary>`
- Imperative, present tense; 50–72 chars preferred; no trailing period.
- Types: `feat, fix, refactor, perf, test, docs, chore, ci, build, revert`
- Scope: short area name (`api, auth, db, frontend, infra, deps, workers, billing, etc.`)

If scope is unclear or cross-cutting, use a broad scope like `core` or omit scope:
- `<type>: <imperative summary>`

### 4) Write the PR description (default template)

If no repo PR template exists, use this structure:

- `## Summary` (2–5 bullets)
- `## Context / Why` (short)
- `## Changes` (bulleted, concrete)
- `## How to Test` (step-by-step + commands for any newly added tests. Otherwise N/A)
- `## Rollout / Backout` (flags, migration order, revert notes)
- `## Risks / Notes` (compat, perf, monitoring, edge cases)
- `## Checklist` (tests/docs/logging)

Rules:
- Keep bullets specific (what changed, where, why).
- Mention migrations, flags, env vars, and backward compatibility explicitly when relevant.
- If there’s no user-visible change, say so clearly.

### 5) Create or update a GitHub PR (default)

Do this by default after generating title/body. Skip only when the user explicitly asks for text-only output.

Steps (best-effort; if any step fails, fall back to outputting text only):

1. Ensure branch is pushed:
   - `BR=$(git rev-parse --abbrev-ref HEAD)`
   - `git push -u origin "$BR"`
2. If a PR exists for the branch:
   - `gh pr view --json number,url,title,body` (or `gh pr view` if JSON unsupported)
   - Update:
     - `gh pr edit --title "<title>" --body "<body>"`
3. If no PR exists:
   - Create:
     - `gh pr create --base "<base_branch>" --head "$BR" --title "<title>" --body "<body>"`

Never guess labels/reviewers unless the user already specified them.

## Output format

Always return:

PR title:
<one line>

PR description:
<markdown body>

Context used:
- Base: <base_branch> (origin/<base_branch>)
- Merge-base: <sha>
- Commit range: <MB..HEAD>

Always include:
- PR URL (if available)
- Commands executed (verbatim)

## Quality checklist (must satisfy)

- Title matches the dominant change and uses imperative voice
- Description explains **why**, **what**, and **reviewer-relevant impact**
- “How to Test” is runnable and explicit
- Risks / rollout / backout are addressed (or clearly N/A)
- Mentions migrations/config/flags if applicable
- References included only when already provided

## References

- Scenario templates: `references/pr-templates.md`
