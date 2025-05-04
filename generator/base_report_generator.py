from abc import ABC, abstractmethod

class BaseReportGenerator(ABC):
    def __init__(self, data):
        self.data = data
        self.sections = []

    def generate(self):
        self.add_intro()
        self.add_body()
        self.add_summary()

    @abstractmethod
    def add_intro(self): pass

    @abstractmethod
    def add_body(self): pass

    @abstractmethod
    def add_summary(self): pass

    def get_sections(self):
        return self.sections
