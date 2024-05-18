#  Write a Python program to append text to a file and display the text.

def appen(file):
    try:
        file=open("q3.txt","a")
        file.write(add + "\n")
        file.close
    except FileNotFoundError:
        print("file not found")

add=input("enter taxt to append file:")
appen(add)
