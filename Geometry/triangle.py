# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/2/2022
# --------------------------------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return ( (self.x - x) **2 + (self.y - y)**2 ) ** 0.5
    
    def distance_from_origin(self):
        return self.distance(0, 0)

    # def print(point):
    #     print(f"({point.x},{point.y})")

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def midpoint(p1, p2):
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        return Point(mx, my)
    
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def distance_from_point(self, p):
        return self.distance(p.x, p.y)
    
#----------------------------------------------------------------------
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return f"({self.p1}, {self.p2}, {self.p3})"
    
    def length_sides(self):
        a = self.p1.distance_from_point(self.p2)
        b = self.p2.distance_from_point(self.p3)
        c = self.p3.distance_from_point(self.p1)
        return (a,b,c)

    def is_equilateral(self):
        a, b, c = self.length_sides()
        return a == b and b == c
    
    def is_isoceles(self):
        a, b, c = self.length_sides()
        return a == b or b == c or c == a

    def is_right_triangle(self):
        sides = self.length_sides()
        sorted_sides = sorted(sides)

        # after sorting
        # c has to be bigger or equal to a and b
        a, b, c = sorted_sides
        
        return a**2+b**2 == c**2

    def area(self):
        # use heron's formula
        a, b, c = self.length_sides()
        # semi perimeter
        s = ( a + b + c ) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area

#-------------------------------------------------------------

def test_equilateral_triangle():
    p1 = Point(0, 0)
    p2 = Point(6, 0)
    p3 = Point(3, 3*(3**0.5))

    t = Triangle(p1, p2, p3)
    print("All sides are same." if t.is_equilateral() else "Not an equliateral.")
    print(f"Area of triangle is {t.area()}")

def test_isoceles():
    p1 = Point(0, 6)
    p2 = Point(3, 0)
    p3 = Point(-3, 0)

    t = Triangle(p1, p2, p3)
    print("It's an isoceles triangle." if t.is_isoceles() else "Not an isoceles triangle.")
    print(f"The area is {t.area()}")

def test_right_triangle():
    p1 = Point(0, 0)
    p2 = Point(0, 3)
    p3 = Point(4, 0)

    t = Triangle(p1, p2, p3)
    print("Is a right triangle" if t.is_right_triangle() else "Not a right triangle")
    print(f"The area is {t.area()}")

def test_triangles():
    test_equilateral_triangle()
    test_isoceles()
    test_right_triangle()

if __name__ == "__main__":
    test_triangles()
