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

grid1()