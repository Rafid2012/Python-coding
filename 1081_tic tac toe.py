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

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X","O"]
    current_player = 0

    while True:
        board_print(board)
        if current_player == 0:
            print("Player{players[current player]}'s turn")
        try:
         row_input = (input("enter the row or q to quit"))
         if row_input.lower() == "q":
             print("Thanks for playing")
             break
         
         collum_input = (input("enter the collum or q to quit"))
         if collum_input.lower() == "q":
             print("Thanks for playing")
             break
         
         row,collum = int(row_input) -1 , int(collum_input)-1

         if row < 0 or row > 2 or collum < 0 or collum > 2:
             print("invalid input")
             continue
         if board[row,collum] != " ":
             print("The cell is full.")
             continue
         
        except ValueError:
            print("Invalid input")

        else:
          print("computer move(O):")
        move = computer_move(board)
        if move:
                row,collum = move
                print(f"computer chosse row {row+1} and collum {collum+1}")

        else:
            print("No move left for computer")

        board[row,collum] = players[current_player]

        if winner(board,players[current_player]):
            board_print(board)
            if current_player == 0:
                print(f"Player{players[current_player]} won!")
            else:
                print("computer (O) won!")
            break 
    
        if is_full(board):
            board_print(board)
            print("It is a draw")
            break
    
    current_player = current_player -1

if __name__ == "__main__":
    ttt()

        