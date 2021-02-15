#Fizz-Buzz

count = 0
while True:
    if count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print('FiZZ-BuuZZZZzzZZ!!!')
            count += 1
        elif count % 3 == 0:
            print('FiiZzzZZz!!!')
            count += 1
        elif count % 5 == 0:
            print('BuuuZzzZz!!!')
            count += 1
        else:
            print(count)
            count += 1   
    else:
        break

    
    