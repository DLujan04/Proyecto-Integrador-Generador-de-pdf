# components/report_component.py
from abc import ABC, abstractmethod

class ReportComponent(ABC):
    @abstractmethod
    def render(self):
        pass
