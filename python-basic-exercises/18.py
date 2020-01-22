number_1 = int(input("Please enter number 1 "))
number_2 = int(input("Please enter number 2 "))
number_3 = int(input("Please enter number 3 "))


if number_1 == number_2 and number_1 == number_3:
    result = 3 * (number_1 + number_2 + number_3)
else:
    result = number_1 + number_2 + number_3

print(f"Result: {result}")
