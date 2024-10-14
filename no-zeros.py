# This program removes all the zeros from a supplied integer

def no_boring_zeros(n):
    """
    >>> no_boring_zeros(100)
    1
    >>> no_boring_zeros(0)
    0
    >>> no_boring_zeros(1050)
    105
    """
    ## return early if it is just a 0 
    if n == 0:
        return 0
    result = ""

    ## iterate and strip if it is a zero


    for char in reversed(s)
        if (char != '0'):

    ## reverse the string, convert string to int and return

    return int(num_str_rev[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(no_boring_zeros(100))
