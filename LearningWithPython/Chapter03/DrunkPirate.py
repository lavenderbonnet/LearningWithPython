import turtle

def pirate_walk(directions):

    print("pirate walk!")

    # screen
    sc = turtle.Screen()
    sc.bgcolor('blue')
    pirate_ship = '.\Python\LearningWithPython\Chapter03\pirate_ship2_sm.gif'
    sc.register_shape(pirate_ship)

    # pirate
    p = turtle.Turtle()
    p.shape(pirate_ship)
    p.width(5)
    p.color("lightblue")

    # walk
    drunken_moves(p, directions)

    sc.mainloop()

def drunken_moves(p, directions):
    for d in directions:
        p.forward(100)
        p.left(d)

def main():
    d = [160, -43, 270, -97, -43, 200, -940, 17, -86]
    pirate_walk(d)

main()