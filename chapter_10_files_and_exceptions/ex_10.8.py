filename = 'data/cats.txt'

try:
    with open(filename) as f:
        cats = f.readlines()
        for cat in cats:
            print(cat.rstrip())

except FileNotFoundError:
    print(f"Error: file {filename} not found.")

filename = 'data/dogs.txt'

try:
    with open(filename) as f:
        dogs = f.readlines()
        for dog in dogs:
            print(dog.rstrip())

except FileNotFoundError:
    print(f"Error: file {filename} not found.")
