from collections.abc import Iterable

'''
https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
- filtering out None type
'''

def sum_array(arr):
    '''
    >>> sum_array([1,2,3])
    2
    >>> sum_array([4,5,6,7])
    11
    >>> sum_array(None)
    0
    '''
    if isinstance(arr,Iterable) and len(arr) > 1:

        filtered = [x for x in arr if x is not None]
        return sum(filtered) - max(filtered) - min(filtered)
    else: return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
