# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/18/2021
# --------------------------------------------------------------------------

import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def forwards():
    tess.forward(30)

def leftTurn():
    tess.left(45)

def rightTurn():
    tess.right(45)

def quitProgram():
    wn.bye()

wn.onkey(forwards, "Up")
wn.onkey(leftTurn, "Left")
wn.onkey(rightTurn, "Right")
wn.onkey(quitProgram, "q")

wn.listen()
wn.mainloop()