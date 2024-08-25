#!/usr/bin/env python3

"""
Function `sum_list` takes a list of floats
and returns their sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
    input_list (List[float]): The list of floating-point numbers.

    Returns:
    float: The sum of the floating-point numbers in the list.
    """
    return sum(input_list)
