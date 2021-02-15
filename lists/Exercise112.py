#Remove Outliers

def remove_outliers(myList):
    myList.sort()
    myList.pop(-1)
    myList.pop(-1)
    myList.pop(0)
    myList.pop(0)
    return myList

while True:
    numbers_list = []
    n = int(input('Enter your numbers, minimum 4 elements (press zero to exit)---> '))
    while n != 0:
        numbers_list.append(n)
        n = int(input('Enter your numbers, minimum 4 elements (press zero to exit)---> '))
    else:
        print(numbers_list)
        if len(numbers_list)<4:
            print('Enter at least 4 numeric elements')
            continue
        else:
            new_list = remove_outliers(numbers_list)
            print(new_list)
            break
