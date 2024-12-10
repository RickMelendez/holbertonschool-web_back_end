#!/usr/bin/env python3

"""This file contains the Server class for hypermedia pagination"""

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache and return the dataset as a list of lists."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        if page > total_pages:
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
            }

        page_data = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
