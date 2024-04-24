# Write a Python program to convert degree to radian 

import math  #pi=22/7

def d_to_r(degree):
    radian=((degree*math.pi)/180)
    return radian

degree=float(input("enter degree:"))
print(d_to_r(degree))

    