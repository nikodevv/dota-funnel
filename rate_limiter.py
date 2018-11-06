import time
def limit_rate(fn):
	"""
	Limits number of times a function can be called per minute.
	This is required for functions which make a call to Open Dota API
	(Premium Tier access keys have 1200/minute calls).
	Note this is wrapper is insufficient if two modules are
	simultaneously making calls to API.
	"""
	def wrapper(*args, **kwargs):
		args[0].api_calls += 1
		if args[0].api_calls >= 1200:
			time_since_first_call = min(time.time()-args[0].first_call, 60)
			sleep(round(60-time_since_first_call) + 1)
			args[0].first_call = time.time()
			print("Your credit card has been charged $0.12")			
		fn(*args, **kwargs)