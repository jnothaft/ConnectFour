##
# AI Player for use in Connect Four   
#

import random  
from game import *

class AIPlayer(Player):
    """subclass from player for an intelligent computer player 
        that chooses a strategy (left, right or random) to 
        determine its moves
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        s = ''
        lookahead = str(self.lookahead)
        tiebreak = str(self.tiebreak)
        if self.checker == 'X':
            s += 'Player X ' + '('
            s += tiebreak
            s += ', '
            s += lookahead
            s += ')'    
        else:
            s += 'Player O ' + '('
            s += tiebreak
            s += ', '
            s += lookahead
            s += ')'    
        return s
    
    def max_score_column(self, scores):
        """list scores containing a score for each column of the board, 
            and that returns the index of the column with the maximum 
            score
        """
        max_score = max(scores)
        indices = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                indices += [i]
        if self.tiebreak == 'LEFT':
            return indices[0]
        elif self.tiebreak == 'RIGHT':
            return indices[-1]
        else:
            return random.choice(indices)
    
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b. 
        """
        scores = [0] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif  b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                if self.lookahead == 0:
                    scores[col] = 50
                else:
                    opponent_lookahead = self.lookahead - 1
                    opponent = AIPlayer(self.opponent_checker(), \
                               self.tiebreak, opponent_lookahead)
                    opp_scores = opponent.scores_for(b)
                    if max(opp_scores) == 100:
                        scores[col] = 0
                    elif max(opp_scores) == 0:
                        scores[col] = 100
                    elif max(opp_scores) == 50:
                        scores[col] = 50
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ returns the called AIPlayer‘s judgment of its best possible move
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        choice = self.max_score_column(scores)
        return choice