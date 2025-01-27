"""
https://www.codewars.com/kata/570597e258b58f6edc00230d/python
"""

def array(t):
    """
    >>> array('1,2,3')
    '2'
    >>> array('1,2,3,4')
    '2 3'
    >>> array('1,2,3,4,5')
    '2 3 4'
    >>> array('')
    None
    >>> array('1')
    None
    >>> array('1,2')
    None
    """
    elements = t.split(',') # split the string by commas
    if len(elements) < 3:
        return None
    return ' '.join(elements[1:-1])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
