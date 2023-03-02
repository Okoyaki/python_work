#6.8
pets = {
	
	'betty': {
		'animal': 'hamster',
		'owner': 'john',
		},

	'tama': {
		'animal': 'cat',
		'owner': 'yuki',
		},

	'bernard': {
		'animal': 'dog',
		'owner': 'alex',
		},

	}

for name, pet_info in pets.items():
	print(f"\nPet name: {name.title()}")
	print(f"\tAnimal type: {pet_info['animal'].title()}")
	print(f"\tOwner name: {pet_info['owner'].title()}")