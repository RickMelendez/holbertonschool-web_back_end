#!/usr/bin/env python3

"""
Function to_kv takes a string k and an int
OR float v as arguments and returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string `k` and
    the second element is the square of the number `v`.

    Args:
    k (str): A string.
    v (Union[int, float]): An integer or floating-point number.

    Returns:
    Tuple[str, float]: A tuple with the string `k`
    and the square of `v` as a float.
    """
    return (k, float(v ** 2))
