# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 6/5/2022
# --------------------------------------------------------------------------

def num_of_ones(x):
    total = 0
    while x:
        if x & 1:
            total += 1
        x >>= 1

    return total

def parity(total):
    result = 0
    if total%2 == 1:
        result = 1

    return result

def main():
    x = 1000011010
    total = num_of_ones(x)
    print(parity(total))

if __name__ == "__main__":
    main()