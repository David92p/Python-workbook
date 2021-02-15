#Tokenizing a String

def tokenizing(string):
    string = string.replace(" ","")
    tokens = []
    count = 0
    while count <= len(string)-1:
        if string[count] == "*" or string[count] == "/" or string[count] == "+" or string[count] == "-" or string[count] == "ˆ" or string[count]  == "(" or string[count] == ")":
            tokens.append(string[count])
            count += 1
        else:
            numbers = ""
            count2 = count
            while count2 <= len(string)-1:
                if string[count2] != "*" and string[count2] != "/" and string[count2] != "+" and string[count2] != "-" and string[count2] != "ˆ" and string[count2] != "(" and string[count2] != ")":
                    numbers += string[count2]
                    count2 += 1
                    count += 1
                    continue
                else:
                    tokens.append(numbers)
                    numbers = ""
                    break
            if len(numbers)>0:
                tokens.append(numbers)

    return tokens
                   
               
               
def main():
    n = input("Enter a mathematical expression: ")
    tokens = tokenizing(n)
    print("The tokens are:", tokens)

if __name__ == "__main__":
    main()


