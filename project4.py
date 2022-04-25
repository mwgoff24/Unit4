# tic tac toe revisited

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
# variables
player1 = input("What is your name, player 1? ")
player2 = input("What is your name, player 2? ")

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
table = (f"{board[0][0]} | {board[0][1]} | {board[0][2]} \n"
"--------- \n"
f"{board[1][0]} | {board[1][1]} | {board[1][2]} \n"
"--------- \n"
f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

def replace(spot, letter):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if spot == board[i][j]:
                board[i][j] = letter
                print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} \n"
"--------- \n"
f"{board[1][0]} | {board[1][1]} | {board[1][2]} \n"
"--------- \n"
f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

# game loop
while True:
    choice1 = int(input(f"Choose the spot you would like to place your X on, {player1}. "))
    replace(choice1, "X")
    choice2 = int(input(f"Choose the spot you would like to place your O on, {player2}. "))
    replace(choice2, "O")