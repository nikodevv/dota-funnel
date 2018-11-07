import unittest
import time
from rate_limiter import limit_rate

class TestLimiterFull(unittest.TestCase):
	class SimpleClass:
		"""
		Filler class used for testing limit_rate interaction with state
		"""
		@limit_rate
		def call_API(self):
			"""
			Mock method meant to symbolize a call to Open Dota API
			"""
			pass

	def setUp(self):
		self.test_object = self.SimpleClass()

	def test_limit_is_not_capped_for_when_not_necessary(self):
		"""
		Checks that first 1999 calls are not limited by limit_rate
		"""
		start = time.time()
		for i in range(0, 1199):
			self.test_object.call_API()
		self.assertLess(start-time.time(), 60)

	def test_limit_is_capped_when_many_calls_made(self):
		"""
		Checks that no more than 1200 calls can be made per minute
		"""
		start = time.time()
		for i in range(0, 1200):
			self.test_object.call_API()
		self.assertLess(start-time.time(), 60)


if __name__ == "__main__":
	unittest.main()