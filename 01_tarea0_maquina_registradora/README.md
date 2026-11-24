# Máquina Registradora

**Archivo:** [`Máquina registradora - Tarea 0.py`](./M%C3%A1quina%20registradora%20-%20Tarea%200.py)

## ¿De qué se trata?

Simula el flujo de cobro de una caja registradora por consola. Lee secuencialmente productos en formato `nombre,tipo,precio,cantidad` hasta recibir el centinela `FIN LECTURA` y luego descuentos en formato `modalidad,objetivo,porcentaje` (`al total` o `por producto`) hasta `FIN DESCUENTOS`. Valida estructura y rangos numéricos de cada entrada, aplica recargos de impuestos, agrupa costos por tipo de producto, descuenta promociones por categoría y sobre el total, y calcula los puntos acumulados (`total // 100`).

## Tipo de salidas

Salida estándar por consola (`stdout`), compuesta por:
- Mensajes de error por cada producto o descuento con formato o rango inválido (`Error de ingreso en producto/descuento: N`).
- Detalle del monto ahorrado por cada descuento aplicado.
- Total final de la boleta con impuestos incluidos.
- Cantidad de puntos acumulados ("oso puntos") y mensaje de cierre.

## Habilidades de programación evidenciadas

- Control de flujo iterativo con centinelas (`while`) y condicionales anidados (`if`/`elif`/`else`).
- Validación de formato y rangos de entrada del usuario (`input()`).
- Separación de cadenas (`str.split`), conversión de tipos (`int`) y gestión de listas paralelas.
- Agrupación y acumulación de valores numéricos, cálculo de porcentajes y división entera (`//`).
- Formateo de texto dinámico con *f-strings*.
