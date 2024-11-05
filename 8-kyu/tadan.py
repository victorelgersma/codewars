
def hello(name=None):
    """

    >>> hello("john")
    'Hello, John!'
    >>> hello("alice")
    'Hello, Alice!'
    >>> hello("")
    'Hello, World!'
    """
    return f"Hello, {name.capitalize()}!" if defined(name) else 'Hello, World!'


def defined(var=None):
    """
    >>> defined("")
    False
    >>> defined(None)
    False
    >>> defined("Hello")
    True
    >>> defined()
    False
    """
    return bool(var)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
