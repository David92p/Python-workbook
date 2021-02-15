#Pig Latin Improved

def pig_latin_improved(string):
    letters_1 = "aeiouèéùìòAEIOU"
    letters_2 = "bcdfghjklmnpqrstwxyzBCDFGHJKLMNPQRSTWXYZ"
    characters = ".,;:?!'"
    my_string = ""
    my_list = string.split(" ")
    for el in my_list:
        if el[0] in letters_1:
            el = el+"way"
            for c in el:
                if c in characters:
                    el = el.replace(c,"")
                    el += c
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
    

x = "Is a fantastic day to programming a new game"
pig_latin_improved(x)