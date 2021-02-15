from random import randint

def bingo_card():
    n = 15
    card = {}
    lower = 1
    upper = n + 1
    for i in ["B","I","N","G","O"]:
        card[i] = []
        while len(card[i]) != 5:
            new_number = randint(lower,upper)
            if new_number not in card[i]:
                card[i].append(new_number)
        lower = lower + n
        upper = upper + n
    return card
   
def show_bingo_card(card):
    print("B","\t","I","\t","N","\t","G","\t","O")
    for i in range(5):
        for l in ["B", "I", "N", "G", "O"]:
            print(card[l][i], end= "\t")
        print()

def main():
    my_card = bingo_card()
    show_bingo_card(my_card)

if __name__=="__main__":
    main()