# 7.10
vacation_places = {}

polling_active = True

while polling_active:
	name = input("\nPlease, enter your name: ")
	place = input("Please, enter place you would like to spend vacation at: ")

	vacation_places[name] = place

	repeat = input("Would you like another person try the polling? (yes/no) ")
	if repeat == 'no':
		break

print("\n--- Polling Results ---")
for name, place in vacation_places.items():
	print(f"{name.title()} would like to spend vacation at {place.title()}")
