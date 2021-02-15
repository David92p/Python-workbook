#Median of Three Values

def media(par1, par2, par3):
    media = (par1 + par2 + par3)/3
    return media

number1 = float(input('Enter the first number ---> '))
number2 = float(input('Enter the second number ---> '))
number3 = float(input('Enter the third number ---> '))
print('\n+++++++++++++++++++++++++++++++++\n')
media = round(media(number1,number2, number3), 2)
print('Media for your value is', media )