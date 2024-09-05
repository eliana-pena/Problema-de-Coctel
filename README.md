# Problema-de-Coctel
**Fecha:** 3 de septiembre de 2024  
**Autor:** Juan Andres Torres, Julián Rodríguez y Eliana Peña

# Descripción
En este laboratorio, titulado "Problema del cóctel", el objetivo principal es aplicar el análisis en frecuencia de señales de voz para abordar un problema clásico de captura de señales mezcladas. Específicamente, se pretende aislar la voz de interés entre varias fuentes sonoras capturadas por un arreglo de micrófonos, simulando un entorno de "fiesta de cóctel". Este problema es relevante tanto en sistemas de audición humana como artificial, y su resolución es crucial en aplicaciones como el reconocimiento de habla y la cancelación de ruido.

# Tabla de Contenidos
Lista de secciones del informe con enlaces a cada una (opcional pero útil).
1. [Introducción](#introducción)
2. [Metodología](#metodología)
3. [Desarrollo](#desarrollo)
4. [Resultados](#resultados)
5. [Discusión](#discusión)
6. [Conclusión](#conclusión)
7. [Referencias](#referencias)
8. [Anexos](#anexos)
   
# Introducción
El procesamiento de señales de audio es clave en muchas aplicaciones tecnológicas, como el reconocimiento de voz y la mejora de grabaciones. En este laboratorio, se trabajó con grabaciones de voces y sonidos ambientales capturadas con tres teléfonos móviles, con el objetivo de aplicar técnicas de Análisis de Componentes Independientes (ICA) para separar las fuentes de sonido y aislar al menos una voz.

Las grabaciones, realizadas a 44 kHz, presentaron desafíos técnicos como desfases entre señales debido a las diferencias en los micrófonos y tiempos de captura. Se espera mejorar la separación de señales y obtener una buena relación señal-ruido (SNR), evaluando la calidad de la separación obtenida.

# Metodología

El siguiente laboratorio presenta el análisis en frecuencias de las señales de voz, esto por medio del problema presentado por la fiesta de coctel, el problema plantea una situación social donde se colocaron varios micrófonos. Sin embargo, se solicita escuchar la voz de uno de los participantes, a pesar de que los receptores captaron varias fuentes de sonido. En este caso, se colocaron 3 micrófonos que detectarán al mismo tiempo la voz de 3 personas diferentes (los emisores), hablando a la vez como es evidenciado en la la figura 1. 

![coc2](https://github.com/user-attachments/assets/7445aaac-2087-4dfc-8297-4995274543e2)

Figura 1: Es un diagrama que demuestra la posicion de los emisores y receptores de sonido.

Para el desarrollo de esta problemática, se grabó con 3 micrófonos diferentes por medio de la aplicación Recforge II para seleccionar la frecuencia de muestreo de los 3 micrófonos, teniendo estos una frecuencia de 44 kHz. Con respecto a la posicion de los elementos seleccionados, cada uno se distancio por 1.16 m de los receptores de sonido, estando cada elemento separado por esa misma distancia, una vez que los micrófonos capten las pistas de audio por medio del lenguaje de programacion Python se procederá a sacar un análisis de las señales, por medio del procesamiento de la señal donde se implementaron varias librerías. 

En el presente laboratorio se usaron las siguientes librerias:

- **NumPy**: `import numpy as np`  
  Proporciona soporte para arreglos y matrices grandes y multidimensionales, junto con una gran colección de funciones matemáticas para operar sobre estos arreglos.

- **SoundFile**: `import soundfile as sf`  
  Se utiliza para leer y escribir archivos de sonido, como archivos WAV.

- **scikit-learn (FastICA)**: `from sklearn.decomposition import FastICA`  
  Implementa el algoritmo FastICA para el Análisis de Componentes Independientes, una técnica utilizada para separar señales mezcladas.

- **Matplotlib**: `import matplotlib.pyplot as plt`  
  Una biblioteca de gráficos para crear visualizaciones estáticas, animadas e interactivas en Python.

- **SciPy (FFT)**: `import scipy.fftpack as fft`  
  Proporciona funciones para calcular la Transformada Rápida de Fourier, útil para analizar los componentes de frecuencia de las señales.

- **Librosa**: `import librosa` y `import librosa.display`  
  Un paquete de Python para el análisis de música y audio. Proporciona bloques de construcción para crear sistemas de recuperación de información musical.

- **SciPy (Estadística)**: `from scipy.stats import pearsonr`  
  Se utiliza para calcular los coeficientes de correlación de Pearson.

- **SciPy (IO)**: `from scipy.io import wavfile`  
  Proporciona funciones para leer y escribir archivos WAV.

- **SciPy (Procesamiento de Señales)**: `from scipy.signal import butter, lfilter`  
  Proporciona funciones para diseñar y aplicar filtros digitales.

# Desarrollo
A continuacion se presenta el desarrollo de objetivo del laboratorio por medio de herramientas de python: 

### Carga de los audios
Primero, para cargar los archivos existentes, se creó una carpeta que contenía tanto el programa como los audios correspondientes y para cargarlos al codigo se utilizó la librería  `Soundfile`.  
Las variables dato se utilizan para almacenar los audios, y Fs nos indica la frecuencia de muestreo de estos.
```python
#Audios

dato1, Fs = sn.read('audiomass-output (2).wav')
dato2, Fs2 = sn.read('audiomass-output (3).wav')
dato3, Fs3 = sn.read('audiomass-output (1).wav')

#Ruidos

ruido1, Fs4 = sn.read('Ruido2.wav')
ruido2, Fs4 = sn.read('Ruido 1 celular 1-corte.wav')
ruido3, Fs4 = sn.read('r1celular1.wav')
```
### Calculo del SNR
Primero se verifico por medio de un condicional que todas las frecuencias de muestreo sean las mismas.
Para calcular la relación señal-ruido (SNR), se definió una función llamada `calcular_snr`, en la cual se evaluaron los audios junto con sus respectivos ruidos.
```python
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
```
### Análisis temporal y espectral
Para el análisis temporal, se definió la función `analisis_temporal_espectral`. En esta función, `senal` representa la señal de audio que se va a analizar, y `fs` es la frecuencia de muestreo de la señal expresada en Hz.
```python
def analisis_temporal_espectral(senal, fs):
    tiempo = np.arange(len(senal)) / fs
    plt.figure(figsize=(14, 5))
```
Graficamos el análisis temporal de la señal usando la libreria `Matplotlib`.

```python
    plt.subplot(1, 2, 1)
    plt.plot(tiempo, senal)
    plt.title(f'Análisis Temporal - {titulo}')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
```
Para el análisis espectral de frecuencias, se utilizó la Transformada Rápida de Fourier (FFT). Para calcularla se usaron las funciónes `fftfreq` y `fft` de la librería `scipy.fftpack`, asi como la funcion `abs` de `numpy`.

```python
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
```
### Separacion de fuentes-ICA
Puesto que una señal tenia mayor longitud con respecto a las otras, se opto por escalonarlas a la misma longitud usando `min_length`.

```python
min_length = min(len(dato1), len(dato2), len(dato3))
dato1 = dato1[:min_length]
dato2 = dato2[:min_length]
dato3 = dato3[:min_length]
```

 Se Combinaron las tres señales en una sola matriz.
```python
X = np.c_[dato1, dato2, dato3]
````
Mediante FastICA de `sklearn.decomposition`, se creó un objeto ICA para separar tres componentes independientes. La función `ica.fit_transform(X)` ajusta el modelo ICA a la matriz de señales X y transforma X en señales separadas, que se almacenan en la matriz `S_`. Esta matriz `S_` tiene el objetivo de convertir las señales separadas a un rango de amplitud adecuado para el formato de audio de 16 bits.
```python 
ica = FastICA(n_components=3, random_state=0)
S_ = ica.fit_transform(X)
S_ = (S_ / np.max(np.abs(S_))) * 32767
````
A traves de la libreria `scipy.io` se generaron los audios separados en al carpeta de origen.
```python
wavfile.write("separadita1.wav", Fs, S_[:, 0].astype(np.int16))
wavfile.write("separadita2.wav", Fs2, S_[:, 1].astype(np.int16))
wavfile.write("separadita3.wav", Fs2, S_[:, 2].astype(np.int16))
````
Se graficaron las señales mezcladas y separadas.
```python
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(X)
plt.title("Señales mezcladas")
plt.subplot(3, 1, 2)
plt.plot(S_)
plt.title("Señales separadas")
plt.show()
```
### Comprobación de separación de fuentes
Para llevar esto a cabo se utilizaron dos señales, una de referencia y una señal separada. En este caso se presentaron los espectros de frecuencia de ambas señales para observar si se presentan diferencias usando la libreria `Librosa`.
```python

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

```
Calculamos el coeficiente de correlación de Pearson para medir la similitud entre la señal de referencia y una de las señales separadas obtenidas por ICA a traves de la libreria `scipy.stats`. Para que esto se llevara a cabo fue necesario calcular las señales en las dimensiones adecuadas.
```python
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

```






# Resultados
Análisis de resultados (15%): Presenta y discute los resultados del SNR y otros indicadores de calidad de las señales separadas. Relaciona estos resultados con la calidad de la captura de señal y la configuración del sistema descritos anteriormente.
Presentación de los resultados obtenidos: Muestra gráficos, espectrogramas y cualquier otra visualización relevante para interpretar los resultados obtenidos. Explica cómo se relacionan con las expectativas.

# Discusión
En el siguiente apartado se evidenciará la discusión de los resultados, esto por medio de la interpretación de las gráficas evidenciadas en el índice anterior.

Con respecto a cada uno de los SNR, pudimos evidenciar que la adquisición de la señal de ellos fue la adecuada, esto debido al uso de una habitación insonorizada del exterior, lo que al ser valores positivos mayores a diez esta fue una toma idónea como se evidencia en cada uno de los casos, lo que repercute en poca interferencia para tomar las muestras. Aunque el aspecto de la calidad de pistas de audio, pudo variar por el desfase de las señales correspondientes al factor humano, debido a que las señales tuvieron que ser relativamente similares. Sin embargo, hay una de ellas, que cuenta con periodos de tiempo que afectaron el resultado final.
Otro valor a considerar que el filtrado logro eliminar la voz de la 3ra persona, por lo que el filtro realizado por ICA, se muestra como una herramienta que puede eliminar frecuencias bajas como en el caso de la persona 3.	

# Conclusión

Los dos factores que afectaron los resultados en la separación de las fuentes fueron el uso de diferentes micrófonos y el factor humano al momento de capturar las señales.Por lo cual, se concluye que el uso de micrófonos del mismo tipo y la implementación de un software especializado en el procesamiento de audios provenientes de diferentes fuentes son mejoras que podrían reducir el error en este tipo de prácticas de laboratorio.

En la presente practica del laboratorio se pudo evidenciar como la posición relativa de los micrófonos puede afectar a la toma de datos, esto es debido a que la intensidad captada por el receptor en este caso el micrófono, al estar más cerca de la fuente de sonido, captara con mayor intensidad las vibraciones generadas en el aire, logrando opacar las que no estén en la misma distancia o condición, esto se puede evidenciar cuando se opaca la voz 3 en el micrófono 1, al ser la voz más alejada, esa su vez la que menos presencia tiene en la pista de audio.


# Referencias
Citas de libros, artículos o recursos en línea utilizados.

# Anexos 
