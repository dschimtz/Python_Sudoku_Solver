import tkinter as tk
from sudokugame import SudokuGame
import numpy as np

class SudokuFrame(tk.Frame):
    def __init__(self, parent, game):
        """initializes the UI

        Args:
          parent (master TK frame): master frame where the SudokuFrame is stored
          game (SudokuGame object): sudoku game that holds the game's current state
        """

        super().__init__()
        self.parent = parent
        self.game = game

        # Used to draw the grid and the numbers
        self.margin = 20    # The width of the margin in pixels
        self.side = 50  # The width/height of each cell
        self.width = self.margin * 2 + self.side * 9    # Width of entire sudoku board
        self.height = self.margin * 2 + self.side * 9   # Height of entire sudoku board

        self.__create_sudoku_UI()

    def __create_sudoku_UI(self):
        """ Creates the UI which will be contained inside a canvas. Sets 
        the title, creates a dropdown where user can select a starting grid,
        a dropdown where the user can select their algorithm, and a button that
        starts the algorithm
        """
        self.parent.title("Sudoku")

        self.pack(fill=tk.BOTH )
        self.canvas = tk.Canvas(width = self.width, height = self.height)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)

        self.__create_grid_dropdown()
        self.__create_algorithm_dropdown()
        self.__create_start_algo_button()
        
        self.__draw_grid()
        self.__draw_init_numbers()

    def __create_grid_dropdown(self):
        grids = ["Grid 01", "Grid 02", "Grid 03", "Grid 04", "Grid 05"]
        self.dropdown_var = tk.StringVar(self.parent)
        self.dropdown_var.set(grids[0])
        self.grid_dropdown = tk.OptionMenu(self.parent, self.dropdown_var, *grids)
        self.grid_dropdown.pack(fill=tk.BOTH ,side=tk.LEFT)
        self.dropdown_var.trace("w", self.__draw_init_numbers)

    def __create_algorithm_dropdown(self):
        algorithms = ["backtracking"]
        self.algo_var = tk.StringVar(self.parent)
        self.algo_var.set(algorithms[0])
        self.algo_dropdown = tk.OptionMenu(self.parent, self.algo_var, *algorithms)
        self.algo_dropdown.pack(fill=tk.BOTH ,side=tk.RIGHT)

    def __create_start_algo_button(self):
        self.algo_button = tk.Button(self.parent, text="Start Algorithm")
        self.algo_button.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def __draw_grid(self):
        for i in range(10):
            if i % 3 == 0:
                color = "black"
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

    def __draw_init_numbers(self, *args):
        """Draws the initial configuration. Called when the user selects
        a new grid from the grid dropdown menu, or when the grid is first
        drawn.
        """
        self.__delete_all_numbers()
        boardID = int(self.dropdown_var.get()[-2:])

        """Store the initial configuration such that the initial numbers and the
        ones inputted by an algorithm can be differentiated, such that the two
        can be drawn in two different colors"""
        self.init_board = self.game.load_new_board(boardID)

        for i in range(9):
            for j in range(9):
                if self.game.board[i][j] != 0:
                    x = self.margin + i * self.side + self.side / 2
                    y = self.margin + j * self.side + self.side / 2
                    self.canvas.create_text(x, y, text=self.game.board[i][j], tag="numbers", fill="black")

    def update_numbers(self):
        for i in range(9):
            for j in range(9):
                # Only draw the number if it isn't blank and if it isn't part of the starting configuration
                if self.game.board[i][j] != 0 and self.init_board[i][j] == 0:
                    x = self.margin + i * self.side + self.side / 2
                    y = self.margin + j * self.side + self.side / 2
                    self.canvas.create_text(x, y, text=self.game.board[i][j], tag="numbers", fill="green")

    def __delete_all_numbers(self):
        self.canvas.delete("numbers")

root = tk.Tk()
game = SudokuGame()
sudokuUI = SudokuFrame(root, game)
root.mainloop()