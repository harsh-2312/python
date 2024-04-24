# Write a Python program to read a random line from a file.  

import random 

# Open the file in read mode 
with open("MyFile.txt", "r") as file: 
	allText = file.read() 
	words = list(map(str, allText.split())) 

	# print random string 
	print(random.choice(words)) 
