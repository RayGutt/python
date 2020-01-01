from random import randint

class Die:
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		result = randint(1,self.sides)
		print(result)
	
six_sided_die = Die(6)

print("6-sided die:\n")
for i in range(1,11):
	print(f"Try #{i}")
	six_sided_die.roll_die()

ten_sided_die = Die(10)
twenty_sided_die = Die(20)

print("\n10-sided die:\n")
for i in range(1,11):
	print(f"Try #{i}")
	ten_sided_die.roll_die()

print("\n20-sided die:\n")
for i in range(1,11):
	print(f"Try #{i}")
	twenty_sided_die.roll_die()
