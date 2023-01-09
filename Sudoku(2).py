import numpy as np

grid = [[0,8,0,0,0,7,6,0,0],
        [0,0,1,6,5,0,0,0,2],
        [5,0,0,0,0,3,0,0,0],
        [4,0,0,5,2,0,8,0,0],
        [0,0,7,0,0,0,0,4,0],
        [0,0,0,0,3,0,0,0,0],
        [0,0,0,0,0,6,0,0,0],
        [0,9,0,0,0,0,0,0,1],
        [7,0,0,8,4,0,2,0,0]]

def possible(row, column, number):
    global grid

    #is the number already in row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #is the number already in column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    #is the number already in square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range (0,3):
        for j in range(0,3):
            if grid [y0+i] [x0+j] == number:
                return False
    return True

def solve():
    global grid
    for row in range (0,9):
        for column in range(0,9):
            if grid[row] [column] == 0:
                for number in range (1,10):
                    if possible(row, column, number):
                        grid[row] [column] = number
                        solve()
                        grid[row] [column] = 0

                return

    print(np.matrix(grid))
    input('Done')

solve()