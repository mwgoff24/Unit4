'''
Using Python, students will create a Tic-Tac-Toe game. This project has two parts:

designing the game so that two users can play Tic-Tac-Toe against one another; and

creating a Tic-Tac-Toe checker that will check the board to see if Xs or Os have won the game.

Overview
Tic-Tac-Toe is a game in which one player draws X's and another player draws O's inside a set of nine squares and each player tries 
to be the first to fill a row, column, or diagonal of squares with either X's or O's. 
We will be writing an interactive Tic-Tac-Toe program. 
At the end of each turn the computer will check to see if X's have won the game or if the O's have won the game.

Behavior
The program will prompt the user to enter their name and their opponent's name.

Whoever enters their name first will be playing as X's, and the other player will be O's.

The program will print an empty game board as a starting point.

The players will take turns inputting the row and column where they would like to place their mark.

If that spot is invalid or already taken, the program will ask again for a valid spot.

At the end of each player's turn the program will check if that player has won and print the updated game board.

If there are no more spots open and nobody has won the game, the program will print Tie game!.

Implementation Details
Use variables to store the user names for personalized prompts.

Create a game board represented as a list of lists, size 3 by 3.

Note: This is a change from our earlier implementations of Tic-Tac-Toe. Why do you think this might be better?

Check for a winner horizontally, vertically, and on both diagonals.

Do not allow a user to overwrite a spot on the board where a play has already been made.
'''
# tic tac toe revisited


# variables
player1 = input("What is your name, player 1? ")
player2 = input("What is your name, player 2? ")
current_player = player1

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turns = 0

# functions

# replace, replaces whatever spot the player chose with their respective marker
def replace(letter):
    global turns
    valid_spot = False
    # checks to see if input is 1 through 9
    while valid_spot == False:
        spot = int(input(f"Choose the spot you would like to place your marker on, {current_player}. "))
        if spot < 1 or spot > 9:
            print(f"That's not a valid spot, {current_player}.")
        else:
            valid_spot = True
    # replaces the number on the board with the letter
    for i in range(len(board)):
        for j in range(len(board[i])):
            if spot == board[i][j]:
                board[i][j] = letter
                turns +=1


# check win horizontal, checks each row after each turn to see if all the spots are filled with the same marker
def check_win_horizontal(letter, player):
    global turns, board
    for row in board:
        if row == [letter, letter, letter]:
            print(f"{player} has won.")

            turns = 10

# check win vertical, checks each column after each turn to see if all the spots are filled with the same marker
def check_win_vertical(letter, player):
    global turns, board
    # first column
    if board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
        print(f"{player} has won.")
        turns = 10
    # second column
    elif board[0][1] == letter and board[1][1] == letter and board[2][1] == letter:
        print(f"{player} has won.")
        turns = 10
    # third column
    elif board[0][2] == letter and board[1][2] == letter and board[2][2] == letter:
        print(f"{player} has won.")
        turns = 10

# check win diagonal, checks each diagonal after each turn to see if all the spots are filled with the same marker
def check_win_diagonal(letter, player):
    global turns, board
    # left to right
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        print(f"{player} has won.")
        turns = 10
    # right to left
    elif board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        print(f"{player} has won.")
        turns = 10

# print board, prints the entire board and is implemented after each turn
def print_board():
    global board
    print(
            f"{board[0][0]} | {board[0][1]} | {board[0][2]} \n"
            "--------- \n"
            f"{board[1][0]} | {board[1][1]} | {board[1][2]} \n"
            "--------- \n"
            f"{board[2][0]} | {board[2][1]} | {board[2][2]} \n")

# game loop

# print statement added here because I can't code the program to recognize if a spot is taken
# the program does not override the spot or update the turn count if a player tries to place a marker in the spot of another marker
print(f"Welcome to tic-tac-toe, {player1} and {player2}! Before you start, if a player tries to set their marker on your spot, you need to set your marker on your spot again for gameplay " 
"purposes. \n"
f"In other words, if {player1} sets their spot on 1 and {player2} does the same thing afterwards, {player1} needs to set another marker on 1. \n")
while turns < 9:
    current_player = player1
    replace("X")
    print_board()

# all check different types of wins to check
    check_win_horizontal("X", current_player)
    check_win_vertical("X", current_player)
    check_win_diagonal("X", current_player)

    # first conditional catches a tie
    if turns == 9:
        print("Tie game.")
        break
    # if a win is detected on ANY check_win functions, the function sets turns equal to 10
    # this conditional will then run and therefore end the game
    elif turns == 10:
        break
    print(turns)

# same code as code for player1
    current_player = player2
    replace("O")
    print_board()
    check_win_horizontal("O", current_player)
    check_win_vertical("O", current_player)
    check_win_diagonal("O", current_player)
    if turns == 9:
        print("Tie game.")
        break
    elif turns == 10:
        break
    print(turns)