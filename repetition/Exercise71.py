#Approximate π

n = float(3)
pg = []
count = 2
while len(pg) < 15:
    if len(pg) % 2 == 0:
        x = 4 /(count*(count+1)*(count+2))
        n += round(x,10)
        pg.append(n)
        count += 2
    elif len(pg) % 2 != 0:
        x = float(4 / (count*(count+1)*(count+2)))
        n -= round(x,10)
        pg.append(n)
        count += 2
print(pg)



