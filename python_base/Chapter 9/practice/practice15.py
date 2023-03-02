# 9.15
from random import choice

def generate_ticket(lottery):
	ticket = ""
	for value in range(1,5):
		ticket += str(choice(lottery[:10]))

	ticket += choice(lottery[10:])
	return ticket


lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
win = False
cycle_amount = 0

win_ticket = generate_ticket(lottery)
print(f"Generated winning ticket: {win_ticket}")

print("Generating ticket combinations until winning...")
while win == False:
	ticket = generate_ticket(lottery)
	print(ticket)

	if ticket == win_ticket:
		win=True
		print("Found the winning ticket!")

	cycle_amount += 1

print(f"Amount of cycles needed to win: {cycle_amount}")