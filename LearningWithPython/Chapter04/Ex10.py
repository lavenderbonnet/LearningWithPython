import turtle

def window():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("pretty pattern")
    return wn

def turtles():
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    return t

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.rt(144)

def draw_many_stars(t, n):
    """
    drawing stars in the shape of a star
    """
    for i in range(n):
        t.penup()
        t.forward(350)
        t.rt(144)
        t.pendown()
        draw_star(t)

def main():
    wn = window()
    t = turtles()
    draw_many_stars(t, 5)
    wn.mainloop()

main()