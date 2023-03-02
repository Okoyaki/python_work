# 9.4 (code from 9.1)
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


restaurant = Restaurant('japanfish', 'japanese cuisine')
print(restaurant.number_served)

restaurant.number_served = 5
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(2)
print(restaurant.number_served)