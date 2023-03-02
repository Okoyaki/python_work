def count_words(filename):
	"""Подсчет приблизительного количества строк в файле."""

	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'madam_constantia.txt', 'arbiter.txt', 'moby_dick.txt']
for filename in filenames:
	count_words(filename)