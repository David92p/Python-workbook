#Compute a Grade Point Average of A, A+, A-, B, B+, B-, C, C+, C-, D, D+, F 

media = 0
total = 0

while True:
    letter = input('Enter the grade letter to calculate your average (press esc to exit) ')
    letter = letter.lower()
    if letter != 'esc':
        if letter == 'a' or letter == 'a+' or letter == 'a-':
            if letter == 'a' or letter == 'a+':
                media += 4.0
                total += 1
            elif letter == 'a-':
                media += 3.7
                total += 1
            continue
        if letter == 'b' or letter == 'b+' or letter == 'b-':
            if letter == 'b':
                media += 3.0
                total += 1
            elif letter == 'b+':
                media += 3.3
                total += 1
            elif letter == 'b-':
                media += 2.7
                total += 1
            continue
        if letter == 'c' or letter == 'c+' or letter == 'c-':
            if letter == 'c':
                media += 2.0
                total += 1
            elif letter == 'c+':
                media += 2.3
                total += 1
            elif letter == 'c-':
                media += 1.7
                total += 1
            continue
        if letter == 'd' or letter == 'd+':
            if letter == 'd':
                media += 1.0
                total += 1
            elif letter == 'd+':
                media+= 1.3
                total += 1
            continue
        if letter =='f':
            media += 0
            total += 1
            continue
    else:
        break

print('The total average of your grades is equal to', round(media/total,2))