#Unary and Binary Operators

from Exercise129 import tokenizing

def unary_tokens(token_string):
    expression_string = tokenizing(token_string)
    if expression_string[0] == "+" or expression_string[0] == "-":
        expression_string[0] = "u" + expression_string[0]
    for i in range(1,len(expression_string)):
        if expression_string[i] == "+" or expression_string[i] == "-":
            if expression_string[i-1] == "(" or expression_string[i-1] == "+" or  expression_string[i-1] == "-" or expression_string[i-1] == "*" or expression_string[i-1] == "/": 
                expression_string[i] = "u" + expression_string[i]
    return expression_string


def main():
    n = input("Enter a mathematical expression:")
    tokens = unary_tokens(n)
    print("The tokens are:", tokens)

if __name__ == "__main__":
    main()


