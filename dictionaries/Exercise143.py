#Anagrams

letters = {
        1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g",
        8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n",
        15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 19: "t", 20: "u",
        21: "v", 22: "w", 23: "x", 24: "y", 25: "z"
    }

def anagrams(word1, word2):
    if len(word2)>len(word1):
        return False
    for c in letters:
        if letters[c] not in word1 and letters[c] in word2:
            return False
    return True

word1 = input("Enter your word or press space to Exit: ")
word2 = input("Enter the word as a possible anagram: ")
while word1 != " ":
    print(f"The word {word2} is an anagram of {word1}:", anagrams(word1, word2))
    print("***********************************************")
    word1 = input("Enter your word or press space to Exit: ")
    word2 = input("Enter the word as a possible anagram: ")
print("bye Bye")