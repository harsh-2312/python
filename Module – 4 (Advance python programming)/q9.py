#  Write a Python program to count the number of lines in a text file. 

file_name='q4.txt'

def number(file_name):
    try:
        with open(file_name,'r') as file:
            count=len(file.readlines())
        return count
    except FileNotFoundError:
        print("file not found")
print(number(file_name))