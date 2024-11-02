def sp_eng(sentence):
    '''
    >>> sp_eng("abcEnglishdef")
    True
    >>> sp_eng("yello")
    False
    '''
    return "english" in sentence.lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
