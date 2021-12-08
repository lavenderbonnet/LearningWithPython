# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/6/2021
# --------------------------------------------------------------------------


def test_merge():        
    xs = [1, 1, 1, 2, 3, 4, 4, 5, 6]
    ys = [5, 4, 3, 8, 6, 2, 5]

    xys = merge(xs, ys)
    print(xys)

def merge(xs, ys):
    xs.sort()
    ys.sort()

    px = 0
    py = 0
    result = []

    while True:
        if px >= len(xs):
            result.extend(ys[py:])
            break
        if py >= len(ys):
            result.extend(xs[px:])
            break
        if xs[px] > ys[py]:
            result.append(ys[py])
            py += 1
        else:
            result.append(xs[px])
            px += 1

    return result

if __name__ == "__main__":
    test_merge()