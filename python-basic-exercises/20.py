def my_function(string, number):
    result_string = ''

    for i in range(number):
        result_string += string

    return result_string


string = input("Please enter a string ")
number = int(input("Please enter a number "))

my_result = my_function(string, number)
print(my_result)
