import time
from game import Game
from move import Move

class HardBot:
    def __init__(self):
        self.board = Game()
        self.move = Move()
        self.playerSymbol = "X"
        self.botSymbol = "O"

    def startGame(self):
        print("Gra z trudnym botem.\n")
        print("Indexy pól:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]\n")
        while True:
            self.move.playerMove(self.board, self.playerSymbol)
            self.board.printBoard()
            status = self.board.checkWin()
            if status != 0:
                self.endGame(status)
                break

            print("\nRuch bota:")
            time.sleep(0.8)
            self.move.hardBotMove(self.board, self.botSymbol, self.playerSymbol)
            self.board.printBoard()
            status = self.board.checkWin()
            if status != 0:
                self.endGame(status)
                break

    def endGame(self, status):
        if status == self.playerSymbol:
            print("Gratulacje! Wygrałeś!")
        elif status == self.botSymbol:
            print("Bot wygrał!")
        elif status == "Remis":
            print("Remis!")
        self.board.saveResult(status)