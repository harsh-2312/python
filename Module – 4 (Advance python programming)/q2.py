#  Write a Python program to read an entire text file. 

def file_read(fname):
        try:
                txt = open(fname)
                print(txt.read())
        except FileNotFoundError:
                print("file not found")

file_read('q2.txt')