'''
https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

'''

def problem(a):
    '''
    >>> problem('asd')
    'Error'
    >>> problem(4)
    206
    >>> problem(4.0)
    206
    '''
    # Check that the type is either an int or a float
    if isinstance(a, (int, float)):
        return 50*a+6
    else: 
        return 'Error'
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
