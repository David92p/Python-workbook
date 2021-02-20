#Capitalize It

def capitalize(string):
    string = string.lower()
    my_list = list(string)
    new_string = ""
    if my_list[0] == my_list[0].lower():
            my_list[0] = my_list[0].upper()
    for i in range(len(my_list)):
        if my_list[i] is not my_list[len(my_list)-1] and (my_list[i] == "." or my_list[i] == "?" or my_list[i] == "!"):
            if  my_list[i+1] == " ":
                my_list[i+2] = my_list[i+2].upper()
            else:
                my_list[i+1].upper()
        if my_list[i] == "i":
            if my_list[i-1] == " " and my_list[i+1] == " ":
                my_list[i] = "I"
            elif my_list[i-1] == " " and my_list[i+1] == "'" or my_list[i+1] == "?" or my_list[i+1] == "!" or my_list[i+1] == ".":
                my_list[i] = "I"
    new_string = new_string.join(my_list)
    print(new_string)

def main():
    string = input("Enter your string ")
    capitalize(string)
    

if __name__== "__main__":
    main()
