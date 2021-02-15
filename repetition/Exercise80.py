#Prime Factors

while True:
    n = int(input('Enter an integer "2 or greater" '))
    factor = 2
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n /= factor
        else:
            factor += 1
    else:
        continue
