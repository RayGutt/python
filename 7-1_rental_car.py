# 7-1. Rental Car: 

# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as “Let me see if I can find you a Subaru.”

message = "What kind of car would you like to rent? "

car = input(message)

print("Let me see if I can find you a " + car.title() + ".")
