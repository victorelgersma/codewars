'''
Complete the method which accepts an array of integers, and returns one of the following:

    "yes, ascending" - if the numbers in the array are sorted in an ascending order
    "yes, descending" - if the numbers in the array are sorted in a descending order
    "no" - otherwise

You can assume the array will always be valid, and there will always be one correct answer.
'''

def is_sorted_and_how(arr):
    '''
    >>> is_sorted_and_how([1,2])
    'yes, ascending'
    >>> is_sorted_and_how([15,7,3,-8])
    'yes, descending'
    >>> is_sorted_and_how([4,3,30])
    'no'
    '''
    
    if arr==sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
