#List of Proper Divisors

def dividers(element):
    list_div = []
    div = 0
    while div != 1:
        for n in range(2,element+1,1):
            if element % n == 0:
                div = element / n
                list_div.append(int(div))
        element = div
    return(list_div)

if __name__== "__main__":
    while True:
        numbers = []
        number = int(input('Enter your number '))
        if number >= 2:
            numbers=dividers(number)
            print(numbers)
        else:
            print('Enter a number equal two or up')




