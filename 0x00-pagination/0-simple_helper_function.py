#!/usr/bin/env python3
"""
Module declares a function named index_range that takes two integer
 arguments page and page_size.

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a list
for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """returns tuple containing start and end indexes"""
    records = page * page_size
    start = records - page_size
    end = records
    return (start, end)
