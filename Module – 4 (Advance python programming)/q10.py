# Write a Python program to count the frequency of words in a file. 


from collections import Counter
file_name='q10.txt'

def count_(file_name):
    try:
        with open(file_name,'r') as file:
         return Counter(file.read().split())
        # return frequency
    except FileNotFoundError:
        print("file not found")

print(count_(file_name))

