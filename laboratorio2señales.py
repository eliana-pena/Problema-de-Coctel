import numpy as np
import scipy.io.wavfile as wav
import pyroomacoustics as pra
import matplotlib.pyplot as plt
import os

# Cargar audios de los tres micrófonos
fs1, audio1 = wav.read('p2-2cel2-corte.wav')
fs2, audio2 = wav.read('Ep3-2cel3-0.wav')
fs3, audio3 = wav.read('p1-2cel1-01.wav')

# Verificar que las frecuencias de muestreo sean iguales
assert fs1 == fs2 == fs3, "Las frecuencias de muestreo de los audios no coinciden."
fs = fs1

# Recortar las señales al mismo tamaño
min_len = min(len(audio1), len(audio2), len(audio3))
audio1 = audio1[:min_len]
audio2 = audio2[:min_len]
audio3 = audio3[:min_len]

# Crear una matriz con las señales de los micrófonos
signals = np.stack([audio1, audio2, audio3], axis=0)

# Imprimir forma de la matriz de señales
print(f"Forma de signals: {signals.shape}")

# Configurar posiciones de micrófonos (en metros)
mic_positions = np.array([
    [0, 0],      # Micrófono 1 en el origen
    [2, 0],      # Micrófono 2 a 2 metros en el eje X
    [4, 0],      # Micrófono 3 a 4 metros en el eje X
]).T  # Transponer para que cada columna sea una posición

# Imprimir forma de mic_positions
print(f"Forma de mic_positions: {mic_positions.shape}")

# Crear el array de micrófonos
mic_array = pra.MicrophoneArray(mic_positions, fs)

# Dirección deseada (por ejemplo, hacia la persona al frente del micrófono 1)
desired_angle = 90  # 90 grados es en dirección positiva del eje Y

# Convertir ángulo a vector de dirección
direction = np.array([np.cos(np.deg2rad(desired_angle)), np.sin(np.deg2rad(desired_angle))])

# Crear y aplicar el beamformer
bf = pra.Beamformer(mic_array, fs, N=9600, Lg=0.1*fs)

# Aplica las ponderaciones de delay and sum para la dirección deseada
try:
    bf.rake_delay_and_sum_weights(direction)
    output_signal = bf.filter(signals)

    # Guardar el audio resultante
    output_file = 'output.wav'
    wav.write(output_file, fs, output_signal.astype(np.int16))

    # Confirmar que el archivo de audio se ha guardado
    print(f"Archivo de audio guardado en: {output_file}")
    print(f"Tamaño del archivo: {os.path.getsize(output_file)} bytes")

    # Visualizar la forma de onda resultante
    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, len(output_signal)/fs, len(output_signal)), output_signal)
    plt.title('Señal después de Beamforming')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.show()
except Exception as e:
    print(f"Ocurrió un error: {e}")