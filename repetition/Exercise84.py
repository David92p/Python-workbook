#Coin Flip Simulation

from random import randint

total = []
H = 0
T = 0
while H < 3 and T < 3:
    n = randint(1,10)
    if n % 2 == 0:
        total.append("H")
        H += 1
        T = 0
    elif n % 2 == 1:
        total.append("T")
        T += 1
        H = 0

print(f"Your score is equal to {total}")
print(f"To generate 3 equals symbols you are need {len(total)} shoots")