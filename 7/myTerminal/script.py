
def gimme(input_array):
    '''
As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).
    >>> gimme([2,3,1])
    0
    '''
    middle_value=sorted(input_array)[1]
    return input_array.index(middle_value)




if __name__ == "__main__":
    import doctest
    doctest.testmod()

