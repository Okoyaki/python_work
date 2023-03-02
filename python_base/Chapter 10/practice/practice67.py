# 10.6/10.7
print("This is an adding only calculator.")
print("Press 'q' to quit at any time.")

while True:
	first_number = input("\nEnter first number: ")
	if first_number == 'q':
		break
	second_number = input("Enter second number: ")
	if second_number == 'q':
		break

	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Entered value isn't a number!")
	else:
		print(answer)