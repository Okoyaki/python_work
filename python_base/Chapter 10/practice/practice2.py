# 10.2
filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.replace('python', 'c').rstrip())
		