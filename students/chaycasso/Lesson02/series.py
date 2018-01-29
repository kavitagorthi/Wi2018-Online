def fibonacci(n):
    """Return the nth fibonacci sequence number."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return the nth Lucas number."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(8))

def sum_series(n,init1=0,init2=1):
    """Return the nth value in a generalized sum series defined by init1 and init2."""
