# Write a function that always returns a 5
# Bear in mind you can't use the characters 0123456789*+-/

def unusual_five():
    '''
    >>> unusual_five()
    5
    '''
    return ord('\x05')


if __name__ == "__main__":
    print(unusual_five())
