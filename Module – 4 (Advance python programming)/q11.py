# Write a Python program to write a list to a file.  

name=['hhhs','wssgey','.ejhlkeb']
def list_(name):
    with open('q11.txt','w') as file:
        for line in name:
            file.write('%s\n' %line)
        print("done")
list_(name)

# # list of names
# names = ['Jessa', 'Eric', 'Bob']

# # open file in write mode
# with open('q11.txt', 'w') as fp:
#     for item in names:
#         # write each item on a new line
#         fp.write("%s\n" % item)
#     print('Done')

