# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 8/6/2021
# --------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

def area(radius):
    a = 3.14159 * radius**2
    return a

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result



