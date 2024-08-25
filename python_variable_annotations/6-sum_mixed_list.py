#!/usr/bin/env python3

""" Module to define a function for summing a list of """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floating-point numbers.

    Args:
    mxd_lst (List[Union[int, float]]): The list containing
    integers and floating-point numbers.

    Returns:
    float: The sum of the integers and floating-point numbers in the list.
    """
    return float(sum(mxd_lst))
