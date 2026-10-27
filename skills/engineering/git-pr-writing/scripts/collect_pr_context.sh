#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Collect git context for PR title/description drafting.

Usage:
  collect_pr_context.sh [--base <branch>] [--remote <name>] [--no-fetch] [--full] [--show-template]

Options:
  --base <branch>     Base branch to compare against (default: repo default branch)
  --remote <name>     Remote to use for base branch lookup/fetch (default: origin if present)
  --no-fetch          Skip fetching the base branch from the remote
  --full              Include full diff (may be large)
  --show-template     Print PR template contents if found
  -h, --help          Show this help
USAGE
}

base_branch=""
remote_name=""
full=0
no_fetch=0
show_template=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --base)
      base_branch=${2:-}
      if [[ -z "$base_branch" ]]; then
        echo "Error: --base requires a branch name." >&2
        exit 1
      fi
      shift
      ;;
    --remote)
      remote_name=${2:-}
      if [[ -z "$remote_name" ]]; then
        echo "Error: --remote requires a remote name." >&2
        exit 1
      fi
      shift
      ;;
    --no-fetch)
      no_fetch=1
      ;;
    --full)
      full=1
      ;;
    --show-template)
      show_template=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
  shift
 done

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: not inside a git repository." >&2
  exit 1
fi

root=$(git -c color.ui=never rev-parse --show-toplevel)

git_cmd=(git -C "$root" -c color.ui=never)
branch=$("${git_cmd[@]}" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "detached")

if [[ -z "$remote_name" ]]; then
  if "${git_cmd[@]}" remote get-url origin >/dev/null 2>&1; then
    remote_name="origin"
  fi
fi

default_branch_from_remote() {
  local ref=""
  if [[ -n "$remote_name" ]]; then
    if ref=$("${git_cmd[@]}" symbolic-ref -q "refs/remotes/${remote_name}/HEAD" 2>/dev/null); then
      echo "${ref#refs/remotes/${remote_name}/}"
      return 0
    fi
    ref=$("${git_cmd[@]}" remote show "$remote_name" 2>/dev/null | sed -n '/HEAD branch/s/.*: //p' | head -n1 || true)
    if [[ -n "$ref" ]]; then
      echo "$ref"
      return 0
    fi
  fi
  return 1
}

fallback_branch() {
  local candidate
  for candidate in main master trunk develop; do
    if "${git_cmd[@]}" show-ref --verify --quiet "refs/heads/${candidate}"; then
      echo "$candidate"
      return 0
    fi
    if [[ -n "$remote_name" ]] && "${git_cmd[@]}" show-ref --verify --quiet "refs/remotes/${remote_name}/${candidate}"; then
      echo "$candidate"
      return 0
    fi
  done
  return 1
}

if [[ -z "$base_branch" ]]; then
  base_branch=$(default_branch_from_remote || true)
fi
if [[ -z "$base_branch" ]]; then
  base_branch=$(fallback_branch || true)
fi
if [[ -z "$base_branch" ]]; then
  echo "Error: could not determine a base branch. Use --base <branch>." >&2
  exit 1
fi

if [[ -n "$remote_name" && "$no_fetch" -eq 0 ]]; then
  "${git_cmd[@]}" fetch "$remote_name" "$base_branch" >/dev/null 2>&1 || true
fi

base_ref=""
if [[ -n "$remote_name" ]] && "${git_cmd[@]}" show-ref --verify --quiet "refs/remotes/${remote_name}/${base_branch}"; then
  base_ref="${remote_name}/${base_branch}"
elif "${git_cmd[@]}" show-ref --verify --quiet "refs/heads/${base_branch}"; then
  base_ref="$base_branch"
fi

if [[ -z "$base_ref" ]]; then
  echo "Error: base ref not found for branch '${base_branch}'." >&2
  exit 1
fi

merge_base=$("${git_cmd[@]}" merge-base HEAD "$base_ref" 2>/dev/null || true)
if [[ -z "$merge_base" ]]; then
  echo "Error: could not compute merge-base for HEAD and ${base_ref}." >&2
  exit 1
fi

range="${merge_base}..HEAD"

echo "repo: ${root}"
echo "branch: ${branch}"
echo "base branch: ${base_branch}"
echo "base ref: ${base_ref}"
echo "merge-base: ${merge_base}"
echo "range: ${range}"
echo

echo "status:"
"${git_cmd[@]}" status -sb
echo

section() {
  echo "== $1 =="
}

section "commit range (no merges)"
"${git_cmd[@]}" log --oneline --decorate --no-merges "$range" || true
echo

section "diff stat"
"${git_cmd[@]}" diff --stat "$range" || true
echo

section "diff name-status"
"${git_cmd[@]}" diff --name-status "$range" || true
echo

if [[ "$full" -eq 1 ]]; then
  section "diff"
  "${git_cmd[@]}" diff "$range" || true
  echo
fi

section "pr template(s)"
(
  cd "$root"
  templates=()
  if [[ -f .github/pull_request_template.md ]]; then
    templates+=(.github/pull_request_template.md)
  fi
  if [[ -f .github/PULL_REQUEST_TEMPLATE.md ]]; then
    templates+=(.github/PULL_REQUEST_TEMPLATE.md)
  fi
  if compgen -G ".github/PULL_REQUEST_TEMPLATE/*.md" > /dev/null; then
    for path in .github/PULL_REQUEST_TEMPLATE/*.md; do
      templates+=("$path")
    done
  fi

  if [[ ${#templates[@]} -eq 0 ]]; then
    echo "none found"
    exit 0
  fi

  printf '%s\n' "${templates[@]}"

  if [[ "$show_template" -eq 1 ]]; then
    echo
    for path in "${templates[@]}"; do
      echo "== pr template: ${path} =="
      cat "$path"
      echo
    done
  fi
)
