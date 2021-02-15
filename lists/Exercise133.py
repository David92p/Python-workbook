#Does a List Contain a Sublist?

def isSublist(list_1,list_2):
    if len(list_2) > len(list_1):
        return False
    if len(list_2) == 1 and list_2[0] in list_1:
        return True
    if list_2 == []:
        return True
    if list_2 == list_1:
        return True
    if list_2[0] in list_1:  
        count = list_1.index(list_2[0])+1
        count_2 = 1
        while count_2 < len(list_2):
            if list_2[count_2] == list_1[count]:
                count += 1
                count_2 += 1
            else:
                return False
        return True
    return False
           

       


def main():
    list_1 = [4,5,6,7,8,9,10,11,12,13,14]
    list_2 = [5,6,8]
    result = isSublist(list_1, list_2)
    print(f"List {list_2} is a sub-list of list {list_1}: {result}")

if __name__ == "__main__":
    main()