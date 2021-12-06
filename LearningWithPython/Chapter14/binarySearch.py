# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/4/2021
# --------------------------------------------------------------------------

def binary_search(value, target):
    lb = 0
    up = len(value)

    while True:
        if lb == up:
            return -1
            
        middle = lb + ((up - lb) // 2)
        medium = value[middle]

        if medium == target:
            return medium
        if medium < target:
            lb = medium + 1
        if medium > target:
            up = medium

def bin_srch(nums, v):
    l, r = 0, len(nums)


def test_binary_search():
    xs = list(range(0, 251))
    # print(xs)
    i = binary_search(xs, 600)
    print(i)



if __name__ == "__main__":
    test_binary_search()