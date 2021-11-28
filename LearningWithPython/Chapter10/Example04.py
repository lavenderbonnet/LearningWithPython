# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/23/2021
# --------------------------------------------------------------------------

import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def tess_movement():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(tess_movement, 60)

tess_movement()
wn.mainloop()