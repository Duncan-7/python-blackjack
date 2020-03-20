from card import Card
import random

class Deck():

    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        hearts = self.create_suit('hearts')
        diamonds = self.create_suit('diamonds')
        clubs = self.create_suit('clubs')
        spades = self.create_suit('spades')

        deck = hearts + diamonds + clubs + spades
        return deck


    def create_suit(self, suit):
        complete_suit = []
        for i in range(2,11):
            complete_suit.append(Card(suit, i))
        complete_suit.append(Card(suit, 'Jack'))
        complete_suit.append(Card(suit, 'Queen'))
        complete_suit.append(Card(suit, 'King'))
        complete_suit.append(Card(suit, 'Ace'))

        return complete_suit

    def shuffle_deck(self):
        return random.shuffle(self.deck)
    
    def __str__(self):
        for card in self.deck:
            print(f"{card.value} of {card.suit}")
        return "" 

    def __len__(self):
        return len(self.deck)