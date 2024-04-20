# How will you remove last object from a list?  
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?  


# To remove the last object from a list in Python,
# you can use the pop() method without passing any index,
# or you can use slicing to create a new list without the last element.
# Here's how to do it using both methods


list1=[2,33,222,14,25]

list1.pop()

# list1=list1[:-1]
print(list1)