# 11.3 (class part)
class Employee():
	"""Класс, представляющий работника."""

	def __init__(self, first, last, salary):
		"""Инициализация атрибутов класса."""
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, increment_salary=5000):
		"""Увеличивает ежегодный оклад на $5000."""
		self.salary += increment_salary