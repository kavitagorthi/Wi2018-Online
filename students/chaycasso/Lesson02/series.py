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

def sum_series(n,init1=0,init2=1):
    """Return the nth value in a generalized sum series defined by init1 (n=1) and init2 (n=2)."""
    if n == 1:
        return init1
    elif n == 2:
        return init2
    else:
        return sum_series(n-1,init1,init2) + sum_series(n-2,init1,init2)

print(sum_series(8))