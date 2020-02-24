class SudokuGame():
    def __init__(self, **kwargs):
        self.__init_board(0)

    def __init_board(self, boardID):
        with open("sudokuboards.txt", 'r') as f:
            lines = f.readlines()
            index = boardID * 10 - 10
            self.board = []
            for i in range(index+1, index+10):
                string = lines[i]
                row = []
                for j in range(9):
                    row.append(int(string[j]))
                self.board.append(row)

    def load_new_board(self, boardID):
        self.__init_board(boardID)