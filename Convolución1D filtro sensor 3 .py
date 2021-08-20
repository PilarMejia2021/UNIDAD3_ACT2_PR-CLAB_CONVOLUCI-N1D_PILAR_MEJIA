#Usaremos la libreria pyserial para la adquisición serial

import serial
import numpy as np
from matplotlib import pyplot as plt
from time import time
import re

%matplotlib notebook

# Iniciamos comunicación serial
com_ser = serial.Serial('/COM3', 230400)
com_ser.flushInput()

# Configuración en la visualización
RangoY = [700, 900]  # Define el rango de la gráfica en el eje y
VentanaTiempo = 5  # Define la ventana de tiempo que si visualiza en tiempo real
TiempoFinal = 30  # Define el tiempo total de adquisición

# Configuración de la figura
plt.ion()
figura1 = plt.figure()
figura1.suptitle('Gráfica en tiempo real', fontsize='16', fontweight='bold')
plt.xlabel('Tiempo (s)', fontsize='14')
plt.ylabel('Amplitud', fontsize='14')
plt.axes().grid(True)

# Lista para guardar datos Tiempo y Amplitud
timepoints = []
ydata = []

# Configuración de la curva
line1, = plt.plot(ydata, marker='+', markersize=4, linestyle='-')
plt.ylim(RangoY)
plt.xlim([0, VentanaTiempo])

run = True
start_time = time()

while run:
    com_ser.reset_input_buffer()
    data = str(com_ser.readline())  # Lectura del puerto

    # El envío se realiza con un marcador $, sólo si la trama tiene ese marcador se separará los datos de la trama
    if (len(data.split('$')) >= 2):
        data_sp = data.split('$')[1].split('\\r\\n')[0]

    try:
        # Agregamos los datos de amplitud y tiempo a cada lista
        ydata.append(float(data_sp))
        timepoints.append(time() - start_time)
        current_time = timepoints[-1]

        # Se actutaliza los datos en la grafica
        line1.set_xdata(timepoints)
        line1.set_ydata(ydata)

        # Se actualiza la ventan de observación de la gráfica
        if current_time > VentanaTiempo:
            plt.xlim([current_time - VentanaTiempo, current_time])

        # La ejecución termina cuando el tiempo de ejecución llega al límite
        if timepoints[-1] > TiempoFinal: run = False

    except:
        pass

# Actualiza la gráfica
    figura1.canvas.draw()

# Cierra el puerto serial
com_ser.close()

I=np.array(ydata)
t=np.array(timepoints)

k=np.array([0.25,0.25,0.25,0.25])
S=np.convolve(I,k,mode='same')
print(len(S),len(I),len(k))

fig, ax1 = plt.subplots(1)
ax1.plot(t,I,'-')
ax1.plot(t[2:-1] ,S[2:-1] ,'-')
plt.show()

datos= {'Tiempo':timepoints,'Amplitud':ydata}
df = pd.DataFrame(datos)
df.to_csv('DatosRegistrados.csv', index=False)



