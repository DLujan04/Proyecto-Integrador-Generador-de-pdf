class ReportDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_report(self, sections):
        self.builder.add_title("Reporte de Ventas")
        for section in sections:
            self.builder.add_section(section)
