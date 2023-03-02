# 7.5/7.6
active = True

while active:
	age = input("\nPlease, enter your age: ")

	if age == 'quit':
		break

	age = int(age)

	if age < 3:
		print("The ticket is free.")
	elif age >= 3 and age <= 12:
		print("The ticket costs $10.")
	else:
		print("The ticket costs $15.")