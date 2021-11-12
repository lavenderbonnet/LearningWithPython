# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/11/2021
# --------------------------------------------------------------------------

# fruit = "banana"
# count = 0
# for char in fruit:
#     if char == "a":
#         count += 1
# print(count)

def count_letters(string, letter):
    count = 0
    str(letter)
    str(string)
    for char in string:
        if char == letter:
            count += 1
    return count

def main():
    print(count_letters("banana", "a"))

main()