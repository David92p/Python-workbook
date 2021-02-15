#Letter Grade to Grade Points

letter = input('Insert the letter to calculate your vote ')
letter =  letter.lower()

if letter == 'a' or letter == 'a+' or letter == 'a-':
    if letter == 'a+' or letter == 'a':
        print('letter', letter, ' grade points 4.0')
    elif letter == 'a-':
        print('letter', letter, ' grade points 3.7')
elif letter == 'b' or letter == 'b+' or letter == 'b-':
    if letter == 'b+':
        print('letter', letter, ' grade points 3.3')
    elif letter == 'b-':
        print('letter', letter, ' grade points 2.7')
    elif letter == 'b':
        print('letter', letter, ' grade points 3.0')
elif letter == 'c' or letter == 'c+' or letter == 'c-':
    if letter == 'c+':
        print('letter', letter, ' grade points 2.3')
    elif letter == 'c-':
        print('letter', letter, ' grade points 1.7')
    elif letter == 'c':
        print('letter', letter, ' grade points 2.0')
elif letter == 'd' or letter == 'd+':
    if letter == 'd+':
        print('letter', letter, ' grade points 1.3')
    elif letter == 'd':
        print('letter', letter, ' grade points 1.0')
elif letter == 'f':
    print('letter', letter, ' grade points 0')
else:
    print('you entered incorrect data')