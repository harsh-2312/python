# Write a Python program to calculate surface volume and area of a cylinder 

import math

def volum(radius,heigth):
    return 2 * math.pi * radius *(radius + heigth)

def area(radius,heigth):
    return math.pi * radius**2 * heigth

radius=float(input("enter radius:"))
heigth=float(input("enter heigth:"))

print("volums of cylinder:",volum(radius,heigth))
print("area of cylinder:",area(radius,heigth))