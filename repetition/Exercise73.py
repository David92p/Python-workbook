#Caesar Cipher

def code(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz '
    code = ''
    index = 0
    for l in string:
        if l in letters:
            while index < len(letters):
                if l == 'x':
                    code += 'a'
                    index = 0
                    break
                elif l == 'y':
                    code += 'b'
                    index = 0
                    break
                elif l == 'y':
                    code += 'c'
                    index = 0
                    break
                elif l == letters[index]:
                    i = index + 3
                    code += letters[i]
                    index = 0
                    break
                elif l == ' ':
                    code += ' '
                    break
                else:
                    index += 1
                    continue
    print(code.upper())


def de_code(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz '
    code = ''
    index = 0
    for l in string:
        if l in letters:
            while index < len(letters):
                if l == 'a':
                    code += 'x'
                    index = 0
                    break
                elif l == 'b':
                    code += 'y'
                    index = 0
                    break
                elif l == 'c':
                    code += 'z'
                    index = 0
                    break
                elif l == letters[index]:
                    i = index - 3
                    code += letters[i]
                    index = 0
                    break
                elif l == ' ':
                    code += ' '
                    break
                else:
                    index += 1
                    continue
    print(code.upper())



string1 = 'Veni vidi vici'
code(string1)

string2 = 'YHQL YLGL YLFL'
de_code(string2)
            



