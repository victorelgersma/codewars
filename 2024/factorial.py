def factorial(n):
    '''
    A recursive factorial function
    >>> factorial(5)
    120
    >>> factorial(13)
    Traceback (most recent call last):
    ...
    ValueError: argument out of range
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: argument out of range
    '''

    if n > 12 or n < 0:
        raise ValueError('argument out of range')
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return n * factorial(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(factorial(3))