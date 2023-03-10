import time

#List used later in the code for checking if moves are availabel
AvailableOptions = [1,2,3,4,5,6,7,8,9]

#This is a dictionary with currently nothing in it, later this is where the players moves are stored
board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
    }

#These list all define different ways the players could win (if all variabels in any of them are the same that player wins)
first_row = [board[1],board[2],board[3]]
second_row = [board[4],board[5],board[6]]
third_row = [board[7],board[8],board[9]]

first_collumn = [board[1],board[4],board[7]]
second_collumn = [board[2],board[5],board[8]]
third_collumn = [board[3],board[6],board[9]]

first_diagonal = [board[1],board[5],board[9]]
second_diagonal = [board[3],board[5],board[7]]

#WIP win checker
def checkPlayerX(first_row,second_row,third_row):
    element = "X"

    #All the rows are set to true, if not all elements in a row are X the rows set to false
    check_first_row = True
    check_second_row = True
    check_third_row = True

    for item in first_row:
        if element != item:
            check_first_row = False
            break

    for item in second_row:
        if element != item:
            check_second_row = False
            break
    
    for item in third_row:
        if element != item:
            check_third_row = False
            break

    if check_first_row or check_second_row or check_third_row == True:
        print("Congratuations Player X you won!")
        quit()

#The typewrite functions doesnt serve a real purpose its purely cosmetic
def typewrite(str):
    for x in str:
        time.sleep(0.01)
        print(x,end="")

#This just prints the current board layout
def printBoard():
    global board
    print(" ",board[1] + "|" + " " + board[2] + " " + "|" + board[3])
    print("---+---+---")
    print(" ",board[4] + "|" + " " + board[5] + " " + "|" + board[6])
    print("---+---+---")
    print(" ",board[7] + "|" + " " + board[8] + " " + "|" + board[9])


def playerX():
    global AvailableOptions
    print(AvailableOptions)
    option = int(input("What field would you like to play in?\n"))
    if option in AvailableOptions:
        AvailableOptions.remove(option)
        board[option] = "X"
        printBoard()
    else:
        print("NOT AVAILABLE")


def playerO():
    global AvailableOptions
    print(AvailableOptions)
    option = int(input("What field would you like to play in?\n"))
    if option in AvailableOptions:
        AvailableOptions.remove(option)
        board[option] = "O"
        printBoard()
    else:
        print("NOT AVAILABLE")
  
#Just a small startup welcome menu/info screen
def startup():
    typewrite("Welcome to Tic tac toe in Python - By Luis Wettre\n\n")
    typewrite("""The Rules are simple, there are 2 players that take turns on choosing a field.
The first player to reach 3 off their charachter in a row (Horizontal, Diagonal or Vertical) wins the game
if no one manages to do this, the game is a draw!\n
You pick the square you want to play in py choosing a number between 1 - 9, the first row being 1 - 3, second row 4 - 6 and third row 7 - 9\n\n""")
    
#Here i call all functions to start the game
startup()
printBoard()
playerX()
checkPlayerX()
playerO()
playerX()
checkPlayerX()
playerO()
playerX()
checkPlayerX()