# Proyectos de Programación en Python (2023)

Colección de scripts y aplicaciones modulares desarrolladas en Python durante 2023, abarcando desde lógica algorítmica por consola hasta análisis de datos y visualización geoespacial.

## Índice de proyectos

| Carpeta | Proyecto | Tipo de salida | Habilidades principales |
| :--- | :--- | :--- | :--- |
| [`01_tarea0_maquina_registradora`](./01_tarea0_maquina_registradora/README.md) | Máquina registradora | Consola (`stdout`) | Ciclos con centinela, validación de entradas, listas paralelas, aritmética comercial |
| [`02_tarea1_budokai_tenkaichi`](./02_tarea1_budokai_tenkaichi/README.md) | Simulador de torneo eliminatorio | Consola (`stdout`) | Ordenamiento manual por selección, listas anidadas, `ord()` ASCII, simulación de rondas |
| [`03_tarea2_tablero_ajedrez`](./03_tarea2_tablero_ajedrez/README.md) | Validador y detector de jaque en ajedrez | Retorno de funciones (`int`, `bool`, matrices) | Modularización, matrices 2D (8×8), geometría en grillas, detección de obstrucciones |
| [`04_tarea3_laberinto`](./04_tarea3_laberinto/README.md) | Recorrido de laberinto con portales | Retorno de funciones (matrices y rutas) | Lectura de archivos `.lab`, matrices 2D, navegación ortogonal, manejo de portales |
| [`05_control1_carrera_tiempos`](./05_control1_carrera_tiempos/README.md) | Evaluación de tiempos de carrera | Consola (`stdout`) | Parseo multinivel (`;`, `,`, `:`), conversión `HH:MM:SS` a segundos, detección de empates |
| [`06_control2_evaluacion_asistencia`](./06_control2_evaluacion_asistencia/README.md) | Auditoría de registro de asistencia | Archivo `test_resultado.txt` + retorno | Lectura/escritura de archivos, segmentación por bloques, comparación binaria |
| [`07_proyecto_final_plan_forestacion`](./07_proyecto_final_plan_forestacion/README.md) | Plan Forestación (Calama) | GUI (`tkinter`), gráficos embebidos y `map.html` | Programación orientada a eventos, `pandas`, `matplotlib`, `folium`, modelado aplicado |

## Progresión técnica del repositorio

1. **Fundamentos y algoritmos por consola** (`Tarea 0`, `Tarea 1`, `Control 1`): control de flujo, validación de entradas, parseo de texto estructurado y algoritmos de ordenamiento manual sin librerías externas.
2. **Modularización, matrices y archivos** (`Tarea 2`, `Tarea 3`, `Control 2`): descomposición en funciones con contratos claros de entrada/salida, manipulación de grillas 2D y lectura/escritura de archivos de texto.
3. **Aplicación integrada de escritorio y datos** (`Proyecto Final`): integración de interfaz gráfica (`tkinter`), análisis tabular (`pandas`), gráficos embebidos (`matplotlib`) y cartografía interactiva (`folium`).

## Requisitos de ejecución

- **Módulos 01 al 06:** Python 3 (solo biblioteca estándar).
- **Proyecto Final (`07_proyecto_final_plan_forestacion`):** Python 3 con `tkinter`, `pandas`, `matplotlib`, `folium` y `openpyxl`, además de los archivos externos locales referenciados en el código original.
