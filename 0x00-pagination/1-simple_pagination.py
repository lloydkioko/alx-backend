#!/usr/bin/env python3

"""
file conntains get_page method
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    assert isinstance(page, int) and page > 0, "page must be an int > 0"
    assert isinstance(page_size, int) and page_size > 0, "page_size > 0"
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
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
        """Returns the appropriate page of the dataset using pagination
        """
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
