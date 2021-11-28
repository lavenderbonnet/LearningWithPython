# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/23/2021
# --------------------------------------------------------------------------

import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling mouse clicks!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
alex = turtle.Turtle()
alex.color("blue")

alex.forward(100)

def handler_for_tess(x, y):
    wn.title(f"Tess clicked at {x}, {y}")
    tess.left(42)
    tess.forward(30)

def handler_for_alex(x, y):
    wn.title(f"Alex clicked at {x}, {y}")
    alex.right(84)
    alex.forward(50)

tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.mainloop()