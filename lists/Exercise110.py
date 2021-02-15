#Sorted Order

my_list = []
n = int(input('Enter an integer, 0 to exit '))

while n != 0:
    my_list.append(n)
    n = int(input('Enter an integer, 0 to exit '))

my_list.sort()

for i in my_list:
    print(i)


