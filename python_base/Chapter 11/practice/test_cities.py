# 11.1/11.2 (test part)
import unittest
from city_functions import get_formatted_location

class LocTestCase(unittest.TestCase):
	"""Тесты для 'city_functions.py'."""

	def test_city_country(self):
		"""Работают ли локации вида 'Santiago, Chile'?"""
		formatted_location = get_formatted_location('santiago', 'chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Работают ли строки вида 'Santiago, Chile, population - 5000000"""
		formatted_location = get_formatted_location(
			'santiago', 'chile', '5000000')
		self.assertEqual(formatted_location, 
			'Santiago, Chile, Population - 5000000')

if __name__ == '__main__':
	unittest.main()