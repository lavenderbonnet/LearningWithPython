# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/22/2021
# --------------------------------------------------------------------------

import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color()
tess.pensize(3)
tess.shape("circle")

def coordinates(x, y):
    tess.goto(x, y)
    wn.title(f"Got click at coords {x}, {y}")

wn.onclick(coordinates)
wn.mainloop()