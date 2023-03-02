# 10.12
import json

filename = 'favorite_number.json'

try:
	with open(filename) as f:
		favorite_number = json.load(f)
except FileNotFoundError:
	favorite_number = input("Enter your favorite number: ")
	with open(filename, 'w') as f:
		json.dump(favorite_number, f)
else:
	print(favorite_number)