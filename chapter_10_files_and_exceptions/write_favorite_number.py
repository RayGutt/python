import json

number = input("What is your favorite number? ")

filename = 'data/favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
