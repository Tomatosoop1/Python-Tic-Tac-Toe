import time
import os

CurrentPlayer = "X"
AvailableOptions = [1,2,3,4,5,6,7,8,9]
#The typewrite functions doesnt serve a real purpose its purely cosmetic
def typewrite(str):
    for x in str:
        time.sleep(0.022)
        print(x,end="")

def rematch():
    global AvailableOptions
    global board
    AvailableOptions = [1,2,3,4,5,6,7,8,9]
    board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
    }
    user_input = input("Do you want to play again y/n ? \n")
    while True:
        if user_input == "y":
            os.system('cls')
            printBoard()    
            Player()
            break
        elif user_input == "n":
            quit()
        else:
            print("Not a valid answer")
            rematch()
            break

os.system('cls')

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


def checkPlayerX(first_row,second_row,third_row,first_collumn,second_collumn,third_collumn,first_diagonal,second_diagonal):
    element = "X"

    first_row = [board[1],board[2],board[3]]
    second_row = [board[4],board[5],board[6]]
    third_row = [board[7],board[8],board[9]]
    
    first_collumn = [board[1],board[4],board[7]]
    second_collumn = [board[2],board[5],board[8]]
    third_collumn = [board[3],board[6],board[9]]

    first_diagonal = [board[1],board[5],board[9]]
    second_diagonal = [board[3],board[5],board[7]]

    check_first_row = True
    check_second_row = True
    check_third_row = True

    check_first_collumn = True
    check_second_collumn = True
    check_third_collumn = True

    check_first_diagonal = True
    check_second_diagonal = True

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
    
    for item in first_collumn:
        if element != item:
            check_first_collumn = False
            break

    for item in second_collumn:
        if element != item:
            check_second_collumn = False
            break 

    for item in third_collumn:
        if element != item:
            check_third_collumn = False
            break 
    
    for item in first_diagonal:
        if element != item:
            check_first_diagonal = False
            break 
    
    for item in second_diagonal:
        if element != item:
            check_second_diagonal = False
            break 


    if check_first_row or check_second_row or check_third_row or check_first_collumn or check_second_collumn or check_third_collumn or check_first_diagonal or check_second_diagonal == True:
        print("Congratuations Player X you won!")
        rematch()

def checkPlayerO(first_row,second_row,third_row,first_collumn,second_collumn,third_collumn,first_diagonal,second_diagonal):
    element = "O"

    first_row = [board[1],board[2],board[3]]
    second_row = [board[4],board[5],board[6]]
    third_row = [board[7],board[8],board[9]]
    
    first_collumn = [board[1],board[4],board[7]]
    second_collumn = [board[2],board[5],board[8]]
    third_collumn = [board[3],board[6],board[9]]

    first_diagonal = [board[1],board[5],board[9]]
    second_diagonal = [board[3],board[5],board[7]]

    check_first_row = True
    check_second_row = True
    check_third_row = True

    check_first_collumn = True
    check_second_collumn = True
    check_third_collumn = True

    check_first_diagonal = True
    check_second_diagonal = True

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
    
    for item in first_collumn:
        if element != item:
            check_first_collumn = False
            break

    for item in second_collumn:
        if element != item:
            check_second_collumn = False
            break 

    for item in third_collumn:
        if element != item:
            check_third_collumn = False
            break 
    
    for item in first_diagonal:
        if element != item:
            check_first_diagonal = False
            break 
    
    for item in second_diagonal:
        if element != item:
            check_second_diagonal = False
            break 

    if check_first_row or check_second_row or check_third_row or check_first_collumn or check_second_collumn or check_third_collumn or check_first_diagonal or check_second_diagonal == True:
        print("Congratuations Player O you won!")
        rematch()

def printBoard():
    global board
    print(" ",board[1] + "|" + " " + board[2] + " " + "|" + board[3])
    print("---+---+---")
    print(" ",board[4] + "|" + " " + board[5] + " " + "|" + board[6])
    print("---+---+---")
    print(" ",board[7] + "|" + " " + board[8] + " " + "|" + board[9])

def Player():
    global AvailableOptions
    global CurrentPlayer
    while True:
        if CurrentPlayer == "X":
            while True:
                print(AvailableOptions)
                try:
                    option = int(input("What field would you like to play in?\n"))
                except ValueError:
                    print("Not and int!")
                    continue

                if option in AvailableOptions:
                    AvailableOptions.remove(option)
                    board[option] = "X"
                    os.system('cls')
                    printBoard()
                    checkPlayerX(first_row,second_row,third_row,first_collumn,second_collumn,third_collumn,first_diagonal,second_diagonal)
                    CurrentPlayer = "O"
                    gameEnd = len(AvailableOptions)

                    if gameEnd == 0:
                        print("It's a draw!")
                        quit()
                    break
                else:   
                    print("NOT AVAILABLE")  
        elif CurrentPlayer == "O":
             while True:
                print(AvailableOptions)
                try:
                    option = int(input("What field would you like to play in?\n"))
                except ValueError:
                    print("Not and int!")
                    continue
                
                if option in AvailableOptions:
                    AvailableOptions.remove(option)
                    board[option] = "O"
                    os.system('cls')
                    printBoard()
                    checkPlayerO(first_row,second_row,third_row,first_collumn,second_collumn,third_collumn,first_diagonal,second_diagonal)
                    CurrentPlayer = "X"
                    break
                else:
                    print("NOT AVAILABLE")  


#Just a small startup welcome menu/info screen this will be more usefull later when i add a remtach feature, rn this would need to be a function
def startup():
    typewrite("Welcome to Tic tac toe in Python - By Luis Wettre\n\n")
    typewrite("""The Rules are simple, there are 2 players that take turns on choosing a field.
The first player to reach 3 off their charachter in a row (Horizontal, Diagonal or Vertical) wins the game
if no one manages to do this, the game is a draw!\n
You pick the square you want to play in py choosing a number between 1 - 9, the first row being 1 - 3, second row 4 - 6 and third row 7 - 9\n\n""")
    
#Here i call all functions to start the game




startup()
printBoard()    
Player()

