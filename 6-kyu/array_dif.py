def array_diff(a, b):
    '''
    >>> array_diff([1,2,2], [2])
    [1]
    '''
    # iterate through a: if a in b, remove it
    return [i for i in a if i not in b]



if __name__ == "__main__":
    import doctest
    doctest.testmod()
