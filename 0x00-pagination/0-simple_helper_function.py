#!/usr/bin/env python3
"""Pagination function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a list for those particular pagination parameters..
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
