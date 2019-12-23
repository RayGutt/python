def city_country(name, country):
	"""Print a simple message about city"""
	return '"' + name.title() + ", " + country.title() + '"'

message = city_country('paris', 'france')
print(message)

message = city_country('paris', 'texas')
print(message)

message = city_country('london', 'england')
print(message)
