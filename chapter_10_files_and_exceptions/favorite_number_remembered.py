import json
filename='data/favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
        number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(number, f)
else:
    print(f"Your favorite number is {number}")
