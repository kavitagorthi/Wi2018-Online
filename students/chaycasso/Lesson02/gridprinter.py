#Grid Printer Exercise
#Chay Casso, 1/29/18

def grid1():
    """Draw a simple 2x2 grid composed of 5x5 squares."""
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print(plus + blankminus * 4 + blank + plus + blankminus * 4 + blank + plus)
    for i in range(1, 5):
        print(pipe + blank * 9 + pipe + blank * 9 + pipe)
    print(plus + blankminus * 4 + blank + plus + blankminus * 4 + blank + plus)
    for i in range(1, 5):
        print(pipe + blank * 9 + pipe + blank * 9 + pipe)
    print(plus + blankminus * 4 + blank + plus + blankminus * 4 + blank + plus)

def GridLine2(gridsize=3):
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print(plus + blankminus * int((gridsize - 1) / 2) + blank + plus + blankminus * int((gridsize - 1) / 2) + blank + plus)

def GridSpace2(gridsize=3):
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print(pipe + blank * gridsize + pipe + blank * gridsize + pipe)

def grid2(gridsize=3):
    GridLine2(gridsize)
    for i in range(1, int((gridsize + 1) / 2)):
        GridSpace2(gridsize)
    GridLine2(gridsize)
    for i in range(1, int((gridsize + 1) / 2)):
        GridSpace2(gridsize)
    GridLine2(gridsize)

# The use of gridsize is different between Part 2 and Part 3 because it changes in the given examples for Part 2 and
# Part 3.

def GridLine3(columns = 2, gridsize = 3):
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print((plus + blankminus * gridsize + blank) * columns + plus)

def GridSpace3(columns = 2, gridsize = 3):
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print((pipe + blank * (gridsize * 2 + 1)) * columns + pipe)

def grid3(columns = 2, gridsize = 3):
    for j in range(1, columns + 1)
        GridLine3(columns, gridsize)
        for i in range(1, gridsize + 1)):
            GridSpace3(columns, gridsize)
    GridLine3(columns, gridsize)

grid3(3,4)
