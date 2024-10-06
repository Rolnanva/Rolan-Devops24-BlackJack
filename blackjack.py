import random

class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.aces = 0

    def draw_card(self):
        """Draws a card and returns its value and name."""
        card = random.randint(2, 14)
        if card == 14:
            self.aces += 1
            return card, 'Ace'
        elif card == 11:
            return card, 'Jack'
        elif card == 12:
            return card, 'Queen'
        elif card == 13:
            return card, 'King'
        else:
            return card, str(card)

    def update_total(self, card):
        """Updates the player's total score, handling aces as either 1 or 14."""
        if card == 14:
            if self.total + 14 <= 21:
                self.total += 14
            else:
                self.total += 1
        else:
            self.total += card
        return self.total

    def adjust_aces(self):
        """Adjust if total is over 21 and aces can be reduced to 1."""
        while self.total > 21 and self.aces > 0:
            self.total -= 13  # Change an ace from 14 to 1
            self.aces -= 1

class Blackjack:
    def __init__(self):
        self.player = Player("Player")
        self.computer = Player("Computer")

    def play(self):
        print("Welcome to Blackjack!")

        # Player's turn
        self.player_turn()

        # Computer's turn if the player hasn't busted
        if self.player.total <= 21:
            self.computer_turn()

        # Decide the winner
        self.determine_winner()

    def player_turn(self):
        """Handles the player's card drawing."""
        while True:
            card, card_name = self.player.draw_card()
            self.player.update_total(card)
            print(f"You drew {card_name}. Your total is now {self.player.total}.")
            
            # Adjust aces if over 21
            self.player.adjust_aces()

            if self.player.total > 21:
                print("You went over 21! The computer wins.")
                return
            
            continue_playing = input("Do you want to draw another card? (yes/no): ").lower()
            if continue_playing != 'yes':
                break

    def computer_turn(self):
        """Handles the computer's card drawing."""
        while self.computer.total < self.player.total and self.computer.total <= 21:
            card, card_name = self.computer.draw_card()
            self.computer.update_total(card)
            print(f"The computer drew {card_name}. The computer's total is now {self.computer.total}.")
            
            # Adjust aces if over 21
            self.computer.adjust_aces()

    def determine_winner(self):
        """Determines the winner of the game."""
        if self.player.total > 21:
            print("The computer wins because you went over 21!")
        elif self.computer.total > 21:
            print("You win! The computer went over 21.")
        elif self.computer.total >= self.player.total:
            print(f"The computer wins with {self.computer.total} against your {self.player.total}.")
        else:
            print(f"You win with {self.player.total} against the computer's {self.computer.total}.")

# Start the game
game = Blackjack()
game.play()
