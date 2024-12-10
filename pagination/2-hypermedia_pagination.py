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
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the records corresponding to the current page."""
        # Validate input
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Calculate start and end index for the required page
        start_index, end_index = self.index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):  # If the page is out of range, return an empty list
            return []

        return data[start_index:end_index]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Return the start and end index for the pagination."""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a dictionary containing pagination information.
        
        It includes the data for the current page, page size, total pages, and navigation details.
        """
        # Validate input
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Calculate the total number of pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # If the requested page is beyond the total pages, return an empty response
        if page > total_pages:
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
            }

        # Get the data for the current page
        page_data = self.get_page(page, page_size)

        # Determine the next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),  # Number of items on the current page
            'page': page,                 # Current page number
            'data': page_data,            # List of items on this page
            'next_page': next_page,       # Next page number, or None if this is the last page
            'prev_page': prev_page,       # Previous page number, or None if this is the first page
            'total_pages': total_pages    # Total number of pages
        }
