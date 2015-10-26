from classes import Deck, Hand, Cards, BlackJack

import random



def create_deck():
    deck = Deck()
    deck.shuffle(deck)
    return deck

def create_hand():
    player_hand = Hand


def deal_hand_player(deck):
    card = deck.draw_card()
    yield card

def deal_hand_dealer(deck):
    card = deck.draw_card()
    yield card
 
def hit(hand):
    yield hand.hit_or_stay()

def main():
    deck = create_deck()
    player_hand = deal_hand_player(deck)
    dealer_hand = deal_hand_dealer(deck)
    player_score = player_hand.get_score()
    #while score != 21:



       




main()