import numpy as np
import soundfile as sf
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

# Leer los archivos de audio
signal1, samplerate1 = sf.read('Ep3-2cel3-0.wav')
signal2, samplerate2 = sf.read('p2-2cel2-corte.wav')
#signal3, samplerate3 = sf.read('s3-1cel3.wav')

# Asegúrate de que todas las señales tengan la misma longitud
min_length = min(len(signal1), len(signal2)) #,len(signal3)#)
signal1 = signal1[:min_length]
signal2 = signal2[:min_length]
#signal3 = signal3[:min_length]

# Crear una matriz donde cada fila es una señal de los micrófonos
X = np.c_[signal1, signal2]#, signal3]

# Aplicar ICA
ica = FastICA(n_components=3)
S_ = ica.fit_transform(X)  # Señales separadas
A_ = ica.mixing_  # Matriz de mezcla estimada

# Guardar las señales separadas
for i, separated_signal in enumerate(S_.T):
    sf.write(f'separated_signal_{i+1}.wav', separated_signal, samplerate1)

# Opcional: visualizar las señales originales y separadas
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title("Señales mezcladas")
for i, signal in enumerate(X.T):
    plt.plot(signal, label=f'Signal {i+1}')
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Señales separadas")
for i, signal in enumerate(S_.T):
    plt.plot(signal, label=f'Separated Signal {i+1}')
plt.legend()

plt.tight_layout()
plt.show()