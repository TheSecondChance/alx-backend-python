#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
