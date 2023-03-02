# 9.3
class User():
	"""Модель пользователя"""
	
	def __init__(self, first_name, last_name, age, location):
		"""Инициализирует атрибуты описания пользователя."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location

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


user_a = User('max', 'shushakov', 21, 'ufa')
user_b = User('egor', 'grigorev', 21, 'ufa')
user_c = User('andrew', 'neverov', 21, 'novosibirsk')

user_a.describe_user()
user_a.greet_user()

user_b.describe_user()
user_b.greet_user()

user_c.describe_user()
user_c.greet_user()
