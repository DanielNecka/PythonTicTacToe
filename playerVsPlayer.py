from game import Game
from move import Move

class PlayerVsPlayer:
    def __init__(self):
        self.board = Game()
        self.move = Move()
        self.player1Symbol = "X"
        self.player2Symbol = "O"

    def startGame(self):
        print("Gra dla dwóch graczy lokalnie.\n")
        print("Indexy pól:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]\n")
        while True:
            self.move.playerMove(self.board, self.player1Symbol)
            self.board.printBoard()
            status = self.board.checkWin()
            if status != 0:
                self.endGame(status)
                break

            self.move.playerMove(self.board, self.player2Symbol)
            self.board.printBoard()
            status = self.board.checkWin()
            if status != 0:
                self.endGame(status)
                break

    def endGame(self, status):
        if status == self.player1Symbol:
            print("Gratulacje! Gracz 1 wygrał!")
        elif status == self.player2Symbol:
            print("Gratulacje! Gracz 2 wygrał!")
        elif status == "Remis":
            print("Remis!")
        self.board.saveResult(status)