def checkValues(values, val):
    if val == ".":
        return True
    val = int(val) - 1
    if values[val] == 0:
        values[val] = 1
    else:
        print("Duplicate found", val+1)
        return False
    return True

def checkValidRow(grid, rowNum):
    # returns true if there is exactly one "val" in given row
    values = [0] * 9
    for val in grid[rowNum]:
        if not checkValues(values, val):
            return False
    return True


def checkValidCol(grid, colNum):
    values = [0] * 9

    for i in range(9):
        val = grid[i][colNum]
        if not checkValues(values, val):
            return False
    return True

def checkValidBlock(grid, r,c):
    # this is the hard one, return true if the "val" only appears once in a 3x3 grid
    values = [0] * 9

    for i in range(3):
        for j in range(3):
            val = grid[(r*3)+i][(c*3)+j]
            if not checkValues(values, val):
                return False
    return True


def sudoku2(grid):
    for i in range(9):
        if not checkValidRow(grid, i):
            print ("Error in row", i)
            return False
        if not checkValidCol(grid, i):
            print ("Error in col", i)
            return False
        
    for i in range(3):
        for j in range(3):
            if not checkValidBlock(grid, i,j):
                print ("Error in block", i, j)
                return False

    return True

grid = [[".",".",".","1","4",".",".","2","."], 
 [".",".","6",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".","1",".",".",".",".",".","."], 
 [".","6","7",".",".",".",".",".","9"], 
 [".",".",".",".",".",".","8","1","."], 
 [".","3",".",".",".",".",".",".","6"], 
 [".",".",".",".",".","7",".",".","."], 
 [".",".",".","5",".",".",".","7","."]]

sudoku2(grid)