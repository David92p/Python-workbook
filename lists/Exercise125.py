#Shuffling a Deck of Cards


import random 

def create_deck_scala40():
    deck = []
    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            deck.append(value+suit)
    return deck

def shuffle_scala40(list):
    shuffle_list = []
    count = len(list)
    while count > 0:
        n = random.randint(0,len(list)-1)
        shuffle_list.append(list[n])
        del list[n]
        count -= 1
    return shuffle_list
    

        
if __name__ == "__main__":
    deck = create_deck_scala40()
    print(deck)
    shuffle_deck = shuffle_scala40(deck)
    print(shuffle_deck)
   






