# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 4/17/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()

wn.bgcolor("red2")
wn.title("Pocky Stickz")

# The turtles
b = turtle.Turtle()
b.shape("blank")
b.pensize(10)
b.color("peach puff")
b.speed(10)

c = turtle.Turtle()
c.shape("blank")
c.pensize(15)
c.color("chocolate4")
c.speed(10)

# Starts at very left
b.penup()
c.penup()

b.backward(300)
c.backward(300)

b.pendown()
c.pendown()

for v in range(15):
    # Drawing the pocky
    b.right(90)
    b.forward(80)
    b.left(90)
    
    c.left(90)
    c.forward(300)
    c.right(90)
    
    # Moving the next one
    b.penup()
    c.penup()
    
    b.forward(20)
    c.forward(20)
    
    b.pendown()
    c.pendown()
    
    # Drawing the second one
    b.right(90)
    b.backward(80)
    b.left(90)
    
    c.left(90)
    c.backward(300)
    c.right(90)
    
    # Moving the next one
    b.penup()
    c.penup()

    b.forward(20)
    c.forward(20)
    
    b.pendown()
    c.pendown()

wn.mainloop()