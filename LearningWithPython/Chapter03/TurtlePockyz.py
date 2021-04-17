# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 4/17/2021
# --------------------------------------------------------------------------


import turtle

def create_screen():
    screen = turtle.Screen()
    screen.bgcolor("red2")
    screen.title("Pockeyzzzzzzzzzzzzzzzz")
    return screen
# create_screen end


def vertical(pen, speed, length, thickness, color):
    pen.lt(90)
    horizontal(pen, speed, length, thickness, color)

def horizontal(pen, speed, length, thickness, color):
    pen.shape("blank")

    pen.color(color)
    pen.speed(speed)

    pen.pensize(thickness)
    pen.fd(length) # same as forward
# draw_line end

def draw_pocky(x ,y, angle):
    t = turtle.Turtle()
    t.speed(0)
    # send to start position
    t.penup()
    t.goto(x,y)
    t.pendown()
    # now we draw the pocky
    t.rt(angle)
    horizontal(t, 10, 40, 6, "peach puff")
    horizontal(t, 10, 150, 9, "chocolate4")

def circle(angle, x,y):
    for v in range(360//angle):
        draw_pocky(x,y, v*angle)

def main():

    # create screen
    s = create_screen()
    
    # pockys
    circle(10, 300, 0)
    circle(10, -300, 0)
    circle(10, 0, 300) 
    circle(10, 0, -300)

    # show on screen
    s.mainloop()

main()

