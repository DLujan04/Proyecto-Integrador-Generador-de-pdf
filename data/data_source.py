# data/data_source.py
from abc import ABC, abstractmethod

class SalesDataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass
