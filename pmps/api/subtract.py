"""api.subtract module
"""
from pmps.core.subtract import subtract as core_subtract


def subtract(num1: int, num2: int) -> int:
    """
    Subtract up two integer numbers.

    This function simply wraps the ``-`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1
        First number.
    num2
        Second number to subtract.

    Returns
    -------
    int
        The subtraction of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> core_subtract(2, 2)
    4
    >>> core_subtract(25, 0)
    25
    >>> core_subtract(10, -10)
    0
    """
    return core_subtract(num1, num2)
