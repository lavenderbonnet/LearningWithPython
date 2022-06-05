# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 6/5/2022
# --------------------------------------------------------------------------

def count_ones(x):
    count = 0
    while x:
        # print(bin(x))
        if x & 1:
            count += 1
        x >>= 1
    return count

def main():
    x = 1145674567456876567876
    print(count_ones(x))

if __name__ == "__main__":
    main()