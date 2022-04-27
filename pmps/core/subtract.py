"""core.subtract module
"""


def subtract(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``-`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number.
    num2 : int
        Second number to subtract to first number.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> subtract(2, 2)
    0
    >>> subtract(25, 0)
    25
    >>> subtract(10, -10)
    20
    """
    return num1 - num2
