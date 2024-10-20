

def get_middle(s):
    '''
    >>> get_middle('test')
    'es'
    >>> get_middle('testing')
    't'
    >>> get_middle('middle')
    'dd'
    >>> get_middle('A')
    'A'
    '''
    if len(s) % 2 == 0:
        return s[len(s) // 2 -1 ] + s[len(s) // 2]

    else :
        index = (len(s) -1 )// 2
        return s[index]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


    

