# Evaluación de Tiempos de Carrera

**Archivo:** [`Carrera de tiempos.py`](./Carrera%20de%20tiempos.py)

## ¿De qué se trata?

Evalúa los resultados de una carrera de tres vueltas recibiendo una única línea de entrada donde los competidores se separan por `;`, las tres vueltas por `,` y cada marca en formato `HH:MM:SS`. Convierte cada vuelta a segundos, acumula el tiempo total por competidor, ordena los resultados de menor a mayor tiempo e identifica al ganador (numerado desde 1) o si se produjo un empate en el primer lugar.

## Tipo de salidas

Salida estándar por consola (`stdout`):
- Un número entero correspondiente al competidor con menor tiempo total (indexado desde `1`), o
- El texto `Hubo un empate` en caso de igualdad en el mejor tiempo.

## Habilidades de programación evidenciadas

- Parseo multinivel de cadenas con delimitadores jerárquicos (`;`, `,`, `:`).
- Conversión y agregación de unidades de tiempo (`HH:MM:SS` a segundos totales).
- Ordenamiento manual por selección y evaluación de mínimos y empates sobre estructuras de listas.
