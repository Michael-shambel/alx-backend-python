#!/usr/bin/env python3
"""
given the parameters and the return values, add
type annotations to the function
"""
from typing import Any, Union, Mapping, TypeVar
T = TypeVar ('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    take dict, key, default value and retunr the dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default

