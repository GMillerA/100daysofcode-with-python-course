class Roll:
    def __init__(self, name):
        # type: (object) -> object
        self.name = name
        #self.defeats = defeats
        #self.loses_to = loses_to

    def can_defeat(self, p2_roll):
        """Returns the win conditions for each roll based on p2_roll"""
        if self.name == "Rock" and p2_roll.name == "Scissors":
            return "Win"
        elif self.name == "Scissors" and p2_roll.name == "Paper":
            return "Win"
        elif self.name == "Paper" and p2_roll.name == "Rock":
            return "Win"
        elif self.name == p2_roll.name:
            return "Tie"
        else:
            return "Lose"





class Player:
    def __init__(self, name):
        self.name = name