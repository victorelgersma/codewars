'''
Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists

Unfortunately list(set(seq)) doesn't do the trick because the order of the
sequence has to stay the same
'''

def distinct(seq):
    '''
    >>> distinct([1, 1, 2])
    [1, 2]
    >>> distinct([1,2,1,1,3,2])
    [1, 2, 3]
    '''
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

