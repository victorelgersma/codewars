# This program removes all the zeros from a supplied integer
def no_boring_zeros(n):
    """
    >>> no_boring_zeros(100)
    1
    >>> no_boring_zeros(0)
    0
    >>> no_boring_zeros(1050)
    105
    >>> no_boring_zeros(2016)
    2016
    """
    ## return early if it is just a 0 
    if n == 0:
        return 0

    count = 0

    for char in reversed(str(n)):
        if (char == '0'):
            count = count+1
        else: 
            break
    num_str = str(n)
    trimmed_str = num_str[0:len(num_str)-count]
    if trimmed_str == '':
        return 0  # or some other default behavior
    return int(trimmed_str)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
