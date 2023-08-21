
#!/usr/bin/env python3

"""
file contains function index_range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start index and end index for pagination.

    Args:
        page (int): The current page number(1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    if page <= 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index
