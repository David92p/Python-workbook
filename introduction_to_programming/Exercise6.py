#Tax and Tip

meal_price = input('the price of the meal is $ ')

meal_price = float(meal_price)
tax_meal = (22*meal_price)/100
possibility_of_tipping = (18*meal_price)/100


print('the meal tax is $', '%.2f'%tax_meal)
print('the meal tip is $', '%.2f'%possibility_of_tipping)

total = meal_price+tax_meal+possibility_of_tipping
print('the total price for your delicious meal is ', '%.2f'%total)