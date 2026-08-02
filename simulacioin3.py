import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

frecuencia_muestreo = 1000                                                      #Definición de la señal de entrada en Hz
tiempo = np.linspace(0, 1, frecuencia_muestreo, endpoint=False)

frecuencia_original = 50                                                        #Señal original 
frecuencia_ruido = 300                                                          #Ruido de alta frecuencia
senal_pura = np.sin(2 * np.pi * frecuencia_original * tiempo)
ruido = 0.5 * np.sin(2 * np.pi * frecuencia_ruido * tiempo)
senal_con_ruido = senal_pura + ruido

frecuencia_corte = 100                                                          #Diseño del filtro pasa bajos Butterworth
orden_filtro = 4
frecuencia_nyquist = 0.5 * frecuencia_muestreo
corte_normalizado = frecuencia_corte / frecuencia_nyquist

b, a = butter(orden_filtro, corte_normalizado, btype='low', analog=False)       #Generación de los coeficientes del filtro

senal_filtrada = filtfilt(b, a, senal_con_ruido)                                #Aplicación del filtro a la señal

plt.figure(figsize=(10, 6))                                                     #Visualización de los resultados

plt.subplot(3, 1, 1)
plt.plot(tiempo[0:100], senal_pura[0:100], 'g')
plt.title('Señal Original Pura (50 Hz)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(tiempo[0:100], senal_con_ruido[0:100], 'r')
plt.title('Señal con Ruido (50 Hz + 300 Hz)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(tiempo[0:100], senal_filtrada[0:100], 'b')
plt.title('Señal después del Filtro Pasa Bajos')
plt.grid(True)

plt.tight_layout()
plt.show() 
