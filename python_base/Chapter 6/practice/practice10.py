# 6.10
lucky_numbers = {
	'max': [42, 13, 26],
	'egor': [132],
	'andrew': [13, 777],
	'nikita': [77],
	'ilya': [1, 11, 111],
}

for person, numbers in lucky_numbers.items():
	print(f"\nPerson's name: {person.title()}")
	if len(numbers) > 1:
		print("His lucky numbers are:")
		for number in numbers:
			print(number)
	else:
		print("His lucky number is:")
		print(numbers[0])