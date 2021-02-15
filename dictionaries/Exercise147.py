from Exercise146 import *
from random import randint

def define_card(card):
    numbers = []
    while len(numbers)<30:
        n = randint(1,75)
        if n not in numbers:
            numbers.append(n)
    for n in range(len(numbers)):
        for value in card.values():
            for i, v in enumerate(value):
                if numbers[n] == value[i]:
                    value[i] = "**"
                 
    return card

           
def win_or_lose(card):
    if card["B"][0] == "**" and card["I"][1] == "**" and card["N"][2] == "**" and card["G"][3] == "**" and card["O"][4] == "**":
        return True
    elif card["O"][0] == "**" and card["G"][1] == "**" and card["N"][2] == "**" and card["I"][3] == "**" and card["B"][4] == "**":
        return True
    for k in card:
        for i in k:
            i = 0
            if card[k][i] == "**":
                i += 1
                if i == 5:
                    return True
    if card["B"][0] == "**" and card["I"][0] == "**" and card["N"][0] == "**" and card["G"][0] == "**" and card["O"][0] == "**":
        return True
    if card["B"][1] == "**" and card["I"][1] == "**" and card["N"][1] == "**" and card["G"][1] == "**" and card["O"][1] == "**":
        return True
    if card["B"][2] == "**" and card["I"][2] == "**" and card["N"][2] == "**" and card["G"][2] == "**" and card["O"][2] == "**":
        return True
    if card["B"][3] == "**" and card["I"][3] == "**" and card["N"][3] == "**" and card["G"][3] == "**" and card["O"][3] == "**":
        return True
    if card["B"][4] == "**" and card["I"][4] == "**" and card["N"][4] == "**" and card["G"][4] == "**" and card["O"][4] == "**":
        return True
   
    return False

print()
print("Welcome to the game of bingo, each box is made up of several numbers.\
 There will be 30 random draws. Get 5 numbers drawn horizontally, vertically or crosswise to take home the 'BINGOOO' prize pool")
print()
print("*********************************************************************************")
print()
player = int(input("Let's start playing, how many lotto cards do you want to buy? "))
print()
while player != 0:
   for i in range(player):
      card = define_card(bingo_card())
      if win_or_lose(card) == True:
         show_bingo_card(card)
         print()
         print("***************************")
         print()
         print("It's your lucky day, you won!")
         print()
         print("***************************")
         print()
      if win_or_lose(card) == False:
         show_bingo_card(card)
         print()
         print("***************************")
         print()
         print("I'm sorry, you lost ..")
         print()
         print("***************************")
         print()
   player = int(input("Let's start playing, how many lotto cards do you want to buy? "))
   print()
print()
print("***************************")
print()
print("Come back to play with us soon")

