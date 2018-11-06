import requests
import json
BASE_URL = "https://api.opendota.com/api/"
def pull_match_data(match_id):
	match_url = "%smatches/%s" % (BASE_URL, match_id)
	r = requests.get(match_url)
	try:
		history = json.loads(r.text.encode("ascii", 'replace').decode())["chat"]
	except KeyError as e:
		print(r.text)
		return None
	if history == None:
		return None
	for msg in history:
		if msg['type'] == "chat":
			print(msg)

if __name__=="__main__":
	pull_match_data("4200138505")
