import random
from game import Game

class Move:
    def playerMove(self, board: Game, symbol):
        while True:
            try:
                choice = int(input("Twój ruch (1-9): "))
            except ValueError:
                print("Podaj poprawną opcję")
                continue
            if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if board.makeMove(choice, symbol):
                    break
                else:
                    print("To pole jest zajęte!")
            else:
                print("Podaj poprawną opcję")

    def easyBotMove(self, board: Game, symbol):
        while True:
            choice = random.randint(1, 9)
            if board.checkPlace((choice - 1) // 3, (choice - 1) % 3):
                board.makeMove(choice, symbol)
                break

    def hardBotMove(self, board: Game, symbol, opponent_symbol):
        for row in range(3):
            for col in range(3):
                if board.checkPlace(row, col):
                    board.board[row][col] = symbol
                    if board.checkWin() == symbol:
                        return
                    board.board[row][col] = 0

        for row in range(3):
            for col in range(3):
                if board.checkPlace(row, col):
                    board.board[row][col] = opponent_symbol
                    if board.checkWin() == opponent_symbol:
                        board.board[row][col] = symbol
                        return
                    board.board[row][col] = 0

        if board.checkPlace(1, 1):
            board.board[1][1] = symbol
            return

        for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if board.checkPlace(row, col):
                board.board[row][col] = symbol
                return

        for row, col in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if board.checkPlace(row, col):
                board.board[row][col] = symbol
                return