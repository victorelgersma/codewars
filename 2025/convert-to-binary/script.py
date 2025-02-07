def to_binary(n):
    """
    >>> to_binary(11)
    1011
    """
    return int(bin(n)[2:])




if __name__ == "__main__":
    import doctest
    doctest.testmod()