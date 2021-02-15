#Postal Codes

province_territory = {
    "A":"Newfoundland", "B": "Nova Scotia","C":"Prince Edward Island", "E":"New Brunswick",
    "G":"Quebec", "H":"Quebec","J":"Quebec", "K": "Ontario", "L": "Ontario", "M":"Ontario",
    "N": "Ontario", "P": "Ontario", "R":"Manitoba", "S": "Saskatchewan", "T": "Alberta",
    "V": "British Columbia", "X": "Nunavut or Northwest Territories", "Y":"Yukon"
    }

postal_code = input("Enter your postal code or press space to Exit: ")
while postal_code != " ":
    postal_code = postal_code.upper()
    province_territory_letters = "ABCEGHJKLMNPRSTVXY"
    valid_numbers = "0123456789"
    if postal_code[0] in province_territory_letters and postal_code[1] in valid_numbers:
        if postal_code[1] == "0":
            for i in province_territory:
                if postal_code[0] == i:
                    print("Postal code is for a rural address in", province_territory[i])
                    postal_code = input("Enter your postal code or press space to Exit: ")
        if postal_code[1] > "0":
            for i in province_territory:
                if postal_code[0] == i:
                    print("Postal code is for an urban address in", province_territory[i])
                    postal_code = input("Enter your postal code or press space to Exit: ")
    else:
        print("Your postal code is incorrect")
        postal_code = input("Enter your postal code or press space to Exit: ")
print("bye Bye")