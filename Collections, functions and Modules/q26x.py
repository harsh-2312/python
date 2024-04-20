# Write a Python program to replace last value of tuples in a list. 

tup_list=[(1,2,3),(4,5,6),(7,8,9)]

for t in tup_list:
    t[:-1]+(10)
    print(tup_list)