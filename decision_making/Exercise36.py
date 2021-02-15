#Dog Years

while True:
    human_year = input("Enter the years to convert \n")
    human_year = int(human_year)
    rest_year = human_year - 2

    if human_year == 1:
        print("\nYour dog is 10 years old")
    elif human_year == 2:
        print("\nYour dog is 21 years old")
    elif human_year > 2:
        result = 4 * rest_year + 21
        print("\nYour dog is",result, "years old")
    else:
        print("\nERROR: The number is not valid")

    loop = input("Do you want to perform another operation? YES - NO: ")
    loop = loop.lower()

    if loop == "yes":
        continue
    else:
        break

print('See you soon')
