# 9.6
class Restaurant():
	"""Простая модель ресторана"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты описания ресторана."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Возвращает описание ресторана."""
		print(f"\nRestaurant's name is {self.restaurant_name.title()}.")
		print(f"Restaurant's cuisine type is {self.cuisine_type.title()}.")

	def open_restaurant(self):
		"""Возвращает сообщение о состоянии ресторана."""
		print("The restaurant is open!")

	def set_number_served(self, number):
		"""Устанавливает значение обслуженных клиентов."""
		self.number_served = number

	def increment_number_served(self, number_inc):
		"""Увеличивает количество обслуженных клиентов."""
		self.number_served += number_inc


class IceCreamStand(Restaurant):
	"""Представляет аспекты ресторана, специфические для киоска с мороженым."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты класса-родителя."""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['strawberry', 'pistachio', 'chocolate']

	def describe_flavors(self):
		"""Выводит список сортов мороженого."""
		print("\nThis icecream stand has these flavors:")
		for flavor in self.flavors:
			print(f"- {flavor}")


stand1 = IceCreamStand('icy ice', 'ice cream')

stand1.describe_flavors()