#Classifying Triangles

side1 = input('Enter the measure of first side ')
side2 = input('Enter the measure of second side ')
side3 = input('Enter the measure of third side ')

side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

if side1 == side2 and side1 == side3  and side2 == side3:
    print('This is an equilateral triangle')
elif side1 != side2 and side1 != side3  and side2 != side3:
    print('This is a scalene triangle')
else:
    print('We have an isoscile triangle')

