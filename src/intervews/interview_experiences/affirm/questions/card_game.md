
### Part 1

this is a two player card game the game starts with a deck of 52 cards represented as unique integers [1...52] the cards are randomly shuffled and then dealt out to both players evenly on each turn: both players turn over their top-most card the player with the higher valued card takes the cards and puts them in their scoring pile (scoring 1 point per card) this continues until all the players have no cards left the player with the highest score wins if they have the same number of cards in their win pile, tiebreaker goes to the player with the highest card in their win pile

### Part 2

Support the ability to play the game with N players. An input to the game will now be a list of strings (of length N) indicating the player names. The deck contains M cards of distinct integers. It is not guaranteed M % N == 0. If there are leftover cards they should randomly be handed out to remaining players. i.e. with 17 cards and 5 people: 2 people get 4 cards and 3 get 3 cards For example the input: game(["Joe", "Jill", "Bob"], 5) would be a game between 3 players and 5 cards. you should print the name of the player that won the game.

import random
from collections import deque

```python
class Card:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        # Helps with debugging
        return f"Card({self.value})"

class Player:
    def __init__(self, pname):
        self.pname = pname
        self.hand = deque()
        # We don't need a separate win pile. We can just track score and max won card.
        self.score = 0
        self.max_won_card = 0 # This will be the tiebreaker

class CardGame:
    # Part 2: Initialize with N players and M cards
    def __init__(self, player_names, num_cards=52):
        if len(player_names) == 0:
            raise ValueError("Must have at least one player.")
        if num_cards < len(player_names):
            raise ValueError("Number of cards must be at least the number of players.")
            
        self.players = deque([Player(pname) for pname in player_names])
        
        # Create and shuffle the deck
        deck = [Card(i) for i in range(1, num_cards + 1)]
        random.shuffle(deck)
        self.deck = deque(deck)

    def deal(self):
        # Part 2: To randomly distribute extra cards, we can shuffle the players list first.
        # A simple rotation (popleft/append) is also a fair, if not truly random, distribution.
        # We will deal one by one.
        player_queue = self.players.copy()
        while self.deck:
            player = player_queue.popleft()
            card = self.deck.popleft()
            player.hand.append(card)
            player_queue.append(player)

    def play_turn(self):
        # Players still in the game play a card
        # Using a list for the pot allows us to check all cards
        pot = []
        players_in_round = []
        
        # Each active player puts a card into the pot
        for player in self.players:
            if player.hand:
                card = player.hand.popleft() # Play from the top
                pot.append(card)
                players_in_round.append(player)

        if not pot:
            return False # No cards were played, round is over

        # Find the winning card and player
        # We iterate through cards and players together
        highest_card_value = -1
        winning_player = None
        
        # Note: The original rules don't specify what to do in case of a tie in a single turn.
        # In this implementation, the first player to play the highest card wins the turn.
        # A more complex game like "War" would have a tie-breaking "war" round.
        for i, card in enumerate(pot):
            if card.value > highest_card_value:
                highest_card_value = card.value
                winning_player = players_in_round[i]

        # Award points and update the tiebreaker card for the winner
        if winning_player:
            winning_player.score += len(pot)
            winning_player.max_won_card = max(winning_player.max_won_card, highest_card_value)
            # print(f"{winning_player.pname} wins the round with a {highest_card_value}. Score: {winning_player.score}") # Optional: for debugging

        return True # The round was played

    def get_winner(self):
        # The winner is determined by score, with max_won_card as the tiebreaker.
        # We can sort the players based on a tuple of their score and max_won_card.
        # The `reverse=True` means higher scores/cards come first.
        sorted_players = sorted(self.players, key=lambda p: (p.score, p.max_won_card), reverse=True)
        
        if not sorted_players:
            return None # No players

        return sorted_players[0]

    def play_game(self):
        print(f"--- Starting a new game with {len(self.players)} players and {len(self.deck) + sum(len(p.hand) for p in self.players)} cards. ---")
        self.deal()
        
        # The game continues as long as at least one player has cards
        num_cards_in_play = sum(len(player.hand) for player in self.players)
        while num_cards_in_play > 0:
            self.play_turn()
            num_cards_in_play = sum(len(player.hand) for player in self.players)
        
        print("\n--- Game Over ---")
        for player in self.players:
            print(f"Player: {player.pname}, Final Score: {player.score}, Highest Card Won: {player.max_won_card}")

        winner = self.get_winner()
        if winner:
            print(f"\nThe winner is {winner.pname}!")
            return winner.pname
        else:
            print("There is no winner.")
            return None

# Example usage from Part 2
def game(player_names, num_cards):
    card_game = CardGame(player_names, num_cards)
    return card_game.play_game()

# --- Run the example ---
if __name__ == "__main__":
    # Part 1 style game (2 players, 52 cards)
    game(["Alice", "Bob"], 52)
    
    print("\n" + "="*40 + "\n")
    
    # Part 2 example (3 players, 5 cards)
    # Expected outcome: With 5 cards, 2 players get 2 cards, 1 player gets 1.
    # There will be two rounds.
    game(["Joe", "Jill", "Jane"], 5)