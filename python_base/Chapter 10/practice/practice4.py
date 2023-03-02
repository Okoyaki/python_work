# 10.4
filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
	while True:
		username = input("Enter username (press 'q' to quit): ")
		if username == 'q':
			break

		message = f"Hello, {username.title()}!"
		print(message)
		file_object.write(message + '\n')
