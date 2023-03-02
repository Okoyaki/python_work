# 10.5
filename = 'reasons.txt'

with open(filename, 'a') as file_object:
	while True:
		reason = input("Why do you like programming (press 'q' to quit): ")
		if reason == 'q':
			break

		file_object.write(reason + '\n')