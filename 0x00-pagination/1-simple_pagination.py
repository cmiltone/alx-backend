#!/usr/bin/env python3
"""
module Implements a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.

You have to use the data.csv CSV file
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should
be returned.
"""
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """returns tuple containing start and end indexes"""
    records = page * page_size
    start = records - page_size
    end = records
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns expected section of dataset"""
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError('Both page and page_size must be integers')
        if page < 0 or page_size < 0:
            error_msg = 'Both page and page_size must be greater than 0'
            raise AssertionError(error_msg)

        records = self.dataset()

        (start, end) = index_range(page, page_size)
        if start > len(records):
            return []

        return records[start:end]
