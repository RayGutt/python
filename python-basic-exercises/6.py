# accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

sequence = input("please enter a comma-separated list of numbers: ")

my_list = sequence.split(",")
my_tuple = tuple(my_list)

print("List: ",my_list)
print("Tuple: ",my_tuple)
