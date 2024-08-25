#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values
with the appropriate types.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence from the input iterable
    and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., list of strings or list of lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples. Each tuple contains a sequence from the input
        iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
