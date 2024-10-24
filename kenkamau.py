def capitalize_list(s):
    """
    >>> capitalize_list("abcdef")
    ['AbCdEf', 'aBcDeF']
    >>> capitalize_list("")
    ['', '']
    """
    first = []
    second = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            first.append(char.upper())
            second.append(char)
        else:
            first.append(char)
            second.append(char.upper())
    return [''.join(first), ''.join(second)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
