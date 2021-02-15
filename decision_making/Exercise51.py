#Roots of a Quadratic Function

a = int(input('Enter the first number '))
b = int(input('Enter the second number '))
c = int(input('Enter the third number '))

discriminate =  b**2 - 4 * a * c

print(discriminate)

if discriminate < 0:
    print('*'* 60)
    print('the square equation has no real value')
    print('*'* 60)
elif discriminate == 0:
    print('*'* 60)
    root = -b/(2*a)
    print('the square equation has a real value of', root)
    print('*'* 60)
elif discriminate > 0:
    print('*'* 60)
    root1 = (-b + discriminate) / (2*a)
    root2 = (-b - discriminate) / (2*a)
    print('the square equation has two real values equal to', root1, 'and', root2)
    print('*'* 60)