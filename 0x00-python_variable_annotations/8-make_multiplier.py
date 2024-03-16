from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a float argument and
        returns the product of the input float and the multiplier.

    Example:
        >>> times_2 = make_multiplier(2.0)
        >>> times_2(5.0)
        10.0
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func

