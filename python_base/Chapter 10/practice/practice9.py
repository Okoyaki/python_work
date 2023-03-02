# 10.9 (code from 10.8)
def read_names(filename):
	try:
		with open(filename) as file_object:
			names = file_object.read()
	except FileNotFoundError:
		pass
	else:
		for name in names.split():
			print(name)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	read_names(filename)

