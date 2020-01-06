import json

filename = 'data/favorite_number.json'
with open(filename) as f:
    favorite_number = json.load(f)


print(f"I know your favorite number, it's {favorite_number}")
