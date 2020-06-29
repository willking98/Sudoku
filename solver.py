# Sudoku solver
import numpy as np
grid = [[0, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 4, 0, 0, 0, 7],
        [4, 0, 9, 0, 0, 0, 0, 3, 0],
        [7, 0, 2, 0, 0, 8, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 6, 0, 0, 8, 0, 9],
        [0, 4, 0, 0, 0, 0, 6, 0, 3],
        [5, 0, 0, 0, 7, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 5, 0]]


def possible(y, x, n):
    global grid

    # Check row for number
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # Check column for number
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # Check box for number
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False

    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))

solve()
