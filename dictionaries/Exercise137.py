#Two Dice Simulation

from random import randint

def two_dice():
    count1 = randint(1,6)
    count2 = randint(1,6)
    count3 = count1 + count2
    return count3

counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for i in range(1000):
    n = two_dice()
    counts[n] += 1
print(counts)

