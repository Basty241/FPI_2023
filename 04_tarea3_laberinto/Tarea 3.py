#
# AUTOR
# NOMBRE: Bastián Alexander Araya Villa
# CARRERA: Ingeniería Civil en Biotecnología


# DEFINICIONES
# Cargar laberinto
def cargar_laberinto(nombre):
  """
  Función que valida un archivo .lab y lo entrega como un laberinto
  Entrada: Un archivo
  Salida: Una lista de listas
  """

  laberinto = []
  # Primero verificamos que se encuentre bien escrito
  puntos = 0
  for i in nombre:
    if i == ".":
      puntos += 1

  # Luego verificamos la extensión del archivo
  if puntos == 1:
    lista = nombre.split(".")

    # De ser correcta leemos el archivo.
    if lista[1] == "lab":
      with open(nombre, "r") as mapa:
        filas = mapa.readlines()

      # Eliminamos los saltos de línea, y transformamos la información
      # de los string a lista
      for i in filas[0:len(filas) - 1]:
        i = list(i)
        i.pop((len(i) - 1))
        i = "".join(i)
        i = i.split(" ")
        laberinto.append(i)

      # La última linea no presenta salto de línea, por lo que sólo es
      # transformada a lista
      filas[len(filas) - 1] = filas[len(filas) - 1].split(" ")
      laberinto.append(filas[len(filas) - 1])

  return laberinto


def encontrar_entrada(laberinto):
  """
  Función que entrega la posición de la entrada del laberinto
  Entrada: Una lista de listas
  Salida: Una lista
  """
  # Voy a reutilizar código de la tarea 2
  # Iteramos por fila y columna en busca de la pieza
  for fila in range(len(laberinto)):
    for columna in range(len(laberinto[fila])):
      if laberinto[fila][columna] == "EE":
        return [fila, columna]


def encontrar_salida(laberinto):
  """
  Función que entrega la posición de la salida del laberinto
  Entrada: Una lista de listas
  Salida: Una lista
  """
  # voy a reutilizar código de la tarea 2
  # Iteramos por fila y columna en busca de la pieza
  for fila in range(len(laberinto)):
    for columna in range(len(laberinto[fila])):
      if laberinto[fila][columna] == "SS":
        return [fila, columna]


def recuperar_camino(laberinto):
  """
  Función que entrega el recorrido desde la entrada a la salida
  Entrada: Una lista de listas
  Salida: Una lista
  """
  # Hacer una lista de listas con las posiciones de las casillas "**"
  camino = []
  portal = []
  for fila in range(len(laberinto)):
    for columna in range(len(laberinto[fila])):
      if laberinto[fila][columna] == "**":
        pos = [fila, columna]
        camino.append(pos)

      # Usaré una lista distinta para los portales
      elif laberinto[fila][columna] == "PP":
        pos = [fila, columna]
        portal.append(pos)

  # Utilizamos las funciones definidas anteriormente para hayar la entrada y
  # salida
  entrada = encontrar_entrada(laberinto)
  salida = encontrar_salida(laberinto)
  camino.append(salida)

  # Luego identifico la casilla más próxima e indico su posición con
  # respecto a la casilla actual.
  recuperado = []
  actual = entrada
  i = 0
  while i < len(camino):
    casilla = camino[i]
    if actual[0] == casilla[0] and actual[1] - casilla[1] == 1:
      actual = casilla
      camino.pop(i)
      recuperado.append("IZ")
      i = -1

    elif actual[0] == casilla[0] and actual[1] - casilla[1] == -1:
      actual = casilla
      camino.pop(i)
      recuperado.append("DE")
      i = -1

    elif actual[1] == casilla[1] and actual[0] - casilla[0] == 1:
      actual = casilla
      camino.pop(i)
      recuperado.append("AR")
      i = -1

    elif actual[1] == casilla[1] and actual[0] - casilla[0] == -1:
      actual = casilla
      camino.pop(i)
      recuperado.append("AB")
      i = -1

    # En caso de haber portales, indicamos en qué dirección se encuentra, y
    # cúando se entra en uno
    elif len(portal) > 0:

      if actual[0] == portal[0][0] and actual[1] - portal[0][1] == 1:
        actual = portal[1]
        portal = []
        recuperado.append("IZ")
        recuperado.append("Portal")
        i = -1

      elif actual[0] == portal[0][0] and actual[1] - portal[0][1] == -1:
        actual = portal[1]
        portal = []
        recuperado.append("DE")
        recuperado.append("Portal")
        i = -1

      elif actual[1] == portal[0][1] and actual[0] - portal[0][0] == 1:
        actual = portal[1]
        portal = []
        recuperado.append("AR")
        recuperado.append("Portal")
        i = -1

      elif actual[1] == portal[0][1] and actual[0] - portal[0][0] == -1:
        actual = portal[1]
        portal = []
        recuperado.append("AB")
        recuperado.append("Portal")
        i = -1

      elif actual[0] == portal[1][0] and actual[1] - portal[1][1] == 1:
        actual = portal[0]
        portal = []
        recuperado.append("IZ")
        recuperado.append("Portal")
        i = -1

      elif actual[0] == portal[1][0] and actual[1] - portal[1][1] == -1:
        actual = portal[0]
        portal = []
        recuperado.append("DE")
        recuperado.append("Portal")
        i = -1

      elif actual[1] == portal[1][1] and actual[0] - portal[1][0] == 1:
        actual = portal[0]
        portal = []
        recuperado.append("AR")
        recuperado.append("Portal")
        i = -1

      elif actual[1] == portal[1][1] and actual[0] - portal[1][0] == -1:
        actual = portal[0]
        portal = []
        recuperado.append("AB")
        recuperado.append("Portal")
        i = -1

    i += 1

  # Por último, se agrega la entrada y salida del laberinto.
  recorrido = ["Entrada"] + recuperado + ["Salida"]
  return recorrido
