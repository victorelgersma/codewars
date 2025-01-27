'''
https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
'''

def capitals(word):
    '''
    >>> capitals("CodEWaRs")
    [0, 3, 4, 6]
    '''
    capitals = []
    for i in range(len(word)):
        letter = word[i]
        if letter.isupper():
            capitals.append(i)
    return capitals

if __name__ == "__main__":
    import doctest
    doctest.testmod()
