# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 3/22/2021
# --------------------------------------------------------------------------

import turtle
wn = turtle.Screen()

# Color of Background
n = input("Please choose a color for your background.")
wn.bgcolor(n)

# We can rename what the pop out tab is called
wn.title("Turbo Turtlez")


theo = turtle.Turtle()
taylor = turtle.Turtle()

# We colored the turtles
b = input("Please choose another color.")
g = input("Please choose one more color.")

theo.color(b)
taylor.color(g)

# We changed how big the turtles are
l = input("Pick a number.")
w = input("Pick another number.")

theo.pensize(l)
taylor.pensize(w)


theo.forward(100)
taylor.backward(100)

theo.left(90)
taylor.left(90)

theo.forward(150)
taylor.forward(150)

theo.left(90)
taylor.right(90)

theo.forward(90)
taylor.forward(90)

theo.left(180)
taylor.right(180)

theo.forward(180)
taylor.forward(180)


# Waits for the person using the computor to close the window
wn.mainloop()