
def apple(x):
    """
    >>> apple('50')
    "It's hotter than the sun!!"
    """
    if float(x)**2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
