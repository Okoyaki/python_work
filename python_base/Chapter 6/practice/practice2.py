# 6.2
lucky_numbers = {
	'max': 42,
	'egor': 132,
	'andrew': 13,
	'nikita': 77,
	'ilya': 1,
}

for person in lucky_numbers:
	print(f"{person.title()}'s lucky number is {lucky_numbers[person]}.")