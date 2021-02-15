#Admission Price


infant_price = 0.00
price_children = 14.00
adult_price = 23.00
elderly_price = 18.00

total = 0

line = input('Enter the age of the people who want to participate, press space to exit ')
while line != ' ':
    years = int(line)
    if years <= 2:
        total += infant_price
    elif years > 2 and years <= 12:
        total += price_children
    elif years > 12 and years < 65:
        total += adult_price
    else:
        total += elderly_price
    
    line = input('Enter the age of the people who want to participate, press space to exit ')

print('The total ticket price is $',round(total,3))


   
   
