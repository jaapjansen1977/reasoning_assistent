import copy
import json
from pathlib import Path
import unittest

from scripts.knowledge_tools import render, validate

ROOT = Path(__file__).resolve().parents[1]


class KnowledgeIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = json.loads((ROOT / 'reasoning_assistent/knowledge/regions/low_back.v1.json').read_text(encoding='utf-8'))

    def test_region_has_no_dangling_references_or_missing_core_fields(self):
        self.assertEqual(validate(self.module), [])

    def test_unresolved_question_is_rejected(self):
        module = copy.deepcopy(self.module)
        module['conditions'][0]['question_ids'].append('missing_question')
        self.assertTrue(any('unresolved reference' in e for e in validate(module)))

    def test_duplicate_source_id_is_rejected(self):
        module = copy.deepcopy(self.module)
        module['sources'].append(copy.deepcopy(module['sources'][0]))
        self.assertTrue(any('duplicate id' in e for e in validate(module)))

    def test_draft_cannot_enable_automatic_advice(self):
        module = copy.deepcopy(self.module)
        module['activation']['automatic_advice_enabled'] = True
        self.assertTrue(any('automatic_advice_enabled' in e for e in validate(module)))

    def test_readable_review_document_matches_source(self):
        path = ROOT / 'docs/knowledge/low_back.v1.md'
        self.assertEqual(path.read_text(encoding='utf-8'), render(self.module))

    def test_available_index_entries_exist_and_match_status(self):
        folder = ROOT / 'reasoning_assistent/knowledge/regions'
        index = json.loads((folder / 'index.json').read_text(encoding='utf-8'))
        for region in index['regions']:
            if region['status'] != 'planned':
                module = json.loads((folder / region['path'].removeprefix('regions/')).read_text(encoding='utf-8'))
                self.assertEqual(module['id'], region['id'])
                self.assertEqual(module['status'], region['status'])


if __name__ == '__main__':
    unittest.main()
