def alphabet_position(text):
    """
    >>> alphabet_position("The sunset sets at twelve o' clock.")
    '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
    """
    output_list= []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in text.lower():
        if char.isalpha():
            output_list.append(str(alphabet.find(char)+1))
    output = " ".join(output_list)
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()


