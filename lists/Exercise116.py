#Perfect Numbers

from Exercise115 import dividers

limit = 10000

def perfect_number(element):
    list = []
    list = dividers(element)
    count =  0
    for n in list:
        count += n
    if count == element:
        return True 
    return False
    


def main():
    print("Perfect numbers between 1 and", limit, "are")
    for i in range(2,limit+1):
        if perfect_number(i):
            print(i)
        
main()