#Pig Latin

def pig_latin(string):
    string = string.lower()
    letters_1 = "aeiouèéùìò"
    letters_2 = "bcdfghjklmnpqrstwxyz"
    my_string = ""
    my_list = string.split(" ")
    for el in my_list:
        if el[0] in letters_1:
            el = el+"way"
            my_string += str(el) + " "
        elif el[0] in letters_2:
            for i in el:
                if i in letters_2:
                    el = el.replace(i,"")
                    el += i
                else:
                    break
            my_string += str(el)+ "ay" + " "
    print(my_string)
       

my_string = "computer think algorithm office"
pig_latin(my_string)