import unittest
import os
from GameManager import GameManager

class TestGameManager(unittest.TestCase):
	def setUp(self):
		self.gmanager = GameManager()

	def test_can_find_files_blonging_to_dataset(self):
		DIR_MATCH_DATA = os.path.abspath("./")
		keyword = "test_keyword"
		self.gmanager.keyword = keyword
		self.gmanager.find_files()
		self.assertEqual(len(gmanager.dataset_file_DIRs), 2)
		for DIR in gmanager.dataset_file_DIRs:
			self.assertIn(keyword, str(DIR))