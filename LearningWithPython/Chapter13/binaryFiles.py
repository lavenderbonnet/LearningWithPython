# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/3/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

f = open("somefile.zip", "rb") # adding "b" tells the program there's binary
g = open("thecopy.zip", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break
    g.write(buf)

f.close()
g.close()