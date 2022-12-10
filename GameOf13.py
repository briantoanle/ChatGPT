'''
The game of 13 is a simple card game that is played with a standard deck of 52 cards. The objective of the game is to be the first player to get rid of all of your cards.

Here are the rules for the game:

The game is played by two to four players.
The deck is shuffled and dealt out evenly to all of the players. Each player should have the same number of cards.
The player to the left of the dealer goes first and play continues clockwise around the table.
On each turn, a player can play one or more cards from their hand that add up to 13. For example, a player could play a 6 and a 7, a 4, a 3, and a 6, or a single king.
If a player has no cards that can be played, they must draw one card from the deck. If the card can be played, the player can play it immediately. Otherwise, it is added to their hand and the turn passes to the next player.
The first player to get rid of all of their cards wins the game.
That's it! The game of 13 is a simple and fun card game that is easy to learn and can be enjoyed by players of all ages.
'''

# side note, the game doesn't even work
from random import shuffle

# A class representing a deck of cards
class Deck:
  # Initialize the deck and shuffle the cards
  def __init__(self):
    self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    shuffle(self.cards)

  # Draw a card from the top of the deck
  def draw(self):
    return self.cards.pop()

# A class representing a player in the game
class Player:
  # Initialize the player with a given name and an empty hand
  def __init__(self, name):
    self.name = name
    self.hand = []

  # Add a card to the player's hand
  def add_card(self, card):
    self.hand.append(card)

  # Play a card or cards that add up to 13
  def play(self, cards):
    if sum(cards) == 13:
      for card in cards:
        self.hand.remove(card)
      return True
    return False

# A class representing a game of 13
class Game:
  # Initialize the game with a given set of player names
  def __init__(self, names):
    self.deck = Deck()
    self.players = [Player(name) for name in names]

  # Play the game
  def play(self):
    # Deal the cards to the players
    for _ in range(13):
      for player in self.players:
        player.add_card(self.deck.draw())

    # Keep track of the current player and the number of cards they have left
    current_player = 0
    player_counts = [len(player.hand) for player in self.players]

    # Continue playing until one player has no cards left
    while max(player_counts) > 0:
      # Print the current state of the game
      print('Current player:', self.players[current_player].name)
      print('Player hands:')
      for player in self.players:
        print(player.name, player.hand)

      # Ask the current player for their move
      cards = input('Enter the cards you want to play, separated by commas: ').split(',')

      # Check if the player's move is valid
      if not self.players[current_player].play(cards):
        print('Invalid move!')
        continue

      # Update the number of cards each player has left
      player_counts = [len(player.hand) for player in self.players]

      # Move to the next player
      current_player = (current_player + 1) % len(self.players)

    # The game is over, so print the winner
    print('Game over!')
    print('Winner:', self.players[current_player].name)

# Create a new game with three players
game = Game(['Alice', 'Bob', 'Carol'])

# Play the game
game.play()