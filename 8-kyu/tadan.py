
def hello(name=""):
    """

    >>> hello("john")
    'Hello, John!'
    >>> hello("alice")
    'Hello, Alice!'
    >>> hello("")
    'Hello, World!'
    """
    return f"Hello, {name.capitalize()}!" if bool(name) else 'Hello, World!'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
