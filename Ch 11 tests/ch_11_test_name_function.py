import unittest
from name_function import get_formatted_name_2

class NamesTestCase(unittest.TestCase):
	"""Tests for 'ch_11_testing.py'."""

	def test_first_last_name(self):			
		"""Do names like 'Janis Joplin' work?"""
		name = get_formatted_name_2('janis', 'joplin')
		self.assertEqual(name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like John Paul Jones work?"""
		name = get_formatted_name_2('john', 'jones', 'paul')
		self.assertEqual(name, 'John Paul Jones')

if __name__ == '__main__':
	unittest.main()