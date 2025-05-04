from components.report_component import ReportComponent

class Section(ReportComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self):
        rendered = f"\n=== {self.title} ===\n"
        for c in self.children:
            rendered += c.render() + "\n"
        return rendered
