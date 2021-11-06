# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 10/24/2021
# --------------------------------------------------------------------------

import sys


def absolute_value(n): # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        n = -n
    return n

# --------------------------------------------------------------------------

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""

# --------------------------------------------------------------------------

def distance_formula(x1, y1, x2, y2):
    d = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
    return d

# --------------------------------------------------------------------------

compass = ["N", "E", "S", "W"]

def turn_clockwise(d):
    if 0 <= d <= len(compass):
        i = compass.index(d)
        l = len(compass)
        next_i = (i + 1) % l
        return compass[next_i]
    else:
        return None


def turn_counter_clockwise(d):
    i = compass.index(d)
    l = len(compass)
    next_i = (i - 1) % l
    return compass[next_i]

# d = 'N'
# for i in range(10):
#     d = turn_counter_clockwise(d)
#     print(d)

# --------------------------------------------------------------------------

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite_abs_val():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

def test_suite_distance():
    test(distance_formula(0, 0, 0, 1) == 1)
    test(distance_formula(1, 0, 4, 0) == 3)
    test(distance_formula(1, 1, 2, 2) == (2)**0.5)

def test_suite_directions():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

def main():
    # print(find_first_2_letter_word(["This", "is", "bread"]))
    # test_suite_distance()
    test_suite_directions()

main()
# test_suite_abs_val() # Here is the call to run the tests

