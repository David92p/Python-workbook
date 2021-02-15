#Random Lottery Numbers

import random

def lottery_numbers():
    my_numbers = []
    while len(my_numbers) < 6:
        n = random.randint(1,49)
        if n not in my_numbers:
            my_numbers.append(n)
    my_numbers.sort()
    print(my_numbers)
   
       
my_numbers = lottery_numbers()