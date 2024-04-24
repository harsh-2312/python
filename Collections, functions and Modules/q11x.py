# Write a Python function that takes a list and returns a new list with unique 
# elements of the first list.  

list1=[1,5,8,3,8,7,3,2]
un=[]
d=[]
for i in list1:
    if i!=list1:
        un.append(i)
    if un==list1:
        d.append(un)
        
# for i in list1:
#     if i not in un:
#         un.append(i)
print(un)