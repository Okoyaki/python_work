# 11.1/11.2 (function part)
def get_formatted_location(city, country, population=''):
	"""Выводит отформатированное местоположение."""
	if population:
		location = f"{city}, {country}, population - {population}"
	else:
		location = f"{city}, {country}"
	return location.title()