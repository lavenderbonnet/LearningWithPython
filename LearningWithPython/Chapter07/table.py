# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/6/2021
# --------------------------------------------------------------------------

def table():
    for x in range(13):
        print(x, "\t", 2**x)

def two_table(n, m):
    for i in range(1, m + 1):
        print(n*i, end="   ")
    print()

def multiple_tables(n, m):
    for i in range(1, n + 1):
        two_table(i, m)

def main():
    # table()
    multiple_tables(20, 20)

main()