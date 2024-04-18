#!/usr/bin/env python3
'''This Task 11' module.
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Ret = Union[Any, T]
Defu = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Defu = None) -> Ret:
    '''This for Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
