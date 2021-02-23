#Bottle Deposits

max_1_liter_containers = input('drink containers holding one liter or less ')
up_1_liters_continers = input('drink containers holding more than one liter ')

cash_back1 = 0.10 * int(max_1_liter_containers)
cash_back2 = 0.25 * int(up_1_liters_continers)
total_cash_back = cash_back1 + cash_back2

print('cash back from containers one liter or less $', '%.2f'%cash_back1)
print('cash back from containers holding more than one liter $', '%.2f'%cash_back2)
print('total cashback is $', '%.2f'%total_cash_back)
