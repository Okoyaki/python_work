# 9.2 (code from 9.1)
class Restaurant():
	"""Простая модель ресторана"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты описания ресторана."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Возвращает описание ресторана."""
		print(f"\nRestaurant's name is {self.restaurant_name.title()}.")
		print(f"Restaurant's cuisine type is {self.cuisine_type.title()}.")

	def open_restaurant(self):
		"""Возвращает сообщение о состоянии ресторана."""
		print("The restaurant is open!")


restaurant1 = Restaurant('japanfish', 'japanese cuisine')
restaurant2 = Restaurant('sphagett', 'italian cuisine')
restaurant3 = Restaurant('goroshek', 'russian cuisine')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()