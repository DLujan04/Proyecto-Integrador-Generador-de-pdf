# builder/pdf_report_builder.py
from fpdf import FPDF
from builder.builder_interface import ReportBuilder

class PDFReportBuilder(ReportBuilder):
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def add_title(self, title):
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, txt=title, ln=True, align="C")
        self.pdf.set_font("Arial", size=12)

    def add_section(self, section):
        content = section.render()
        for line in content.split("\n"):
            if line.strip():
                self.pdf.cell(200, 10, txt=line.strip(), ln=True)

    def get_result(self):
        return self.pdf

    def save(self, filename):
        self.pdf.output(filename)
