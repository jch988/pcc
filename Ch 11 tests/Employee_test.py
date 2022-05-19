import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):


	def setUp(self):
		self.emp = Employee('Ron', 'Swanson', 50_000)

	def test_give_default_raise(self):
		self.emp.give_raise()
		self.assertEqual(self.emp.salary, 55_000)

	def test_give_custom_raise(self):
		self.emp.give_raise(10_000)
		self.assertEqual(self.emp.salary, 60_000)


if __name__ == '__main__':
	unittest.main()

# >>> ..
# >>> ----------------------------------------------------------------------
# >>> Ran 2 tests in 0.000s
# >>> 
# >>> OK