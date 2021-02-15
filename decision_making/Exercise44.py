#Faces onMoney

while True:
    value = input('Enter the banknote denomination or press esc to exit ---> ')
    value = value.lower()
    if value == "1":
        print('George Washington $ 1')
        continue
    elif value == "2":
        print('Thomas Jefferson $ 2')
        continue
    elif value == "5":
        print('Abraham Lincoln $ 5')
        continue
    elif value == '10':
        print('Alexander Hamilton $10')
        continue
    elif value == '20':
        print('Andrew Jackson $20')
        continue
    elif value == '50':
        print('Ulysses S. Grant $50')
        continue
    elif value == '100':
        print('Benjamin Franklin $100')
        continue
    elif value == "esc":
        break
    else:
        print("Type of banknote not recognized")
        continue

print('See you soon')