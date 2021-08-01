# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 7/27/2021
# --------------------------------------------------------------------------

import turtle

def window():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("triangle")
    return wn

def turtles(t):
    t = turtle.Turtle()
    t.pensize(3)
    t.color("hotpink")
    t.speed(8)
    return t

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.lt(int(360/n))

def draw_equitriangles(t, sz):
    draw_poly(t, 3, sz)

def main():
    wn = window()
    t = turtles("toppsy")
    draw_equitriangles(t, 50)
    wn.mainloop()

if __name__ == "__main__":
    main()




