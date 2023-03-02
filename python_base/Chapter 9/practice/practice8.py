# 9.8
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

class Privilege():
	"""Простая модель привилегий пользователя."""

	def __init__(self):
		"""Инициализация атрибутов класса."""
		self.privileges = ['adding messages', 'deleting users', 
						   'banning users' ]

	def show_privileges(self):
		"""Выводит привелегии пользователя."""
		print("\nThese are the user's privileges:")
		for privilege in self.privileges:
			print(f"- {privilege}")

class Admin(User):
	"""Представляет аспекты пользователя, специфические для администратора."""

	def __init__(self, first_name, last_name, age, location):
		"""Инициализирует атрибуты класса-родителя."""
		super().__init__(first_name, last_name, age, location)
		self.Privileges = Privilege()


Admin = Admin('max', 'shushakov', 21, 'ufa')
Admin.Privileges.show_privileges()