# Write a Python program to read first n lines of a file. 

def read(n):
    try:
        file=open("q4.txt",'r')
        for i in range(n):
            print(file.readline())
    except FileNotFoundError:
        print("file not found")

n=int(input("enter number:"))
read(n)








   