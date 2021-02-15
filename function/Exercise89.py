#Convert an Integer to Its Ordinal Number

number = int(input('Enter the number between 1 to 12 '))

def ordinal_number(int):
    if int == 1:
        print('1 ---> Firts')
    elif int == 2:
        print('2 ---> Second')
    elif int == 3:
        print('3 ---> Third')
    elif int == 4:
        print('4 ---> Fourth')
    elif int == 5:
        print('5 ---> Fourth')
    elif int == 6:
        print('6 ---> Sixth')
    elif int == 7:
        print('7 ---> Seventh')
    elif int == 8:
        print('8 ---> Eigth')
    elif int == 9:
        print('9 ---> Nineth')
    elif int == 10:
        print('10 ---> Tenth')
    elif int == 11:
        print('11 ---> Eleventh')
    elif int == 12:
        print('12 ---> Twelfth')
    else:
        print('Wrong number')

ordinal_number(number)


