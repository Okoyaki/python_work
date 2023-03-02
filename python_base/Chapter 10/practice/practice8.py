# 10.8
def read_names(filename):
	try:
		with open(filename) as file_object:
			names = file_object.read()
	except FileNotFoundError:
		print(f"File {filename} couldn't be found.")
	else:
		for name in names.split():
			print(name)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	read_names(filename)

