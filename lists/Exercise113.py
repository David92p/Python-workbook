#Avoiding Duplicates

words = []
my_word = input('Enter your word or press space to exit ')
while my_word != ' ':
    if my_word not in words:
        words.append(my_word)
    my_word = input('Enter your word or press space to exit ')

for element in words:
    print(element)

    

