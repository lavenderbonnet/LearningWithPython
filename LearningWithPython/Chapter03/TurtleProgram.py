# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 3/22/2021
# --------------------------------------------------------------------------

# Allows us to use turtles
import turtle

# Creats a "playground" for turtles
wn = turtle.Screen()

# We can color the playground
wn.bgcolor("peach puff")

# We can rename what the pop out tab is called
wn.title("Turbo Turtlez")



# We created turtles
alex = turtle.Turtle()
alan = turtle.Turtle()
ally = turtle.Turtle()

# We colored the turtles
alex.color("blue")
alan.color("red")
ally.color("purple")

# We changed how big the turtles are
alex.pensize(3)
alan.pensize(5)
ally.pensize(10)



# Tells alex and alan to move forward by 50 units
alex.forward(50)
alan.backward(50)

# Tells alex and alan to make a 90 degree turn
alex.left(90)
alan.right(90)

# Complete the second side of a rectangle
alex.forward(30)
alan.forward(30)



# Completeing the rectangles

alex.left(90)
alan.left(90)

alex.forward(50)
alan.forward(50)

alex.left(90)
alan.left(90)

alex.forward(30)
alan.forward(30)


# ally tries to make a shaded box

ally.left(45)
ally.forward(70)
ally.left(135)
ally.forward(20)


# Dunno how to loop/repeat yet soooooo 
# cooooooopy & paste

ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)

ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)
ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)
ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)
ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)
ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)
ally.right(90)
ally.forward(10)
ally.right(90)
ally.forward(20)
ally.left(90)
ally.forward(10)
ally.left(90)
ally.forward(20)



# Waits for the person using the computor to close the window
wn.mainloop()