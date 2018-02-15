import random
import time
#import sys
#import os
from time import sleep

#2D array to store the grid selections for user
grid = [['1','2','3'],['4','5','6'],['7','8','9']]

#Variable used to monitor turns
playerTurn = 0

def initGrid(grid):
    #variable gobalised so it can be accessed insdie the function
    global playerTurn
    #Prints out the current grid to the user
    print("\n\t\t\t\t\t"+str(grid[0][0])+" | "+grid[0][1]+" | "+grid[0][2]+"\n\t\t\t\t\t---------\n\t\t\t\t\t"+grid[1][0]+" | "+grid[1][1]+" | "+grid[1][2]+"\n\t\t\t\t\t---------\n\t\t\t\t\t"+grid[2][0]+" | "+grid[2][1]+" | "+grid[2][2])
    #Decides whos turn it is depending if its an even or odd number, then calling the respective functions
    checkWin(grid,playerTurn)
    if playerTurn%2 == 0:
        userChoice()
    else:
        computerChoice()
def userChoice():
    #Dashes to show user that its another round of turns
    print("\t\t\t-------------------------------------------")
    #variable gobalised so it can be accessed insdie the function
    global choice
    choice = 0
    #choice must be between 1-9, else they must try again.
    while str(choice) not in ['1','2','3','4','5','6','7','8','9']:
        choice = input("\n\t\t\t\tPlease enter between 1- 9: ")
    #after valid selection, the grid is updated with users choice.
    updateGrid()

#user choice is updated on the grid
def updateGrid():
    #variable gobalised so it can be accessed insdie the function
    global choice
    global playerTurn
    #count is used to check if the chosen box is already taken so the userChoice() is called again.
    count = 0
    #Loop and logic to search for option on grid, if taken, user enters choice again, if not, matrix is updated with new choice.
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if str(grid[i][j]) == str(choice):
                    grid[i][j] = "X"
                    count = 1
    #if count=0, this means the choice was taken and user must re do chice, call userChoice funcyion again
    if count == 0:
        #User feedback
        print("\t\t\t\t\tThat choice is already taken")
        userChoice()
    else:
        #If option is avaliable, the playerTurn inceremets to show its the oppositions turn(computer)
        playerTurn += 1
        initGrid(grid)

def computerChoice():
    #variable gobalised so it can be accessed insdie the function
    global choice
    global playerTurn
    choice = None
    #Array to hold the avaliable choices
    choicesLeft = []
    #This loops adds all the integers in the grid (the avaliable options) to the choicesLeft array
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            try:
                choicesLeft.append(int(grid[i][j]))
            #If the choice is taken, it will not be a number, it will be an X or O, therefore execption Error is used.
            except ValueError:
                #This value is not added to the array.
                pass
    #If no choices avalible, the game is a draw and app closes.
    if len(choicesLeft) == 0:
        time.sleep(1)
        print("\n\t\t\t\t\t Draw!")
        time.sleep(1)
        exit()
    #Computer generates a random number from 1-9 until the option chosen is avaliable.
    while choice not in choicesLeft:
        choice = random.randint(1,9)
    #update the grid with computer choice
    updateGridcomp()

def updateGridcomp():
    time.sleep(1)
    print("\n\t\t\t\t     Computer's turn")
    time.sleep(1)
    #variable gobalised so it can be accessed insdie the function
    global playerTurn
    global choice
    #Loop and logic to search for option on grid, if taken, user enters choice again, if not, matrix is updated.
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if str(grid[i][j]) == str(choice):
                    grid[i][j] = "O"
    #The grid is then printed out to user and the turns are switched.
    playerTurn += 1
    initGrid(grid)


#This is all the possible combinations of winning
#if any one is present at any given time, the display winner function is triggered.
def checkWin(grid,lastTurn):
    winner = lastTurn%2
    if grid[0] == ['X','X','X'] or grid[1] == ['X','X','X'] or grid[2] == ['X','X','X']:
        displayWinner(winner)
    elif grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        displayWinner(winner)
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        displayWinner(winner)
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        displayWinner(winner)
    elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        displayWinner(winner)
    elif grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        displayWinner(winner)


    elif grid[0] == ['O','O','O'] or grid[1] == ['O','O','O'] or grid[2] == ['O','O','O']:
        displayWinner(winner)
    elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        displayWinner(winner)
    elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        displayWinner(winner)
    elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        displayWinner(winner)
    elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        displayWinner(winner)
    elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        displayWinner(winner)
        
def displayWinner(whoWon):
    #if user was the last one to have a turn they win.
    if whoWon == 1:
        time.sleep(1)
        print("\n\n\t\t\t\t\t You Win!")
        time.sleep(1)
        exit()
    #if user wasnt the lastone to havea  turn, the computer wins.
    else:
        time.sleep(1)
        print("\n\n\t\t\t\t      Computer Wins!")
        time.sleep(1)
        exit()

initGrid(grid)
