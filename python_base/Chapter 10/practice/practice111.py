# 10.11 (part 1)
import json

filename = 'favorite_number.json'
favorite_number = input("Enter your favorite number: ")

try:
	with open(filename, 'w') as f:
		json.dump(favorite_number, f)
except FileNotFoundError:
	print(f"File {filename} couldn't be found.")