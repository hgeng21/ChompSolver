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
        self.board_ref = self.gen_empty_board_ref()
      
      
    ## generate all legal moves of current state
    def genmoves(self):
        legal_moves = []
        for i in range(self.size[0]+1):
            for j in range(self.size[1]+1):
                if self.board[i,j] == 1:
                    legal_moves.append([i,j]) 
        legal_moves = np.asarray(legal_moves)
        return legal_moves
    
    
    ## copy board
    def copy(self):
        b = ChompBoard(self.size)
        b.current_player = self.current_player
        b.board = np.copy(self.board)
        return b    
    
    
    ## generate empty board of size row,col in 2D array
    def gen_empty_board(self):
        """
        in[0]: None
        out[1]: self.board
        ------------------------------
        0: blocks of chocolates taken
        1: blocks of chocolates not been taken
        8: poisoned chocolate
        ------------------------------
        """        
        board = np.ones(self.size) ##create empty gameboard
        board[self.size[0]-1,0] = 8
        self.board = np.zeros((self.size[0]+2,self.size[1]+2))    ##initialize self.board with padding background
        self.board[1:self.size[0]+1,1:self.size[1]+1] = board  ##add padding to self.board
        return self.board        
    
        
    ## generate empty board of size row,col in 2D array
    def gen_empty_board_ref(self):
        board = np.full(self.size,self.value) ##create empty gameboard
        board[self.size[0]-1,0] = 8
        self.board_ref = np.zeros((self.size[0]+2,self.size[1]+2))    ##initialize self.board with padding background
        self.board_ref[1:self.size[0]+1,1:self.size[1]+1] = board  ##add padding to self.board
        return self.board_ref
    
    ## check if the move given is legal
    def is_legal(self,row,col):
        """
        in[2]: row,col
        out[1]: T/F
        ------------------------------  
        """
        if self.board[row,col]!=0:
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
        ## update self.board
        ## set all removed cells to zero
        mask = np.zeros((row,self.size[1]-col+1))
        self.board[1:row+1,col:self.size[1]+1] = mask
        ## update self.board_ref:
        ## subtract all removed cells by one
        mask = np.ones((row,self.size[1]-col+1))
        temp_board_ref = np.zeros((self.size[0]+2,self.size[1]+2))
        temp_board_ref[1:row+1,col:self.size[1]+1] = mask
        self.board_ref = self.board_ref - temp_board_ref
        ## change current player
        self.current_player = BoardUtil.opponent(self.current_player)
    
    
    ## print out gameboard
    def showboard(self):
        print(self.board[1:self.size[0]+1,1:self.size[1]+1])
        
        
    ## print out gameboard reference, used for tracking previous moves and undo
    def showboard_ref(self):
        print(self.board_ref[1:self.size[0]+1,1:self.size[1]+1])
        
        
    def minimax(self,legal_moves,depth,maxPlayer,player):
        
        move_values = np.zeros(0)
        
        ## if terminal node or max depth, return heuristic value
        if depth == 0 or len(legal_moves) == 0:
            if self.current_player==player: 
                #print("player {} wins,-1".format(3-player))
                return -1 # if maxPlayer win, return 1, otherwise return -1
            else: 
                #print("player {} wins,+1".format(player))
                return 1
            
        #print(">>> Now is player {}'s turn.".format(self.current_player))
        #print("legal moves: {}".format(legal_moves))
        
        for move in legal_moves:
            #print("---take move {}:".format(move))
            temp_board = self.copy()
            temp_board.play_move(move[0],move[1])
            #temp_board.showboard() 
            value= temp_board.minimax(temp_board.genmoves(),depth-1,not maxPlayer,player)
            #print("===for this move, the best value we can get is {}, the best move is {}".format(value, best_move))
            move_values = np.append(move_values,value)
        
        #print("<<<<<<<<<<<<< The move values are: {} >>>>>>>>>>>>>>".format(move_values))
        ## if maximizing player:
        if maxPlayer:
            best = max(move_values)
        else:
            best = min(move_values)
        
        #print("final best = {}, best_move = {}".format(best, best_move))
        #print("===========================================")
        return best