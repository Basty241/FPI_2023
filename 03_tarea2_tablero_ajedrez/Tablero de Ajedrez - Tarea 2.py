#
# AUTOR
# NOMBRE: Bastián Alexander Araya Villa
# CARRERA: Ingeniería Civil en Biotecnología


# DEFINICIONES
# Validar Casillas
def validar_posicion(pos, tablero):
  """
  Función que valida una posición en el tablero
  Entrada: Un string y una lista de listas
  Salida: Un entero
  """
  # LISTA.
  COLUMNAS = ["A", "B", "C", "D", "E", "F", "G", "H"]
  
  # Cortamos el string de la posición
  pos = list(pos)

  # Identificamos la columna en la lista
  columna = 9
  for j in range(len(COLUMNAS)):
    if pos[0] == COLUMNAS[j]:
      columna = j

  # Identificamos la fila en la lista
  fila = 8 - int(pos[1])

  # Validamos la existencia de la posición
  if fila in range(0,8) and columna in range(0,8):
    
    # Verificamos si la posición está disponible
    if tablero[fila][columna] == "  ":
      return 0

    # Si no está disponible, y existe, implica que está en uso .
    else:        
      return 1

  # La posición no existe en el tablero
  else: 
    return -1

    
# Entregar piezas ubicadas
def entregar_tablero(piezas):
  """
  Función que posiciona una serie de piezas en el tablero
  Entrada: Un string
  Salida: Una lista de listas
  """
  # LISTAS
  TABLERO = [['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  '],
             ['  ','  ','  ','  ','  ','  ','  ','  ']]
  
  COLUMNAS = ["A" , "B", "C", "D", "E", "F", "G", "H"]
  
  # Separamos el string e iteramos la lista.
  piezas = piezas.split(",")

  for i in piezas:
    # Valida la pieza y posición en el tablero.
    if validar_posicion(i[2:4], TABLERO) == 0:
      
      # Identificamos la columna en la lista.
      columna = 9
      for j in range(len(COLUMNAS)):
        if i[2] == COLUMNAS[j]:
          columna = j
  
      # Identificamos la fila en la lista.
      fila = 8 - int(i[3])
      
      # Colocamos la pieza
      TABLERO[fila][columna] = i[0:2]
        
  return TABLERO   

# Revisar si el tablero es válido
def es_valido(tablero):
  """
  Función que valida un tablero en juego.
  Entrada: Una lista de listas
  Salida: Un booleano
  """
  # Lista de casillas negras.
  CASILLAS_N = [[0,1], [0,3], [0,5], [0,7],
                [1,0], [1,2], [1,4], [1,6],
                [2,1], [2,3], [2,5], [2,7],
                [3,0], [3,2], [3,4], [3,6],
                [4,1], [4,3], [4,5], [4,7],
                [5,0], [5,2], [5,4], [5,6],
                [6,1], [6,3], [6,5], [6,7],
                [7,0], [7,2], [7,4], [7,6]]
  
  # Primero nos aseguramos que no hayan peones en la primera, ni en la última fila.
  for fila in tablero[0:8:7]:
    for pieza in fila:
      if pieza[1] == "P":
        return False

  # Creamos contadores.
  peones_b = 0
  peones_n = 0
  rey_b=0
  rey_n=0
  torres_b=0
  torres_n=0
  damas_b=0
  damas_n=0
  caballos_b=0
  caballos_n=0

  # Contamos las piezas.
  for fila in tablero:
    for pieza in fila:
      if pieza[0:2] == "BP":
        peones_b += 1
      elif pieza[0:2] == "NP":
        peones_n += 1

      elif pieza[0:2] == "BR":
        rey_b += 1
      elif pieza[0:2] == "NR":
        rey_n += 1

      elif pieza[0:2] == "BT":
        torres_b += 1
      elif pieza[0:2] == "NT":
        torres_n += 1
        
      elif pieza[0:2] == "BD":
        damas_b += 1
      elif pieza[0:2] == "ND":
        damas_n += 1

      elif pieza[0:2] == "BC":
        caballos_b += 1
      elif pieza[0:2] == "NC":
        caballos_n += 1

  # Verificamos el número de peones
  if peones_b > 8 or peones_n > 8:
    return False

  # Verificamos el número de torres
  if torres_b > 2 or torres_n > 2:
    return False

  # Verificamos el número de damas
  if damas_b > 1 or damas_n > 1:
    return False

  # Verificamos el número de caballos
  if caballos_b > 2 or caballos_n > 2:
    return False

  # Verificamos la existencia de un Rey por lado.
  if rey_b != 1 or rey_n != 1:
    return False
  
  # Contamos el número de alfiles
  alfil_b = []
  alfil_n = []
  for fila in range(0,8): 
    for columna in range(0,8):  
      
      if tablero[fila][columna][0:2] == "BA":
        alfil_b.append([fila, columna])  
      elif tablero[fila][columna][0:2] == "NA":
        alfil_n.append([fila, columna])

  # Si hay menos de 2 alfiles por lado, entonces siempre será verdadero.
  if len(alfil_b) < 2 and len(alfil_n) < 2:
    return True

  # De haber más de 2 alfiles, entonces siempre será falso.
  if len(alfil_b) > 2 or len(alfil_n) > 2:
    return False
    
  # De haber 2 alfiles blancos, verificamos que vayan en casillas de distinto color.
  if len(alfil_b) == 2:
    if alfil_b[0] in CASILLAS_N and alfil_b[1] not in CASILLAS_N:
      alfil_b = True
    else:
      return False

  # De haber 2 alfiles negros, verificamos que vayan en casillas de distinto color.
  if len(alfil_n) == 2:
    if alfil_n[0] in CASILLAS_N and alfil_n[1] not in CASILLAS_N:
      alfil_n = True
    else:
      return False

# Verificar si los reyes están en jaque.
def hay_jaque(tablero):
  """
  Función que verifica si los reyes se encuentran en jaque.
  Entrada: Una lista de listas
  Salida: Un entero
  """
  # Vamos a primero definir la posición de las piezas.
  rey_b = []
  rey_n = []
  piezas = []
  for fila in range(0,8): 
    for columna in range(0,8):
      # Los reyes se añaden en listas aparte, para facilitar la iteración de las piezas
      if tablero[fila][columna] == "BR":
        rey_b = [fila, columna]
        
      elif tablero[fila][columna] == "NR":
        rey_n = [fila, columna]

      elif tablero[fila][columna] != "  ":
        pieza = tablero[fila][columna] + str(fila) + str(columna)
        piezas.append(pieza)

  # Definimos variables que nos permitan controlar el flujo de la iteración.
  amenaza_b = False
  amenaza_n = False
  mov_hor = ["D", "T"]
  mov_diag = ["D", "A"]
  
  # Iteramos las piezas.
  for k in piezas:
    fila = int(k[2])
    columna = int(k[3])

    # Verificamos si está en amenaza por un peon
    if k[0:2] == "NP":
      if rey_b[0] - 1 == fila and abs(rey_b[1] - columna) == 1:
        amenaza_b = True

    elif k[0:2] == "BP":
      if rey_n[0] + 1 == fila and abs(rey_n[1] - columna)==1:
        amenaza_n = True

    # Verificamos si está en amenaza por un caballo, con los valores absolutos de la
    # diferencia para definir las 2 posibles forma de la "L" en distintas direcciones.
    elif k[0:2] == "NC":
      if abs(rey_b[0] - fila) == 2 and abs(rey_b[1] - columna) == 1:
        amenaza_b=True
        
      elif abs(rey_b[0]-fila) == 1 and abs(rey_b[1]-columna) == 2:
        amenaza_b=True

    elif k[0:2] == "BC":
        if abs(rey_n[0]-fila) == 2 and abs(rey_n[1]-columna) == 1:
          amenaza_n=True
          
        elif abs(rey_n[0]-fila) == 1 and abs(rey_n[1]-columna) == 2:
          amenaza_n=True
    
    # Verificamos si el rey blanco está en riesgo por una pieza de movimiento recto.
    if k[0] == "N" and k[1] in mov_hor and amenaza_b is False:

      # Misma fila distinta columna.
      if rey_b[0] == fila and rey_b[1]-columna < 0:
        amenaza_b=True
        for i in range(rey_b[1]+1, columna):
          if tablero[fila][i] != "  ":
            amenaza_b=False

      elif rey_b[0] == fila and rey_b[1]-columna > 0:
        amenaza_b=True
        for i in range(columna+1, rey_b[1]):
          if tablero[fila][i] != "  ":
            amenaza_b=False

      # Misma columna distinta fila.
      elif rey_b[1] == columna and rey_b[0]-fila > 0:
        amenaza_b=True
        for i in range(fila+1, rey_b[0]):
          if tablero[i][columna] != "  ":
            amenaza_b=False

      elif rey_b[1] == columna and rey_b[0]-fila < 0:
        amenaza_b=True
        for i in range(rey_b[0]+1, fila):
          if tablero[i][columna] != "  ":
            amenaza_b = False

    # Verificamos si el rey negro está en riesgo por una pieza de movimiento recto.
    elif k[0] == "B" and k[1] in mov_hor and amenaza_n is False:

      # Misma fila distinta columna.
      if rey_n[0] == fila and rey_n[1] - columna < 0:
        amenaza_n = True
        for i in range(rey_n[1] + 1, columna):
          if tablero[fila][i] != "  ":
            amenaza_n = False
  
      elif rey_n[0] == fila and rey_n[1] - columna > 0:
        amenaza_n = True
        for i in range(columna + 1, rey_n[1]):
          if tablero[fila][i] != "  ":
            amenaza_n = False

      # Misma columna distinta fila.
      elif rey_n[1] == columna and rey_n[0] - fila > 0:
        amenaza_n = True
        for i in range(fila + 1, rey_n[0]):
          if tablero[i][columna] != "  ":
            amenaza_n = False
  
      elif rey_n[1] == columna and rey_n[0] - fila < 0:
        amenaza_n = True
        for i in range(rey_n[0] + 1, fila):
          if tablero[i][columna] != "  ":
            amenaza_n = False

    # Verificamos si el rey blanco está en riesgo por una pieza de movimiento diagonal
    if k[0] == "N" and k[1] in mov_diag and amenaza_b is False:
      if abs(rey_b[0] - fila) == abs(rey_b[1] - columna):
        amenaza_b = True
        # Definimos distancia y sentido.
        rango = abs(rey_b[0] - fila)
        sentido = [str(rey_b[0] - fila), str(rey_b[1] - columna)]

        # Los cuadrantes están rotados en sentido anti-horario, por lo que la pieza
        # se encuentra en el 2do cuadrante, en un plano cartesiano típico.
        if sentido[0][0] != "-" and sentido[1][0] != "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_b[0] - i][rey_b[1] - i] != "  ":
              amenaza_b = False

        # La pieza se encuentra en el tercer cuadrante.
        elif sentido[0][0] == "-" and sentido[1][0] != "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_b[0] + i][rey_b[1] - i] != "  ":
              amenaza_b = False

        # La pieza se encuentra en el cuarto cuadrante.
        elif sentido[0][0] == "-" and sentido[1][0] == "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_b[0] + i][rey_b[1] + i] != "  ":
              amenaza_b = False

        # La pieza se encuentra en el primer cuadrante.
        elif sentido[0][0] != "-" and sentido[1][0] == "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_b[0] - i][rey_b[1] + i] != "  ":
              amenaza_b = False

    # Verificamos si el rey negro está en riesgo por una pieza de movimiento diagonal
    elif k[0] == "B" and k[1] in mov_diag and amenaza_n is False:
      if abs(rey_n[0] - fila) == abs(rey_n[1] - columna):
        amenaza_n = True
        rango = abs(rey_n[0] - fila)
        sentido = [str(rey_n[0] - fila), str(rey_n[1] - columna)]

        # Los cuadrantes están rotados en sentido anti-horario, por lo que la pieza
        # se encuentra en el segundo cuadrante, en un plano cartesiano típico.
        if sentido[0][0] != "-" and sentido[1][0] != "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_n[0] - i][rey_n[1] - i] != "  ":
              amenaza_n = False

        # La pieza se encuentra en el tercer cuadrante.
        elif sentido[0][0] == "-" and sentido[1][0] != "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_n[0] + i][rey_n[1] - i] != "  ":
              amenaza_n = False

        # La pieza se encuentra en el cuarto cuadrante.
        elif sentido[0][0] == "-" and sentido[1][0] == "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_n[0] + i][rey_n[1] + i] != "  ":
              amenaza_n = False

        # La pieza se encuentra en el primer cuadrante.
        elif sentido[0][0] != "-" and sentido[1][0] == "-" and rango != 0:
          for i in range(1,rango):
            if tablero[rey_n[0] - i][rey_n[1] + i] != "  ":
              amenaza_n = False

  # Devolvemos el nivel de amenaza
  amenaza = -1
  if amenaza_b is True:
    amenaza += 1
  if amenaza_n is True:
    amenaza += 2
  return amenaza
