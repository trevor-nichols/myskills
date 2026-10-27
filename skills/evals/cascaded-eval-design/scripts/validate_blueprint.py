#!/usr/bin/env python3
"""Structural validator for a cascaded-eval decision blueprint.

Accepts a JSON blueprint as illustrated by assets/blueprint.example.json.
Checks declarations and graph metrics, NOT whether a claimed expert decision
or causal edge is substantively valid. Domain experts must verify those.
No third-party dependencies required.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.@-]*$")
ALLOWED_EDGE_TYPES = {"substantive", "calculation", "presentation"}
ALLOWED_ABLATION_STATES = {"planned", "executed"}


def analyze(bp: Any, profile: str = "auto", require_verified: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    holds: list[str] = []

    if not isinstance(bp, dict):
        return {"errors": ["Top-level blueprint must be a JSON object"], "warnings": [], "profile_holds": [], "metrics": {}}

    if not isinstance(bp.get("title"), str) or not bp["title"].strip():
        errors.append("Missing non-empty title")
    dps = bp.get("decisions")
    if not isinstance(dps, list) or not dps:
        errors.append("decisions must be a non-empty list")
        dps = []
    declared: dict[str, dict[str, Any]] = {}
    for i, dp in enumerate(dps):
        if not isinstance(dp, dict):
            errors.append(f"decisions[{i}] must be an object")
            continue
        dp_id = dp.get("id")
        if not isinstance(dp_id, str) or not ID_RE.fullmatch(dp_id):
            errors.append(f"decisions[{i}].id must be a stable identifier")
            continue
        if dp_id in declared:
            errors.append(f"Duplicate decision ID {dp_id}")
            continue
        declared[dp_id] = dp
        if not isinstance(dp.get("qualified"), bool):
            errors.append(f"{dp_id}: qualified must be explicitly true or false")
        if not isinstance(dp.get("question"), str) or not dp["question"].strip():
            warnings.append(f"{dp_id}: missing meaningful expert decision question")
        paths = dp.get("candidate_paths")
        if not isinstance(paths, list) or len(paths) < 2 or any(not isinstance(p, str) or not p.strip() for p in paths):
            warnings.append(f"{dp_id}: fewer than two stated plausible candidate paths")
        if not isinstance(dp.get("decisive_evidence"), str) or not dp["decisive_evidence"].strip():
            warnings.append(f"{dp_id}: no documented decisive solver-visible evidence")
        if not isinstance(dp.get("intended_state"), str) or not dp["intended_state"].strip():
            warnings.append(f"{dp_id}: no intended resulting state documented")

    qualified_ids = {dp_id for dp_id, dp in declared.items() if dp.get("qualified") is True}
    edges = bp.get("edges", [])
    if not isinstance(edges, list):
        errors.append("edges must be a list")
        edges = []
    all_adj: dict[str, set[str]] = defaultdict(set)
    in_degree = {dp_id: 0 for dp_id in declared}
    substantive_edges: set[tuple[str, str]] = set()
    seen_edges: set[tuple[str, str, str]] = set()

    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}] must be an object")
            continue
        src, dst, kind = edge.get("from"), edge.get("to"), edge.get("kind")
        if not isinstance(src, str) or not isinstance(dst, str):
            errors.append(f"edges[{i}] from/to must be decision ID strings")
            continue
        if src not in declared or dst not in declared:
            errors.append(f"edges[{i}] uses unknown decision IDs: {src} -> {dst}")
            continue
        if src == dst:
            errors.append(f"Self-loop not allowed: {src} -> {dst}; use versioned states")
            continue
        if not isinstance(kind, str) or kind not in ALLOWED_EDGE_TYPES:
            errors.append(f"{src} -> {dst}: invalid edge kind {kind!r}")
            continue
        triple = (src, dst, kind)
        if triple in seen_edges:
            warnings.append(f"Duplicate declared edge: {src} -> {dst} ({kind})")
            continue
        seen_edges.add(triple)
        if dst not in all_adj[src]:
            all_adj[src].add(dst)
            in_degree[dst] += 1
        if kind == "substantive":
            substantive_edges.add((src, dst))
            if not isinstance(edge.get("reason"), str) or len(edge["reason"].strip()) < 12:
                errors.append(f"{src} -> {dst}: substantive edge requires a specific causal explanation")
            if src not in qualified_ids or dst not in qualified_ids:
                errors.append(f"{src} -> {dst}: substantive decision edges require qualified endpoints")

    queue = deque(sorted(n for n, deg in in_degree.items() if deg == 0))
    topo: list[str] = []
    while queue:
        v = queue.popleft()
        topo.append(v)
        for nxt in sorted(all_adj[v]):
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)
    if len(topo) != len(declared):
        errors.append("Decision graph contains a cycle: represent reassessments as versioned states")

    distances = {node: 0 for node in qualified_ids}
    if len(topo) == len(declared):
        for src in topo:
            for dst in all_adj[src]:
                if (src, dst) in substantive_edges and src in qualified_ids and dst in qualified_ids:
                    distances[dst] = max(distances[dst], distances[src] + 1)
    dependent = {dst for src, dst in substantive_edges if src in qualified_ids and dst in qualified_ids}
    count = len(qualified_ids)
    density = len(dependent) / count if count else 0.0
    max_path = max(distances.values(), default=0)

    ablations = bp.get("ablations", [])
    if not isinstance(ablations, list):
        errors.append("ablations must be a list")
        ablations = []
    a_ids: set[str] = set()
    executed = 0
    for i, ablation in enumerate(ablations):
        if not isinstance(ablation, dict):
            errors.append(f"ablations[{i}] must be an object")
            continue
        aid = ablation.get("id")
        if not isinstance(aid, str) or not aid.strip():
            errors.append(f"ablations[{i}] missing id")
        elif aid in a_ids:
            errors.append(f"Duplicate ablation ID {aid}")
        else:
            a_ids.add(aid)
        first = ablation.get("first_wrong_dp")
        if not isinstance(first, str) or first not in qualified_ids:
            errors.append(f"Ablation {aid}: first_wrong_dp {first!r} is not a qualified DP")
        state = ablation.get("status")
        if not isinstance(state, str) or state not in ALLOWED_ABLATION_STATES:
            errors.append(f"Ablation {aid}: status must be planned or executed")
        if state == "executed":
            executed += 1
            if not ablation.get("terminal_difference"):
                warnings.append(f"Ablation {aid}: executed but no terminal difference described")

    selected_profile = bp.get("profile", "expert") if profile == "auto" else profile
    if not isinstance(selected_profile, str) or selected_profile not in ("foundational", "expert", "flagship", "custom"):
        errors.append(f"Unknown profile {selected_profile!r}")
    elif selected_profile == "expert":
        if count < 3:
            holds.append("Expert structural target: at least 3 qualified DPs")
        if max_path < 2:
            holds.append("Expert structural target: at least 2 substantive decision edges on a path")
    elif selected_profile == "flagship":
        if count < 6:
            holds.append("Flagship structural target: at least 6 qualified DPs")
        if len(dependent) < 4:
            holds.append("Flagship structural target: at least 4 dependent DPs")
        if density < 0.60:
            holds.append("Flagship structural target: at least 60% dependent DPs")
        if max_path < 4:
            holds.append("Flagship structural target: at least 4 substantive decision edges on a path")
        if len(ablations) < 3:
            holds.append("Flagship ablation planning target: at least 3 distinct wrong paths")

    verification = bp.get("verification", {})
    if require_verified:
        if not isinstance(verification, dict):
            errors.append("verification must be an object when --require-verified is used")
            verification = {}
        for field in ("source_verified", "gold_verified", "empirically_validated"):
            if verification.get(field) is not True:
                holds.append(f"Release evidence missing: verification.{field} is not true")
        if not ablations or executed != len(ablations):
            holds.append("Release evidence missing: every declared ablation must be executed")

    if count and not substantive_edges:
        warnings.append("No declared substantive DP edges: graph may only measure parallel or mechanical work")
    warnings.append("Structural checks cannot verify expert validity, source recoverability, or actual ablation results")
    metrics = {
        "declared_decisions": len(declared),
        "qualified_decisions": count,
        "substantive_edges": len(substantive_edges),
        "dependent_decisions": len(dependent),
        "dependency_density": round(density, 4),
        "longest_causal_path_edges": max_path,
        "longest_causal_path_decisions": max_path + 1 if count else 0,
        "planned_or_executed_ablations": len(ablations),
        "executed_ablations": executed,
        "profile": selected_profile,
    }
    return {"errors": errors, "warnings": warnings, "profile_holds": holds, "metrics": metrics}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", type=Path, help="JSON blueprint to check")
    parser.add_argument("--profile", choices=("auto", "foundational", "expert", "flagship", "custom"), default="auto")
    parser.add_argument("--require-verified", action="store_true", help="Also require release verification flags and executed ablations")
    parser.add_argument("--json", action="store_true", help="Print machine-readable report")
    args = parser.parse_args(argv)
    try:
        bp = json.loads(args.blueprint.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read blueprint JSON: {exc}", file=sys.stderr)
        return 2
    report = analyze(bp, args.profile, args.require_verified)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print("Cascaded Eval — Structural Blueprint Check")
        for name, value in report["metrics"].items():
            print(f"  {name}: {value}")
        for label, field in (("ERROR", "errors"), ("HOLD", "profile_holds"), ("NOTE", "warnings")):
            for message in report[field]:
                print(f"  {label}: {message}")
        print("  Verdict: " + ("INVALID" if report["errors"] else "HOLD" if report["profile_holds"] else "STRUCTURALLY CONSISTENT (not substantively certified)"))
    return 2 if report["errors"] else 1 if report["profile_holds"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
