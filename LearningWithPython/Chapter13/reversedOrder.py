# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/4/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

o_f = open("reverseOriginalFile.txt", "r")
c = o_f.readlines()
# print(c)
o_f.close()

c.reverse()
# print(c)

ro_f = open("reversedFile.txt", "w")
for s in c:
    ro_f.write(s)
ro_f.close()