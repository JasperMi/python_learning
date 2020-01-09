import unittest
from chapter_11.city_functions import get_formatted_city_name


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_name = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_city_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city_name = get_formatted_city_name('santiago', 'chile', popluation=5000000)
        self.assertEqual(formatted_city_name, 'Santiago, Chile-Population 5000000')


if __name__ == "__main__":
    unittest.main()
