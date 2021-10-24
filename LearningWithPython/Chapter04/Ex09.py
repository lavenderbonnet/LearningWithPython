import turtle

def window():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("pretty pattern")
    return wn

def turtles(t):
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    return t

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.rt(144)


def main():
    wn = window()
    t = turtles("tess")
    draw_star(t)
    wn.mainloop()

main()