#Maximum Integer

from random import randint

n = []
for i in range(100):
    x = randint(1,100)
    n.append(x)
print(n)

count = n[0]
step = 0
for i in range(len(n)):
    if n[i] > count:
        step += 1
        count = n[i]
print(count)
print(step)
