#Morse Code

def morse_code(string):
    string = string.lower()
    string_morse = ""
    code_morse = {
        "a":".-", "b": "-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.",
        "g":"--.", "h":"....", "i":"..", "j": ".---", "k":"-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u":"..-", "v": "...-", "w": ".--", "x": "-..-", 
        "y": "-.--", "z":"--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."  
    }
    for i in string:
        if i in code_morse:
            string_morse += code_morse[i]+" "
    return string_morse

def main():
    morse_message = input("Enter your message or press space to Exit: ")
    while morse_message != " ":
        message = morse_code(morse_message)
        print("Your morse messsage is", message)
        morse_message = input("Enter your message or press space to Exit: ")
    print("bye Bye")

if __name__ == "__main__":
    main()

