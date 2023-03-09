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
















