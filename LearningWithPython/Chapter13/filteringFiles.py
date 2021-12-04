# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/3/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue

        outfile.write(text)

    infile.close()
    outfile.close()