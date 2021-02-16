#Decimal to Binary

from math import floor

def decimal_to_binary(decimal):
    binary = []
    while decimal > 0:
        binary.append(decimal%2)
        decimal = floor(decimal/2)
    binary.reverse()
    return binary
        

decimal = input("Enter your decimal number or press space to exit ")
while decimal != " ":
    print(decimal_to_binary(int(decimal)))
    decimal = input("Enter your decimal number or press space to exit ")
print("byeBye!!")