from datetime import date

current_year = date.today().year

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
number = int(input("Also enter a number: "))

hundredth_anniversary = current_year + 100 - age

for i in range(number):
    print(f"Matt, you'll turn 100 in {hundredth_anniversary}.\n")
