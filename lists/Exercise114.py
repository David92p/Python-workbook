#Negatives,Zeros and Positives

numbers_min = []
numbers_0 = []
numbers_max = []
my_number = input('Enter your number or press space to exit ')
while my_number != ' ':
    if int(my_number) < 0:
        numbers_min.append(int(my_number))
    elif int(my_number) == 0:
        numbers_0.append(int(my_number))
    elif int(my_number) > 0:
        numbers_max.append(int(my_number))

    my_number = input('Enter your number or press space to exit ')


total_list = numbers_min + numbers_0 + numbers_max

for element in total_list:
    print(element)