# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/28/2021
# --------------------------------------------------------------------------

import random

rng = random.Random(3)
# rng stands for random number generator

for n in range(1,100):
    dice_throw = rng.randrange(1, 7) # doesn't actually include 7
    delay_in_seconds = rng.random() # * 5.0 [0,1)

    # print(dice_throw)
    print(delay_in_seconds)

n = 1000001
histogram = [0] * 10
for i in range(1,n):
    # uniform distribution
    v = rng.randrange(100)
    histogram[v//10] = histogram[v//10] + 1

    # bell curve distribution
    v = int(rng.normalvariate(50,10))
    histogram[v//10] = histogram[v//10] + 1
    print(v)

print(histogram)


# SHUFFLE CARDS
colors = ['\u2660', '\u2665', '\u2666', '\u2663']
cards = []

for c in colors:
  for i in range(1,14):
      cards.append((c,i))

print(cards)
# shuffle the cards
rng.shuffle(cards)
print(cards[:10])