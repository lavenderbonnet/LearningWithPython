# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/30/2021
# --------------------------------------------------------------------------

import weekdays

def tell_me_the_day(n):
    return weekdays.get_day_of_the_week(n)


def test_days():
    for i in range(1,8):
        print(tell_me_the_day(i))


if __name__ == "__main__":
    test_days()