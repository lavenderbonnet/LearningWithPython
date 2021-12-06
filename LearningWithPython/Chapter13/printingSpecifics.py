# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/4/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

f = open("printingSpec.txt", "r")

lines = f.readlines()

for l in lines:
    if "snake" in l:
        print(l)