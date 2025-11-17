from game import Game
from move import Move

class EasyBotVsEasyBot:
    def __init__(self):
        self.board = Game()
        self.move = Move()
        self.bot1Symbol = "X"
        self.bot2Symbol = "O"

    def startGame(self):
        print("Gra Easy Bot vs Easy Bot.\n")
        print("Indexy pól:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]\n")
        while True:
            print("\nRuch Bota 1:")
            self.move.easyBotMove(self.board, self.bot1Symbol)
            self.board.printBoard()
            status = self.board.checkWin()
            if status != 0:
                self.endGame(status)
                break

            print("\nRuch Bota 2:")
            self.move.easyBotMove(self.board, self.bot2Symbol)
            self.board.printBoard()
            status = self.board.checkWin()
            if status != 0:
                self.endGame(status)
                break

    def endGame(self, status):
        if status == self.bot1Symbol:
            print("Bot 1 wygrał!")
        elif status == self.bot2Symbol:
            print("Bot 2 wygrał!")
        elif status == "Remis":
            print("Remis!")
        self.board.saveResult(status)