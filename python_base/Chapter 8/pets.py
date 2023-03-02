def describe_pet(animal_type, pet_name):
	"""Выводит информацию о животном"""
	print(f"I have a {animal_type}.")
	print(f"His name is {pet_name.title()}.")
	
describe_pet('hamster', 'harry')