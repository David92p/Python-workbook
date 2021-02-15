#Discount Table

count = 4.95

for i in range(0,5,1):
    if i < 5:
        print('Basic Price is $', count)
        a = (count * 60)/100
        sale = count - a
        print ('Basic price is $', round(sale,2))
        count+=5

