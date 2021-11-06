# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/3/2021
# --------------------------------------------------------------------------

# Write a function to count how many odd numbers are in a list.

def counting_odds(l):
    no = 0
    for x in l:
        if x%2 != 0: no += 1
    return no

def counting_odds_lc(ll):
    odds = [x for x in ll if x % 2 != 0]
    return len(odds)

def main():
    ll = [2,3,4,5,6,7,8,101,103]
    no = counting_odds(ll)
    print(no)

    no2 = counting_odds_lc(ll)
    print(no2)

main()
