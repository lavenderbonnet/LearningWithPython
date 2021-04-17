# --------------------------------------------------------------------------
# Author : Lilac Walia   (with Pranali)
# Date : 4/2/2021
# --------------------------------------------------------------------------



name = input("What's your name? ")
year = int(input("What year is it? "))
age = int(input("How old are you? "))
repeat = int(input("Pick a number, any number. "))

x = int(100 - age)
z = int(year + x)

for x in range(repeat):
    print("\n" + name + ", in the year " + str(z) + " you will turn 100 years old.")

