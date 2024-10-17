from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    '''
    Checks that the codes match and that the coupon is not expired
    >>> check_coupon("123", "123", "July 9, 2015", "July 9, 2015")
    True
    >>> check_coupon("123", "123", "July 9, 2015", "July 2, 2015")
    False
    '''
    current_date_obj = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date_obj = datetime.strptime(expiration_date, "%B %d, %Y")

    return expiration_date_obj >= current_date_obj and entered_code == correct_code


if __name__ == "__main__":
    import doctest
    doctest.testmod()
