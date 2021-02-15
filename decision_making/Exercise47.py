#Season from Month and Day

month = input('Enter the month ---> ')
month = month.lower()
day = input('Enter the day ---> ')
day = int(day)


if month == 'April' or month == 'may':
    print(month, day, 'is the time of spring')
elif month == 'july' or month == 'august':
    print(month, day, 'is the time of summer')
elif month == 'october'or month == 'november':
    print(month, day, 'is the time of fall')
elif month == 'january' or month == 'february':
    print(month, day, 'is the time of winter')
elif month == 'march' and day < 20:
    print(month, day, 'is the time of winter')
elif month == 'march' and day >= 20:
    print(month, day, 'is the time of spring')
elif month == 'june' and day < 21:
    print(month, day, 'is the time of spring')
elif month == 'june' and day >= 21:
    print(month, day, 'is the time of summer')
elif month == 'september' and day < 22:
    print(month, day, 'is the time of summer')
elif month == 'september' and day >= 22:
    print(month, day, 'is the time of fall')
elif month == 'december' and day < 21:
    print(month, day, 'is the time of fall')
elif month == 'december' and day >= 21:
   print(month, day, 'is the time of winter')