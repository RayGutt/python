def describe_city(city_name, country='france'):
	"""accepts the name of a city and its country.
	Prints a simple sentence about this info."""

	print("\n" + city_name.title() + " is in " + country.title())
	

print("Default country")
describe_city('paris')

print("\n\nExplicit, positional arguments")
describe_city('paris', 'france')

print("\n\nExplicit, keyword arguments")
describe_city(country='england', city_name='london')
