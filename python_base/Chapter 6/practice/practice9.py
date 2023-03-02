# 6.9
favorite_places = {
	'andrew': ['park', 'square', 'train'],
	'ilya': ['train'],
	'egor': ['school', 'park'],
	}

for person, places in favorite_places.items():
	print(f"\nPerson's name: {person.title()}")
	if len(places) > 1:
		print("His favorite places are:")
		for place in places:
			print(place.title())
	else:
		print("His favorite place is:")
		print(places[0].title())
