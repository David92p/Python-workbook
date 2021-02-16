#Is It a Valid Triangle?

def valid_triangle(l1,l2,l3):
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return False
    if l1 == l2 and l1 == l3 and l2 == l3:
        return True 
    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
        return False
    if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1 + l2:
        return True


while True:   
    l1 = int(input("Enter the first length: "))
    l2 = int(input("Enter the second length: "))
    l3 = int(input("Enter the third length: "))
    print((f"The measures entered can form a triangle: {valid_triangle(l1,l2,l3)}"))

