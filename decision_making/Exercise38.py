#Name That Shape

shape_sides = input('Enter the sides of your geometric shape ')

shape_sides = int(shape_sides)

if shape_sides < 3:
    print('You entered a wrong shape')
elif shape_sides == 3:
    print('You have entered a triangle')
elif shape_sides == 4:
    print('You have entered a square')
elif shape_sides == 5:
    print ('You have entered a pentagon')
elif shape_sides == 6:
    print('You have entered a hexagon')
elif shape_sides == 7:
    print('You have entered a polygon')
elif shape_sides == 8:
    print('You have entered an octagon')
elif shape_sides == 9:
    print('You have entered an ennagon')
elif shape_sides == 10:
    print('You have entered a decagon')
else:
    print('You entered a wrong shape')