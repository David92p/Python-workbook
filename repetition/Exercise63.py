#Average

sum = 0
divider = 0

while True:
    n = int(input('Enter the number and press "0" to calculate '))
    if n != 0:
        sum += n
        divider += 1
        continue
    else:
        break

average = sum / divider

print(round(average,2))
