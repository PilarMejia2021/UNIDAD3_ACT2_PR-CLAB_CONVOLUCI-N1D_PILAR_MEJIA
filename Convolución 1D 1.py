
import numpy as np
import matplotlib.pyplot as plt

#Creamos una señal de entrada I, y un kernel de convolución k. Luego graficamos las señales y verificamos su longitud
I = np.array([0,2,2,2,-1,-1,0])
k = np.array([0,1,1])

print('Longitud de la señal de entrada: {}'.format(len(I)))
print('Longitud del kernel de convolucion: {}'.format(len(k)))

fig, axs = plt.subplots(2,sharex=True, sharey=True)

axs[0].stem(I)
axs[1].stem(k)

#Realizamos la operacion de convolución entre I y k
S = np.convolve(I,k)
print('La longitud de S debe ser (len(I)+ len(k)-1): {}'.format(len(S)))

plt.stem(S)


