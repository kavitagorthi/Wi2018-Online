#Grid Printer Exercise
#Chay Casso, 1/29/18

def grid1():
    """Draw a simple 2x2 grid composed of 5x5 squares."""
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    print(plus + minus * 4 + plus + minus * 4 + plus)
    for i in range(1,5):
        print(pipe + blank * 4 + pipe + blank * 4 + pipe)
    print(plus + minus * 4 + plus + minus * 4 + plus)
    for i in range(1, 5):
        print(pipe + blank * 4 + pipe + blank * 4 + pipe)
    print(plus + minus * 4 + plus + minus * 4 + plus)

grid1()