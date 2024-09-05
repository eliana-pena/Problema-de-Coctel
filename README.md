# Problema-de-Coctel
**Fecha:** 3 de septiembre de 2024  
**Autor:** Juan Andres Torres, Julián y Eliana Peña

## Descripción
En este laboratorio, titulado "Problema del cóctel", el objetivo principal es aplicar el análisis en frecuencia de señales de voz para abordar un problema clásico de captura de señales mezcladas. Específicamente, se pretende aislar la voz de interés entre varias fuentes sonoras capturadas por un arreglo de micrófonos, simulando un entorno de "fiesta de cóctel". Este problema es relevante tanto en sistemas de audición humana como artificial, y su resolución es crucial en aplicaciones como el reconocimiento de habla y la cancelación de ruido.

## Tabla de Contenidos
Lista de secciones del informe con enlaces a cada una (opcional pero útil).
1. [Introducción](#introducción)
2. [Metodología](#metodología)
3. [Desarrollo](#desarrollo)
4. [Resultados](#resultados)
5. [Discusión](#discusión)
6. [Conclusión](#conclusión)
7. [Referencias](#referencias)
8. [Anexos](#anexos)
   
## Introducción
El procesamiento de señales de audio es clave en muchas aplicaciones tecnológicas, como el reconocimiento de voz y la mejora de grabaciones. En este laboratorio, se trabajó con grabaciones de voces y sonidos ambientales capturadas con tres teléfonos móviles, con el objetivo de aplicar técnicas de Análisis de Componentes Independientes (ICA) para separar las fuentes de sonido y aislar al menos una voz.

Las grabaciones, realizadas a 44 kHz, presentaron desafíos técnicos como desfases entre señales debido a las diferencias en los micrófonos y tiempos de captura. Se espera mejorar la separación de señales y obtener una buena relación señal-ruido (SNR), evaluando la calidad de la separación obtenida.

## Metodología
El siguiente laboratorio presenta el análisis en frecuencias de las señales de voz, esto por medio del problema presentado por la fiesta de coctel, el problema plantea una situación social donde se colocaron varios micrófonos. Sin embargo, se solicita escuchar la voz de uno de los participantes, a pesar de existir diferentes emisores de sonido. En este caso, se colocaron 3 micrófonos que detectarán al mismo tiempo la voz de 3 personas diferentes (los emisores) hablando a la vez como es evidenciado en la imagen. 

Para el desarrollo de esta problemática, se grabó con 3 micrófonos diferentes por medio de la aplicación Recforge II para seleccionar la frecuencia de muestreo de los 3 micrófonos, teniendo estos una frecuencia de 44 kHz, una vez que los micrófonos capten las pistas de audio, por medio de Python se procederá a sacar un análisis de las señales. 

# Audio Processing Script

This repository contains a Python script for audio processing that utilizes various powerful libraries. Below is a brief overview of the libraries imported in the script:

## Libraries Used

- **NumPy**: `import numpy as np`  
  Provides support for large, multi-dimensional arrays and matrices, along with a large collection of mathematical functions to operate on these arrays.

- **SoundFile**: `import soundfile as sf`  
  Used to read and write sound files, such as WAV files.

- **scikit-learn (FastICA)**: `from sklearn.decomposition import FastICA`  
  Implements the FastICA algorithm for Independent Component Analysis, a technique used to separate mixed signals.

- **Matplotlib**: `import matplotlib.pyplot as plt`  
  A plotting library for creating static, animated, and interactive visualizations in Python.

- **SciPy (FFT)**: `import scipy.fftpack as fft`  
  Provides functions for computing the Fast Fourier Transform, which is useful for analyzing the frequency components of signals.

- **Librosa**: `import librosa` and `import librosa.display`  
  A Python package for music and audio analysis. It provides building blocks to create musical information retrieval systems.

- **SciPy (Stats)**: `from scipy.stats import pearsonr`  
  Used to calculate Pearson correlation coefficients.

- **SciPy (IO)**: `from scipy.io import wavfile`  
  Provides functions to read and write WAV files.

- **SciPy (Signal Processing)**: `from scipy.signal import butter, lfilter`  
  Provides functions for designing and applying digital filters.

## Usage

To use the script, ensure you have the required libraries installed. You can install them using `pip`:

```bash
pip install numpy soundfile scikit-learn matplotlib scipy librosa


## Desarrollo
Análisis temporal y frecuencial (15%): Aquí, explica cómo realizaste el análisis en el dominio del tiempo y la frecuencia. Detalla las escalas utilizadas (lineal, logarítmica) y describe cómo estas características se relacionan con el objetivo del experimento.
Separación de fuentes (10%): Detalla cómo implementaste la separación de fuentes utilizando técnicas como ICA. Explica los resultados obtenidos en términos de claridad de las señales separadas y cómo se puede verificar la efectividad de la separación.
Código fuente en Python: Explica el código que has utilizado para lograr estos análisis, haciendo énfasis en las partes que corresponden a la captura, el análisis temporal y frecuencial, y la separación de fuentes.

## Resultados
Análisis de resultados (15%): Presenta y discute los resultados del SNR y otros indicadores de calidad de las señales separadas. Relaciona estos resultados con la calidad de la captura de señal y la configuración del sistema descritos anteriormente.
Presentación de los resultados obtenidos: Muestra gráficos, espectrogramas y cualquier otra visualización relevante para interpretar los resultados obtenidos. Explica cómo se relacionan con las expectativas.

## Discusión
Análisis de los resultados: Reflexiona sobre los resultados obtenidos en relación con las expectativas iniciales. Compara con resultados previos o lo que esperabas obtener, y discute las posibles razones por las que los resultados no fueron los esperados.

## Conclusión
Resumen de los hallazgos más importantes: Aquí, resume los aspectos clave discutidos en el informe, incluyendo la efectividad de la configuración del sistema, la calidad de la captura de señal, y la separación de fuentes.

## Referencias
Citas de libros, artículos o recursos en línea utilizados.

## Anexos 
