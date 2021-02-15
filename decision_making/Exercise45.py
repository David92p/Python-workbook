#Date to Holiday Name

while True:
    day = input('Enter the Day ---> ')
    month = input('Enter the month ---> ')
    month =  month.lower()
    if day == '1' and month == 'january':
        print("New Year’s Day")
        continue
    elif day == '1' and month == 'july':
        print('Canada Day')
        continue
    elif day == '25' and month == 'december':
        print('Christmas Day')
        continue
    else:
        print('Not known holiday')
        break

    