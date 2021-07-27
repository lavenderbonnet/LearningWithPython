# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 7/23/2021
# --------------------------------------------------------------------------

import turtle

def window():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("pretty pattern")
    return wn

def turtles(t):
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    return t

def draw_square(t):
    for i in range(4):
        t.forward(100)
        t.lt(90)

def rotate_figure(t):
    for i in range(20):
        t.lt(18)
        print(i)
        draw_square(t)

def main():
    wn = window()
    t = turtles("tess")
    rotate_figure(t)
    wn.mainloop()

if __name__ == "__main__":
    main()


