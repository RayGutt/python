def make_shirt(size='large', message='I love Python.'):
	"""prints a sentence summarizing the size of the shirt and the message printed on it."""
	print("\nThe T-shirt size is: " + size)
	print("\nThe message printed on the shirt is :")
	print("\n\t" + '"' + message + '"')

print("All default:")
make_shirt()

print("Default message, medium size:")
make_shirt(size='medium')

print("Size small, odd message:")
make_shirt(size='small', message='Prout!')

