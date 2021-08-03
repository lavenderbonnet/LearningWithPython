# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 8/2/2021
# --------------------------------------------------------------------------

# You go on a wonderful holiday (perhaps to jail, 
# if you don’t like happy exercises) leaving on day 
# number 3 (a Wednesday). You return home after 137 
# sleeps. Write a general version of the program 
# which asks for the starting day number, and the 
# length of your stay, and it will tell you the name 
# of day of the week you will return on.

n = int(input("Choose a number 0 - 6. "))
d = int(input("How many days are you staying there? "))

if (n + d) % 7 == 0:
    print("You'll come back on a Sunday!")

elif (n + d) % 7 == 1:
    print("You'll come back on a Monday!")

elif (n + d) % 7 == 2:
    print("You'll come back on a Tuesday!")

elif (n + d) % 7 == 3:
    print("You'll come back on a Wednesday!")

elif (n + d) % 7 == 4:
    print("You'll come back on a Thursday!")

elif (n + d) % 7 == 5:
    print("You'll come back on a Friday!")

elif (n + d) % 7 == 6:
    print("You'll come back on a Saturday!")

else:
    print("...")
