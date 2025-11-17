import datetime

class Game:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def makeMove(self, place, symbol):
        row = (place - 1) // 3
        col = (place - 1) % 3
        if self.board[row][col] == 0:
            self.board[row][col] = symbol
            return True
        return False

    def printBoard(self):
        for row in self.board:
            row_str = [str(cell) if cell != 0 else " " for cell in row]
            print(" | ".join(row_str))
        print()

    def checkWin(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != 0:
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0:
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]

        if all(cell != 0 for row in self.board for cell in row):
            return "Remis"

        return 0

    def saveResult(self, winner):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("result.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{now}\n")
            for row in self.board:
                row_str = [str(cell) if cell != 0 else " " for cell in row]
                file.write(" | ".join(row_str) + "\n")
            file.write(f"Wynik: {winner}\n")