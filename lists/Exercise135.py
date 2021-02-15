#The Sieve of Eratosthenes

limit = input("Enter the limit of your prime numbers ")
limit = int(limit)
list_numbers = []
prime_numbers = []
for i in range(0,limit+1):
    list_numbers.append(i)
list_numbers[1] = 0

p = 2
while p < limit:
    for n in range(p*2,limit+1,p):
        list_numbers[n] = 0
    p += 1
for i in range(2,limit+1):
    if list_numbers[i] != 0:
        prime_numbers.append(list_numbers[i])

print(prime_numbers)

