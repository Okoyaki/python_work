# 9.13
from random import randint

class Die():
	"""Простая модель игрального кубика."""

	def __init__(self, sides=6):
		"""Иниациализация атрибутов класса."""
		self.sides = sides

	def roll_die(self):
		print(f"Number is: {randint(1, self.sides)}")


die = Die(20)

for roll in range(1,11):
	die.roll_die()