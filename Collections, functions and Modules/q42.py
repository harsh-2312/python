# Write a Python program to print all unique values in a dictionary.  


dic1={'a':10,'b':20,'c':30,'d':10,'e':20}

uniq=set()

for v in dic1.values():
    uniq.add(v)
print(uniq)
