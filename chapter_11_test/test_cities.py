import unittest
from city_functions import get_city_country_string 

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        string = get_city_country_string('santiago', 'chile')
        self.assertEqual(string, 'Santiago, Chile')

    def test_city_country_population(self):
        string = get_city_country_string('santiago', 'chile', 5000000)
        self.assertEqual(string, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
