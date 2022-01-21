# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/20/2022
# About : Adding a randomizer
# --------------------------------------------------------------------------


# diagonal checking
def share_diagonal(x1, y1, x2, y2):
    dis_x = abs(x2 - x1)
    dis_y = abs(y2 - y1)
    return dis_x == dis_y

v = share_diagonal(5, 2, 2, 0)
print(v)
v = share_diagonal(5, 2, 3, 0)
print(v)
v = share_diagonal(5, 2, 4, 3)
print(v)
v = share_diagonal(5, 2, 4, 1)
print(v)

print("--------------------------------")

def column_clashes(p, c):
    for i in range(c):
        if share_diagonal(i, p[i], c, p[c]):
            return True
    return False

clash = column_clashes([6, 4, 2, 0, 5], 4)
print(clash)
clash = column_clashes([6,4,2,0,5,7,1,3], 7)
print(clash)
clash = column_clashes([2,0,1,3], 1)
print(clash)
clash = column_clashes([0,1], 1)
print(clash)
clash = column_clashes([5,6], 1)
print(clash)
clash = column_clashes([6,5], 1)
print(clash)
clash = column_clashes([0,6,4,3], 3)
print(clash)
clash = column_clashes([5,0,7], 2)
print(clash)
clash = column_clashes([2,0,1,3], 2)
print(clash)

def has_clashes(board):
    for column in range(1, len(board)):
        if column_clashes(board, column):
            return True
    return False

def main():
    import random
    rng = random.Random()

    bd = list(range(8))
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print(f"Found solution {bd} in {tries} tries")
            tries = 0
            num_found += 1

if __name__ == "__main__":
    main()