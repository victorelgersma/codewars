def capitalize(s):
    """
    >>> capitalize("abcdef")
    ['AbCdEf', 'aBcDeF']
    """
    first = ''
    second = ''
    for i in range(len(s)):
        if i % 2 == 0:
            first += s[i].upper()
            second += s[i]
        else:
            first += s[i]
            second += s[i].upper()
    return [first, second]




if __name__ == "__main__":
    import doctest
    doctest.testmod()
