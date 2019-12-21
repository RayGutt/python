glossary = {
	'dictionary': 'key-value pair list',
	'list': 'an ordered collection of items',
	'tuple': 'immutable list',
	'variable': 'used to store data',
	'loop': 'repeating the same actions',
	'set': 'a list with unique items',
	}

for key, value in glossary.items():
	print(key.title() + ":\n\t" + value)
