# ----------------------------------
# # Author : Lilac Walia
# Date : 2/21/2021
# ----------------------------------

# So I want to calculate, given an age, how 
# many hours, minutes, and seconds you have lived

age = int(input("How old are you? "))

weeks = age * 52
days = weeks * 7

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("You have lived for", seconds, "seconds.")