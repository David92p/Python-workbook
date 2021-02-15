#Reverse Order

n = int(input("Enter an integer, 0 to exit "))
list = []

while n != 0:
    list.append(n)
    n = int(input("Enter an integer, 0 to exit "))

list.reverse()
for i in list:
    print(i)