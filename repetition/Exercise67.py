#Compute the Perimeter of a Polygon
from math import sqrt
p = 0
while True:
    x1 = input('Enter the first point X (blank to quit) ')
    if x1 != " ":
        y1 = input('Enter the first point Y ')
        x2 = input('Enter the second point X ')
        y2 = input('Enter the second point Y ')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        distance = sqrt((x2-x1 )**2+(y2-y1)**2)
        distance = round(distance, 3)
        p += round(distance,3)
        print('Distance for these points are',distance)
        print('*'*50)
        print('total perimeter of the polygon is', p)
        continue
    else:
        print('********************ByBy******************************') 
        break
