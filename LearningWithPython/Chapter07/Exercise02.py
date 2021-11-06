# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/3/2021
# --------------------------------------------------------------------------

# Sum up all the even numbers in a list

def sum_evens(ll):
    evens = [x for x in ll if x % 2 == 0]
    return sum(evens)

def main():
    ll = [2, 3, 4, 5, 6]
    evens = sum_evens(ll)
    print(evens)

main()