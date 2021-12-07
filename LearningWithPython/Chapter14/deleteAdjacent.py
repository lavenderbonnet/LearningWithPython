# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/5/2021
# --------------------------------------------------------------------------

def test_delete_adjacent_dup():
    xs = [2, 3, 3, 4, 5, 6, 6]
    print(xs)
    l = delete_adjacent_dup(xs)
    print(xs)
    print(l)

def delete_adjacent_dup(xs):
    print(xs)
    new_xs = []
    prev_ele = None
    for e in xs:
        if e != prev_ele:
            new_xs.append(e)
            prev_ele = e

    return new_xs

if __name__ == "__main__":
    test_delete_adjacent_dup()