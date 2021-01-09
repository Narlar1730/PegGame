import math
import colorama
from colorama import Fore, Style


class gameBoard:
    def __init__(self):
        self.board = ["R", "R", "R", "R", "O", "O", "B", "B", "B", "B"]

    def printBoard(self):
        outStr = ""
        for i in self.board:
            outStr = outStr + i
            if i == "R":
                print(Fore.RED + i + " ", end='')
            elif i == "B":
                print(Fore.BLUE + i + " ", end='')
            elif i == "O":
                print(Style.RESET_ALL, end='')
                print(i + " ", end='')

        print(Style.RESET_ALL)


    def printLabels(self):
        total = len(self.board)
        for i in range(0, total):
            print(str(i) + " ", end = '')
        print(Style.RESET_ALL)

    def printNewLine(self):
        for i in self.board:
            print("--", end ='')
        print(Style.RESET_ALL)

newGame = gameBoard()
newGame.printBoard()
newGame.printLabels()
newGame.printNewLine()
