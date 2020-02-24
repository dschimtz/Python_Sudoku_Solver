import pprint

def load_board(gridID):
    with open("sudokuboards.txt", 'r') as f:
        lines = f.readlines()
        index = gridID * 10 - 10
        puzzle = []
        for i in range(index+1, index+10):
            string = lines[i]
            row = []
            for j in range(9):
                row.append(string[j])
            puzzle.append(row)
        
        pprint.pprint(puzzle)

load_board(50)