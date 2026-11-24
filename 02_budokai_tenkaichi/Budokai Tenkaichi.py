#
# AUTOR
# NOMBRE: Bastián Alexander Araya Villa
# CARRERA: Ingeniería Civil en Biotecnología

# ENTRADAS
# Preselección
q_pre = int(input())
q_cupos = int(input())
participantes = []

for i in range(q_pre):
  participante = input()
  participante = participante.split(",")
  participantes.append(participante)

for i in range(q_pre):
  if participantes[i][1] != "MAQUINA DESTRUIDA":
    participantes[i][1] = int(participantes[i][1])

# Sorteo 
sorteo = input()
sorteo = sorteo.split(",")
for i in range(len(sorteo)):
  sorteo[i] = int(sorteo[i])

# PROCESAMIENTO Y SALIDAS
# Preselección
i=0
clasificados = []
participantes_o = []
# Si el participante rompe la máquina se le asume clasificado, de no hacerlo se le posiciona en una lista ordenada según poder.
maq_dest = 0
while i < len(participantes):
  if participantes[i][1] == "MAQUINA DESTRUIDA":
    maq_dest += 1
    clasificados.append(participantes[i][0])
    participantes.pop(i)
    
  else:
    j=0
    mayor = 0 
    while j < len(participantes):
      if participantes[j][1] != "MAQUINA DESTRUIDA":
        if participantes[j][1] > mayor:
          mayor = participantes[j][1]
          num = j
      j+=1
    participantes_o.append(participantes[num])
    participantes.pop(num)

for i in range(q_cupos-maq_dest):
  clasificados.append(participantes_o[i][0])

#Primera Salida: Participantes seleccionados
print("Y los participantes seleccionados son:")
for i in clasificados:
  print(i)
  
# Sorteo
# Adjuntamos su lugar en las batallas a cada uno de los participantes clasificados
for i in range(len(sorteo)):
  clasificados[i] = [clasificados[i], sorteo[i]]

# Ordenamos según la posición obtenida del sorteo
sorteo_o = []
i=0
while i < len(clasificados):
  k=0
  menor = 3000

  while k < len(clasificados):
    if clasificados[k][1] < menor:
      menor = clasificados[k][1]
      num = k
    k+=1
  sorteo_o.append(clasificados[num])
  clasificados.pop(num)

# Segunda Salida: Combates
print("")
print("Ya tenemos los combates!!!!!")
for i in range(0,q_cupos,2):
  print(str(sorteo_o[i][0]) + " vs " + str(sorteo_o[i+1][0]))
  
# Torneo
# Obtenemos el poder oculto de cada competidor
for i in range(len(sorteo_o)):
  poder_oculto = 0
  letras=0
  
  for j in sorteo_o[i][0]:
    poder_oculto += ord(j)
    letras +=1

  poder_oculto = poder_oculto//letras
  sorteo_o[i].append(poder_oculto)

# Determinamos número de rondas
numero_de_rondas = 0
while q_cupos%2 == 0:
  numero_de_rondas +=1
  q_cupos = q_cupos/2

# Determinamos el ganador de cada combate
print("")
print("Y se lleva a cabo el torneo:")

for k in range(numero_de_rondas):
  i=0
  while i < len(sorteo_o):
    if sorteo_o[i][2] > sorteo_o[i+1][2]:
      print(str(sorteo_o[i][0]) + " vs " + str(sorteo_o[i+1][0]) + " -> Gana  " + str(sorteo_o[i][0]))
      sorteo_o.pop(i+1)
      
    elif sorteo_o[i][2] < sorteo_o[i+1][2]:
      print(str(sorteo_o[i][0]) + " vs " + str(sorteo_o[i+1][0]) + " -> Gana  " + str(sorteo_o[i+1][0]))
      sorteo_o.pop(i)
      
    elif sorteo_o[i][2] == sorteo_o[i+1][2] and sorteo_o[i][2]%2 == 0:
      print(str(sorteo_o[i][0]) + " vs " + str(sorteo_o[i+1][0]) + " -> Gana  " + str(sorteo_o[i][0]))
      sorteo_o.pop(i+1)
      
    elif sorteo_o[i][2] == sorteo_o[i+1][2] and sorteo_o[i][2]%2 != 0:
      print(str(sorteo_o[i][0]) + " vs " + str(sorteo_o[i+1][0]) + " -> Gana  " + str(sorteo_o[i+1][0]))
      sorteo_o.pop(i)
       
    i+=1

print("Y el campeon y poseedor del título del mas fuerte bajo el cielo es: " + str(sorteo_o[0][0]) + " !!!!!")
