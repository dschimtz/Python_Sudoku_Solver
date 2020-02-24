import tkinter as tk
from sudokugame import SudokuGame

class SudokuFrame(tk.Frame):
    def __init__(self, parent, game):
        super().__init__()
        self.parent = parent
        self.game = game

        self.margin = 20
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9

        self.__create_sudoku_UI()

    def __create_sudoku_UI(self):
        self.parent.title("Sudoku")

        self.pack(fill=tk.BOTH )
        self.canvas = tk.Canvas(width = self.width, height = self.height)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)

        var = tk.StringVar(self.parent)
        var.set("0")
        self.dropdown = tk.OptionMenu(self.parent, var, "one", "two", "three")
        self.dropdown.pack(side=tk.LEFT)
        

        self.__draw_grid()
        self.__draw_numbers()

    def __draw_grid(self):
        for i in range(10):
            if i % 3 == 0:
                color = "blue"
            else:
                color = "gray"
            x0 = self.margin + i * self.side
            y0 = self.margin
            x1 = self.margin + i * self.side
            y1 = self.height - self.margin
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = self.margin
            y0 = self.margin + i * self.side
            x1 = self.width - self.margin
            y1 = self.margin + i * self.side
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_numbers(self):
        for i in range(9):
            for j in range(9):
                if self.game.board[i][j] != 0:
                    x = self.margin + i * self.side + self.side / 2
                    y = self.margin + j * self.side + self.side / 2
                    self.canvas.create_text(x, y, text=self.game.board[i][j])

root = tk.Tk()
game = SudokuGame(boardtype="random")

sudokuUI = SudokuFrame(root, game)

root.mainloop()