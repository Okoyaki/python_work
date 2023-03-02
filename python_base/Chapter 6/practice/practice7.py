# 6.7
people = {
	
	'smax21': {
		'first': 'max',
		'last': 'shushakov',
		'age': 21,
		'city': 'ufa',
		},
	
	'gegor21': {
		'first': 'egor',
		'last': 'grigorev',
		'age': 21,
		'city': 'ufa',
		},
	
	'nandrew21': {
		'first': 'andrew',
		'last': 'neverov',
		'age': 21,
		'city': 'novosibirsk'
		},
	}

for person, person_info in people.items():
	print(f"\nUsername: {person}")
	full_name = f"{person_info['first']} {person_info['last']}"
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {person_info['city'].title()}")