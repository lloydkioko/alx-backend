#!/usr/bin/env python3

"""
file
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
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
        """Get a page of the dataset
        """
        assert isinstance(page, int) and page > 0, "page should be int > 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size,int>0"

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
            str, Union[int, List[List], None]]:
        """Get a page of the dataset with hypermedia metadata
        """
        data_page = self.get_page(page, page_size)
        total_pages = int(math.ceil(len(self.dataset()) / page_size))
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes based on page and page_size
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
