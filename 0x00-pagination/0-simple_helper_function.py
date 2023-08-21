#!/usr/bin/env python3
"""
Defines index range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    for a range of indexes to return in a list for those particular
    pagination parameters
    """
    start_idx = (page_size * page) - page_size
    end_idx = (page_size * page)
    return (start_idx, end_idx)
