# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 10/24/2021
# --------------------------------------------------------------------------

# Write a function find_hypot which, given the length of 
# two sides of a right-angled triangle, returns the length 
# of the hypotenuse. 
# (Hint: x ** 0.5 will return the square root.)

def hypotenuse(x, y):
    """
    Returns hypotenuse of a right angle triangle given 2 sides
    """
    return ((x**2) + (y**2))**(0.5)
# --------------------------------------------------------------------------
def is_rightangled(x, y, z):
    h = hypotenuse(x, y)
    # if h == z:
    if abs(h-z) < 0.0001:
        print("True")
    else:
        print("False")
# --------------------------------------------------------------------------
def test_floating_point_errors():
    import math
    a = math.sqrt(2.0)
    print(a, a*a)
    print(a*a == 2.0)
# --------------------------------------------------------------------------
def main():
    x = float(input())
    y = float(input())
    z = float(input())
    print(hypotenuse(x, y))
    is_rightangled(x, y, z)
    # test_floating_point_errors()

main()

