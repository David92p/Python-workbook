#Is a List already in Sorted Order?

def ascending_order(list):
    order_list = []
    for i in list:
        order_list.append(i)
    order_list.sort()
    if list == order_list:
        return True
    else: 
        return False

def main():
    my_list = []
    while True:
        n = input('Enter your number or press enter to exit ')
        if n == "":
            break
        n = float(n)
        my_list.append(n)
    print(my_list)
    is_order = ascending_order(my_list)
    print(is_order)

main()
