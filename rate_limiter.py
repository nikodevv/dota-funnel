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
		# Creates initial instance variables in object to which fn belongs
		# so that total API calls made by that object can be 
		# recorded.
		if not ((hasattr(args[0], 'api_calls')) or (hasattr(args[0], 'first_call'))):
			args[0].api_calls = 0
			args[0].first_call = time.time()
			args[0].total_cost = float(0)

		args[0].api_calls += 1
		args[0].total_cost += 0.0001 # Cost per API call
		
		# Stalls program when API minute-long limit is reached.
		if args[0].api_calls >= 1200:
			time_since_first_call = min(time.time()-args[0].first_call, 60)
			time.sleep(round(60-time_since_first_call) + 1)
			args[0].api_calls = 0
			args[0].first_call = time.time()
			print("Your credit card has been charged $0.12. Your total cost is " 
				+ str(args[0].total_cost))
		fn(*args, **kwargs)
	return wrapper
