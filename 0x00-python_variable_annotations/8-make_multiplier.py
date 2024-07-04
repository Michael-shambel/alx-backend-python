#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function takes a number of float and
    calcute the number with the multiplier
    """
    def multplierCalc(x: float) -> float:
        """
        this is multiplier calc
        """
        return x * multiplier
    return multplierCalc
