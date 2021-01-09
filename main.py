import math
import colorama
from colorama import Fore, Style
import sys
# Globals
playing = False

class gameBoard:
    def __init__(self):
        self.board = ["R", "R", "R", "R", "O", "O", "B", "B", "B", "B"]
    
    def copy(self, otherBoard):
        size = len(self.board)
        for i in range(0, size):
            self.board[i] = otherBoard.board[i]             



    ### PRINT BOARD ###

    def print(self):
        self.printBoard()
        self.printLabels()
        self.printNewLine()

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

    ### Make MOVE ###
    # R -> RIGHT
    # B -> LEFT
    def makeMove(self, Move, verbose):
        canCheck = self.moveInputCheck(Move, verbose)
        validMove = canCheck[0]
        move_int = canCheck[1]
        boardList = self.board
        moveMade = False
        if validMove:
            currentPiece = boardList[move_int]
            # RED LOGIC
            if currentPiece == "R":
                try:
                    pieceUp = boardList[move_int+1]
                    if pieceUp == "O":
                        boardList[move_int+1] = "R"
                        boardList[move_int] = "O"
                        moveMade = True
                    elif pieceUp == "B":
                        try:
                            pieceUpUp = boardList[move_int + 2]
                            if pieceUpUp == "O":
                                boardList[move_int + 2] = "R"
                                boardList[move_int] = "O"
                                moveMade = True
                            else:
                                pieceUpUp = boardList[20000]
                        except:
                            if verbose:
                                print(Fore.RED + "Invalid move, space is full or off the board" + Style.RESET_ALL)
                    else:
                        if verbose:
                            print(Fore.RED + "Invalid move, can't jump same colour" + Style.RESET_ALL)
                except:
                    if verbose:
                        print(Fore.RED + "Cannot move piece: " + Move + " it is on the edge of the board" + Style.RESET_ALL)
            # BLUE LOGIC
            elif currentPiece == "B":
                try:
                    pieceDown = boardList[move_int-1]
                    if pieceDown == "O":
                        boardList[move_int] = "O"
                        boardList[move_int-1] = "B"
                        moveMade = True
                    elif pieceDown == "R":
                        try:
                            pieceDownDown = boardList[move_int - 2]
                            if pieceDownDown == "O":
                                boardList[move_int - 2] = "B"
                                boardList[move_int] = "O"
                                moveMade = True
                            else:
                                pieceDownDown = boardList[20000]
                        except:
                            if verbose:
                                print(Fore.RED + "Invalid move, space is full or off the board" + Style.RESET_ALL)
                    else:
                        if verbose:
                            print(Fore.RED + "Invalid move, can't jump same colour" + Style.RESET_ALL)
                except:
                    if verbose:
                        print(Fore.RED + "Cannot move piece: " + Move + " it is on the edge of the board" + Style.RESET_ALL)
        
        return moveMade

    def moveInputCheck(self, Move, verbose):
        move_int = 100
        out = [False, move_int]
        if Move == "l" or Move == "L":
          sys.exit()
        try:
            move_int = int(Move)
            if move_int > 10 or move_int < 0:
                if verbose:
                    print(Fore.RED + "Move ERR. Move Number: " + Move + " is not a valid move" + Style.RESET_ALL)
            else:
                out = [True, move_int]
        except:
            if verbose:
                print(Fore.RED + "Move ERR. Cannot Convert move: " + Move + " into an integer, please try again" + Style.RESET_ALL)
        return out
        
    # Win and lose conditions
    def GameWon(self):
        boardLst = self.board
        if boardLst == ["B", "B", "B", "B", "O", "O", "R", "R", "R", "R"]:
            return True
        return False

    def GameLostSlow(self):
        AllMoves = self.GetAllMoves()
        if len(AllMoves) == 0:
            return True
        return False

    #FIXME
    def GameLostQuick(self):
        pass

    def GetAllMoves(self):
        boardList = self.board
        sizeList = len(boardList)
        newBoard = gameBoard()
        AllMoves = []

        for i in range(0, sizeList):
            newBoard.copy(self)
            moveMade = newBoard.makeMove(i, False)
            if moveMade:
                AllMoves.append(i)
        return AllMoves

def makeAllmoves(board):
    pass

newGame = gameBoard()
if playing:
    while playing:
        newGame.print()
        print("All Moves available: " + str(newGame.GetAllMoves()))
        text = input("Move? ")
        moveMade = newGame.makeMove(text, True)
        #print("Game Won: " + str(newGame.GameWon()))
        #print("Game LostSlow: " + str(newGame.GameLostSlow()))

        if newGame.GameLostSlow():
            playing = False
            print(Fore.RED + "GAME OVER, FINAL BOARD: " + Style.RESET_ALL)
            newGame.print()
else:
    movesMade = []
    


