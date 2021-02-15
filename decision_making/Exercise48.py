#BirthDate toAstrological Sign

month = input('Enter the month ---> ')
month = month.lower()
day = input('Enter the day ---> ')
day = int(day)

if month == 'december':
    if day <= 21:
        print('you are a Sagittarius')
    else:
        print('you are a Capricorn')
elif month == 'january':
    if day <= 19:
        print('you are a Capricorn')
    else:
        print('you are an Aquarius')
elif month == 'february':
    if day <= 18:
        print('you are an Aquarius') 
    else:
        print('you are a Pisces')
elif month == 'march':
    if day <= 20:
        print('you are a Pisces')
    else:
        print('you are a Aries')
elif month == 'april':
    if day <= 19:
        print('you are a Aries')
    else:
         print('you are a Taurus')
elif month == 'may':
    if day <= 20:
        print('you are a Taurus')
    else:
        print('you are a Gemini')
elif month == 'june':
    if day <= 20:
        print('you are a Gemini')
    else:
        print('you are a Cancer')
elif month == 'july':
    if day <= 22:
        print('you are a Cancer')
    else: 
        print('you are a Leo')
elif month == 'august':
    if day <= 22:
        print('you are a Leo')
    else:
        print('you are a Virgo')
elif month == 'september':
    if day <= 22:
        print('you are a Virgo')
    else:
        print('you are a Libra')
elif month == 'october':
    if day <= 22:
        print('you are a Libra')
    else:
        print('you are a Scorpio')
elif month == 'november':
    if day <= 21:
        print('you are a Scorpio')
    else:
        print('you are a Sagittarius')