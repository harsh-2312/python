# Write a Python program to select an item randomly from a list.  

import random
list1=[101,111,243,555,212,433,432,789]

rn = random.randrange(0,len(list1))
randomlist=list1[rn]
print(randomlist)


