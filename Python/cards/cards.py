#!/usr/bin/env python3

import random

RANKS = range(1,14)
SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # rank names - queen ace etc

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

def create_deck():
    """ Returns a standard deck of playing cards as a list.
    """
    return [Card(rank, suit) for suit in SUITS for rank in RANKS]

def draw_hand(deck, hand_size=5):
    """ Draw hand_size cards from the top of the deck.
        Assume that the deck can accomodate the hand size.
        Returns the drawn hand and the remainder of the deck.
    """
    pass

def contains_pair(hand):
    """ Returns a boolean indicating whether or
        not the hand has at least two cards of the same rank.
    """
    pass

def verify_deck_size(deck, size):
    """ Verify that the deck is of a certain size.
        Error out if this verification fails.
    """
    if len(deck) != size:
        raise Exception(" Deck size error ")

def count_suits(hand):
    """ Return a mapping of suit:count for each of the
        four suits based on the cards in hand.
    """
    pass
    
if __name__ == "__main__":
    deck = create_deck()
    #print(deck)
    random.shuffle(deck)
    hand, deck = draw_hand(deck)
    verify_deck_size(deck, 47)

    print("Hand          : %s" % hand)
    print("Contains pair : %s" % contains_pair(hand))
    print("Suit counts   : %s" % count_suits(hand))
