def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.

    Parameters:
    x (int | float): The number to be squared.

    Returns:
    int | float: The square of the input number.
    """
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """
    Calculate the power of a number raised to itself.

    Parameters:
    x (int | float): The base number.

    Returns:
    int | float: The result of x raised to the power of x.
    """
    return (x ** x)


def outer(x: int | float, function) -> object:
    """
    Create a closure that applies a function to a number.

    Parameters:
    x (int | float): The initial number.
    function (callable): The function to apply.

    Returns:
    object: A closure that applies the function to the number.
    """
    count = 0

    def inner() -> float:
        """
        Apply the function to the number or the result of the last
        application.

        Returns:
        float: The result of the function application.
        """
        nonlocal count
        if (count == 0):
            count = function(x)
            return count
        count = function(count)
        return count
    return inner
