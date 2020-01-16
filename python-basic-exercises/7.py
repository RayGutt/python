# Write a Python program to accept a filename from the user and print the extension of that

filename = input("Enter a filename: ")

extension = filename.split(".")

print("The extension for the file " + str(filename) + " is " + str(extension[-1]))
