# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 10/24/2021
# --------------------------------------------------------------------------

import turtle

def window():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("bar graph")
    return wn

def turtles(t):
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(8)
    return t

def set_color_by_height(t, height):
    if height >= 200:
        t.color("red")
    elif 100 <= height < 200:
        t.color("yellow")
    else:
        t.color("green")

def draw_bar(t, height):
    set_color_by_height(t, height)
    t.begin_fill()
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.write('    ' + str(height))  # Writes #s at the top
    t.right(90)
    t.forward(40)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.end_fill()
    t.penup()
    t.forward(10)         # Leave small gap after each bar
    t.pendown()


bargraph = [48, 117, 200, 240, 160, 260, 220]

def main():
    wn = window()
    t = turtles("toppsy")
    for v in bargraph:
        draw_bar(t, v)
    wn.mainloop()

if __name__ == "__main__":
    main()
