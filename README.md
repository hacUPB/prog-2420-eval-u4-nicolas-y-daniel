[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gzRFP7VK)
# Unidad 4
---
## Documentación del proyecto
**Nombres:**
1. Nicolás Briceño Montoya; ID: 000231129
2. Daniel Alexander COlmenares Rolón; ID: 000542675
---

# Gestor de archivos .txt y .csv

Este proyecto tiene como objetivo principal desarrolar un programa que permita realizar distintas tareas con archivos de texto y separados por comas. Este programa llevara una secuencia de la siguiente forma:

**Menú Principal**

El menú principal debe brindar opciones para navegar entre distintas funcionalidades. Como requerimientos principales, aquí el programa debe:

1. Listar archivos en una ruta: Listar archivos de una ruta le permitirá al usuario conocer qué tiene disponible trabajar sin necesidad de salir del programa, de igual forma, ayuda a evitar errores en la escritura del nombre del archivo, pues estos quedan momentaneamente grabados en la consola.
2. Procesar archivos de texto y CSV: Cada tipo de archivo requiere un submenú específico con diferentes operaciones que le permitirán al usuario gestionar sus archivos de acuerdo a sus necesidades.
3. Salir: La opción de salida permitirá cerrar el programa de forma segura.


**Submenú para Archivos de Texto (.txt)**

Las opciones de procesamiento para archivos de texto incluyen funciones que interactúan con el contenido textual de varias maneras:

1. Contar número de palabras: Esta funcionalidad le dará al usuario la posibilidad de conocer la extensión de su texto, permitiendole obtener rápidamente una visión general de la densidad de texto.
2. Reemplazar palabras: Esta operación requiere leer el archivo, reemplazar una palabra específica dentro del texto por una que será proporcionada por el usario, y luego guardar los cambios.
3. Contar caracteres: El programa debe proporcionar al usuario dos opciones para contar caracteres; la primera, incluyendo espacios en blanco y la segunda, excluyendo estos caracteres.

**Submenú para Archivos CSV (.csv)**

Trabajar con CSV implica una estructura tabular. Para dar una mejor vista de sus archivos al usuario, sería util hacer uso de gráficas que cumplan las siguientes funciones:

1. Mostrar las 15 primeras filas: Esta opción le permitirá al usuario identificar solo las primera 15 lineas de su archivo; es apropiado tener en cuenta qué hacer con los archivos que cuentan con menos de 15 líneas.
2. Calcular estadísticas: Esta opción requiere identificar la columna y aplicar operaciones matemáticas que nos permitan conocer los datos solicitados.
3. Graficar columna de datos: Esto puede ayudar al usuario a realizar análisis visuales de manera eficiente, obervando tendencias en un ítem específico de su documento.

Estos son los requerimientos principales del programa, pero en busqueda de una mejor interacción con el usuario sería apropiado que el programa sea intuitivao y permita ingresar opciones sin mucha complejidad, mostrando instrucciones claras y concisas. De igual forma, es necesario validar la entrada del usuario y manejar excepciones como archivos inexistentes, rutas incorrectas o tipos de datos no válidos.

Así mismo, el programa presentará un archivo principal donde estará el código base y en diferentes documentos se proporcionarán las funciones que permitan la correcta operación de cada uno de los requerimientos. Lo anterior se hace en busqueda de facilitar la lectura y la posibilidad de mejoras en el futuro.