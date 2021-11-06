# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/06/2021
# --------------------------------------------------------------------------


import sys

def cal_distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    r = ((x**2)+(y**2))**(1/2)
    return r

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = f"Test on line number {linenum} passed."
    else:
        msg = f"Test on line number {linenum} failed."
    print(msg)

def test_cal_distance():
    test(cal_distance(0, 0, 3, 4) == 5.0)
    test(cal_distance(1, 1, 1, 2) == 1.0)
    test(cal_distance(3, 5, 0, 5) == 3.0)

def main():
    test_cal_distance()

main()