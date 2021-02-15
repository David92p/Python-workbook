#The Chinese zodiac

year = int(input('enter the year whose zodiac sign you want to know '))


dragon_year = 2000
snake_year = 2001
horse_year = 2002
sheep_year = 2003
monkey_year = 2004
rooster_year = 2005
dog_year = 2006
pig_year = 2007
rat_year = 2008
ox_year = 2009
tiger_year = 2010
hare_year = 2011

if year % 12 == 8:
    print ('it is the year of the Dragon')
elif year % 12 == 9:
    print('it is the year of the Snake')
elif year % 12 == 10:
    print('it is the year of the Horse')
elif year % 12 == 11:
    print('it is the year of the Sheep')
elif year % 12 == 0:
    print('it is the year of the Monkey')
elif year % 12 == 1:
    print('it is the year of the Rooster')
elif year % 12 == 2:
    print('it is the year of the Dog')
elif year % 12 == 3:
    print('it is the year of the Pig')
elif year % 12 == 4:
    print('it is the year of the Rat')
elif year % 12 == 5:
    print('it is the year of the Ox')
elif year % 12 == 6:
    print('it is the year of the Tiger')
elif year % 12 == 7:
    print('it is the year of the Hare')