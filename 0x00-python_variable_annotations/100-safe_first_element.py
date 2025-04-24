#!/usr/bin/env python3
"""Module that provides a function to safely return the first element of a sequence."""


from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence or None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
