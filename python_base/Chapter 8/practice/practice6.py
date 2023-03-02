# 8.6
def city_country(city, country):
	address = f"{city}, {country}"
	return address.title()

address = city_country('moscow', 'russia')
print(address)

address = city_country('beijing', 'china')
print(address)

address = city_country('tokyo', 'japan')
print(address)