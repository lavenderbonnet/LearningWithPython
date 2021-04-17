# --------------------------------------------------------------------------
# Author : Lilac Walia   (with Pranali)
# Date : 4/6/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()

wn.bgcolor("red2")
wn.title("Pocky Stick")


breadstick = turtle.Turtle()
breadstick.color("peach puff")
breadstick.pensize(10)

chocolate = turtle.Turtle()
chocolate.color("chocolate4")
chocolate.pensize(15)


# Drawing the pocky
breadstick.right(90)
breadstick.forward(80)

chocolate.left(90)
chocolate.forward(300)



wn.mainloop()