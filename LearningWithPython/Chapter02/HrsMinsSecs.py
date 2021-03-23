# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 2/21/2021
# --------------------------------------------------------------------------


#  To   //   means dividing and only getting the quotient
#  To   %    means dividing and only getting the remainder

TotalSecs = int(input("How many seconds, in total?"))

#  input = asking question in terminal

Hours = TotalSecs // 3600
SecsStillRemaining = TotalSecs % 3600

Minutes = SecsStillRemaining // 60
SecsFinallyRemaining = SecsStillRemaining % 60

print("Hrs = ", Hours, "  Mins = ", Minutes, "  Secs = ", SecsFinallyRemaining)
