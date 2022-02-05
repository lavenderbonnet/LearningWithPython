# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 2/2/2021
# --------------------------------------------------------------------------

import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
    
def koch_2(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)


def main():
    wn = turtle.Screen()
    wn.bgcolor = "green"

    t = turtle.Turtle()
    t.speed = 0
    t.setx(-450)

    koch_2(t, 3, 900)

    wn.mainloop()


main()