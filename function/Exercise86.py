#Taxi Fare

def taxi_tax(km, fixed_quote=4, variable=0.25):
    meters = km * 1000
    totale = (variable*meters)/140+fixed_quote
    return round(totale,2)

while True:
    calculation = input('Do you want to calculate your rate? Si - No ---> ')
    calculation = calculation.lower()
    if calculation == "si":
        count = float(input('Enter the km traveled to calculate the fare ---> '))
        rate = taxi_tax(count)
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        print('The rate to', count,'km is', rate, '$')
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        continue
    elif calculation == 'no':
        break

print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
print('See you soon')
