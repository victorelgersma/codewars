
def is_valid_walk(walk):
    """
    >>> is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
    True
    >>> is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])
    False
    """
    return is_closed(walk) and distance(walk) == 10


def is_closed(walk):
    """
    >>> is_closed(['n','s'])
    True
    >>> is_closed(['s','s'])
    False
    
    """
    return walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


def distance(walk):
    return len(walk)

if __name__ == "__main__":
    import doctest
    doctest.testmod()