# --------------------------------------------------------------------------
# Author : Lilac Walia   (with Pranali)
# Date : 4/6/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()

wn.bgcolor("red2")
wn.title("Pocky Stick")

# You can change the color of the turtles!!!

breadstick = turtle.Turtle()
breadstick.color("red2")
breadstick.pensize(10)

chocolate = turtle.Turtle()
chocolate.color("red2")
chocolate.pensize(15)

# Starts at very right
breadstick.forward(300)
chocolate.forward(300)

# Change the color back
breadstick.color("peach puff")
chocolate.color("chocolate4")

# Drawing the pocky
breadstick.right(90)
breadstick.forward(80)
breadstick.right(90)

chocolate.left(90)
chocolate.forward(300)
chocolate.left(90)

# Making it move to the next
breadstick.color("red2")
chocolate.color("red2")

breadstick.forward(50)
chocolate.forward(50)


# Change the color back
breadstick.color("peach puff")
chocolate.color("chocolate4")

# Drawing the pocky
breadstick.right(90)
breadstick.forward(80)
breadstick.right(90)

chocolate.left(90)
chocolate.forward(300)
chocolate.right(90)


wn.mainloop()