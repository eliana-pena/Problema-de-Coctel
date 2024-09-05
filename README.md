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
Análisis temporal y frecuencial (15%): Aquí, explica cómo realizaste el análisis en el dominio del tiempo y la frecuencia. Detalla las escalas utilizadas (lineal, logarítmica) y describe cómo estas características se relacionan con el objetivo del experimento.
Separación de fuentes (10%): Detalla cómo implementaste la separación de fuentes utilizando técnicas como ICA. Explica los resultados obtenidos en términos de claridad de las señales separadas y cómo se puede verificar la efectividad de la separación.
Código fuente en Python: Explica el código que has utilizado para lograr estos análisis, haciendo énfasis en las partes que corresponden a la captura, el análisis temporal y frecuencial, y la separación de fuentes.
 
### Carga de los audios
Primero, para cargar los archivos existentes, se creó una carpeta que contenía tanto el programa como los audios correspondientes. Luego, en el código se utilizó la librería  `Soundfile`.  
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









# Resultados
Análisis de resultados (15%): Presenta y discute los resultados del SNR y otros indicadores de calidad de las señales separadas. Relaciona estos resultados con la calidad de la captura de señal y la configuración del sistema descritos anteriormente.
Presentación de los resultados obtenidos: Muestra gráficos, espectrogramas y cualquier otra visualización relevante para interpretar los resultados obtenidos. Explica cómo se relacionan con las expectativas.

# Discusión
Análisis de los resultados: Reflexiona sobre los resultados obtenidos en relación con las expectativas iniciales. Compara con resultados previos o lo que esperabas obtener, y discute las posibles razones por las que los resultados no fueron los esperados.

# Conclusión
Resumen de los hallazgos más importantes: Aquí, resume los aspectos clave discutidos en el informe, incluyendo la efectividad de la configuración del sistema, la calidad de la captura de señal, y la separación de fuentes.

# Referencias
Citas de libros, artículos o recursos en línea utilizados.

# Anexos 
