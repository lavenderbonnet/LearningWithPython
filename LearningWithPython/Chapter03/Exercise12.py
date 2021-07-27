# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 6/20/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

clock = turtle.Turtle()
clock.shape("turtle")
clock.color("blue")

def start():
    clock.penup()
    clock.goto(0,0)
    clock.stamp()

def line():
    clock.forward(120)
    clock.pendown()
    clock.stamp()

for i in range(12):
    start()
    clock.left(30)
    line()


wn.mainloop()