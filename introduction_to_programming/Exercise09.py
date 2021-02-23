#Compound Interest

count = int(input('Enter the amount deposited '))
count = round(count,2)

year1 = count + (count*4/100)
year2 = year1 + (year1*4/100)
year3 = year2 + (year2*4/100)

print('The total amount including interest in the first year is ', round(year1,2),'\n'
'The total amount including interest in the second year is ', round(year2,2),'\n'
'The total amount including interest in the third year is ', round(year3,2))