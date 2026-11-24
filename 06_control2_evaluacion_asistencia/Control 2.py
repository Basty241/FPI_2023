#
# AUTOR
# NOMBRE: Bastián Araya Villa
# CARRERA: Ingeniería Civil en Biotecnología
# <Incluya aquí una breve descripción del programa>


def evaluar(a_asistencia, a_asistencia_ia):

  with open(a_asistencia, "r") as tradicional:
    a_trad = tradicional.readlines()

# Estoy reutilizando de mi código de la tarea 3
  lista_trad = []
  for i in a_trad[0:len(a_trad) - 1]:
    i = list(i)
    i.pop((len(i) - 1))
    i = "".join(i)
    i = i.split(" ")
    lista_trad.append(i)

  dias = []
  j = 0
  lista_trad.pop(0)
  for i in range(len(lista_trad)):
    if lista_trad[i][0] == "Clase":
      diaria = lista_trad[j:i]
      j = i + 1
      dias.append(diaria)

  dias.append(lista_trad[j:len(lista_trad) - 1])

  # Hacemos una lista con los alumnos
  alumnos = []
  asistencia = []
  for i in lista_trad:
    if i[0] != "Clase" and i not in alumnos:
      alumnos.append(i)
      asistencia.append([])

  # Hacemos una lista semejante a la de la IA
  for i in dias:
    for j in range(len(alumnos)):
      if alumnos[j] in i:
        asistencia[j].append("1")
      else:
        asistencia[j].append("0")

  # Abrimos el archivo de la IA
  with open(a_asistencia_ia, "r") as artificial:
    a_art = artificial.read()

  a_art = a_art.split(" ")

  # Comparamos listas
  # Primero identificamos el alumno
  alumno = 38
  for i in range(len(alumnos)):
    if alumnos[i] == a_art[0:2]:
      alumno = i

  # Luego comparamos la asistencia del alumno
  resultado = []
  resultado.append(alumnos[alumno][0])
  resultado.append(alumnos[alumno][1])
  for i in range(len(asistencia[alumno])):
    if asistencia[alumno][i] == a_art[i + 2]:
      resultado.append("O")
    else:
      resultado.append("X")

  # Por último, ajustamos el formato de entrega
  resultado = " ".join(resultado)
  with open("test_resultado.txt", "w") as salida:
    a_sal = salida.write(resultado)

  return salida
