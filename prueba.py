import matplotlib.pyplot as plt
import soundfile as sn
import numpy as np
from scipy.fft import fft, fftfreq

plt.close('all')

# Leer archivos de sonido
data, Fs = sn.read('s1cel1.wav')
datas, Fs2 = sn.read('s2cel2.wav')
dato, Fs3 = sn.read('s3cel3.wav')
datar, Fs4 = sn.read('Ruido2.wav')

# Verificar que todas las frecuencias de muestreo sean iguales
if not (Fs == Fs2 == Fs3 == Fs4):
    raise ValueError("Las frecuencias de muestreo no son iguales. No se puede continuar.")

# Análisis temporal
time = np.arange(0, len(data)) / Fs
time_datas = np.arange(0, len(datas)) / Fs
time_dato = np.arange(0, len(dato)) / Fs
time_datar = np.arange(0, len(datar)) / Fs

plt.figure(figsize=(10, 6))

plt.plot(time, data, label='Señal 1 persona 1', color='blue')
plt.plot(time_datas, datas, label='Señal 1 persona 2', color='green')
plt.plot(time_dato, dato, label='Señal 1 persona 3', color='red')
plt.plot(time_datar, datar, label='Ruido', color='orange')

plt.title("Análisis Temporal de Todas las Señales")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.show()

# Análisis espectral usando FFT
N = len(data)
T = 1.0 / Fs

yf_data = fft(data)
yf_datas = fft(datas)
yf_dato = fft(dato)
yf_datar = fft(datar)

xf = fftfreq(N, T)[:N//2]

plt.figure(figsize=(10, 6))

plt.plot(xf, 2.0/N * np.abs(yf_data[:N//2]), label='Señal 1 persona 1', color='blue')
plt.plot(xf, 2.0/N * np.abs(yf_datas[:N//2]), label='Señal 1 persona 2', color='green')
plt.plot(xf, 2.0/N * np.abs(yf_dato[:N//2]), label='Señal 1 persona 3', color='red')
plt.plot(xf, 2.0/N * np.abs(yf_datar[:N//2]), label='Ruido', color='orange')

plt.title("Análisis Espectral usando FFT de Todas las Señales")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.legend()
plt.show()