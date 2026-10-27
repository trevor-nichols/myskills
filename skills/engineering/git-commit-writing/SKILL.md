---
name: git-commit-writing
description: Draft professional git commit summaries and descriptions and perform the commit. Use when asked to write, improve, or standardize commit messages, or to commit worktree changes. Always analyze both staged and unstaged diffs, stage all changes, and commit without asking follow-up questions. Uses a Conventional Commits summary and a structured body (Why / What changed / Impact / Tests / Notes / Refs) for non-trivial changes, with a minimal format only for tiny edits.
metadata:
  version: "1.0.0"
---

# Git Commit Writing

## Overview

Generate a professional commit summary and description from the current work tree, then commit the changes. Always include both staged and unstaged changes and do not ask questions.

## Default behavior (no questions)

- Always inspect both staged and unstaged diffs.
- Always stage all changes before committing.
- Always include a Tests line. If unknown, write: `Tests: Not run (not requested)`.
- Include Refs only if the user provided them earlier in the conversation.
- Do not ask for commit style; use the professional format below.

## Workflow

1. Collect context (always both staged + unstaged)
   - `git status -sb`
   - `git diff --cached`
   - `git diff`
   - Optional: `scripts/collect_git_context.sh --all`

2. Synthesize intent and impact
   - Identify the primary change and why it exists.
   - Call out behavior changes, risk, compatibility, and migrations when present.

3. Choose format
   - Use structured body for non-trivial changes.
   - Use minimal format only for tiny edits (single-file docs/formatting or very small diff).

4. Write the summary (subject line)
   - Conventional Commits: `<type>(<scope>): <imperative summary>`
   - Imperative, present tense; 50–72 characters preferred; no trailing period.
   - Type set: feat, fix, refactor, perf, test, docs, chore, ci, build, revert.
   - Scope is a short area name (api, auth, db, frontend, infra, deps, etc.).

5. Write the description (body, structured format)
   - Use section headers exactly:
     - `Why`
     - `What changed`
     - `Impact`
     - `Tests`
     - `Notes`
     - `Refs` (only if already provided)
   - Each section uses short bullets.
   - `Impact` must state user-visible change or "No user-visible change".
   - `Tests` must be explicit; default to `Not run (not requested)`.
   - `Notes` must be present; if nothing applies, write `- None`.

6. Commit
   - Stage all: `git add -A`
   - Commit: `git commit -m "<summary>" -m "<description>"`

7. If nothing changed
   - State that there are no changes to commit and stop.

## Output format

Return both pieces, ready to paste, and confirm the commit command used:

Commit summary:
<one line>

Commit description:
<structured body with Why/What changed/Impact/Tests/Notes and optional Refs>

Commit command:
`git commit -m "<summary>" -m "<description>"`

## Quick quality checklist

- Accurate to the diff
- Clear intent and user impact
- Rationale included
- Risk or compatibility notes when relevant
- Testing status explicit
- References included only when available

## References

- Scenario templates: `references/commit-templates.md`
