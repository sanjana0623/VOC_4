#!/usr/bin/env python
# coding: utf-8

# Assigment week 4: Create a basic game like a Tic-Tac-Toe

# In[5]:


# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (a draw)
def check_draw(board):
    return " " not in board

# Main game loop
current_player = "X"
while True:
    print_board(board)
    print(f"Player {current_player}'s turn")
    move = int(input("Enter your move (1-9): ")) - 1

    # Check if the chosen move is valid
    if 0 <= move <= 8 and board[move] == " ":
        board[move] = current_player
    else:
        print("Invalid move. Try again.")
        continue

    # Check if the current player has won
    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins! Congratulations!")
        break

    # Check if the game is a draw
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"


# In[ ]:





# In[ ]:





# In[ ]:




