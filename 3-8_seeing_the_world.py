places = ['New-York', 'Amsterdam', 'Oslo', 'Copenhagen', 'Roma', 'Toronto']

print("Original order: ")
print(places)

print("Alphabetical order (temporary)")
print(sorted(places))

print("Places:")
print(places)

places.reverse()
print("Places after reverse()")
print(places)

places.reverse()
print("Places after a second reverse()")
print(places)

places.sort()
print("Places after sort()")
print(places)
