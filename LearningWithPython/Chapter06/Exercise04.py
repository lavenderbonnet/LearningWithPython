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



def vacation(d,n):
    
    n % 7
    pass