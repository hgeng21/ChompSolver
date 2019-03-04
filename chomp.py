# chomp.py
# this is the main program for implementing player for chomp!

from chomp_board import ChompBoard

size = (4,6)

def main():
    ##create a chomp_board of size mxn
    chomp_board = ChompBoard(size) 
    ##print board
    chomp_board.showboard()
    ##play chomp!
    play_chomp(chomp_board)
    #mode = int(input("1-pvp, 2-pvc, 3-solver"))
    #if mode == 1:
        #play_chomp(chomp_board)
    #elif mode == 2:
        #pass
    #elif mode == 3:
        #solve_chomp(chomp_board)
    

def solve_board(chomp_board):
    print("solve")
    BoardUtil.solve_chomp(chomp_board)
    
    

def play_chomp(chomp_board):
    game_end = False
    
    print("Note: move format is row number followed by column number, separated by a space")
    while not game_end:
        
        command = input(">>>Enter command/move: ")
        if command == "solve":
            solve_board(chomp_board)
            break
        try:
            row, col = command.split()
            row = int(row)
            col = int(col)
            if row>size[0] or col>size[1]:
                raise
            
            ##check if the move is legal
            if chomp_board.is_legal(row,col):
                
                ##check if the game is over
                game_end,winner = chomp_board.is_game_end(row,col)
                print(">>>Player {}: move ({},{})".format(chomp_board.current_player,row,col))
                if game_end:
                    print(">>>Game over, winner is {}".format(winner))
                else:
                    ##play the move, update board.
                    chomp_board.play_move(row,col)
                    chomp_board.showboard()
            
            else:
                pass
                #print("Illegal move, please pick move that is non-zero.")
        
        except ValueError:
            pass
            #print("Invalid input, please enter two integers")
        except:
            pass
            #print("Input number out of range")
    
          
          
main()