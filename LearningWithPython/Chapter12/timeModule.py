# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/28/2021
# --------------------------------------------------------------------------

import timeit

def sum_all_num(list_of_num):
    sum = 0
    for n in list_of_num:
        sum += n
    return sum

def test_sum_all_num():
    n = 1*1000*1000
    testdata = range(n)
    my_result = sum_all_num(testdata)

time = timeit.timeit(test_sum_all_num, setup='', number=10)

print(time)
