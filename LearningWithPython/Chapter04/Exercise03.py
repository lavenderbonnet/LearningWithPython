# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 7/23/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("polygon")

def draw_poly(t, n, sz):
    t = turtle.Turtle()
    t.pensize(3)
    t.color("hotpink")
    t.speed(8)

    for i in range(n):
        t.forward(sz)
        t. lt(int(360/n))

def main():
    draw_poly("tess", 8, 50)
    wn.mainloop()

if __name__ == "__main__":
    main()

