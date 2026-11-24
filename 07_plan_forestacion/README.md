# Plan Forestación (Calama)

**Archivo:** [`Plan de forestación.py`](./Plan%20de%20forestaci%C3%B3n.py)

## ¿De qué se trata?

Aplicación de escritorio en Python (sección `0-L-4`, Grupo 1) orientada a evaluar un plan de forestación con tamarugos en Calama para una superficie configurable (`ha = 100`, a razón de 44 tamarugos/ha). Mediante una interfaz gráfica con cuatro botones permite:
1. **Emisiones:** leer series de emisiones de CO₂eq (2020–2022) desde Excel y graficar su evolución mensual.
2. **Requerimientos Hídricos:** calcular y graficar en barras el consumo mensual de agua (en litros) durante 12 meses según el régimen de riego.
3. **Mapa de Calama:** delimitar 3 polígonos georreferenciados de áreas de sembradío en un mapa interactivo.
4. **Precio de Tamarugos:** estimar el costo total de insumos desde Excel y desplegarlo en pantalla.

## Tipo de salidas

- **Interfaz gráfica de usuario (GUI)** en `tkinter` (800×500 px) con gráficos `matplotlib` embebidos (líneas de emisiones y barras de requerimiento hídrico) y etiquetas dinámicas de costo total.
- **Archivo HTML externo (`map.html`)** con un mapa interactivo de Calama y polígonos con *popups*, abierto automáticamente en el navegador web.

## Habilidades de programación evidenciadas

- Desarrollo de interfaces gráficas orientadas a eventos con `tkinter` (widgets, botones y *callbacks*).
- Integración de librerías científicas y geoespaciales: `pandas`, `matplotlib` (`FigureCanvasTkAgg`), `folium` y `webbrowser`.
- Ingesta de datos tabulares desde hojas de cálculo (`.xlsx`) y visualización integrada en escritorio y navegador.
- Modelado cuantitativo aplicado a un problema de ingeniería ambiental (densidad de plantación, balance hídrico y costos).

> **Nota técnica:** El script original requiere `pandas`, `matplotlib`, `folium` y `openpyxl`, y referencia archivos externos locales (`Datos.xlsx`, `Costos.xlsx`, `Instrucciones.docx`) mediante rutas absolutas que no forman parte de este repositorio.
