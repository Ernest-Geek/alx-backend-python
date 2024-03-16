#!/usr/bin/env python3
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Convert a string-key and int/float-value pair to a tuple.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element
        and the second element is the square of the int/float value 'v'.
    """

    return k, v ** 2.0
