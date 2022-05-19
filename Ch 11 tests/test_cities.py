import unittest
from city_functions import location

class NamesTestCase(unittest.TestCase):


	def test_city_country(self):
		"""Do inputs with required 2 parameters work?"""
		place = location('san antonio', 'the united states')
		self.assertEqual(place, 'San Antonio is in The United States')

	def test_city_country_population(self):
		"""Do inputs with optional population work?"""
		place = location('san antonio', 'the united states', '1.4 million')
		self.assertEqual(place, 'San Antonio is in The United States and has a population of 1.4 million people')


if __name__ == '__main__':
	unittest.main()