# chomp_board.py:
# ------------------
# used to generate board for playing chomp!
import numpy as np
from board_util import BoardUtil
"""
chomp_board.py

Implements a basic chomp! board with functions to:
- initialize to a given board size
- check if a move is legal
- play a move

The board uses a 1-dimensional representation with padding
"""


class ChompBoard(object):
    
    
    ## initialize parameters
    def __init__(self, size):
        self.size = size
        self.value = size[0]*size[1]    ## value used to represent each block
        self.current_player = 1
        self.board = self.gen_empty_board()
        
    ## generate empty board of size row,col in 2Darray
    def gen_empty_board(self):
        """
        in[0]: None
        out[1]: self.board
        ------------------------------
        0: blocks of chocolates taken
        1: blocks of chocolates not been taken
        2: paddings
        8: poisoned chocolate
        ------------------------------
        """
        board = np.full(self.size,self.value) ##create empty gameboard
        board[self.size[0]-1,0] = 8
        self.board = np.zeros((self.size[0]+2,self.size[1]+2))    ##initialize self.board with padding background
        self.board[1:self.size[0]+1,1:self.size[1]+1] = board  ##add padding to self.board
        return self.board
    
    ## check if the move given is legal
    def is_legal(self,row,col):
        """
        in[2]: row,col
        out[1]: T/F
        ------------------------------  
        """
        if self.board[row,col]==self.value:
            return True
        else: return False
        
    ## check if the game ends with the move
    def is_game_end(self,row,col):
        """
        in[2]: row,col
        out[2]: T/F,winner
        ------------------------------  
        """        
        if self.board[row,col]==8:
            return True,BoardUtil.opponent(self.current_player)
        else: return False,None
        
    ## play move, change current player
    def play_move(self,row,col):
        mask = np.ones((row,self.size[1]-col+1))
        temp_board = np.zeros((self.size[0]+2,self.size[1]+2))
        temp_board[1:row+1,col:self.size[1]+1] = mask
        self.board = self.board - temp_board
        ## change current player
        self.current_player = BoardUtil.opponent(self.current_player)
    
    ## print out gameboard
    def showboard(self):
        print(self.board[1:self.size[0]+1,1:self.size[1]+1])