#!/usr/bin/python
import sys
import string
# ma pobierać dane od użytkownika
# funkcja ma nie przyjmowac parametrów
# return: funkcja ma zwracać położenie kółka x,y
def player():

    exception = 1
    while exception:
        exception = 0
        try:
            x = int(input("Enter coordinate x: "))
            y = int(input("Enter coordinate y: "))
        except Exception as e:
            print("Coordinate is a number, man!")
            exception = 1

    while True:
        if ((x >= 0 and x <=2) and (y >= 0 and y <= 2)):
            return x,y

        else:
            print("You're playing in tic tac toe game. Choose coordinate: 0, 1 or 2.")
            x,y = player()



# Funkcja ma wyświtlać planszę
# Funkcja potrzebuje planszę
# return: ma nie zwracać
def printBoard(stage):

    for i in range(len(stage)):
        for j in range(len(stage[i])):
        # print without new line
            print(stage[i][j], end=' ')
        print()

#sprawdzanie czy podane wspolrxedne sa wolne
def checkStageForPlayer(x,y):

    if (stage[x][y] != " "):
        return False
    else:
        return True


def checkWinner(stage, pionek):

    if ((stage[0][0] == pionek and stage[0][1]== pionek and stage[0][2]== pionek) #
    or (stage[1][0] == pionek and stage[1][1]== pionek and stage[1][2]== pionek)#
    or (stage[2][0] == pionek and stage[2][1]== pionek and stage[2][2]== pionek)#
    or (stage[0][0] == pionek and stage[1][0]== pionek and stage[2][0]== pionek)#
    or (stage[0][1] == pionek and stage[1][1]== pionek and stage[2][1]== pionek)#
    or (stage[0][2] == pionek and stage[1][2]== pionek and stage[2][2]== pionek)#
    or (stage[0][0] == pionek and stage[1][1]== pionek and stage[2][2]== pionek)#
    or (stage[2][0] == pionek and stage[1][1]== pionek and stage[0][2]== pionek)):
        return True
    else:
        return False

def checkDraw(stage):

    for i in range(len(stage)):
        for j in range(len(stage[i])):
            if (stage[i][j] == " "):
                return False
    return True

#########################################

movePlayer1 = 0
movePlayer2 = 0

stage = [[' ', ' ', ' ',],  #plansza
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

while (True):

# gracz 1
    print("Player 1: ")
    x, y = player()
    if checkStageForPlayer(x,y):
        stage[x][y] = 'o'
    else:
        print("This place is already occupied.")
        continue

    movePlayer1 += 1

    printBoard(stage)

    if(movePlayer1 >=3):
        if (checkWinner(stage, "o")):
            print("Player 1: Congratulations, you win!!!")
            exit()

    if (checkDraw(stage)):
        print("Ups, it's a draw. Try again.")
        exit()



# gracz2
    print("Player 2: ")
    x, y = player()
    if checkStageForPlayer(x, y):
        stage[x][y] = 'x'
    else:
        print("This place is already occupied.")
        continue

    movePlayer2 += 1

    printBoard(stage)

    if(movePlayer2 >=3):
        if (checkWinner(stage, "x")):
            print("Player 2: Congratulations, you win!!!")
            exit()

    if (checkDraw(stage)):
        print("Ups, it's a draw. Try again.")
        exit()






