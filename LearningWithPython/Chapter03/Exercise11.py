# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 4/25/2021
# --------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.title("Starry Skies")

star = turtle.Turtle()
star.color("Gold")
star.pensize(5)


for v in range(5):
    star.fd(100)
    star.rt(144)



wn.mainloop()