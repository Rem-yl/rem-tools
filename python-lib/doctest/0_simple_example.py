def division(a, b):
    """ 使用除法示例 doctest 用法

    Example:
    >>> division(3, 1)
    3.0
    >>> division(3, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """

    return a / b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
