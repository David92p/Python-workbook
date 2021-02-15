#Shipping Calculator

def express_shipping(item):
    shipping = 10.95
    if item >1:
        plus = 2.95*(item-1)
        return shipping + plus
    else:
        return shipping

quantity = int(input('How many items did you buy? '))

total_price = round(express_shipping(quantity),2)

print('The total shipping price is $', total_price)