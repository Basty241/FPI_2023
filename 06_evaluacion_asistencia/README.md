# Auditoría de Registro de Asistencia (Tradicional vs. IA)

**Archivo:** [`Evaluación de asistencia.py`](./Evaluaci%C3%B3n%20de%20asistencia.py)

## ¿De qué se trata?

Define la función `evaluar(a_asistencia, a_asistencia_ia)` para contrastar el registro de asistencia generado por una IA contra una lista tradicional separada por bloques `"Clase"`. Transforma el archivo tradicional en vectores binarios de asistencia (`"1"` presente, `"0"` ausente) por estudiante, identifica al alumno especificado en el archivo de IA y compara clase a clase marcando coincidencias (`"O"`) y errores (`"X"`).

## Tipo de salidas

- **Archivo de texto generado:** `test_resultado.txt` con una línea en formato `<Nombre> <Apellido> <O|X> <O|X> ...`.
- **Valor de retorno:** objeto de archivo (`TextIOWrapper`) asociado a `test_resultado.txt`.

## Habilidades de programación evidenciadas

- Lectura y escritura de archivos de texto con *context managers* (`with open`).
- Segmentación de registros secuenciales usando encabezados delimitadores (`"Clase"`).
- Construcción de matrices binarias de presencia/ausencia y comparación elemento a elemento entre dos fuentes de datos.
- Reutilización de rutinas previas de limpieza y tokenización de texto.
