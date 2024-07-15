import random

# Define the card deck and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Function to handle player choice
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Function to display cards
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# Functions to handle game outcomes
def player_busts(player, dealer):
    print("Player busts! Dealer wins.")

def player_wins(player, dealer):
    print("Player wins!")

def dealer_busts(player, dealer):
    print("Dealer busts! Player wins!")

def dealer_wins(player, dealer):
    print("Dealer wins!")

def push(player, dealer):
    print("It's a tie! Push.")

# Game logic
def play_blackjack():
    while True:
        print("Welcome to Blackjack!")

        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        # Deal initial two cards to each player
        for _ in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        show_some(player_hand, dealer_hand)

        while True:
            choice = input("\nWould you like to hit or stay? Enter 'h' or 's': ")

            if choice.lower() == 'h':
                hit(deck, player_hand)
                show_some(player_hand, dealer_hand)

                if player_hand.value > 21:
                    player_busts(player_hand, dealer_hand)
                    break

            elif choice.lower() == 's':
                print("Player stands. Dealer's turn.")
                break

            else:
                print("Invalid input. Please enter 'h' or 's'.")

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand)
            else:
                push(player_hand, dealer_hand)

        new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
        if new_game.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    play_blackjack()
