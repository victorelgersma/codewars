# This program removes all the zeros from a supplied integer

def no_boring_zeros(n):
    """
    >>> no_boring_zeros(100)
    1
    >>> no_boring_zeros(0)
    0
    >>> no_boring_zeros(105)
    10
    """
    ## return early if it is just a 0 
    if n == 0:
        return 0

    ## convert number to string

    num_str = str(n)

    ## reverse the string
    
    num_str_rev = num_str[::-1]

    ## iterate and strip if it is a zero

    for char in num_str_rev:
        if (char == '0'):
            num_str_rev = num_str_rev[1:]

    ## reverse the string, convert string to int and return

    num_str_rev_rev = num_str_rev[::-1]

    return int(num_str_rev[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(no_boring_zeros(100))
