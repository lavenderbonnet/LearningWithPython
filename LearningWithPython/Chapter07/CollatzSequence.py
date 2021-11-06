# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/3/2021
# --------------------------------------------------------------------------

import sys

#  The Collatz 3n + 1 sequence
def seq3np1(n):
    """
    This is called a docstring. It works as a 
    comment for a function and the author of the 
    program is supposed to write what the program 
    does in this.

    This program is about the Collatz 3n + 1 Sequence.
    We want to print the 3n+1 sequence from n.
    terminating it when it reaches 1.
    """
    l = []
    while n != 1: # while n doesn't equal 1
        l.append(n)
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
    l.append(n)
    print(n, end="\n")
    return l

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def test_suite_seq3np1():
    test(seq3np1(2) == [2, 1])
    # print(seq3np1(5))
    test(seq3np1(5) == [5, 16, 8, 4, 2, 1])
    # test(seq3np1(12) == 1)
    # test(seq3np1(1000000) == 1)
    # test(seq3np1(209372843) == 1)
    # test(seq3np1(-20) == 1)

def main():
    test_suite_seq3np1()

main()