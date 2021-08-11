# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 8/3/2021
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

def test_day_name():
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

test_day_name()