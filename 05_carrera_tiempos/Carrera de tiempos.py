#  
# AUTOR  
# NOMBRE: Bastián Alexander Araya Villa  
# CARRERA: Ingeniería Civil en Biotecnología  
# <Se ha realizado una carrera y se han registrado los tiempos realizados por los participantes para cada una de las tres vueltas de la competencia. Se desea saber cuál de los participantes hizo menor tiempo o si hubo un empate entre los mejores tiempos. Para esto se le solicita entregar el número del jugador que ganó contando desde 1, en caso de haber empate debe solamente decir 'Hubo un empate.'.>

# ENTRADAS
# Separamos los competidores
competidores = input().split(";")

# PROCESAMIENTO
# Separamos las carreras por competidor
for i in range(len(competidores)):
  competidores[i] = competidores[i].split(",")

# Separamos los valores de hora, minuto y segundo
for i in range(len(competidores)):
  competidores[i][0] = competidores[i][0].split(":")
  competidores[i][1] = competidores[i][1].split(":")
  competidores[i][2] = competidores[i][2].split(":")
  
# Sumamos los tiempos en segundos
i=0
competidor = []
while i < len(competidores):
  tiempo_seg = 0
  carrera_1 = competidores[i][0]
  carrera_2 = competidores[i][1]
  carrera_3 = competidores[i][2]
  
  tiempo_seg += ((int(carrera_1[0])+ int(carrera_2[0]) + int(carrera_3[0]))*3600)
  tiempo_seg += ((int(carrera_1[1])+ int(carrera_2[1]) + int(carrera_3[1]))*60)
  tiempo_seg += (int(carrera_1[2])+ int(carrera_2[2]) + int(carrera_3[2]))
  
  competidor.append(tiempo_seg)
  i+=1
  
# Ordenamos la lista
i=0
competidor_ord = []
while i < len(competidor):
  menor = 100000000000000
  j=0
  while j<len(competidor):
    if competidor[j] < menor:
      menor = competidor[j]
      num =j
    j+=1
# El primer valor corresponde al tiempo en segundos del competidor, y el segundo corresponde al número del competidor.
  competidor_ord.append([competidor[num],num+1])
  competidor.pop(num)

# Revisamos si hay empate
ganador = competidor_ord[0]
empate = 0
i = 1
#De ser un empate, vamos almacenando todos los que hayan obtenido el mismo tiempo.
while competidor_ord[i] == ganador:
  empate += 1
  i+=1

# Si empate es igual a 0, implica que no hubo ningún empate.
if empate == 0:
  print(competidor_ord[0][1])

# Si empate es distinto de 0, se indicará que hubo un empate
else:
  print("Hubo un empate")
