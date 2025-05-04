
import streamlit as st
import pandas as pd
from builder.pdf_report_builder import PDFReportBuilder
from builder.director import ReportDirector
from generator.detailed_report import DetailedReport
import os

st.set_page_config(page_title="Generador de Reportes", layout="centered")
st.title("📄 Generador de Reportes PDF desde CSV")

uploaded_file = st.file_uploader("Sube un archivo CSV de ventas", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        data = df.to_dict(orient="records")
        df.dropna(how="all", inplace=True)          
        df.dropna(axis=1, how="all", inplace=True)  
        df = df.loc[:, ~df.columns.str.contains("Unnamed")] 


        st.success("✅ Archivo CSV cargado correctamente.")
        st.write("Vista previa de los datos:")
        st.dataframe(df)

        report_generator = DetailedReport(data)
        report_generator.generate()

        builder = PDFReportBuilder()
        director = ReportDirector(builder)
        director.construct_report(report_generator.get_sections())

        output_filename = "reporte_streamlit.pdf"
        builder.save(output_filename)

        with open(output_filename, "rb") as f:
            st.download_button(
                label="📥 Descargar reporte PDF",
                data=f,
                file_name="reporte.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {e}")
