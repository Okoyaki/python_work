# 9.14
from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
ticket = ""

for value in range(1,5):
	ticket += str(choice(lottery[:10]))

ticket += choice(lottery[10:])

print(f"The winning ticket is: {ticket}")
"""
for roll in range(1,5):
	print(f"{choice(lottery[:10])}")
print(f"{choice(lottery[10:])}")

print("This is the winning ticket!!")
"""