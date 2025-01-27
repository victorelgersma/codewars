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
    206.0
    '''
    try: 
        return 50*a+6
    except TypeError:
        return 'Error'
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
