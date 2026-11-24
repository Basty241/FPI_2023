# Simulador de Torneo Eliminatorio

**Archivo:** [`Budokai Tenkaichi - Tarea 1.py`](./Budokai%20Tenkaichi%20-%20Tarea%201.py)

## ¿De qué se trata?

Simula un torneo eliminatorio de artes marciales en tres etapas:
1. **Preselección:** recibe participantes (`nombre,puntaje` o `MAQUINA DESTRUIDA`), otorga clasificación directa a quienes destruyen la máquina y completa los cupos restantes ordenando por mayor puntaje.
2. **Sorteo:** asigna y ordena las llaves iniciales según el orden del sorteo recibido.
3. **Torneo:** calcula un "poder oculto" por competidor (promedio entero de los valores ASCII de su nombre) y resuelve las rondas eliminatorias hasta definir un campeón, aplicando desempate según la paridad del poder oculto.

## Tipo de salidas

Salida estándar por consola (`stdout`) organizada en tres bloques:
- Listado de participantes clasificados (`Y los participantes seleccionados son:`).
- Emparejamientos iniciales del torneo (`A vs B`).
- Desarrollo combate por combate (`A vs B -> Gana X`) y anuncio del campeón final.

## Habilidades de programación evidenciadas

- Implementación manual de algoritmos de ordenamiento por selección (ascendente y descendente) con ciclos `while` anidados.
- Manipulación de listas anidadas y modificación *in-place* mediante `.pop()`.
- Procesamiento de caracteres con valores ASCII (`ord()`), división entera (`//`) y aritmética modular (`%`).
- Modelado de algoritmos multi-etapa y simulación de llaves eliminatorias (cálculo iterativo de rondas).
