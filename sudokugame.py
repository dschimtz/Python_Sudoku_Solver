class SudokuGame():
    def __init__(self, **kwargs):
        self.__init_board(0)

    def __init_board(self, boardID):
        """Loads in a new sudoku board

        Args:
            boardID (int): identifier for the board you want to load in
        """
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
            
            # transpose the board
            temp = self.board
            self.board = [[row[i] for row in temp] for i in range(len(temp[0]))]


    def load_new_board(self, boardID):
        """Loads a new board and returns it"""
        self.__init_board(boardID)
        return self.__init_board(boardID)

    def check_row(self, rowid):
        """Checks whether the inputted row is legal

        Args:
            row (int): row to check. Valid inputs are [0,8]

        Out: True if column is legal, else false
        """
        row = []
        for i in range(9):
            row.append(self.board[i][rowid])
        print(row)
        return set(row) == set(range(1,10))

    def check_column(self, colid):
        """Checks whether the inputted column is legal

        Args:
            column (int): column to check. Valid inputs are [0,8]

        Out: True if column is legal, else false
        """
        column = self.board[colid]
        return set(column) == set(range(1,10))

    def check_square(self, rowid, colid):
        """Checks whether the square that the inputted row
        and column is in is legal

        Args:
            rowid (int): row of the square. Valid inputs are 0,1,2
            colid (int): column of the square. Valid inputs are 0,1,2

        Out: True if square is legal, else false
        """
        square = [
            self.board[r][c] 
            for r in range(rowid * 3, (rowid + 1) * 3) 
            for c in range(colid * 3, (colid + 1) * 3)
        ]

        print(square)

    def find_square(self, rowid, colid):
        """Finds which square the inputted row and column resides in

        Args:
            rowid (int): row of the grid point. Valid inputs are [0,8]
            colid (int): column of the grid point. Valid inputs are [0,8]

        Out:
            row and column of the square rowid and colid resides in as a tuple (row,column)
        """
        if rowid <= 2:
            column = 0
        elif rowid > 2 and rowid <= 5:
            column = 1
        elif rowid > 5 and rowid <= 8:
            column = 2

        if colid <= 2:
            row = 0
        elif colid > 2 and rowid <= 5:
            row = 1
        elif colid > 5 and rowid <= 8:
            row = 2

        return(row, column)