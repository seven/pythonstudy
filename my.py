def factorial(n):
    """
    Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> factorial(30)
    265252859812191058636308480000000L

    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    pass

if __name__ == '__main__' and '--test' in sys.argv:
    import doctest
    doctest.testmod()
