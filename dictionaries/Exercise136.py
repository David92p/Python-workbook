#Reverse Lookup

def reverseLookup(dictionary,my_value):
    keys = []
    for key in dictionary:
        if dictionary[key] == my_value:
            keys.append(dictionary[key])
    return keys


my_dictionary = {"Hello": "Ciao", "Thank You": "Grazie", "Please":"Perfavore"}


def main():
    word = "Perfavore"
    print("The Italian word for 'Please' is ",reverseLookup(my_dictionary,"Perfavore"))

if __name__=="__main__":
    main()