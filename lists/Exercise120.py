#Formatting a List

def form_value():
    words = input("Enter your word or press enter to Exit ")
    my_words = []
    while words != "":
        my_words.append(words)
        words = input("Enter your word or press enter to Exit ")
    if len(my_words) == 1:
        return str(my_words[0])
    if len(my_words) == 2:
        return str(my_words[0]+" and "+ my_words[1])
    list_my_words = ""
    for i in range(0, len(my_words)-2):
        list_my_words += str(my_words[i]+", ")
    list_my_words += str(my_words[-2] + " and " + my_words[-1])
    return list_my_words

                                              
if __name__ == "__main__":
    my_list = form_value()
    print(my_list)

    