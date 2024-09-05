# Problema-de-Coctel
**Fecha:** 3 de septiembre de 2024  
**Autor:** Juan Andres Torres. Julián y Eliana 

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

##aasllsd
   
## Introducción
Configuración del sistema (10%): En la introducción, contextualiza la importancia de la configuración del sistema en el procesamiento de señales. Explica brevemente cómo la disposición de los micrófonos y la configuración de captura afectan la calidad del análisis de señales.
Objetivos específicos del laboratorio: Asegúrate de incluir objetivos que reflejen la importancia de una configuración rigurosa y la correcta captura de la señal.
##gmd
## Metodología
El siguiente laboratorio presenta el análisis en frecuencias de las señales de voz, esto por medio del problema presentado por la fiesta de coctel, el problema plantea una situación social donde se colocaron varios micrófonos. Sin embargo, se solicita escuchar la voz de uno de los participantes, a pesar de existir diferentes emisores de sonido. En este caso, se colocaron 3 micrófonos que detectarán al mismo tiempo la voz de 3 personas diferentes (los emisores) hablando a la vez como es evidenciado en la imagen. 

Para el desarrollo de esta problemática, se grabó con 3 micrófonos diferentes por medio de la aplicación Recforge II para seleccionar la frecuencia de muestreo de los 3 micrófonos, teniendo estos una frecuencia de 44 kHz, una vez que los micrófonos capten las pistas de audio, por medio de Python se procederá a sacar un análisis de las señales. 

## Desarrollo
Análisis temporal y frecuencial (15%): Aquí, explica cómo realizaste el análisis en el dominio del tiempo y la frecuencia. Detalla las escalas utilizadas (lineal, logarítmica) y describe cómo estas características se relacionan con el objetivo del experimento.
Separación de fuentes (10%): Detalla cómo implementaste la separación de fuentes utilizando técnicas como ICA. Explica los resultados obtenidos en términos de claridad de las señales separadas y cómo se puede verificar la efectividad de la separación.
Código fuente en Python: Explica el código que has utilizado para lograr estos análisis, haciendo énfasis en las partes que corresponden a la captura, el análisis temporal y frecuencial, y la separación de fuentes.

## Discusión
Análisis de los resultados. Comparación con expectativas o resultados previos con lo ereales, colocar por que no reulsto como queriamos.

## Conclusión
Resumen de los hallazgos más importantes. Reflexión sobre el cumplimiento de los objetivos.

## Referencias
Citas de libros, artículos o recursos en línea utilizados.
