# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/7/2021
# --------------------------------------------------------------------------

class Line:
    def Line(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def Lenght(self, p1, p2):
        px = (p2.x - p1.x)**2
        py = (p2.y - p1.y)**2
        (px + py)**(1/2)