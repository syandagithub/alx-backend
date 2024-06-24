#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular child names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance."""
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset or load it if not already loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Return the dataset indexed by its original order."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Optional[object]]:
        """Retrieve paginated data starting from a specific index."""
        data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(data), "Index out of range."
        
        page_data = []
        data_count = 0
        next_index = None

        for i in range(index, len(data)):
            if data_count < page_size:
                page_data.append(data[i])
                data_count += 1
            else:
                next_index = i
                break

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
