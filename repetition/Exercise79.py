#Greatest Common Divisor

first_number = int(input("Enter the first number "))
second_number = int(input("Enter the second number "))

divisor = 0
if first_number <= second_number:
    divisor = first_number
else:
    divisor = second_number

count = divisor
while count > 0:
    if first_number % count == 0 and second_number % count == 0:
        print("The greatest common divisor of", first_number, "and", second_number, "is", count)
        break
    else:
        count -=1

        

