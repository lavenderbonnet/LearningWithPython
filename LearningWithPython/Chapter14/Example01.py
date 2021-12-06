# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/4/2021
# --------------------------------------------------------------------------

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)



def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (index, value) in enumerate(xs):
        if value == target:
            return index
    return -1

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

test(search_linear(friends, "Zoe") == 1)
test(search_linear(friends, "Joe") == 0)
test(search_linear(friends, "Paris") == 6)
test(search_linear(friends, "Bill") == -1)