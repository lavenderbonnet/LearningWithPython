# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/7/2021
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