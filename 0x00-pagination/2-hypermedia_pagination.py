#!/usr/bin/env python3
"""Pagination sample."""

import csv
import math
from typing import Dict, List, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indexes for a given page and page size."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Paginating a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance."""
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Gets the cached dataset or load it if not already loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Gets a page of data."""
        assert isinstance(page, int) and isinstance(page_size, int), "Page and page_size must be integers."
        assert page > 0 and page_size > 0, "Page and page_size must be greater than 0."
        
        start, end = index_range(page, page_size)
        data = self.dataset()
        
        if start >= len(data):
            return []
        
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[object]]:
        """Retrieve hypermedia pagination information for a page."""
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.dataset()) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
