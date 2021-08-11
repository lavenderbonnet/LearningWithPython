# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 8/6/2021
# --------------------------------------------------------------------------

def area(radius):
    a = 3.14159 * radius**2
    return a

def absolute_value(x):
    if x < 0:
        return -x
    else: 
        return x

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""