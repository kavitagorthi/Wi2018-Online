#!/usr/local/bin/python3

def Fib(n):
    """Recursive function returning Fibonacci seq or Lucas"""
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1)+Fib(n-2)

def Lucus(n):
    """Recursive function returning lucus seq"""
    if n == 0: return 2
    elif n == 1: return 1
    else: return Lucus(n-1)+Lucus(n-2)

def calc(type,n):
    """Iterate though a range of numbers adding the fib or lucus numbers to a string"""
    result = ''
    for i in range(n):
        if type == 'fib': result += str(Fib(i)) + ','
        if type == 'lucus': result += str(Lucus(i)) + ','
    return result

print('Fibonacci:::',calc('fib',10))
print('Lucus:::::::',calc('lucus',10))
