# 10.10

def count_words(filename, word):
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"File {filename} couldn't be found.")
	else:
		print(f"Amount of '{word}'s in {filename} is {contents.count(word)}.")

filenames = ['alice.txt', 'arbiter.txt', 'madam_constantia.txt']
word = 'the'

for filename in filenames:
	count_words(filename, word)