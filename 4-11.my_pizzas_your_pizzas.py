pizzas = ['margherita', 'veggie', 'cheese', 'neptune']

for pizza in pizzas:
   print("\nI like " + pizza + " pizza.")

print("\n\nI really love pizza!!!")

friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
friend_pizzas.append('pomodoro')

print("\n\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\n\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
