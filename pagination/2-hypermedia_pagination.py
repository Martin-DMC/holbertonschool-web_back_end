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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        This method takes two parameters and returns a
        dictionary with detailed information.
        Args:
            page (int, optional): The page number requested. Defaults to 1.
            page_size (int, optional): The number of items per page.
                                        Defaults to 10.
        Returns:
            dict: A dictionary containing:
                - page_size (int): The number of items in the current page.
                - page (int): The current page number.
                - data (list): The list of items for the requested page.
                - next_page (int or None): The number of the next page, or
                                            None if no next page exists.
                - prev_page (int or None): The number of the previous page, or
                                            None if no previous page exists.
                - total_pages (int): The total number of pages in the dataset.
        """
        paginas = self.dataset()
        data = self.get_page(page, page_size)
        total_paginas = int(math.ceil(len(paginas) / page_size))
        next_page = None
        prev_page = None
        if 1 < page < total_paginas:
            next_page = page + 1
            prev_page = page - 1
        elif page == 1:
            next_page = page + 1
        elif page == total_paginas:
            prev_page = page - 1
        dict_return = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_paginas': total_paginas
        }
        return dict_return
