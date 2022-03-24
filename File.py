import os
# We created the path string using join function
path = os.path.join(os.path.expanduser('~'), 'Documents', 'python', 'file.txt')

# Using with closes the file automatically.
with open(path, "r") as File1:
    file_stuff = File1.readlines()
    print(file_stuff)
    print(File1.name) #Prints the name of the file
    print(File1.mode) #Prints the mode-'read', 'write' of the file