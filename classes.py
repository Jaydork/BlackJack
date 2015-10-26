import random

class Hand():
    '''Holds cards to display to player'''

    def __init__(self, owner, card1, card2):
        self.hand = []
        self.owner = owner
        self.card1 = card1
        self.card2 = card2

    def get_score(self):
        return sum(c for c in self.cards)


class Cards:
    ''' Creates cards'''
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6","7","8","9","10","Jack","Queen","King"]

    def __init__(self, suit = 0, rank = 1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return(self.ranks[self.rank] + " of " + self.suits[self.suit])

class Deck():
    '''Deck of 52 cards with various methods to implement
    Methods:
    Shuffle: Randomizes the 52 card deck, might not be needed if using tuple.
    Cards_left: Displays how many cards left in the deck after each card draw.
    Constructor: Creates a new deck after each game.
    Draw_card: Take a random card from the deck, put it in the players hand (or dealers).'''

    def __init__(self):
        '''Initializes a new deck'''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Cards(suit,rank))

    def __str__(self):
        s = " "
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s



    def shuffle(self, cards):
        ''' Shuffles the deck before a game'''
        random.shuffle(self.cards)


    def cards_left(self):
        ''' Displays how many cards still in a deck'''
        return len(self.cards)

    def constructor(self):
        '''Resets deck'''
        return Deck()


    def empty_deck(self):
        return self.cards == []

    def draw_card(self):
        '''Draw a card, then remove card from possiblities of cards. Can be used for dealing or drawing.'''
        return self.cards.pop()

    def sort(self):
        '''Sorts deck in a particular order'''
         

class BlackJack(Hand, Cards, Deck):
    ''' Lays out the logic and rules of BlackJack such as hitting, staying, folding etc.
    Methods:
    Hit: Draws a card and gives to appropriate player.
    Fold: Start game over
    Stay: Keep your hand and see if you win.'''

    def __init__(self):
        pass

    def hit(self, deck, hand):
        return hand.append(deck.draw_card())

