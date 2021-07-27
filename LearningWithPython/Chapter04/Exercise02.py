# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 7/23/2021
# --------------------------------------------------------------------------

import turtle

# Assignment: Write a program to draw squares in squares. 
# The innermost square is 20 units per side. Every square 
# boxing the previous is 20 units bigger per side.

def squaresize(t):
        for i in range(4):
            t.forward(20*i)
            t.lt(90)

def nextsquare(t):
    t.penup()
    t.rt(135)
    t.forward(10)
    t.lt(45)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("squares")

t = turtle.Turtle()
t.color("hotpink")
t.pensize(3)

for i in range(5):
    squaresize(t)
    nextsquare(t)

wn.mainloop()
