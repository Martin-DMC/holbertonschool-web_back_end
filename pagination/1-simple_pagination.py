#!/usr/bin/env python3
"""
This module contains the Server class, which manages a database
file and provides methods for pagination
"""

import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """
        Retrieves a specific page from the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of rows per page.

        Returns:
            List[List]: A list of lists representing the rows for the
            requested page.
            Returns an empty list if the page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indice = index_range(page, page_size)
        listas = self.dataset()
        if indice[0] > len(listas):
            return []
        return listas[indice[0]:indice[1]]
