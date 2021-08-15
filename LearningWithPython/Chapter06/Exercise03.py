# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 8/13/2021
# --------------------------------------------------------------------------

import sys

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def day_name(d):
    if 0 < d and d < 7:
        return days[d]
    else:
        return None

def day_num(d):
    print(d)
    i = days.index(d)
    return i

def test_day_num():
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")

test_day_num()