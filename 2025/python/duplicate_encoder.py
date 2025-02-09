def duplicate_encode(word):
    """
    Returns a new string where each character in the new string is "(" if that character appears only once i nthe original string, or ")" if that character appears more than once in the original string
    >>> duplicate_encode("din")
    '((('
    >>> duplicate_encode("recede")
    '()()()'
    """
    word = word.lower()
    my_set = get_chars_with_more_than_one_occurrence(word)
    my_list = []
    for i in word:
        if i in my_set:
            my_list.append(")")
        else:
            my_list.append("(")
    return "".join(my_list)


def get_chars_with_more_than_one_occurrence(word):
    """
    Returns a set of characters which occur more than once in a string
    >>> get_chars_with_more_than_one_occurrence("hello")
    {'l'}
    """
    my_set = set()
    for i in word:
        if word.count(i) > 1:
            my_set.add(i)
    return my_set


if __name__ == "__main__":
    import doctest
    doctest.testmod()