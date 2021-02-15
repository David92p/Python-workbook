#Vowel or Consonant

letter = input('Enter your letter: ')

letter = letter.lower()

if letter == 'y':
    print(letter, 'This could be both a vowel and a consonant')
elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('This is a vowel')
else:
    print('This is a consonant')