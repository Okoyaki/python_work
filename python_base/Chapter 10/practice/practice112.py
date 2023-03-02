# 10.11 (part 2)
import json

filename = 'favorite_number.json'

try:
	with open(filename) as f:
		favorite_number = json.load(f)
except FileNotFoundError:
	print(f"File {filename} couldn't be found.")
else:
	print(favorite_number)