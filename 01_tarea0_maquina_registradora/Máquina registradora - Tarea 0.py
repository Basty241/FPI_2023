#  
# AUTOR  
# NOMBRE: Bastián Alexander Araya Villa
# CARRERA: Ingeniería Civil en Biotecnología 
# Programa de lectura de precios y descuentos, entregando cantidad de dinero ahorado, total a pagar, cantidad de puntos acumulados y un mensaje de despedida cuando el programa finaliza

# VARIABLES
num_prod = 0
nombre = []
tipo = []
precio = []
cantidad = []

num_dcto = 0 

motivo = []
porc_dcto_1 = []

prod_dcto = []
porc_dcto_2 = []

subtotal = 0
dcto_total = 0

# ENTRADAS
prod = input()
while prod != "FIN LECTURA":

  prod = prod.split(",")
  num_prod += 1
  if len(prod) == 4:
    
    if int(prod[2]) >= 1 and int(prod[3]) >= 1:
      nombre.append(prod[0])
      tipo.append(prod[1])
      precio.append(int(prod[2]))
      cantidad.append(int(prod[3]))
      
    else:
      print(f"Error de ingreso en producto: {num_prod}")
    
  else:
    print(f"Error de ingreso en producto: {num_prod}")
  prod = input()

# Entrada Descuentos
dcto = input()
while dcto != "FIN DESCUENTOS":
    
  dcto = dcto.split(",")
  num_dcto += 1 

  if len(dcto) == 3:
    
    if int(dcto[2]) <= 99 and int(dcto[2]) >= 0:
    
      if dcto[0] == "al total":
        motivo.append(dcto[1])
        porc_dcto_1.append(int(dcto[2]))
    
      elif dcto[0] == "por producto":
        prod_dcto.append(dcto[1])
        porc_dcto_2.append(int(dcto[2]))

      else:
        print(f"Error de ingreso en descuento: {num_dcto}")

    else:
      print(f"Error de ingreso en descuento: {num_dcto}")
    
  else:
      print(f"Error de ingreso en descuento: {num_dcto}")
  dcto = input()
  
# PROCESAMIENTO
# Impuestos
for i in range(len(tipo)):
  if i == "vinos" or i == "cigarros" or i == "bebidas alcohólicas" or i == "cosas de furros":
    precio[i] = precio[i] * 1.25
    
  else:
    precio[i] = precio[i] * 1.2

# Costo total por nombre de producto
for i in range(len(nombre)):
      precio[i] = precio[i]*cantidad[i]
  
# Costo total por tipo de producto
i=0
while i < len(tipo):
  j=0
  while j < len(precio):
    if tipo[i] == tipo[j] and nombre[i] != nombre[j]: 
      precio[j] = precio[i] + precio[j]
      tipo.pop(i)
      precio.pop(i)
      i += -1
      break
    j += 1
  i += 1
  
# Subtotal
for i in range(len(tipo)):
  subtotal += precio[i]
  
#Descuentos por producto
k=0
while k < len(prod_dcto):
  i=0
  while i < len(tipo):  
    if tipo[i] == prod_dcto[k]:
      ahorro = precio[i] * (porc_dcto_2[k]/100)
      print(f"Con el descuento '{prod_dcto[k]}', te ahorraste ${ahorro}")
      subtotal = subtotal - ahorro
      tipo.pop(i)
      precio.pop(i)
    i +=1
  k += 1
  
# Descuentos al total
for i in range(len(motivo)):
  ahorro = subtotal * (porc_dcto_1[i]/100)
  print(f"Con el descuento '{motivo[i]}', te ahorraste ${ahorro}")
  subtotal = subtotal - ahorro

#Total de la boleta
total = subtotal
print(f"El total de su boleta es de ${total}, impuestos incluidos") 

# Oso puntos
oso_puntos = int(total//100)
print(f"Esta compra acumula {oso_puntos} oso puntos")

# Despedida
print("Gracias, vuelva prontos")



