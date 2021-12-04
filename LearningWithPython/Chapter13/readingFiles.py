# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/3/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

text_file = open("test.txt", "r")
while True:                             # Continues reading linea fter line
    line_reading = text_file.readline()
    if len(line_reading) == 0:               # till there are no more lines to read
        break

    # To proccess the line(s) just read
    print(line_reading, end="")

text_file.close()