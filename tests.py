from classes import Deck, Hand, Cards, BlackJack
import random

def test_cards_class():
    card = Cards(3,5)
    assert card.rank == 5
    assert card.suit == 3
    card = Cards()
    assert card.rank == 1
    assert card.suit == 0
    card = Cards(None, None)
    assert card.rank == None
    assert card.suit == None
    card = Cards("a", 6)
    assert card.suit == "a"
    assert card.rank == 6


#test deck class 
def test_deck_init():
    pass

def test_deck_shuffle():
    pass

def test_draw_card():

def test_constructor():
    pass


def main():
    test_cards_class()
    test_deck_init()
    #test_remove_method()
    #test_deck_shuffle()
    #test_draw_card()
    #test_constructor()

main()

