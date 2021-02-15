#The Collatz Conjecture

n = int(input('Enter your number '))
print(n)
while n != 1:
    if n % 2 == 0:
        n = n / 2 
        print(float(n))
        continue
    else:
        n = n*3 +1
        print(float(n))
        continue