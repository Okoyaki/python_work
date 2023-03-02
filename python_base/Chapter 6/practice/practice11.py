# 6.11
cities = {
	
	'moscow': {
		'country': 'russia',
		'population': 11980000,
		'fact': 'Capital of Russia',
		},

	'beijing': {
		'country': 'china',
		'population': 21540000,
		'fact': 'Capital of China',
		},

	'tokyo': {
		'country': 'japan',
		'population': 13960000,
		'fact': 'Capital of Japan',
		},

	}

for city, city_info in cities.items():
	print(f"\nCity: {city.title()}")
	print(f"\tCountry: {city_info['country'].title()}")
	print(f"\tPopulation: {city_info['population']} people")
	print(f"\tFact: {city_info['fact']}")