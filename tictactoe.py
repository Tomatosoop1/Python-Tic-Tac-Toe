board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
    }
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
            break
        
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
    else:
        print("It was a draw!")
    

printBoard()
player_x()
player_o()
player_x()
player_o()
player_x()
player_o()
player_x()
player_o()
player_x()
winner()















