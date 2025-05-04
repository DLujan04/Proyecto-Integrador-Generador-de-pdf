from generator.base_report_generator import BaseReportGenerator
from components.section import Section
from components.text import Text

class DetailedReport(BaseReportGenerator):
    def add_intro(self):
        intro = Section("Introducción")
        intro.add(Text("Este es un reporte generado a partir del archivo CSV subido."))
        self.sections.append(intro)

    def add_body(self):
        body = Section("Contenido del archivo CSV")
        for fila in self.data:
            linea = ", ".join(f"{clave}: {valor}" for clave, valor in fila.items())
            body.add(Text(linea))
        self.sections.append(body)

    def add_summary(self):
        summary = Section("Resumen")
        summary.add(Text(f"Total de registros: {len(self.data)}"))
        self.sections.append(summary)
