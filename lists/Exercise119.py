#Below and Above Average

list_numbers = []
while True:
    number = input('Enter your number (blank to quit): ')
    if number != " ":
        list_numbers.append(int(number))
    else:
        break

media_number = sum(list_numbers)/len(list_numbers)
print(f'media of your values is {round(media_number)}')

lower = []
higher = []
media_numbers = []
for i in list_numbers:
    if i < media_number:
        lower.append(i)
    elif i > media_number:
        higher.append(i)
    else:
        media_numbers.append(i)

print(f"Lower than media numbers are {lower}")
print(f'Greater than media numbers are {higher}')
if len(media_numbers) > 0:
    print(f"Equal to the media numbers{media_numbers}")