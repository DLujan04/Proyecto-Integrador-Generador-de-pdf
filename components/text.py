# components/text.py
from components.report_component import ReportComponent

class Text(ReportComponent):
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content
