import requests
import json

class MatchFinder:
	def __init__(self, max_match_id="4000000000"):
		# by default query results returned by ascending mmr
		self.query_order = "mmr_ascending" 
		self.max_match_id = max_match_id
		self.MATCH_FINDER_URL = "https://api.opendota.com/api/publicMatches?"
		self.load_data()

	def load_data(self):
		"""
		Downloads match ids and saves to memory.
		"""
		r = requests.get(self.MATCH_FINDER_URL)
		self.data = json.loads(r.text.encode("ascii","replace").decode())
		print(self.data)

if __name__=="__main__":
	find_matches = MatchFinder()