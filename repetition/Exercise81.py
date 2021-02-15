#Binary to Decimal

def binary_to_decimal(binary):
    count = 0
    index = len(binary)-1
    total = 0
    while index >= 0:
        total += int(binary[index]) * (2**count)
        index -= 1
        count += 1
    return total 



n = input("Enter the binary number: ")

print(binary_to_decimal(n))



