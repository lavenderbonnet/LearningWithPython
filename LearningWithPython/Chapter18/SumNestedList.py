# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 2/4/2021
# --------------------------------------------------------------------------

import sys

def recursion_sum(nested_num_list):
    total = 0
    for element in nested_num_list:
        if type(element) == type([]):
            total += recursion_sum(element)
        else:
            total += element
    
    return total


def r_max(nxs):
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e
        
        if first_time or val > largest:
            largest = val
            first_time = False
        
    return largest


def recursion_depth(number):
    print(f"{number}, ", end ="")
    recursion_depth(number + 1)


def fib(n):
    print("fibonacci", n)
    if n <= 1:
        return n

    fn_1 = fib(n - 1)
    print("out of fn_1")
    fn_2 = fib(n - 2)
    f = fn_1 + fn_2
    return f


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def main():
    # print(recursion_sum([9, 0, [5,[7,8], 6], 1]))

    # test(r_max([2, 9, [1, 13], 8, 6]) == 13)
    # test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    # test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    # test(r_max(["joe", ["sam", "ben"]]) == "sam")

    # recursion_depth(0)

    fib(3)

main()