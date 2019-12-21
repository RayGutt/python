rivers = {
	'amazon': 'brazil',
	'seine': 'france',
	'thames': 'england',
	}

for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title())

print("\nList of all the rivers included in the dictionary: ")
for river in rivers.keys():
	print(river.title())

print("\nList of all the countries included in the dictionary: ")
for country in rivers.values():
	print(country.title())
