import random
##First define the skeleton of the tic-tac-toe game

def display_board(board):
    
    print (board[7]+' | '+board[8]+' | '+board[9])
    print('----------')
    print (board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print (board[1]+' | '+board[2]+' | '+board[3])


test_board = [' ']*10
display_board(test_board)

##Second part defines the input for the player to decide if he wants to start as 'X' or 'O'
def player_input():

    marker = ""

    #Define which Player 1 will choose between X or O

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose between X or O: ').upper()

    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    
    #Pass the opposite marker to Player 2


##Set the position of the Marker on the board
def marker_local(board, marker, position):

    board[position] = marker

##Define the function that will score (X or O) and check if it won
def winner_check(board, mark):

    

    # Win Tic Tac Toe

    #Check all lines

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # horizontal top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # horizontal middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # horizontal bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # vertical from left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # middle vertical
    (board[9] == mark and board[6] == mark and board[3] == mark) or # right vertical
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

## Randomly determine which player starts first
def choose_first():

    luck = random.randint(0,1)

    if luck == 0:
        return 'Player 1'
    else:
        return 'Player 2'

## Create the function to determine if space on the board is still available
def check_space(board, position):

    return board[position] == ' '

## Create a function to determine whether the entire board is full or not
def check_board_full(board):

    for i in range(1,10):
        if check_space(board, i):
            return False
    return True

##Function used for the player to choose a next position
def choice_player(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board, position):
        position = int(input("Choose a position: (1-9)"))
    return position

#Gather all the codes to run the game
print("Welcome to Tic-Tac-Toe")

while True:

    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()

    print(turn + " Will play first")

    play = input("Ready to play? Y or N: ").upper()

    if play == "Y":
        play = True
    else:
        play = False


    while play:

        if turn == "Player 1":

            #Show the board
            display_board(the_board)
            #Choose a position
            position = choice_player(the_board)
            #Place the marker in position
            marker_local(the_board, player1_marker, position)
            #Check if you won
            if winner_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 WON!!")
                play = False
            else:
                if check_board_full(the_board):
                    display_board(the_board)
                    print('DEAT')
                    play = False
                
                else:
                    turn = 'Player 2'
        else:
            
            #Show the board
            display_board(the_board)
            #Choose a position
            position = choice_player(the_board)
            #Place the marker in position
            marker_local(the_board, player2_marker, position)
            #Check if you won
            if winner_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 WON!!")
                play = False
            else:
                if check_board_full(the_board):
                    display_board(the_board)
                    print('DEAT')
                    play = False
                
                else:
                    turn = 'Player 1'

    ##Create a function to determine whether the player should play again or stop
    def replay():

        choice = input("Do you want to play again? Say Y or N: ").upper()

        return choice == 'Y'

    if not replay():
        break