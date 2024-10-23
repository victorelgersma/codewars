'''
https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
'''

def sum_mul(n, m):
    '''
    Finds the sum of all multiples of n below m
    >>> sum_mul(2,9)
    20
    >>> sum_mul(4,-7)
    'INVALID'
    >>> sum_mul(5,3)
    0
    '''
    if m <= 0 or n <=0:
        return "INVALID"
    if m < n:
        return 0

    summand = 0
    for i in range(n, m, n):
        summand = summand + i
    return summand
    

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
