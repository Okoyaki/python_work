# 5.11
numbers = list(range(1,10))

for number in numbers:
	if number > 0 and number < 2:
		print(f"{number}st")
	elif number >= 2 and number < 3:
		print(f"{number}nd")
	elif number >=3 and number < 4:
		print(f"{number}rd")
	else:
		print(f"{number}th")