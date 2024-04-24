# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':  
# 300}, o {'item': 'item1', 'amount': 750}]  
# Expected Output: 
# Counter ({'item1': 1150, 'item2': 300})  


dic1=[{'item':'item1','amount':400},
      {'item':'item2','amount':300},
      {'item':'item1','amount':750}]  

combine={}

for i in dic1:
    for key,value in i.items():
        if key in combine:
            combine[key]+=value
        else:
            combine[key]=value
print(combine)