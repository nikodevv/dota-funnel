import unittest
import os
from GameManager import GameManager

class TestGameManager(unittest.TestCase):
	def setUp(self):
		self.gmanager = GameManager()

	def test_can_find_files_blonging_to_dataset(self):
		# overwriting data DIR for GameManager settings
		TEST_DIR = os.path.abspath("tests/test_data/")
		keyword = "test_keyword"
		self.gmanager.dataset_matchlist_DIR = TEST_DIR

		self.gmanager.keyword = keyword
		self.gmanager.find_files()
		self.assertEqual(len(self.gmanager.dataset_matchlist_files), 2)
		for DIR in self.gmanager.dataset_matchlist_files:
			self.assertIn(keyword, str(DIR))