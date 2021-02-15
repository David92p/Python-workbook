#Month Name to Number of Days

name_month = input("Enter the month ")
name_month = name_month.lower()
month = 31

if name_month == "april" or name_month == "june" or name_month == "september" or name_month == "november" :
    month = 30
elif name_month == 'february':
    month = '28 or 29 days'

print("The month of", name_month, 'has', month, 'days')