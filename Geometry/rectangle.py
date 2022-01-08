# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/2/2022
# --------------------------------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h
    
    def __str__(self):
        return f"({self.corner}, {self.width}, {self.height})"

    def area(self):
        area = self.width * self.height
        return area
    
    def perimeter(self):
        perimeter = (2*self.width) + (2*self.height)
        return perimeter
    
    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
    
    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy


def test_points():
    box = Rectangle(Point(0, 0), 100, 200)
    bomb = Rectangle(Point(100, 80), 5, 10)
    print("box: ", box)
    print("bomb: ", bomb)

def test_changing_rectangles():
    r = Rectangle(Point(10, 5), 100, 50)
    r = r.grow(25, -10)
    print(r)
    r = r.move(-10, 10)
    print(r)

def test_move():
    r = Rectangle(Point(10, 5), 100, 50)
    r.move(-10, 10)

def test_rectangles():
    test_points()
    test_changing_rectangles()

if __name__ == "__main__":
    test_rectangles()