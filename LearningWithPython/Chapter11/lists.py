# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/26/2021
# --------------------------------------------------------------------------

# clubs
clubs = ['chess', 'math', 'programming', 'makeup', 'kpop']
for c in clubs:
    print(c)

# list initializer
zeroes = [0] * 5
for z in zeroes:
    print(z)

# slice
math_clubs = clubs[1:3]
for nc in math_clubs:
    print(nc)

# mutable
clubs[0] = 'hulahoops'
for c in clubs:
    print(c)

clubs[0:2] = "baking", "chinese"
for c in clubs:
    print(c)

clubs[1:3] = []
for c in clubs:
    print(c)

clubs[4:4] = ["skating", "french"]
for c in clubs:
    print(c)

print("--------------------------------")

friends = ["Sally", "Sam", "Jack"]
for f in friends:
    print(f)
for (i, f) in enumerate(friends):
    print(i, f)


def double_stuff(random_list):
    for (idx, n) in enumerate(random_list):
        random_list[idx] = 2*n

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
double_stuff(numbers)
print(numbers)