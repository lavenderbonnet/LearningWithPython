# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/3/2021
# --------------------------------------------------------------------------

import os

os.chdir("D:\Lilac\Coding\Python\LearningWithPython\Chapter13")
cwd = os.getcwd()

unsorted = open("alphaFriends.txt", "r")
email_list = unsorted.readlines()
unsorted.close()

email_list.sort()

sorted = open("alphabeticalFriends.txt", "w")
for e in email_list:
    sorted.write(e)
sorted.close()