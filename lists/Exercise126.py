#Dealing Hands of Cards

from Exercise125 import create_deck_scala40, shuffle_scala40

def scala40_game(players, n_cards, deck):
    players = [[] for player in range(players)]
    for card in range(n_cards):
        for player in players:
            player.append(deck[card])
            del deck[card]
    return players


       
if __name__ == "__main__":
    print("Let's play Scala40:")
    print()
    players = 4
    deck = shuffle_scala40(create_deck_scala40())
    player_cards = 5
    start_play = scala40_game(players,player_cards,deck)
    print(start_play)
    print()
    print("Cards in the deck")
    print()
    print(deck)
