#Count the Elements

def count_range(list_n, min_n, max_n):
    count = 0
    for n in list_n:
        if n >= min_n and n <= max_n:
            count += 1
    return count
           

def main():
    my_list = [2,4,7,9,12,17,21,36,54,62,74,88,91]
    print(f"The elements in list {my_list} between 1 and 100 are")
    print(count_range(my_list, 1, 100))
    print(f"The elements in list {my_list} between 50 and 70 are")
    print(count_range(my_list, 50, 70))
    print(f"The elements in list {my_list} between -20 and 1 are")
    print(count_range(my_list, -20, 1))
    print(f"The elements in list {my_list} between 10 and 40 are")
    print(count_range(my_list, 10, 40))


main()