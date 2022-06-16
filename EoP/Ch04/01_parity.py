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

# ----------------------------

def book_parity_01(x):
    result = 0
    while x:                # notice that x & 1 is not x ^ 1
        result ^= x & 1     # simplified version of result = result ^ (x & 1)
        x >>= 1             # removes the last digit from the binary string
        # print(result)
    
    return result

def book_parity_02(x):
    result = 0
    while x:
        result ^= 1         # XOR the 0/1 with 1
        x &= x - 1          # drops the lowest set bit of x
    
    return result

# ----------------------------

def main():
    x = 1000011011
    # total = num_of_ones(x)
    # print(parity(total))
    # book_parity_01(x)
    print(book_parity_02(x))

    

if __name__ == "__main__":
    main()