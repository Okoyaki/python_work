"""Набор классов для представления администратора."""

from user import User

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
		self.privileges = Privilege()
