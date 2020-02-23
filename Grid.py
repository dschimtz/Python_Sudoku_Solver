from tkinter import *

class SudokuFrame(Frame):
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.margin = 20
        self.side = 50
        self.width = self.margin * 2 + self.side * 9
        self.height = self.margin * 2 + self.side * 9

        self.__createSudokuUI()

    def __createSudokuUI(self):
        self.window.title("Sudoku")

        self.pack(fill=BOTH )
        self.canvas = Canvas(width = self.width, height = self.height)
        self.canvas.pack(fill=BOTH, side=TOP)

        self.__drawGrid()
        self.__drawPuzzle()

    def __drawGrid(self):
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

    def __drawPuzzle(self):
        for i in range(10):
            for j in range(10):
                x = self.margin + i * self.side + self.side / 2
                y = self.margin + j * self.side + self.side / 2
                self.canvas.create_text(x, y, text="0", )



root = Tk()

sudokuUI = SudokuFrame(root)

root.mainloop()