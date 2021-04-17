# --------------------------------------------------------------------------
# Author : Lilac Walia   (with Pranali)
# Date : 4/2/2021
# --------------------------------------------------------------------------



# 5)

p = 10000
n = 12
r = 0.08
t = int(input("Choose a number of years. "))

a = p*(1 + (r/n))**(n*t)

print(a)


# 7)

# Dividing = /
# Dividing without decimal = //
# Remainder = %

# print((2 + 51)%12)


t = int(input("What is the time now, in hours? "))
m = input("Is it AM or PM? ")
w = int(input("How many hours shall you wait? "))

if m == 1:
    mm = "am"

else:
    mm = "pm"

a = (t + w)%12

if a==0:
    print ("12", mm)
 
else:
    print(a, mm)


