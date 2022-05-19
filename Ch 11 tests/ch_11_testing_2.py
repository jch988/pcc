

# Testing Classes

common assert methods in unittest.TestCase

	assertEqual(a, b)

	assertNotEqual(a, b)

	assertTrue(x)

	assertFalse(x)

	assertIn(item, list)

	assertNotIn(item, list)



# Create survey class and code to run along with it


class AnonymousSurvey:
	"""Collect Anonymous answers to survey questions"""

	def __init__(self, question):
		"""Store the question and prepare to store responses"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the survey question"""
		print(self.question)

	def store_responses(self, new_response):
		"""Store a single response to the survey"""
		self.responses.append(new_response.title())

	def show_results(self):
		"""Show all of the responses that have been given"""
		print("Survey results:")
		for response in self.responses:
			print(f"\t- {response}")



question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()

print(f"Enter 'q' to quit at any time")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_responses(response)

print("\nThank you to everyone who participated in the survey")
my_survey.show_results()


# Works as is.
# But want to add other classes and functionalities.
# Along the way we want to make sure this class works correctly

# first, write a test to make sure that a single response is stored correctly (current functionality)

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""

	def test_store_single_response(self):
		"""Tests that a single response is stored properly"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)					# make an instance of the class to test it
		my_survey.store_response('english')						# single response
		self.assertIn('English', my_survey.responses)			# check to make sure 'English' is in the list self.responses of the instance my_survey

if __name__ == '__main__':
	unittest.main()
# >>> .
# >>> ----------------------------------------------------------------------
# >>> Ran 1 test in 0.000s
# >>> 
# >>> OK


# now verify that three respones can be stored correctly


# added def test_store_three_responses

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""

	def test_store_single_response(self):
		"""Tests that a single response is stored properly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('english')
		self.assertIn('English', my_survey.responses)

	def test_store_three_responses(self):
		"""Tests that three individual responses are stored properly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
	unittest.main()
# >>> ..
# >>> ----------------------------------------------------------------------
# >>> Ran 2 tests in 0.000s
# >>> 
# >>> OK



# test fails if language names are not capitalized in responses



# this works but is repetitive to type out. Use setUp() method
# creates a survey instance and set of responses that can be used in the test methods


import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""


	def setUp(self):
		"""Create a survey and a set of responses for use in all test methods"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)				
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""Tests that a single response is stored properly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Tests that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
	unittest.main()
# >>> ..
# >>> ----------------------------------------------------------------------
# >>> Ran 2 tests in 0.000s
# >>> 
# >>> OK


# added this on my own

	def test_show_question(self):
		"""Tests that the survey question is displayed properly"""
		self.assertEqual(self.my_survey.question, 'What language did you first learn to speak?')
# >>> ...
# >>> ----------------------------------------------------------------------
# >>> Ran 3 tests in 0.000s
# >>> 
# >>> OK



# But this version with 'self.my_survey.show_question()' doesn't work
# I don't understand why

	def test_show_question(self):
		"""Tests that the survey question is displayed properly"""
		# self.my_survey.show_question()
		self.assertEqual(self.my_survey.show_question(), "What language did you first learn to speak?")
# >>> What language did you first learn to speak?
# >>> F..
# >>> ======================================================================
# >>> FAIL: test_show_question (__main__.TestAnonymousSurvey)
# >>> Tests that the survey question is displayed properly
# >>> ----------------------------------------------------------------------
# >>> Traceback (most recent call last):
# >>>  File "/Users/JCH/Python/pcc/Ch 11/test_survey.py", line 29, in test_show_question
# >>>    self.assertEqual(self.my_survey.show_question(), "What language did you first learn to speak?")
# >>> AssertionError: None != 'What language did you first learn to speak?'
# >>> 
# >>> ----------------------------------------------------------------------
# >>> Ran 3 tests in 0.001s
# >>> 
# >>> FAILED (failures=1)