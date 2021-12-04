# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/29/2021
# --------------------------------------------------------------------------

import os

cwd = os.getcwd()

# Print the current working directory
print(f"Current working directory: {cwd}")

# Print the type of the returned object
print(f"os.getcwd() returns an object of type: {type(cwd)}")

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
# os.chdir("LearningWithPython")
# os.chdir("Chapter13")
cwd = os.getcwd()

print(f"Current working directory: {cwd}")

myfile = open("test.txt", "w")
# "w" means opening the file for writing
myfile.write("My first file written from Python\n")
myfile.write("------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()