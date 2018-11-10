from os.path import abspath
from os import listdir, sep
import json

class GameManager(object):
	"""
	A class used for obtaining match data.

	GameManagers can find all files relevant to a 
	particular dataset, detect the matches which
	belong in that dataset, and return full Open Dota data
	for each match. 
	
	A dataset is defined as a set 
	of files with a matching keyword name, i.e. 
	[keyword]-[unixtime_file_was_collected].json.
	
	Only the data of one match is stored in memory at 
	any given time.
	"""
	def __init__(self, keyword=None):
		self.keyword = keyword
		self.data = None
		# Top level directory where matchlists for datasets are 
		# stored.
		self.dataset_matchlist_DIR = abspath("../data/")
		# List of DIR locations to every file containing 
		# match ids associated with the [keyword] dataset
		self.dataset_matchlist_files = []

	def find_files(self):
		"""
		Stores the path of match list files to memory.
		"""
		for file in listdir(self.dataset_matchlist_DIR):
			if self.keyword in file:
				self.dataset_matchlist_files.append(file)

	def set_matchlist(self, filename):
		"""
		Stores list of matches from a matchlist file.
		"""
		path = abspath("%s%s%s" % (self.dataset_matchlist_DIR, sep, filename))
		with open(path, "r") as f:
			self.matchlist = [match["match_id"] for match in json.load(f)]

	def process_matchlist(self, fn):
		"""
		Downloads match data and processes it as dictated by 
		fn parameter.
		"""
		for id in self.matchlist:
			fn(self, self.get_matchlist_data(id))

	def get_matchlist_data(self, match_id):
		return match_id