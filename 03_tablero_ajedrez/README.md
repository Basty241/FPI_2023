# Validador y Detector de Jaque en Ajedrez

**Archivo:** [`Tablero de Ajedrez.py`](./Tablero%20de%20Ajedrez.py)

## ¿De qué se trata?

Módulo de funciones para construir, validar y analizar estados de un tablero de ajedrez de 8×8 representado como matriz de cadenas (`"  "` para casillas vacías y códigos de 2 caracteres como `BR` o `NP` para piezas). Implementa cuatro funciones:
- `validar_posicion(pos, tablero)`: verifica si una coordenada algebraica (`A1`–`H8`) existe y si está libre u ocupada.
- `entregar_tablero(piezas)`: parsea un string de piezas separadas por comas y las posiciona en la matriz 8×8.
- `es_valido(tablero)`: comprueba restricciones reglamentarias (peones fuera de filas extremas, conteo máximo por pieza, un rey por bando y alfiles en casillas de distinto color).
- `hay_jaque(tablero)`: evalúa amenazas sobre ambos reyes por peones, caballos, torres, alfiles y damas considerando obstrucciones en la trayectoria.

## Tipo de salidas

Valores de retorno por función (módulo importable sin `print` ni ejecución principal):
- `validar_posicion` → `int` (`0` libre, `1` ocupada, `-1` fuera de rango).
- `entregar_tablero` → `list[list[str]]` (matriz 8×8).
- `es_valido` → `bool` (validez reglamentaria del tablero).
- `hay_jaque` → `int` (`-1` sin jaque, `0` rey blanco en jaque, `1` rey negro en jaque, `2` ambos reyes en jaque).

## Habilidades de programación evidenciadas

- Descomposición modular en funciones reutilizables documentadas con *docstrings* (descripción, entrada y salida).
- Representación de matrices 2D y traducción entre notación algebraica (`A1`–`H8`) e índices `[fila][columna]`.
- Lógica geométrica sobre grillas: movimientos ortogonales, diagonales por cuadrantes, saltos en "L" (`abs`) y detección de bloqueos en línea de visión.
- Codificación de reglas de dominio complejas y estados combinados en códigos de retorno.
