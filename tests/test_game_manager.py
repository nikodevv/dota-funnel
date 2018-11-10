import unittest
import os
from GameManager import GameManager

class TestGameManager(unittest.TestCase):
	def setUp(self):
		self.gmanager = GameManager()
		# overwriting data DIR for GameManager settings
		self.gmanager.dataset_matchlist_DIR = os.path.abspath("tests/test_data/")

	def test_can_find_files_blonging_to_dataset(self):
		self.gmanager.keyword = "test_keyword"
		self.gmanager.find_files()
		self.assertEqual(len(self.gmanager.dataset_matchlist_files), 2)
		for DIR in self.gmanager.dataset_matchlist_files:
			self.assertIn(self.gmanager.keyword, str(DIR))

	def test_can_open_extract_matchlist_from_file(self):
		TEST_FILENAME = "[test_keyword]-[1541609180.436662].json"
		self.gmanager.set_matchlist(TEST_FILENAME)
		match_ids = self.gmanager.matchlist
		self.assertEqual(len(match_ids), 100)
		self.assertEqual(match_ids[0], 4208474207)
		self.assertEqual(match_ids[-1], 4208443917)