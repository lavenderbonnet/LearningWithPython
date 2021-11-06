# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 10/24/2021
# --------------------------------------------------------------------------

compass = ["N", "E", "S", "W"]
# --------------------------------------------------------------------------

def turn_clockwise(d):
    i = compass.index(d)
    l = len(compass)
    next_i = (i + 1) % l
    return compass[next_i]

def turn_counter_clockwise(d):
    i = compass.index(d)
    l = len(compass)
    next_i = (i - 1) % l
    return compass[next_i]

# --------------------------------------------------------------------------

d = 'N'
for i in range(10):
    d = turn_counter_clockwise(d)
    print(d)
# --------------------------------------------------------------------------