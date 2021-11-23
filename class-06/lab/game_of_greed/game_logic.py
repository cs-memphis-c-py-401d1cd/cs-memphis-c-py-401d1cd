from collections import Counter
from random import randint

# The GameLogic class encapsulates the functionality to perform and check rolls
class GameLogic:
    @staticmethod
    def roll_dice(num=6):
        rolled_dice = []
        # TODO: Could look at refactoring how we build die set
        for i in range(num):
            # roll each die (random number 1 - 6)
            rolled_dice.append(randint(1, 6))
        return rolled_dice


    # This method will calculate the (possible) score based on the roll
    @staticmethod
    def calculate_score(dice):
        # dice parameter is a list of integers that represent the user's selected dice pulled out from current roll 
        if len(dice) > 6:
            # Should never pass in more than 6 dice. Throw an exception if happens
            raise Exception("Specified more than 6 selections!")

        # Start with possible score of zero     
        score = 0

        # Use Counter to determine how many of each value was rolled
        counts = Counter(dice)
        
        # debug message
        print(f'debug - counts = {counts}')

        # TODO: Check for 6 of a kind

        # TODO: Check for 3 of a kind(s)
        
        # Make sure that there is at least 1(s) and/or 5(s) to proceed
        ones_used = fives_used = False

        # TODO: Any other checks that need to happen here? 

        # Max possible 1s score
        if not ones_used:
            score += counts.get(1, 0) * 100

        # Max possible 5s score
        if not fives_used:
            score += counts.get(5, 0) * 50

        # debug
        print(f'debug - Max possible 1s and 5s score {score}')

        # return zero if zilch, else return *possible* score depending on what user ends up selecting
        return score

    @staticmethod
    # TODO: Need a method to validate the dice player enters to keep. For now always return valid
    def validate_keepers(roll, keepers):
        return True
       
    @staticmethod
    # TODO: Need a method to determine scoring from dice kept (if any) and return the scores for scorable dice
    def get_scorers(dice):
        # Make a list of scored dice
        scorers = []
        # TODO: Build list of scored dice and return it
        return scorers
       
