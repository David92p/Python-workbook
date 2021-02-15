#What Color Is That Square?

while True:
    letter = input('Enter the game letter from "A" ad "H" ' )
    number = int(input('Enter the game number from "1" a "8" '))
    letter = letter.upper()
    if letter == 'A' or letter == 'C' or letter == 'E' or letter == 'G':
        if number%2 == 0:
            print('The box', letter, number, 'is white')
            continue
        else:
            print('The box', letter, number, 'is black')
            continue
    if letter == 'B' or letter == 'D' or letter == 'F' or letter == 'H':
        if number%2 == 0:
            print('The box', letter, number, 'is black')
            continue
        else:
            print('The box', letter, number, 'is white')
            continue
    