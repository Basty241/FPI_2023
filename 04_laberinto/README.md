# Recorrido de Laberinto con Portales

**Archivo:** [`Laberinto.py`](./Laberinto.py)

## ¿De qué se trata?

Módulo de funciones para cargar laberintos desde archivos de texto con extensión `.lab` y reconstruir la ruta entre la entrada (`EE`) y la salida (`SS`), siguiendo casillas marcadas (`**`) y manejando pares de portales de teletransporte (`PP`). Define cuatro funciones: `cargar_laberinto`, `encontrar_entrada`, `encontrar_salida` y `recuperar_camino`.

## Tipo de salidas

Valores de retorno por función (módulo importable sin salida directa a consola):
- `cargar_laberinto(nombre)` → `list[list[str]]` (matriz 2D del laberinto, o `[]` si el nombre/extensión no es `.lab`).
- `encontrar_entrada(laberinto)` y `encontrar_salida(laberinto)` → `list[int]` con coordenadas `[fila, columna]`.
- `recuperar_camino(laberinto)` → `list[str]` con la secuencia de desplazamiento (`"Entrada"`, direcciones `"AR"`, `"AB"`, `"IZ"`, `"DE"`, eventos `"Portal"`, y `"Salida"`).

## Habilidades de programación evidenciadas

- Lectura de archivos de texto mediante *context managers* (`with open(...)`) y validación básica de extensiones.
- Parseo de archivos estructurados por espacios a matrices 2D y limpieza de saltos de línea.
- Búsqueda de elementos en grillas bidimensionales y navegación paso a paso por adyacencia ortogonal (4-conectividad).
- Composición y reutilización de funciones dentro de un mismo módulo, junto con manejo de transiciones especiales de estado (portales).
