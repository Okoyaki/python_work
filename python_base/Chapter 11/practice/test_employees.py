# 11.3 (test part)
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Тесты для класса Employee."""

	def setUp(self):
		"""
		Создание опроса и набора ответов для всех тестовых методов.
		"""
		self.employee = Employee('max', 'shushakov', 90000)

	def test_give_default_raise(self):
		"""Проверяет, повышается ли оклад на величину по умолчанию."""
		self.employee.give_raise()

	def test_give_custom_raise(self):
		"""Проверяет, повышается ли оклад на заданную величину."""
		self.employee.give_raise(3000)

if __name__ == '__main__':
	unittest.main()