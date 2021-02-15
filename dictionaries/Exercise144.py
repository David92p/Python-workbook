##Anagrams Again

letters = {
        1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g",
        8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n",
        15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 19: "t", 20: "u",
        21: "v", 22: "w", 23: "x", 24: "y", 25: "z"
    }

def phrases_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    list_string1 = list(string1)
    list_string2 = list(string2)
    letters_string1 = []
    letters_string2 = []
    for c in list_string1:
        if c in letters.values():
            letters_string1.append(c)
    for c in list_string2:
        if c in letters.values():
            letters_string2.append(c)
    if len(letters_string1)>len(letters_string2):
        return False
    for c in letters_string1:
        if c not in letters_string2:
            return False
    return True

a = "William Shakespeare!"
b = "I am a weakish speller"
print(phrases_anagrams(a,b))