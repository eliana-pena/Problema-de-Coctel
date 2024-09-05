import numpy as np
import soundfile as sf
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt
import scipy.fftpack as fft
import librosa.display
import soundfile as sn
import librosa
from scipy.stats import pearsonr
from scipy.io import wavfile
from scipy.signal import butter, lfilter




# Cargar los audios
dato1, Fs = sn.read('audiomass-output (2).wav')
dato2, Fs2 = sn.read('audiomass-output (3).wav')
dato3, Fs3 = sn.read('audiomass-output (1).wav')

# Cargar la voz de referencia 
voz_referencia, Fs5 = librosa.load('voz_refrencia.wav', sr=None)
S_referencia = librosa.stft(voz_referencia)
S_referencia_db = librosa.amplitude_to_db(np.abs(S_referencia), ref=np.max)

# Cargar los ruidos
ruido1, Fs4 = sn.read('Ruido2.wav')
ruido2, Fs4 = sn.read('Ruido 1 celular 1-corte.wav')
ruido3, Fs4 = sn.read('r1celular1.wav')

# Verificar que las frecuencias de muestreo sean iguales
if not (Fs == Fs2 == Fs3 == Fs4 == Fs5):
    raise ValueError("Las frecuencias de muestreo no son iguales. No se puede continuar.")

# Calcular SNR
def calcular_snr(senal, ruido):
    potencia_senal = np.mean(senal ** 2)
    potencia_ruido = np.mean(ruido ** 2)
    snr = 10 * np.log10(potencia_senal / potencia_ruido)
    return snr

# SNR para cada micrófono
snr1 = calcular_snr(dato1, ruido2)
print(f"La relación señal a ruido (SNR) del micrófono 1 es: {snr1:.2f} dB")

snr2 = calcular_snr(dato2, ruido2)
print(f"La relación señal a ruido (SNR) del micrófono 2 es: {snr2:.2f} dB")

snr3 = calcular_snr(dato3, ruido2)
print(f"La relación señal a ruido (SNR) del micrófono 3 es: {snr3:.2f} dB")

# Análisis temporal y espectral
def analisis_temporal_espectral(senal, fs, titulo):
    tiempo = np.arange(len(senal)) / fs
    plt.figure(figsize=(14, 5))

    # Análisis temporal
    plt.subplot(1, 2, 1)
    plt.plot(tiempo, senal)
    plt.title(f'Análisis Temporal - {titulo}')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')

    # Análisis espectral
    freqs = fft.fftfreq(len(senal), 1/fs)
    fft_senal = np.abs(fft.fft(senal))
    plt.subplot(1, 2, 2)
    plt.plot(freqs[:len(freqs)//2], fft_senal[:len(freqs)//2])
    plt.title(f'Análisis Espectral - {titulo}')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Amplitud')

    plt.tight_layout()
    plt.show()

analisis_temporal_espectral(dato1, Fs, "Micrófono 1")
analisis_temporal_espectral(dato2, Fs, "Micrófono 2")
analisis_temporal_espectral(dato3, Fs, "Micrófono 3")

# Asegurarse de que todas las señales tengan la misma longitud
min_length = min(len(dato1), len(dato2), len(dato3))
dato1 = dato1[:min_length]
dato2 = dato2[:min_length]
dato3 = dato3[:min_length]

# Crear la matriz de señales mezcladas
X = np.c_[dato1, dato2, dato3]

# Aplicar FastICA con ajustes para mejorar la convergencia
ica = FastICA(n_components=3, max_iter=3000, tol=0.000001)
S_ = ica.fit_transform(X)  # Señales separadas
A_ = ica.mixing_  # Matriz de mezcla estimada

# Guardar las señales separadas
for i, separated_signal in enumerate(S_.T):
    sf.write(f'separated_signal_{i+1}.wav', separated_signal, Fs)

# Visualizar las señales mezcladas y separadas
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

# Identificación de las voces - Análisis de cada señal separada
for i, signal in enumerate(S_.T):
    plt.figure(figsize=(10, 4))
    plt.plot(signal)
    plt.title(f'Señal Separada {i+1}')
    plt.show()

# Análisis temporal y espectral de las señales separadas
for i, signal in enumerate(S_.T):
    S_stft = librosa.stft(signal)
    S_db = librosa.amplitude_to_db(np.abs(S_stft), ref=np.max)

    plt.figure(figsize=(10, 6))
    librosa.display.specshow(S_db, sr=Fs, x_axis='time', y_axis='hz')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Espectrograma - Señal Separada {i+1}')
    plt.show()

# Determinar si la voz realmente fue separada
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_referencia_db, sr=Fs, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma - Señal de Referencia')
plt.show()

# Espectrograma de una de las señales separadas
S_separada = librosa.stft(S_.T[0])  # Ejemplo con la primera señal separada
S_separada_db = librosa.amplitude_to_db(np.abs(S_separada), ref=np.max)

plt.figure(figsize=(10, 6))
librosa.display.specshow(S_separada_db, sr=Fs, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma - Señal Separada 1')
plt.show()


# Obtén la longitud mínima entre las dos señales
min_length = min(len(S_referencia.flatten()), len(S_.T[2].flatten()))

# Recorta la señal de referencia a la longitud mínima
S_referencia_flat = S_referencia.flatten()[:min_length]
S_T0_flat = S_.T[2].flatten()

# Convierte las señales a sus partes reales
S_referencia_real = S_referencia_flat.real
S_T0_real = S_T0_flat.real

# Calcula la correlación
correlacion = pearsonr(S_referencia_real, S_T0_real)
print(f"Coeficiente de correlación: {correlacion[0]:.4f}")




# Evaluación de los resultados - Cálculo del SNR para señales separadas
potencia_ruido = np.mean(ruido2[:min_length] ** 2)  # Usando el mismo ruido para consistencia
snr_values = []
for i, signal in enumerate(S_.T):
    snr_separada = 10 * np.log10(np.mean(signal**2) / potencia_ruido)
    snr_values.append(snr_separada)

# Presentación de los resultados del SNR en una tabla
print("\nResultados del SNR para señales separadas:")
print("===========================================")
for i, snr in enumerate(snr_values):
    print(f"SNR de la señal separada {i+1}: {snr:.2f} dB")





# Asegurarse de que todas las señales tengan la misma longitud
min_length = min(len(dato1), len(dato2), len(dato3))
dato1 = dato1[:min_length]
dato2 = dato2[:min_length]
dato3 = dato3[:min_length]

X = np.c_[dato1, dato2, dato3]

# Aplicar ICA para separar las fuentes
ica = FastICA(n_components=2, random_state=0)
S_ = ica.fit_transform(X)  # Separar señales

# Escalar las señales separadas para convertirlas a formato de audio
S_ = (S_ / np.max(np.abs(S_))) * 32767  # Normalización al rango de 16 bits

# Guardar las señales separadas en archivos WAV
wavfile.write("separadita1.wav", Fs, S_[:, 0].astype(np.int16))
wavfile.write("separadita2.wav", Fs2, S_[:, 1].astype(np.int16))

# Graficar las señales originales, mezcladas y separadas
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(X)
plt.title("Señales mezcladas")

plt.subplot(3, 1, 2)
plt.plot(S_)
plt.title("Señales separadas")

plt.show()

# Analyze the audio: plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(S_[:, 1].astype(np.int16))
plt.title('Audio Waveform')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.show()

# Analyze the frequency spectrum
audio_fft = np.fft.fft(S_[:, 1].astype(np.int16))
frequencies = np.fft.fftfreq(len(S_[:, 1].astype(np.int16)), 1/Fs)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:len(frequencies)//2], np.abs(audio_fft)[:len(frequencies)//2])
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Find the dominant frequency to identify the voice closest to the microphone
magnitude_spectrum = np.abs(audio_fft)[:len(frequencies)//2]
dominant_frequency_index = np.argmax(magnitude_spectrum)
dominant_frequency = frequencies[dominant_frequency_index]

# Design a bandpass filter centered around the dominant frequency
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Define banda around the dominant frequency
lowcut =2000# 100 Hz below the dominant frequency
highcut =5000  # 100 Hz above the dominant frequency

# Apply the bandpass filter
filtered_audio = bandpass_filter(S_[:, 1].astype(np.int16), lowcut, highcut, Fs, order=6)

# Save the filtered audio to a new file
filtered_audio_path = 'filtered_audio.wav'
wavfile.write(filtered_audio_path, Fs, filtered_audio.astype(np.int16))



