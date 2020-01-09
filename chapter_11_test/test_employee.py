import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Create an employee"""
        self.my_employee = Employee('Joe', 'Harris', 50000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary,55000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(2000)
        self.assertEqual(self.my_employee.annual_salary,52000)


if __name__ == '__main__':
    unittest.main()
