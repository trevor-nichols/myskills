#!/usr/bin/env python3
"""Tests for the dependency-graph structural checker."""

import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_blueprint import analyze  # noqa: E402


class StructuralValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = json.loads((Path(__file__).parent.parent / 'assets' / 'blueprint.example.json').read_text(encoding='utf-8'))

    def test_sample_matches_expert_structure(self):
        result = analyze(self.sample)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['profile_holds'], [])
        self.assertEqual(result['metrics']['qualified_decisions'], 5)
        self.assertEqual(result['metrics']['substantive_edges'], 4)
        self.assertEqual(result['metrics']['dependent_decisions'], 4)
        self.assertEqual(result['metrics']['longest_causal_path_edges'], 4)
        self.assertEqual(result['metrics']['dependency_density'], 0.8)

    def test_flagship_marks_short_graph_on_hold(self):
        result = analyze(self.sample, profile='flagship')
        self.assertTrue(any('6 qualified' in v for v in result['profile_holds']))
        self.assertFalse(result['errors'])

    def test_release_requires_verified_evidence(self):
        result = analyze(self.sample, require_verified=True)
        self.assertTrue(any('verification.gold_verified' in v for v in result['profile_holds']))
        self.assertTrue(any('every declared ablation' in v for v in result['profile_holds']))

    def test_cycle_is_rejected(self):
        doc = copy.deepcopy(self.sample)
        doc['edges'].append({'from':'DP5', 'to':'DP1', 'kind':'substantive', 'reason':'Introduces a prohibited cycle'})
        result = analyze(doc)
        self.assertTrue(any('cycle' in e for e in result['errors']))

    def test_arithmetic_edge_is_not_causal_depth(self):
        doc = copy.deepcopy(self.sample)
        for edge in doc['edges']:
            edge['kind'] = 'calculation'
        result = analyze(doc)
        self.assertEqual(result['metrics']['longest_causal_path_edges'], 0)
        self.assertEqual(result['metrics']['dependent_decisions'], 0)
        self.assertTrue(result['profile_holds'])

    def test_unqualified_endpoint_does_not_count(self):
        doc = copy.deepcopy(self.sample)
        doc['decisions'][2]['qualified'] = False
        result = analyze(doc)
        self.assertTrue(any('qualified endpoints' in e for e in result['errors']))
        self.assertEqual(result['metrics']['qualified_decisions'], 4)

    def test_duplicate_decision_id_is_invalid(self):
        doc = copy.deepcopy(self.sample)
        doc['decisions'].append(copy.deepcopy(doc['decisions'][0]))
        result = analyze(doc)
        self.assertTrue(any('Duplicate decision' in e for e in result['errors']))

    def test_invalid_blueprint_shape(self):
        result = analyze([])
        self.assertTrue(result['errors'])

    def test_missing_decisive_evidence_warning(self):
        doc = copy.deepcopy(self.sample)
        doc['decisions'][0]['decisive_evidence'] = ''
        result = analyze(doc)
        self.assertTrue(any('solver-visible evidence' in w for w in result['warnings']))


if __name__ == '__main__':
    unittest.main()
