# 4.10 (code taken from 4.8/4.9)
numbers = [value**3 for value in range(1,11)]
for number in numbers:
	print(number)

print(f"The first three items in the list are: {numbers[:3]}")
print(f"Three items from the middle of the list are: {numbers[4:7]}")
print(f"The last three items in the list are: {numbers[-3:]}")
