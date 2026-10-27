#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Collect git context for commit message drafting.

Usage:
  collect_git_context.sh [--staged|--unstaged|--all] [--full]

Options:
  --staged     Use staged (index) changes only
  --unstaged   Use unstaged working tree changes only
  --all        Include both staged and unstaged (default)
  --full       Include full diffs (may be large)
  -h, --help   Show this help
USAGE
}

mode="all"
full=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --staged)
      mode="staged"
      ;;
    --unstaged)
      mode="unstaged"
      ;;
    --all)
      mode="all"
      ;;
    --full)
      full=1
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

git_cmd=(git -c color.ui=never)
root=$("${git_cmd[@]}" rev-parse --show-toplevel)
branch=$("${git_cmd[@]}" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "detached")

echo "repo: ${root}"
echo "branch: ${branch}"
echo

echo "status:"
"${git_cmd[@]}" status -sb
echo

section() {
  echo "== $1 =="
}

if [[ "$mode" == "staged" || "$mode" == "all" ]]; then
  section "staged diffstat"
  "${git_cmd[@]}" diff --cached --stat || true
  echo

  section "staged name-status"
  "${git_cmd[@]}" diff --cached --name-status || true
  echo

  if [[ "$full" -eq 1 ]]; then
    section "staged diff"
    "${git_cmd[@]}" diff --cached || true
    echo
  fi
fi

if [[ "$mode" == "unstaged" || "$mode" == "all" ]]; then
  section "unstaged diffstat"
  "${git_cmd[@]}" diff --stat || true
  echo

  section "unstaged name-status"
  "${git_cmd[@]}" diff --name-status || true
  echo

  if [[ "$full" -eq 1 ]]; then
    section "unstaged diff"
    "${git_cmd[@]}" diff || true
    echo
  fi
fi

section "recent commit"
"${git_cmd[@]}" log -1 --oneline
