# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/28/2021
# --------------------------------------------------------------------------

from random import Random

def make_random_integers(num, lb, ub):
    rng = Random()
    result = []
    for i in range(num):
        v = rng.randrange(lb, ub)
        result.append(v)

    return result

# print(make_random_integers(5, 1, 13))
# 5 = number of numbers going to be created
# 1 = the minimum the number can be
# 13 (actually 12) = the maximum the number can be






def make_random_integers_wo_dup(num, lb, ub):

    if ub-lb < num:
        raise Exception("Not enough numbers between the upper and lower bound")

    rng = Random()
    result = []
    for i in range(num):
        while True:
            number = rng.randrange(lb, ub)
            if number not in result:
                break
        result.append(number)
    return result

randomize = make_random_integers_wo_dup(10, 1, 6)
print(randomize)






def shuffle_months():
    rng = Random()
    months = list(range(1, 13))
    rng.shuffle(months)
    result = months[0:5]
    return result