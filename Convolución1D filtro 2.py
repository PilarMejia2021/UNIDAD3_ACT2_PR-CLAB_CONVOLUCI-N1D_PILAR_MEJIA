#Cargamos datos que representan series de tiempo. En este caso datos de un sensor de velocidad de un motor

import pandas as pd
Datos = pd.read_csv('3.data/Motor.csv')
Datos.head()

Datos.plot(x='Tiempo',y='Amplitud')
plt.show()

Datos_numpy=Datos.to_numpy()
I=Datos_numpy[:,1]
t=Datos_numpy[:,0]

k=np.array([0.25,0.25,0.25,0.25])
S=np.convolve(I,k,mode='same')
print(len(S),len(I),len(k))

%matplotlib notebook:
plt.ion()

fig, ax1 = plt.subplots(1)
ax1.plot(t,I,'-*')
ax1.plot(t[1:-1] ,S[1:-1] ,'-')
plt.show()


