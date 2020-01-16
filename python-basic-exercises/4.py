# Accepts the radius of a circle from the user and compute the area
from math import pi

radius = float(input("Please enter the radius of the circle: "))
area = pi * radius**2
print(f"The area of a circle with a radius of {radius} is : {area}")
