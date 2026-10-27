---
name: skill-docs-writer
description: Create, improve, and maintain human-facing documentation for AI agent skills. Use when a SKILL.md is added, changed, renamed, moved, or retired; when publishing a skills collection; or when someone asks for a clear explanation of a skill and when to use it. Write documentation pages grounded in the actual skill, not copies of its internal instructions.
metadata:
  author: trevor-nichols
  version: "1.0.0"
---

# Skill Docs Writer

Turn an agent skill into a documentation page that helps a person decide **whether, when, and how to use it**. Keep those pages accurate as the skills evolve.

A documentation page is a guide for the person selecting a skill. `SKILL.md` is the operating guidance for the agent executing it. Preserve that separation.

## When to use this skill

Use this workflow to:

- Document a new agent skill for teammates or the public.
- Refresh an existing page after a change in what the skill does, expects, or produces.
- Reorganize documentation when a skill changes name or location.
- Deprecate documentation for a retired skill without stranding existing readers.
- Audit a skills directory for missing, confusing, or stale documentation.

Do **not** treat this as a general README generator, a skill implementation generator, or a request to rewrite the skill's own instructions. If asked for those deliverables, clarify the distinction briefly and produce them only when explicitly in scope.

## Establish the repository's rules

Before writing, locate the target `SKILL.md` and identify the repo's existing structure. Read, when relevant:

1. The skill's YAML frontmatter and main instructions.
2. Referenced files, examples, scripts, and templates needed to understand real behavior.
3. Existing documentation for this or related skills.
4. Repository contribution guidance, docs-site settings, navigation files, and changelog entries.
5. Issues or user questions, if accessible, that reveal where readers get confused.

Prefer the project's explicit choices over the defaults here. Determine:

- **Documentation destination:** Use the established docs tree. If none exists, default to `docs/skills/<skill-name>.md`.
- **Coverage:** Document skills the user or repository marks as publishable. Do not assume drafts, experiments, or retired skills should be promoted.
- **Link style:** Match the actual publishing environment. For a hosted website, use stable published URLs when known. For repository-only documentation, relative links are acceptable. Never invent a public URL.
- **Install instructions:** Respect the site's installation workflow. Avoid repeating commands already displayed by a generated installation component. Otherwise provide installation steps only when verified and useful.

If the user requests a single page, don't expand the task into a repository-wide documentation rewrite.

## Extract the reader-facing story

Work from evidence rather than an appealing summary. Identify:

- **Job:** What meaningful problem does the skill solve?
- **Decision point:** In what situation would a person choose it over not using a skill?
- **Invocation:** Is it manually invoked, automatically selected, or both? State only what the skill and target agent environment actually support.
- **Distinctive method:** What is the one approach, constraint, or trade-off that makes it recognizable?
- **Requirements:** Which tools, files, permissions, integrations, or preceding steps are genuinely required?
- **Results:** What artifacts, modifications, or decisions does it produce?
- **Limits:** What is explicitly outside its scope, and which neighboring skill handles that work?
- **Success signals:** What can a user observe to verify the intended result?

Keep the actual instructions as the source of truth. If the skill description and implementation disagree, flag the discrepancy instead of smoothing it over in the documentation.

## Create or revise the page

Use [the page blueprint](assets/documentation-page.md) as a starting point, not a mandatory fill-in form. Match the terminology and tone of the repository. The essential reading path is:

1. **Understand it:** Lead with its job in ordinary language and the trait that distinguishes it.
2. **Recognize the right moment:** Give specific situations where a person should use it, plus an important situation where they should not.
3. **Know what to expect:** State prerequisites only when real, explain the approach without reproducing the complete agent runbook, and name tangible outputs.
4. **Resolve uncertainty:** Answer actual recurring questions when you have evidence. Don't fabricate FAQs just to fill space.
5. **Check the outcome:** Give observable examples of successful behavior, not internal file-equality tests.
6. **See related options:** Link to closely related skills or an existing skills index when those links are real and useful.

Aim for a page that a reader can scan in a minute, with added detail only where it answers a real decision or objection. Prefer short paragraphs, concrete examples, and tables for genuine choices. Do not paste large sections from `SKILL.md`; summarize in original wording.

For a standalone skill with no surrounding catalog, omit catalog/navigation material rather than inventing it. For complex skills, add a small number of custom sections using their actual domain language.

## Keep documentation in sync

Apply the action that matches the change:

| Change | Documentation action |
| --- | --- |
| New publishable skill | Create its page in the established docs location; update the index if one exists. |
| Skill behavior or requirements change | Revise affected explanations, examples, prerequisites, and outcome checks. |
| Skill renamed or moved | Update the page path if the repo's mapping requires it; repair internal links and navigation. Keep redirects when the publishing system supports them. |
| Skill becomes publishable | Add its page if missing. |
| Skill is no longer promoted | Follow the repository's visibility policy; avoid deleting an established public URL without considering readers. |
| Published skill retired | Prefer a short retirement notice with known replacement or last-supported version, while preserving the old route when feasible. |
| Skill removed before publication | Remove stale unpublished documentation if the repository's policy calls for it. |

Do not claim a redirect exists unless it is actually configured. If a stable public URL cannot be retained, report that separately.

## Editorial rules

- Write for people choosing a tool, not for the model running the tool.
- Lead with a concrete capability, not marketing language.
- Separate verified current behavior from planned or optional capabilities.
- Describe invocation behavior accurately; don't assume every agent host treats skill activation the same way.
- Avoid author biography, editorial attribution, sales copy, and unnecessary architecture detail.
- Reuse established project vocabulary; introduce unfamiliar terms only when they help.
- Keep links intentional and valid in the final publishing context.
- Don't include private paths, keys, unpublished endpoints, or unverified claims.
- Preserve intentional human edits while updating facts; don't overwrite unrelated sections wholesale.

## Completion checks

Consult [the review checklist](references/review-checklist.md), then verify the relevant items:

- The file lives at the expected path and matches repository conventions.
- A new reader can explain the skill's purpose, when to use it, and what it produces without opening `SKILL.md`.
- The documented invocation, prerequisites, limits, and examples agree with the current implementation.
- Optional sections are omitted when there is no substantive information to put in them.
- Every included link uses the appropriate URL form, and available link checks pass.
- Renames, retirements, and navigation changes are accounted for.
- No generated site functionality (such as installation widgets) is duplicated by hand.

Finally, report which files were created, edited, moved, or left untouched, and identify anything that needs a maintainer's decision. Do not claim to have published the docs unless deployment actually occurred.

## Sample requests

- "We added `skills/engineering/debug-api/SKILL.md`. Write the docs page in our existing style."
- "This skill is now manually invoked only. Update its documentation and examples."
- "Rename `audit-workflow` to `review-workflow`, keeping existing documentation links usable where possible."
- "Check which published skills have docs that no longer match their SKILL.md files."
