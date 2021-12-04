# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/30/2021
# --------------------------------------------------------------------------

days = ["sun", "mon", "tues", "wed", "thur", "fri", "sat"]

def get_day_of_the_week(n):
    if 1 <= n <= 7:
        return days[n-1]
    else:
        raise ValueError("Days can be only between 1 and 7")

def test_weekdays():
    for i in range(1,8):
        print(get_day_of_the_week(i))

if __name__ == "__main__":
    test_weekdays()