import sys
import os

from game_logic import GameLogic
from banker import Banker

# Class for Game of Greed application
# Encapsulates everything needed for flow of game, keeping up with points, etc.
class Game:
    # Game constructor. Defaults to 3 rounds of game play
    def __init__(self, num_rounds=3):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0
    
    # Utility function to clear console
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls to clear console
            command = 'cls'
        os.system(command)

    # Entry point for playing (or declining) a game
    def play(self):
        # clear console
        self.clearConsole()

        # Welcome player
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        # Check if player doesnt want to play
        if response.lower() == "n":
            print("OK. Maybe another time")
        else:
            # Start/iterate rounds
            for round_num in range(1, self.num_rounds + 1):
                # start next round
                self.start_round(round_num)

    # This method will handle playing one round by the player 
    def start_round(self, round_num):
        num_dice = 6
        print("\n-------------------------")
        print(f"Starting round {round_num}")
        print("-------------------------")
        round_score = 0

        has_not_banked_points = True

        while has_not_banked_points:
            print(f"Rolling {num_dice} dice...")
            roll = GameLogic.roll_dice(num_dice)
            roll_string = " ".join([str(value) for value in roll])
            print(f"*** {roll_string} ***")
            # check for zilch
            preliminary_score = GameLogic.calculate_score(roll)
            if preliminary_score == 0:
                self.zilch(round_num)
                return
            # let player pick dies to keep
            keeper_values = self.check_keepers(roll, roll_string)
            # debug
            print(f'debug - keeper values {keeper_values}')

            # TODO: calculate keeper_score points from dice kept using game_logic
            # For now set score equal to preliminary_score
            keeper_score = preliminary_score
            # Update the score for round
            round_score += keeper_score

            # Update number of dice remaining
            num_dice -= len(keeper_values)

            print(
                f"You have {round_score} unbanked points and {num_dice} dice remaining..."
            )
            # Ask user to roll, bank, or quit
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")

            # Bank the points
            if response.lower() == "b":
                has_not_banked_points = False
                # TODO: Implement banking of points HERE. Set to 0 for now
                print("debug - IMPLEMENT BANKING OF POINTS -")
                banked_points = 0
                # End round after banking points
                self.end_round(round_num, banked_points)
            # Check if a re-roll
            elif response.lower() == "r":
                # If out of dice, reset number of dice to 6
                if num_dice == 0:
                    num_dice = 6
            # Check if quit
            elif response.lower() == "q":
                self.end_game()

    # Let user enter dice to keep and validate selections
    def check_keepers(self, roll, roll_string):
        # Use this flag to determine when user done selecting dice
        user_still_selecting_dice = True
        while user_still_selecting_dice:
            print("Enter dice to keep separated by commas, or (q)uit:")
            response = input("> ")

            # Check if user wants to quit picking dice
            if response == "q":
                self.end_game()
                user_still_selecting_dice = False

            if (user_still_selecting_dice):
                # Build a list of values kept
                keeper_values = []
                # TODO: Consider refactoring. Could pull list of numbers entered in other ways
                # Sample player response: 1,1,5
                for char in response:
                    if char.isnumeric():
                        keeper_values.append(int(char))
                
                # Check that player-selected dice are valid
                if GameLogic.validate_keepers(roll, keeper_values):
                    # kept values valid so return them
                    return keeper_values
                else:
                    print(f'Some/all selections are not available in roll: {keeper_values}')
                    # Re-display current roll
                    print(f"*** {roll_string} ***")

    # Handle zilch condition
    def zilch(self, round_num):
        # No scoring dice were rolled so end round with 0 points
        print("*****************************")
        print("**        ZILCH !!!        **")
        print("**       Round over !      **")
        print("*****************************")

        self.end_round(round_num, 0)

    # End of a round
    def end_round(self, round_num, banked_points):
        # Display Banked points, updated round pts, and finish round
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"You banked {banked_points} points in round {round_num}")
        print(f"Total score is {self.banker.balance} points")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # End of the game
    def end_game(self):
        print(f"\nThanks for playing! You earned {self.banker.balance} points!")
        # Use sys.exit to kill the program
        sys.exit()

# POE
if __name__ == "__main__":
    # TODO: Consider prompting player(s) for number of rouns to play and pass that into Game() - currently defaults to 3 rounds
    # Instantiate a game
    game = Game()
    # Kick off game
    game.play()