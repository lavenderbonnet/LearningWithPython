# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/6/2021
# --------------------------------------------------------------------------

import random
rng = random.Random()
number = rng.randrange(1, 100)

guesses = 0
msg = ""

while True:
    guess = int(input(msg + "\n Guess my number between 1 and 100: "))
    guesses += 1

    if guess > number:
        msg += str(guess) + " is too high. \n"
    elif guess < number:
        msg += str(guess) + " is too low. \n"
    else:
        break

input(f"\nYou got the answer in {guesses} guesses. \n")