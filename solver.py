# Sudoku solver
import numpy as np
import turtle
grid = [[8, 0, 4, 5, 0, 9, 6, 0, 1],
        [0, 9, 1, 0, 0, 0, 7, 4, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [7, 0, 0, 4, 0, 8, 0, 0, 6],
        [0, 0, 3, 0, 0, 0, 9, 0, 0],
        [4, 0, 0, 9, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 7, 6, 0, 0, 0, 5, 8, 0],
        [9, 0, 2, 8, 0, 7, 1, 0, 3]]

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("white")
wn.setup(width=800, height=800)
wn.tracer(0)


# gridline vertical
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=100, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-150, 0)

# gridline vertical
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=100, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(150, 0)

# gridline horizontal
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=0.5, stretch_len=100)
paddle_a.penup()
paddle_a.goto(0, -150)

# gridline horizontal
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=0.5, stretch_len=100)
paddle_a.penup()
paddle_a.goto(0, 150)

while True:
    wn.update()


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
