#!/usr/bin/env python3
"""
function’s parameters and return values with the appropriate types
"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    take an iterable of sequences and returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
