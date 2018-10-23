#!/usr/bin/python
import sys
import string
# ma pobierać dane od użytkownika
# funkcja ma nie przyjmowac parametrów
# return: funkcja ma zwracać położenie kółka x,y
def player():
    wyjatek = 1
    while wyjatek:
        wyjatek = 0
        try:
            x = int(input("podaj wspolrzedne x: "))
            y = int(input("podaj wspolrzedne y: "))
        except Exception as e:
            print("Wspolrzedna to liczba, czopie!")
            wyjatek = 1

    while True:
        if ((x >= 0 and x <=2) and (y >= 0 and y <= 2)):
            return x,y

        else:
            print("Grasz w kolko - krzyzyk! Wybierz wspolrzedne: 0, 1 lub 2.")
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
    print("Gracz 1: ")
    x, y = player()
    if checkStageForPlayer(x,y):
        stage[x][y] = 'o'
    else:
        print("Miejsce jest zajete")
        continue

    movePlayer1 += 1

    printBoard(stage)

    if(movePlayer1 >=3):
        if (checkWinner(stage, "o")):
            print("Gracz 1: Brawo, wygrales!!")
            exit()

    if (checkDraw(stage)):
        print("Ups, remis. Sprobuj ponownie.")
        exit()



# gracz2
    print("Gracz 2: ")
    x, y = player()
    if checkStageForPlayer(x, y):
        stage[x][y] = 'x'
    else:
        print("Miejsce jest zajete")
        continue

    movePlayer2 += 1

    printBoard(stage)

    if(movePlayer2 >=3):
        if (checkWinner(stage, "x")):
            print("Gracz 1: Brawo, wygrales!!")
            exit()

    if (checkDraw(stage)):
        print("Ups, remis. Sprobuj ponownie.")
        exit()






