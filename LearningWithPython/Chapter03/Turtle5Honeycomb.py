# --------------------------------------------------------------------------
# Author : Lilac Walia   (with Pranali)
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


# First Honey Comb

for v in range(6):
    
    honey.forward(60)
    honey.left(60)


# Second Layer

for v in range (6):
    
    honey.right(120)
    
    for v in range(5):
        honey.forward(60)
        honey.right(60)


# First Hexagon of Third

honey.right(120)
honey.forward(60)
honey.right(60)
honey.forward(60)

for v in range(4):
    
    honey.left(60)
    honey.forward(60)

honey.right(180)
honey.forward(60)

# Second Hexagon of Third

honey.left(60)
honey.forward(60)

for v in range(3):
    
    honey.left(60)
    honey.forward(60)

honey.right(180)


# Rest of third

for v in range(5):
    
    for v in range(4):
        honey.forward(60)
        honey.left(60)
    
    honey.left(120)
    
    for v in range(5):
        honey.forward(60)
        honey.left(60)
    
    honey.left(120)



wn.mainloop()