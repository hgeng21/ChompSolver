# board_util.py
# used to play the game and handle commands
# -----------------------------------------


class BoardUtil(object):
    
    @staticmethod
    def opponent(player):
        return 3-player
    
    
    @staticmethod
    def solve_chomp(board):
        ## first find all legal moves
        