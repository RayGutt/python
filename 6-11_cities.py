# 6-11. Cities: 

# Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city 
# and include the country that the city is in, its approximate population, 
# and one fact about that city. 
# The keys for each city’s dictionary should be something like country, 
# population, and fact. 
# Print the name of each city and all of the information 
# you have stored about it.

cities = {
	'paris': {
		'country': 'france',
		'population': 2000000,
		'fact': "has the eiffel's tower",
		},
	'london': {
		'country': 'the united kingdom',
		'population': 9000000,
		'fact': 'has big ben',
		},
	'new-york': {
		'country': 'the united states of america',
		'population': 8000000,
		'fact': 'has the statue of liberty',
		},
	}

for city, info in cities.items():
	print(city.title() + " is in " + info['country'].title() + ", has a population of " +
		str(info['population']) + " and " + info['fact'] + ".")
