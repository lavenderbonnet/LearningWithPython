# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 4/6/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()

wn.bgcolor("orange2")
wn.title("Honeycomb")


honey = turtle.Turtle()
honey.color("LightGoldenrod")
honey.pensize(10)


# Drawing the hexagon

honey.speed(0)

for v in range(6):
    honey.forward(60)
    honey.left(60)

for v in range (6):
    honey.right(120)
    for v in range(5):
        honey.forward(60)
        honey.right(60)

honey.right(120)
honey.forward(60)
honey.right(60)
honey.forward(60)

for v in range(4):
    honey.left(60)
    honey.forward(60)

honey.right(180)
honey.forward(60)

honey.left(60)
honey.forward(60)

for v in range(3):
    honey.left(60)
    honey.forward(60)

honey.right(180)

honey.color("limegreen")

for v in range(5):
    for v in range(4):
        honey.forward(60)
        honey.left(60)
    honey.left(120)
    for v in range(5):
        honey.forward(60)
        honey.left(60)


wn.mainloop()