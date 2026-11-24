# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:44:25 2023

@author: KmanO
"""

# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from folium import Polygon, Popup, Map
from webbrowser import open


def mostrar_grafico():
    """
    Función que transforma la información contenida en un archivo .xlsx, en
    una gráfica de emisiones con respecto al tiempo.
    Entrada: Un link
    Salida: Una gráfica
    """
    
    # Leer el archivo, cambiar el usuario de usar el código en otro ordenador.
    datos = pd.read_excel(r"C:/Users/KmanO/Desktop/Datos.xlsx", sheet_name=0)
    
    # Nombrar los ejes.
    x_axis = datos["Columna1"]
    y_axis1 = datos["2020"]
    y_axis2= datos["2021"]
    y_axis3= datos["2022"]
    
    # Crear Canvas.
    fig, graph = plt.subplots(figsize=(10, 4), layout='constrained')
    widget = FigureCanvasTkAgg(fig, master = ventana)
    
    # Construir las gráficas
    graph.plot(x_axis,y_axis1, marker = "o", label="2020")
    graph.plot(x_axis,y_axis2, marker = "o", label = "2021")
    graph.plot(x_axis,y_axis3, marker = "o", label = "2022")
    graph.legend()
    plt.xlabel("Meses")
    plt.ylabel("CO2eq[ton]")
    
    # Dibujar la gráfica en el canvas
    widget.draw()
    
    # Pack graph
    widget.get_tk_widget().place(x=40, y=50)
    
    # Mostrar las gráficas.
    return widget

def entregar_tamarugos(ha):
    """
    Función que calcula la cantidad de tamarugos por hectarea
    Entrada: Un número real
    Salida: Un número entero
    """
    # Calcula la cantidad de tamarugos
    tamarugos = ha*44//1
    
    return tamarugos

def entregar_hidrico():
    """
    Función que entrega los requerimientos mensuales de agua de la plantación, en un lapso de 12 meses.
    Entrada: Un entero
    Salida: Una gráfica
    """
    # Entrega los requerimientos hídricos
    req_hid = []
    req_plantacion = 10
    tamarugos = entregar_tamarugos(ha)
    
    # Son 9L de agua cada 20 días por planta, durante los 6 meses posteriores a la plantación.
    riegos = 6*30/20
    req_mensual1 = riegos*tamarugos*9
    
    # Son 9L de agua cada 40 días por planta, durante los 3 meses posteriores.
    riegos = 6*30/40
    req_mensual2 = riegos*tamarugos*9
    
    # Se crea la lista a graficar
    req_hid.append(req_plantacion+req_mensual1)
    
    for i in range(0,5):
        req_hid.append(req_mensual1)
        
    for i in range(0,3):
        req_hid.append(req_mensual2)
        
    for i in range(0,3):
        req_hid.append(0)
    
    x_axis = range(1,13)
    y_axis = req_hid
    
    # Crear Canvas.
    fig, bars = plt.subplots(figsize=(10, 4), layout='constrained')
    widget2 = FigureCanvasTkAgg(fig, master = ventana)
    
    # Crear la gráfica.
    bars.bar(x_axis,y_axis)
    plt.xlabel("Meses")
    plt.ylabel("Requerimiento hídrico [L]")
    
    # Dibujar la gráfica en el canvas
    widget2.draw()
    
    # Pack graph
    widget2.get_tk_widget().place(x=40, y=50)
    
    return req_hid   

def mostrar_mapa():
    # crear variable con el mapa/ zoom inicial
    area_sembradio = Map(location=[-22.3169864, -68.8420026], zoom_start=13)
    
    # se indican los puntos a delimitar
    area_points = [
        [-22.3169864, -68.8420026],
        [-22.3073793, -68.8438701],
        [-22.3058651, -68.8406399],
        [-22.3032530, -68.8410079],
        [-22.3007002, -68.8254799],
        [-22.3110316, -68.8276296],
        [-22.3169864, -68.8420026]
    ]
    
    # se delimita el area.
    Polygon(
        locations=area_points,
        color="crimson",
        fill=True,
        popup=Popup("Área de sembradío 1", max_width=250) #popup al hacer click
    ).add_to(area_sembradio)
    
    
    area_points = [
        [-22.3105160, -68.8259822],
        [-22.3007934, -68.8243497],
        [-22.2959132, -68.7963951],
        [-22.3038591, -68.8008157],
        [-22.3105160, -68.8259822],
    ]
    
    
    Polygon(
        locations=area_points, 
        color="blue",
        fill=True,
        popup=Popup("Área de sembradío 2", max_width=250)
    ).add_to(area_sembradio)
    
    
    area_points = [
        [-22.3181591, -68.8392250],
        [-22.3114665, -68.8263936],
        [-22.3055011, -68.8017660],
        [-22.3132786, -68.8064563],
        [-22.3170338, -68.8279724],
        [-22.3207384, -68.8372996],
        [-22.3181591, -68.8392250],
    ]
    
    
    Polygon(
        locations=area_points,
        color="green",
        fill=True,
        popup=Popup("Área de sembradío 3", max_width=250)
    ).add_to(area_sembradio)
    
    # guardar en html para ver mapa
    area_sembradio.save('map.html')
    
    open('map.html')
    
    return


def entregar_costos():
    # Leer el archivo, cambiar el usuario de usar el código en otro ordenador.
    datos = pd.read_excel(r"C:/Users/KmanO/Desktop/Costos.xlsx", sheet_name=0)
    
    # Nombrar los datos.
    x_axis = datos["Insumos"]
    y_axis1 = datos["Precio unitario"]
    y_axis2 = datos["Cantidad x10"]
    
    tamarugos = entregar_tamarugos(ha)
    costo_total = 0
    
    for i in range(len(x_axis)):
        costo = y_axis1[i] * y_axis2[i] * tamarugos // 10
        costo_total += costo  
        
    costo_label.config(text=f"Costo total: ${costo_total}")
    
    with open("C:/Users/KmanO/Desktop/Instrucciones.docx") as instrucciones:
        texto = instrucciones
            
    messageVar = tk.Label(ventana, text="", font = ('Arial',10))
    messageVar.place(x=0, y=0)
    messageVar.config(text=f"{texto}")
    
# Crear una ventana
ventana = tk.Tk()
ventana.geometry("800x500")
ventana.title("Plan Forestación")

# Editar el número de hectáreas
ha = 100

# Crear una etiqueta para mostrar el costo
costo_label = tk.Label(ventana, text="", font = ('Arial',20))
costo_label.place(x=250, y=100)

# Crear un botón para visualizar el gráfico.
plot_button = tk.Button(ventana, width=12, height=2, bg="gray", command = mostrar_grafico, text = "Emisiones")
plot_button.place(x=0, y=0)

# Crear un botón para visualizar el gráfico de barras.
plot_button = tk.Button(ventana, width=12, height=2, bg="gray", command = entregar_hidrico, text = "Requirimientos \n Hidricos")
plot_button.place(x=100, y=0)

# Crear un botón para visualizar el mapa
plot_button = tk.Button(ventana, width=12, height=2, bg="gray", command = mostrar_mapa, text = "Mapa de \n Calama")
plot_button.place(x=200, y=0)

# Crear un botón para visualizar el precio de tamarugos
plot_button = tk.Button(ventana, width=12, height=2, bg="gray", command = entregar_costos, text = "Precio de \n Tamarugos")
plot_button.place(x=300, y=0)


ventana.mainloop()

