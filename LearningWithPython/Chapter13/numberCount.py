# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/3/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

file = open("number13.5toRead.txt")
content = file.read()
file.close()

num_words = len(content.split())
print(f"There are {num_words} words in the file")