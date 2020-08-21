##
# A Connect-Four Player class 
#  

from board import Board

# write your class below

class Player:
    """represent a player of the Connect Four game
    """
    
    def  __init__(self, checker):
        """constructs a new Player object by initializing the 
            attribute checker and the attribute num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """  returns a string representing a Player object
            The string returned should indicate which checker 
            the Player object is using.
        """
        if self.checker == 'X':
            return 'Player X'
        else:
            return 'Player O'
    
    def opponent_checker(self):
        """ returns a one-character string representing the 
            checker of the Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """ that accepts a Board object b as a parameter and 
            returns the column where the player wants to make 
            the next move.
        """
        self.num_moves += 1
        while True:
           col = int(input('Enter a column: '))
           if b.can_add_to(col) == True:
              return col
           else:
               print('Try again!')