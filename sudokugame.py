import numpy as np
import argparse

class SudokuGame():
    def __init__(self, **kwargs):
        self.boardtype = "empty"
        for key, value in kwargs.items():
            if key == "boardtype":
                self.boardtype = value
        self.__init_board()

    def __init_board(self):
        if self.boardtype == "empty":
            self.board = np.zeros([9,9])
        elif self.boardtype == "random":
            self.board = np.random.randint(10, size=[9,9])
        #print(self.board)

