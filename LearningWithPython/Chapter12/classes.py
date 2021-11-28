# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/27/2021
# --------------------------------------------------------------------------

class Human:
    def __init__(self, name, dob, height, weight):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} {self.height}"


def make_human():
    lw = Human('Lilac', '12/10/2007', '5ft6in', '120lbs')
    print(lw)

def main():
    make_human()

main()
