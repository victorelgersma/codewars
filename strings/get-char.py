## https://www.codewars.com/kata/55ad04714f0b468e8200001c/train/python

def get_char(c):
    """
    Gets a character from its ASCII value and returns it
    >>> get_char(65)
    'A'
    >>> get_char(97)
    'a'
    """
    return chr(c)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

