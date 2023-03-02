"""Простая модель пользователя"""

class User():
	"""Модель пользователя"""
	
	def __init__(self, first_name, last_name, age, location):
		"""Инициализирует атрибуты описания пользователя."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		"""Возвращает отформатированное описание пользователя."""
		print("\nUser info:")
		print(f"User's first name: {self.first_name.title()}")
		print(f"User's last name: {self.last_name.title()}")
		print(f"User's age: {self.age}")
		print(f"User's location: {self.location.title()}")

	def greet_user(self):
		"""Возвращает приветствие пользователю."""
		print(f"Hello, {self.first_name.title()}!")

	def increment_login_attempts(self):
		"""Увеличивает кол-во попыток входа"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Сброс кол-ва попыток входа"""
		self.login_attempts = 0	
