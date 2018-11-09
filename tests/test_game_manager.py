import unittest
import os
from GameManager import GameManager

class TestGameManager(unittest.TestCase):
	def setUp(self):
		self.gmanager = GameManager()

	def test_can_find_files_blonging_to_dataset(self):
		# overwriting data DIR for GameManager settings
		TEST_DIR = os.path.abspath("/test_data")
		keyword = "test_keyword"
		self.gmanager.dataset_matchlist_DIRs = TEST_DIR

		self.gmanager.keyword = keyword
		self.gmanager.find_files()
		self.assertEqual(len(self.gmanager.dataset_matchlist), 2)
		for DIR in gmanager.dataset_file_DIRs:
			self.assertIn(keyword, str(DIR))