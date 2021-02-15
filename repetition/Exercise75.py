#Is a String a Palindrome?

def define_string_palindrome(string):
    string = string.lower()
    string1 = list(string)
    list1 = []
    for i in range(len(string1)):
        letter = "abcdefghijklmnopqrstuvwxyz"
        if string1[i] in letter:
            list1.append(string1[i])
    string1 = "".join(list1)
    list2 = []
    for x in range(len(list1)-1,-1,-1):
        list2.append(list1[x])
    string2 = "".join(list2)
    if string1 == string2:
        return True
    else:
        return False

string = input('Enter your palindrome string ')
result = define_string_palindrome(string)
print("Your string is a palindrome:", result)



