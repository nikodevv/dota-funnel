import time
import unittest
from rate_limiter import limit_rate_premium, limit_rate_free
from tests.LimiterBaseTest import LimiterBaseTest

class LimiterBaseTest:
	class SimpleClass:
		"""
		Filler class used for testing limit_rate interaction with state
		"""
		@limit_rate_premium
		def call_API(self):
			"""
			Mock method meant to symbolize a call to Open Dota API
			"""
			pass

	def setUp(self):
		self.test_object = self.SimpleClass()
		self.max_calls = 1200

	def test_limit_is_not_capped_for_when_not_necessary(self):
		"""
		Checks that first 1199 calls are not limited by limit_rate
		"""
		start = time.time()
		for i in range(0, self.max_calls-1):
			self.test_object.call_API()
		self.assertLess(start-time.time(), 60)

	def test_limit_is_capped_when_many_calls_made(self):
		"""
		Checks that no more than 1200 calls can be made per minute
		"""
		start = time.time()
		for i in range(0, self.max_calls):
			self.test_object.call_API()
		self.assertLess(start-time.time(), 60)

	def test_limit_decorator_function_adds_state_variables_to_object(self):
		self.test_object.call_API()
		self.assertIsNotNone(self.test_object.api_calls)
		self.assertIsNotNone(self.test_object.first_call)

class TestLimiterPremium(LimiterBaseTest, unittest.TestCase):
	def test_tracks_credit_card_charges_correctly(self):
		for i in range(0,100):
			self.test_object.call_API()
		self.assertEqual(float(0.01), round(self.test_object.total_cost, 3))

		for i in range(0,50):
			self.test_object.call_API()
		self.assertEqual(float(0.015), round(self.test_object.total_cost, 3))

class TestLimiterFree(LimiterBaseTest, unittest.TestCase):
	class SimpleClass:
		"""
		Filler class used for testing limit_rate interaction with state
		"""
		@limit_rate_free
		def call_API(self):
			"""
			Mock method meant to symbolize a call to Open Dota API
			"""
			pass

	def setUp(self):
		self.test_object = self.SimpleClass()
		self.max_calls = 60

if __name__ == "__main__":
	unittest.main()

