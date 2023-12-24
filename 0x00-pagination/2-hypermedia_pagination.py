#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary
containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
"""
import csv
import math
from typing import List
from typing import Tuple, Dict


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
        if page <= 0 or page_size <= 0:
            error_msg = 'Both page and page_size must be greater than 0'
            raise AssertionError(error_msg)

        records = self.dataset()

        (start, end) = index_range(page, page_size)
        if start > len(records):
            return []

        return records[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """"returns a key-value pairs of details for pagination"""
        (start, end) = index_range(page, page_size)
        records = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = None
        prev_page = None
        _size = len(records)

        if end < len(self.__dataset):
            next_page = page + 1
        
        if start > 0:
            prev_page = page - 1
        _dict = {
            'page_size': _size,
            'page': page,
            'data': records,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return _dict