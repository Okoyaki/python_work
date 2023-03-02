# 8.5
def describe_city(city, country='russia'):
    print(f"{city.title()} is in {country.title()}")


describe_city('moscow')
describe_city('st. petersburg')
describe_city(city='beijing', country='china')