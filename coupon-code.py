
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    '''
    >>> check_coupon("123", "123", "July 9, 2015", "July 9, 2015")
    True
    >>> check_coupon("123", "123", "July 9, 2015", "July 2, 2015")
    False
    '''
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
