# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 7/22/2021
# --------------------------------------------------------------------------

import turtle

# Assignment: Write a void (non-fruitful) function 
# to draw a square. Use it in a program to draw the 
# image shown below. Assume each side is 20 units. 

def squares(t):
    for x in range(4):
        t.forward(20)
        t.lt(90)
    t.penup()
    t.forward(40)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("squares")

t = turtle.Turtle()
t.color("hotpink")
t.pensize(3)

for x in range(5):
    squares(t)

wn.mainloop()
