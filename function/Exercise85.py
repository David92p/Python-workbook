#Compute the Hypotenuse

cat_mag = int(input('Enter the greater cathetus--> '))
cat_min = int(input('Enter the minor cathetus --> '))

def triangle_hypotenuse(par1, par2):
    from math import sqrt
    sqrt = sqrt((par1**2)+(par2**2))
    return sqrt

print('The hypotenuse of your triangular roof ', round(triangle_hypotenuse(cat_mag, cat_min),2))
