# --------------------------------------------------------------------------
# Author : Lilac Walia   (with Pranali)
# Date : 4/2/2021
# --------------------------------------------------------------------------



# 7)

# Dividing = /
# Dividing without decimal = //
# Remainder = %

# print((2 + 51)%12)


t = int(input("What is the time now, in hours? "))
m = input("Is it AM or PM? ")
w = int(input("How many hours shall you wait? "))


a = (t + w) % 12


if m == 1:
    mm = "am"

else:
    mm = "pm"


if a==0:
    print ("12", mm)
 
else:
    print(a, mm)


