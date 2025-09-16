import random

def board_print(board):
    for row in board:
        print("|".join(row))
        print("-"*9)

def winner(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3) or all (board[j][i]==player for j in range(3))):
            return True
    if all(board[i][i]==player for i in range(3) or all(board[i][2-i]==player for i in range(3))):
        return True
    return False

def full_board(board):
    return all(cell != " " for row in board for cell in row )

def computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
               board[i][j] = "o"
               if winner(board,'o'):
                   board[i][j]== " "
                   return (i,j)
            board[i][j]

    for i in range(3):
        for j in range (3):
            if board[i][j] == " ":
                board[i][j]=="x"
            if winner(board,"x"):
                board[i][j]==" "
                return (i,j)
            board[i][j]

    empty = [(i,j) for i in range (3) for j in range(3) == " "]
    return random.choise(empty) if empty else None

def ttt():
    print("----TICK TACK TOE----")
    print("ENTER Q ANYTIME TO QUIT")

    board = [[" " for_in range(3)]for_in range(3)]
    players = ["X","O"]
    current_player = 0