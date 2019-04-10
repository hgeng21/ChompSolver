# board_util.py
# used to play the game and handle commands
# -----------------------------------------
import numpy as np

class BoardUtil(object):
    
    @staticmethod
    def opponent(player):
        return 3-player
  
    @staticmethod
    def solve_chomp(board):
        
        ## init winning move to None
        winning_move = []
        
        ## first find all legal moves
        legal_moves = board.genmoves()
        depth = board.size[0]*board.size[1]//3*2
        ## if there are no legal moves, meaning only the poisoned chocolate is left
        ## opponent wins
        if len(legal_moves) == 0:
            print("Game ends, player {} wins.".format(3-board.current_player))
            return True
        else:
            ## remember the current player
            maxPlayer = True
            player = board.current_player
            
            ## use minimax to find best move
            #best, best_move = board.minimax(legal_moves,depth,maxPlayer,player)
            move_values = np.zeros(0)
            for move in legal_moves:
                temp_board = board.copy()
                temp_board.play_move(move[0],move[1])
                value = temp_board.minimax(temp_board.genmoves(),depth-1,not maxPlayer,player)
                move_values = np.append(move_values,value) 
                if value == 1: 
                    winning_move = legal_moves[len(move_values)-1]
                    break
            
            print("the move_values are {}".format(move_values))
            if winning_move == []:
                print("No winning move for player {}.".format(board.current_player))              
            else:
                print("The best move for player {} is: {}".format(player, winning_move))
    