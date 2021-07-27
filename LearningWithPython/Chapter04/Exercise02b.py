import turtle

def turtle_init():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("squares")
    return wn

def turtle_get_turtle():
    t = turtle.Turtle()
    t.pensize(3)
    t.color("hotpink")
    t.speed(8)
    return t

def turtle_draw_square(t, x, y, l):
    print(f'turtle :draw sq from ({x},{y}) of size {l}')
    # need to set turtle start point
    t.setposition(x,y)
    # turtle moves in 4 straight lines, turning 90 each time
    t.pendown()
    for i in range(4):
        t.forward(l)
        # turn 90 degrees
        t.lt(90)
    t.penup()

def draw_square(t, x, y, l):
    print(f'draw sq from ({x},{y}) of size {l}')
    turtle_draw_square(t, x,y,l)

def draw_n_enclosing_squares(t, n, len, diff):
    for i in range(n):
        # print(f"draw {i} squares")
        draw_square(t, -10*i, -10*i, 20*(i+1))

def main():
    print("main")
    w = turtle_init()
    t = turtle_get_turtle()
    draw_n_enclosing_squares(t, 10, 20, 20)
    # now we listen in the main loop
    w.mainloop()
    

if __name__ == "__main__":
    main()