class AnonymousSurvey:
	"""Collect Anonymous answers to survey questions"""

	def __init__(self, question):
		"""Store the question and prepare to store responses"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the survey question"""
		print(self.question)

	def store_response(self, new_response):
		"""Store a single response to the survey"""
		self.responses.append(new_response.title())

	def show_results(self):
		"""Show all of the responses that have been given"""
		print("Survey results:")
		for response in self.responses:
			print(f"\t- {response}")





