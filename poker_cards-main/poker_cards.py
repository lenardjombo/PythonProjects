import random

# Define card suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Define card values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Define a Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Define a Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Define a Hand class
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Function to determine the winner of the game
def determine_winner(player1_hand, player2_hand):
    player1_max_value = max(card.value for card in player1_hand.cards)
    player2_max_value = max(card.value for card in player2_hand.cards)

    if player1_max_value > player2_max_value:
        return "Player 1 wins with the highest card."
    elif player1_max_value < player2_max_value:
        return "Player 2 wins with the highest card."
    else:
        return "It's a tie!"

# Main function to play the game
def play_poker():
    print("Let's play Poker!")
    deck = Deck()
    player1_hand = Hand()
    player2_hand = Hand()

    # Deal cards to players
    for _ in range(5):
        player1_hand.add_card(deck.deal_card())
        player2_hand.add_card(deck.deal_card())

    print("Player 1's hand:", player1_hand)
    print("Player 2's hand:", player2_hand)

    # Input actions for players
    input("Press Enter for Player 1's action: ")
    print("Player 1's action:")
    print("1. Keep hand")
    print("2. Discard hand")
    action = input("Choose action (1 or 2): ")

    if action == '2':
        # Discard hand and draw new cards
        player1_hand = Hand()
        for _ in range(5):
            player1_hand.add_card(deck.deal_card())
        print("Player 1's new hand:", player1_hand)

    input("Press Enter for Player 2's action: ")
    print("Player 2's action:")
    print("1. Keep hand")
    print("2. Discard hand")
    action = input("Choose action (1 or 2): ")

    if action == '2':
        # Discard hand and draw new cards
        player2_hand = Hand()
        for _ in range(5):
            player2_hand.add_card(deck.deal_card())
        print("Player 2's new hand:", player2_hand)

    # Determine the winner
    print(determine_winner(player1_hand, player2_hand))

if __name__ == "__main__":
    play_poker()
