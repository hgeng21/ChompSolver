# board_util.py
# used to play the game and handle commands
# -----------------------------------------
import numpy as np

class BoardUtil(object):
    
    @staticmethod
    def opponent(player):
        return 3-player
    
    
    @staticmethod
    # first version, not in use anymore
    def solve_chomp_v1(board):
        ## first find all legal moves
        legal_moves = board.genmoves()
        
        ## if there are no legal moves, meaning only the poisoned chocolate is left
        ## opponent wins
        if legal_moves == []:
            print("No winning moves for player {}, player {} wins.".format(board.current_player, 3-board.current_player))
            return True
        else:
            ## init list to contain value for each legal move
            move_values = []
            
            ## remember the current player
            player = board.current_player
            
            ## try each move and get value for that move
            for move in legal_moves:
                temp_board = board.copy()
                value = 0
                value = temp_board.try_move(move,player,value)
                move_values.append(value)
                
            best_move = legal_moves[move_values.index(max(move_values))]
            print("the best move for player {} is: {}".format(player, best_move))
        

    @staticmethod
    def solve_chomp(board):
        ## first find all legal moves
        legal_moves = board.genmoves()
        depth = 10 #board.size[0]*board.size[1]-1
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
                
            print("the move_values are {}".format(move_values))
            if all(i==-1 for i in move_values):
                print("No winning move for player {}, best move can be {}.".format(board.current_player,legal_moves[np.argmax(move_values)]))              
            else:
                print("The best move for player {} is: {}".format(player, legal_moves[np.argmax(move_values)]))
    