
def usdcny(usd):
    """
    >>> usdcny(15)
    '101.25 Chinese Yuan'
    >>> usdcny(2244)
    '15147.00 Chinese Yuan'
    """
    cny_amount = float(usd) * 6.75
    return f"{cny_amount:.2f} Chinese Yuan"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

