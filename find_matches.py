import requests
import json
import time
import os

class MatchFinder:
	def __init__(self, max_match_id="4000000000"):
		self.MATCH_FINDER_URL = "https://api.opendota.com/api/publicMatches?"
		self.settings(max_match_id)
		
	def settings(self, max_match_id):
		self.DATA_DIR = os.path.abspath("data/")
		# by default query results returned by ascending mmr
		self.query_order = "mmr_ascending" 
		self.max_match_id = max_match_id
		# number of chars to incrementally indent inner json 
		# scopes in output file
		self.output_indent = 2


	def load_data(self):
		"""
		Downloads match ids and saves to memory.
		"""
		r = requests.get(self.MATCH_FINDER_URL)
		# prevents encoding errors arising from higher order characters
		# in "team name" field
		self.data = json.loads(r.text.encode("ascii","replace").decode())
	
	def save_data(self, file_name="default", file_prefix="matchlist"):
		"""
		Saves any data from state to designated file. If file_name
		is specified, the data will be stored to ./data/file_name.json.
		If no file_name parameter is given, data will be stored to
		an automatically generated file ./data/file_prefix-timestamp.json
		"""
		f_name = self.__generate_filename(file_name, file_prefix)
		with open(f_name, 'a') as f:
			json.dump(self.data, f, indent=self.output_indent)
		print("Successfully saved file %s." % f_name)

	def __generate_filename(self, name, prefix):
		if name == "default":
			return os.path.join(self.DATA_DIR, "[%s]-[%s].json" % (
				prefix , str(time.time())))
		else:
			return name + ".json"

if __name__=="__main__":
	find_matches = MatchFinder()
	find_matches.load_data()
	find_matches.save_data()
