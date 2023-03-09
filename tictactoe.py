import time
board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
    }
def typewrite(str):
    for x in str:
        time.sleep(0.05,)
        print(x,end="")

def winner():
    global board
    #The first 3 check if player X has won on a row
    if board[1] and board[2] and board[3] == "X":
        print("Player X won!")
    elif board[4] and board[5] and board[6] == "X":
        print("Player X won!")
    elif board[7] and board[8] and board[9] == "X":
        print("Player X won!")
    #The 3 after this check if player X has won in a column
    elif board[1] and board[4] and board[7] == "X":
        print("Player X won!")
    elif board[2] and board[5] and board[8] == "X":
        print("Player X won!")
    elif board[3] and board[6] and board[9] == "X":
        print("Player X won!")
    #The next 2 check if player X won on the diagonal
    elif board[1] and board[5] and board[9] == "X":
        print("Player X has won!")
    elif board[3] and board[5] and board[7] == "X":
        print("Player X has won!")
        #The first 3 check if player O has won on a row
    elif board[1] and board[2] and board[3] == "O":
        print("Player O won!")
    elif board[4] and board[5] and board[6] == "O":
        print("Player O won!")
    elif board[7] and board[8] and board[9] == "O":
        print("Player O won!")
    #The 3 after this check if player O has won in a column
    elif board[1] and board[4] and board[7] == "O":
        print("Player O won!")
    elif board[2] and board[5] and board[8] == "O":
        print("Player O won!")
    elif board[3] and board[6] and board[9] == "O":
        print("Player O won!")
    #The next 2 check if player O won on the diagonal
    elif board[1] and board[5] and board[9] == "O":
        print("Player O has won!")
    elif board[3] and board[5] and board[7] == "O":
        print("Player O has won!")

def printBoard():
    global board
    print(" ",board[1] + "|" + " " + board[2] + " " + "|" + board[3])
    print("---+---+---")
    print(" ",board[4] + "|" + " " + board[5] + " " + "|" + board[6])
    print("---+---+---")
    print(" ",board[7] + "|" + " " + board[8] + " " + "|" + board[9])


def player_x():
    global board
    while True:
        option_x = int(input("What field would you like to choose?"))
        if board[option_x] == "O":
            print("NOT VALID")
        else:
            board[option_x] = "X"
            printBoard()
            winner()
            break

def player_o():
    global board
    while True:
        option_o = int(input("What field would you like to choose?"))
        if board[option_o] == "X":
            print("NOT VALID")
        else:
            board[option_o] = "O"
            printBoard()
            winner()
            break

def startup():
    typewrite("Welcome to Tic tac toe in Python - By Luis Wettre\n\n")
    typewrite("""The Rules are simple, there are 2 players that take turns on choosing a field.\n
The first player to reach 3 off their charachter in a row (Horizontal, Diagonal or Vertical) wins the game
if no one manages to do this, the game is a draw!\n\n
You pick the square you want to play in py choosing a number between 1 - 9, the first row being 1 - 3, second row 4 - 6 and third row 7 - 9\n\n""")
    
def rounds():
    player_x()
    winner()
    player_o()
    player_x()
    winner()
    player_o()
    player_x()
    winner()
    player_o()
    player_x()
    winner()
    player_o()
    winner()
    player_x()


startup()
printBoard()
rounds()

















