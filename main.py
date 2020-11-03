'''
tic tac toe game

implement the computer's turn

'''

import random

# global constants
EMPTY = " "
NUM_SQUARES = 9

# global variables
board = []
player_symbol1 = player_symbol2 = ""
turn = 0

Player1_name = input('Enter name for player 1:')
Player2_name = input('Enter name for player 2:')

win = False



#**************  Functions *************#

'''
set up for a new game
'''
def newgame(board,player1,player2,turn):
    print('''
*** Python Tic Tac Toe ***

On your turn you will move by entering a number 
from 0-8 as shown on the following board:

    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8

    ''')
    
    # get player symbols
    player1 = input("Player 1, would you like to be X or O? ").upper()
    if player1 not in "XO":
        player1 = "X"
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    
    if turn == 0:
        print (Player1_name, "may go first..." ) 
    board = new_board()
    print (Player1_name, " is ", player1, Player2_name, " is ", player2)
    print (Player1_name, "may go first...")
    input("Press any key to begin...")
    print
    return board,player1,player2,turn

    
'''
store moves in a 9 item list
if list == EMPTY, no play has been made in that square
'''    
def new_board():
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board    
    
def show_board(board):
    print()
    print (board[0], "|", board[1], "|", board[2])
    print ("---------")
    print (board[3], "|", board[4], "|", board[5])
    print ("---------")
    print (board[6], "|", board[7], "|", board[8])
    print()
     
        

'''
verify numeric input
return T if numeric, F otherwise
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

'''
get a number from the user in the indicated range
'''
def get_number(question, low, high):
    response = None
    while response not in range(low, high+1):
        response = input(question)
        if is_number(response):
            response = int(response)
        else:
            response = None
    return response
    
'''
is the square open?
'''    
def valid_move(board,move):
    return board[move] == EMPTY


'''
player's move
'''
def player1_turn(board,player_symbol1):
    valid = False
    while not valid:
        move = get_number("Player 1's move: ",0,8)
        valid = valid_move(board,move)
    board[move] = player_symbol1
    return board
    
    
'''
computer's move
just getting a random number for now
'''
def player2_turn(board,player_symbol2):
    valid = False
    while not valid:
        move = get_number("Player 2's move: ",0,8)
        valid = valid_move(board,move)
    board[move] = player_symbol2    
    return board
  



#=========== Main ===========#

board, player_symbol1, player_symbol2, turn = newgame(board,player_symbol1, player_symbol2, turn)

gameover = False
while not gameover:
    win = False
    for i in range(3):
        if board[i] != EMPTY and (board[i] == board[i+3] == board[i+6]):
            win = True
            gameover = True
            winner = board[i] 
            
    for i in [0, 3, 6]:
        if board[i] != EMPTY and (board[i] == board[i+1]== board[i+2]):
            win = True
            gameover = True
            winner = board[i] 
            
    for i in [1,4,7]:
        if board[i] != EMPTY and (board[i] == board[i-1]== board[i+1]):
            win = True
            gameover = True
            winner = board[i] 
            
    for i in [2,5,8]:
        if board[i] != EMPTY and (board[i] == board[i-1] == board[i-2]):
            win = True
            gameover = True
            winner = board[i] 
            
    if board[i] != EMPTY and (board[2] == board[6] == board[4] or board[0] == board[8] == board[4]):
        win = True
        gameover = True
        winner = board[i] 
        
    if turn == 0 and win == False:
        board = player1_turn(board,player_symbol1)
        turn = 1
    elif turn == 1 and win == False:
        board = player2_turn(board,player_symbol2)
        turn = 0  
        
    show_board(board)
    
    if EMPTY not in board:
        gameover = True
        if win == True:
            print ("The " + winner +" player wins!")
        else:
          show_board(board)
          print("It's a draw.")
        

    

while win == True:
    gameover == True
    print("The " + winner +" player wins!")

    break


