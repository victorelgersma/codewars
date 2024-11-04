
def gimme(input_array):
    '''
As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).
    >>> gimme([2,3,1])
    0
    '''
    array_copy = input_array.copy()
    maximum = max(input_array)
    minimum = min(input_array)
    input_array.remove(minimum)
    input_array.remove(maximum)
    return array_copy.index(input_array[0])




if __name__ == "__main__":
    import doctest
    doctest.testmod()

