# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 7/26/2021
# --------------------------------------------------------------------------

import turtle

def window():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("spiral")
    return wn

def turtles(t):
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(1)
    t.speed(0)
    return t

def spiral(t):
    for i in range(100):
        t.forward(2*i)
        t.rt(90)

def turning_spiral(t):
    for i in range(100):
        t.forward(2*i)
        t.rt(90-1)


def main():
    wn = window()
    t = turtles("toppsy")
    # spiral(t)
    turning_spiral(t)
    wn.mainloop()

if __name__ == "__main__":
    main()

