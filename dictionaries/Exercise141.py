 #Write out Numbers in English - the amount of a check

numbers = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
        }

def value_cheque(chequeImport):
    if chequeImport < 20:
        return numbers[chequeImport]
    
    if chequeImport < 100:
        if chequeImport % 10 == 0:
            return numbers[chequeImport]
        else: 
            return numbers[chequeImport//10*10]+ " " +numbers[chequeImport%10]
    
    if chequeImport < 1000:
        if chequeImport % 100 == 0:
            return numbers[chequeImport//100]+"hundred"
        else: 
            return numbers[chequeImport//100]+"hundred"+" "+value_cheque(chequeImport % 100)



def main():
    for n in range(0,1000):
        print(value_cheque(n))


if __name__=="__main__":
    main()

