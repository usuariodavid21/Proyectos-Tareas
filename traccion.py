import pandas as pd
import math
import matplotlib.pyplot as plt
#Usé librerias pandas para leer el excel y asi trabajar con las funciones mas adelante en la creacion del grafico con matplot
#Leer la base de datos
df = pd.read_excel("C:/Users/hombr/Desktop/progra/Cyr/datos_traccion.xlsx")
print(df)

#Funcion que calcula el area
def calcular_area(diametro):
    radio =diametro/2
    area = (math.pi * radio ** 2)
    return area 



#=================
#Inputs(datos de entrada)
diametro = float(input("Introduzca el diametro(mm)"))
#De este dato calcular el area(aun no esta transformada a metros)
area=calcular_area(diametro)
#"12.83(Para comprobar con los datos de la tabla del ppt)"
long=float(input("Introduzca longitud inicial(mm)"))

#"50.8(Para comprobar con los datos de la tabla del ppt)"
#=================

#=================
#Transformaciones de variables y calcular esfuerzo y deformacion
#Con ayuda de funciones lambda hacemos la transformacion y la operacion para el esfuerzo
df["Esfuerzo(kPa)"] = df["Carga"].apply(lambda x: x / area*1000)
print(df)
#Repetimos y aqui no se cambia la medida
df["Deformacion(mm)"] = df["Cambio de longitud"].apply(lambda x: x / long)
print(df)
#=================



#=================
#Creacion del grafico
#Selecciona las dos ultimas columnas de la base de datos
x = df.iloc[:,-1] #(Deformacion)
y = df.iloc[:,-2] #(Esfuerzo)
#Crea el gráfico
plt.plot(x, y)
#Muestra el gráfico
plt.show()
#=================