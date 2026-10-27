# myskills

These are the agent skills I use every day, cleaned up so anyone can use them.

A skill is a folder with a `SKILL.md` file that teaches a coding agent how to do one job well. The agent reads the short description up front and only loads the full instructions when your request matches. Skills follow the open [Agent Skills](https://agentskills.io) format, so the same folder works in Claude Code, Codex, and other agents that support it.

## Skills

### Engineering

| Skill | Say something like | What it does |
| --- | --- | --- |
| [git-commit-writing](skills/engineering/git-commit-writing) | "commit my changes" | Reads your staged and unstaged changes, writes a Conventional Commits message with a short Why / What changed / Impact / Tests body, then stages everything and commits. |
| [git-pr-writing](skills/engineering/git-pr-writing) | "open a PR for this branch" | Compares your branch to the default branch, writes the PR title and description (including how to test it and any risks), then pushes and creates or updates the PR with `gh`. |

### Evals

| Skill | Say something like | What it does |
| --- | --- | --- |
| [cascaded-eval-design](skills/evals/cascaded-eval-design) | "help me design an eval where early decisions change the later steps" | Helps you design, audit, or harden AI evals built from linked expert decisions, where one wrong call early on should change what the rest of a correct answer looks like. Includes templates and a small script that checks your decision graph. |

## Heads up before you use the git skills

Both git skills are built to act, not just suggest. They don't stop to ask questions.

- `git-commit-writing` runs `git add -A`, so anything in your working tree goes into the commit.
- `git-pr-writing` pushes your branch and opens or edits the PR on GitHub.

If you only want the text, say so ("just draft the commit message, don't commit").

## Install

The easiest way is the [skills CLI](https://github.com/vercel-labs/skills), which asks which skills and which agents you want:

```bash
npx skills add trevor-nichols/myskills
```

Or copy them in by hand:

```bash
git clone https://github.com/trevor-nichols/myskills

# Claude Code
mkdir -p ~/.claude/skills
cp -R myskills/skills/*/* ~/.claude/skills/

# Codex and other agents that read the shared skills folder
mkdir -p ~/.agents/skills
cp -R myskills/skills/*/* ~/.agents/skills/
```

The `*/*` matters. Skills are grouped by category in this repo, but agents expect each skill folder to sit directly inside the skills folder.

## Using a skill

You usually don't have to do anything special. Ask for what you want in plain words and the agent picks the matching skill. You can also call one by name, like `/git-commit-writing` in Claude Code or `$git-commit-writing` in Codex.

## Requirements

- `git` for both git skills.
- The [GitHub CLI](https://cli.github.com) (`gh`), logged in with `gh auth login`, for `git-pr-writing`.
- Python 3 if you want to run the blueprint checker in `cascaded-eval-design`. It only uses the standard library.

## License

[MIT](LICENSE)
