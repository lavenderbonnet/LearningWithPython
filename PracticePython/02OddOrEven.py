# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 4/17/2021
# --------------------------------------------------------------------------


n = int(input("Choose a number please. "))
d = int(input("Choose another number. "))

if n%d == 0:
    print("Your number is divisable by your second number. :)")
elif n%4 == 0:
    print("Four fine fresh fish for you.")
elif n%2 == 0:
    print("Your number was even, ha. That's right, I know that.")
elif n%2 == 1:
    print("Your number sucks. An odd? Seriously?")


