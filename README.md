## Proyecto-Integrador-Generador-de-pdf


Este proyecto permite generar reportes PDF a partir de archivos `.csv` utilizando una interfaz web construida con **Streamlit**. 
Aplica cuatro patrones de diseño para lograr una arquitectura modular, extensible y mantenible.

---

## Cómo ejecutar la aplicación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:
```bash
streamlit run app.py
```

3. Subir un archivo `.csv` válido (con una estructura predeterminanda mostrada en el ejemplo de uso) y descargar el PDF generado.

---

## Patrones de diseño aplicados y su justificación

### 1. **Builder** (`PDFReportBuilder`, `ReportBuilder`, `ReportDirector`)

**Problema de diseño:**
Se necesitaba una forma flexible de construir reportes en múltiples pasos (título, secciones, resumen), sin acoplar la lógica de generación al formato de salida (PDF, consola, etc.).

**Solución con el patrón:**
El patrón Builder permitió separar la lógica de construcción del reporte de su representación final. 
Se definió una interfaz `ReportBuilder` con pasos abstractos (`add_title`, `add_section`, etc.) y una implementación concreta `PDFReportBuilder` que los convierte en contenido PDF.

**Resultado:**
Se logró una arquitectura extensible donde en el futuro se podría agregar fácilmente un nuevo tipo de builder (por ejemplo, `ConsoleReportBuilder`, `HTMLReportBuilder`).

---

### 2. **Composite** (`ReportComponent`, `Section`, `Text`)

**Problema de diseño:**
Los reportes están compuestos por múltiples elementos jerárquicos (secciones que contienen textos u otros elementos). Se necesitaba un sistema uniforme para tratarlos.

**Solución con el patrón:**
El patrón Composite permite tratar elementos individuales (`Text`) y compuestos (`Section`) de forma uniforme. Ambos heredan de `ReportComponent` y tienen un método común `render()`.

**Resultado:**
Se obtuvo una estructura jerárquica y extensible para construir el contenido del reporte de forma modular.

---

### 3. **Template Method** (`BaseReportGenerator`, `DetailedReport`)

**Problema de diseño:**
Se necesitaba un flujo estándar para generar reportes, pero con pasos personalizables según el tipo de reporte (intro, cuerpo, resumen).

**Solución con el patrón:**
`BaseReportGenerator` define el flujo general (`generate()`) y delega los pasos a métodos abstractos (`add_intro`, `add_body`, `add_summary`).
`DetailedReport` implementa esos pasos con su propia lógica.

**Resultado:**
Se logró una estructura clara y extensible para crear distintos estilos de reportes, manteniendo la coherencia en su generación.

---

### 4. **Adapter** (`CSVAdapter`, `SalesDataSource`)

**Problema de diseño:**
Los datos pueden venir de distintas fuentes (CSV, JSON, base de datos). Se necesitaba una forma común de acceder a ellos sin acoplar la lógica del generador a un formato específico.

**Solución con el patrón:**
Se definió la interfaz `SalesDataSource` con el método `get_data()`. `CSVAdapter` implementa esta interfaz y convierte archivos CSV a una lista de diccionarios.

**Resultado:**
El sistema es ahora extensible a nuevas fuentes de datos sin modificar la lógica del generador de reportes.

---

##  Estructura del proyecto

```
├── app.py                  # Interfaz web con Streamlit
├── builder/               # Builder Pattern
│   ├── builder_interface.py
│   ├── pdf_report_builder.py
│   └── director.py
├── components/            # Composite Pattern
│   ├── report_component.py
│   ├── section.py
│   └── text.py
├── data/                  # Adapter Pattern
│   ├── data_source.py
│   └── csv_adapter.py
├── generator/             # Template Method Pattern
│   ├── base_report_generator.py
│   └── detailed_report.py
└── requirements.txt       # Dependencias del proyecto
```

---

## Ejemplo de uso

Subir un archivo como:
```csv
producto,monto
Laptop,15000
Monitor,3000
Mouse,500
```
(este formato permite un acomodo mas uniforme del pdf)

Y descargar un PDF con el contenido formateado.

---

## Diagrama UML

```mermaid
classDiagram
    class ReportBuilder {
        +add_title(title)
        +add_section(section)
        +get_result()
        +save(filename)
    }
    class PDFReportBuilder
    class ReportDirector {
        -builder: ReportBuilder
        +construct_report(sections)
    }
    class DataSource {
        +get_data(): list
    }
    class CSVAdapter
    class BaseReportGenerator {
        +generate()
        +get_sections(): list
    }
    class DetailedReport
    class ReportComponent {
        +render(): str
    }
    class Section {
        -title: str
        -children: list
        +add(component)
        +render()
    }
    class Text {
        -content: str
        +render()
    }

    ReportBuilder <|-- PDFReportBuilder
    ReportDirector --> ReportBuilder
    DataSource <|-- CSVAdapter
    BaseReportGenerator <|-- DetailedReport
    ReportComponent <|-- Section
    ReportComponent <|-- Text
    Section --> ReportComponent : contains

    class Pdf_Builder
    Pdf_Builder --> CSVAdapter
    Pdf_Builder --> DetailedReport
    Pdf_Builder --> ReportDirector
    Pdf_Builder --> PDFReportBuilder


