# builder/builder_interface.py
from abc import ABC, abstractmethod

class ReportBuilder(ABC):
    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_section(self, section):
        pass

    @abstractmethod
    def get_result(self):
        pass

    @abstractmethod
    def save(self, filename):
        pass
