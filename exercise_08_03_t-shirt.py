def make_shirt(size, message):
	"""prints a sentence summarizing the size of the shirt and the message printed on it."""
	print("\nThe T-shirt size is: " + size)
	print("\nThe message printed on the shirt is :")
	print("\n\t" + '"' + message + '"')

print("Positional arguments function call:")
make_shirt('XL', 'Hello, world!')

print("\nKeyword arguments function call:")
make_shirt(message='Hello, world!', size='XL')
