# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/6/2021
# --------------------------------------------------------------------------

import sys

def number_digits(n):
    counter = 0
    if n < 0:
        n = abs(n)
    # elif n == 0:
    #     return 1 
    while n != 0:
        digit = n % 10
        if digit == 3:
            counter = counter + 1
        n = n // 10
    return counter

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = f"Test on line number {linenum} passed."
    else:
        msg = f"Test on line number {linenum} failed."
    print(msg)

def test_num_digits():
    test(number_digits(123) == 1)
    test(number_digits(1234) == 1)
    test(number_digits(-1) == 0)
    test(number_digits(0) == 0)

def main():
    test_num_digits()

main()