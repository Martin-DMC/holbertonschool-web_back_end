#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            assert isinstance(index, int) and index >= 0
            assert isinstance(page_size, int) and page_size > 0
            assert index < len(self.dataset())
            indice = self.indexed_dataset()
            if index is None:
                index = 0
            data = []
            current_index = index
            contador = 0
        
            while contador < page_size:
                if current_index in indice:
                    data.append(indice[current_index])
                    contador += 1
                current_index += 1
                if current_index > max(indice.keys(), default=0):
                    break

            next_index = None
            temp_index = current_index
            while True:
                if temp_index in indice:
                    next_index = temp_index
                    break
                
                if temp_index > max(indice.keys(), default=0):
                    break
                temp_index += 1
            dict_return = {
                'index': index,
                'data': data,
                'page_size': len(data),
                'next_index': next_index
            }
            return dict_return
