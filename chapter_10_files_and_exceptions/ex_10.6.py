number_1 = input("Please enter one number: ")
number_2 = input("Please enter another number: ")

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
except ValueError:
    print("Please enter numbers, not strings.")
else:
    sum = number_1 + number_2
    print(f"{number_1} + {number_2} = {sum}")

