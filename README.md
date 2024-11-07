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

# Pseudocódigo.

El psudocódigo de este programa estará estrucutrado, donde se escribirá el código base y luego, por separado, cada una de las funciones del programa:

### Código base

```
Inicio

Definir opcion
Definir ruta
Definir archivos
Definir txt
Definir opcionst
Definir palabra_mod
Definir palabra_ree
Definir csv
Definir opcionsc

Imprimir "Menú principal\n 1. Listar archivos en la ruta actual o ingresar una ruta donde buscar archivos\n 2. Procesar archivo de texto (.txt)\n 3. Procesar archivo separado por comas (.csv)\n 4. Salir"
Leer opcion

Si opcion ≠ 4:
    
    Si opcion = 1:
        Imprimir "Por favor, ingresa la ruta deseada"
        Leer ruta
        archivos = listar archivos en ruta
        Imprimir archivos

    Si opcion = 2:
        Imprimir "Por favor, ingrese el nombre del archivo .txt a procesar"
        Leer txt
        Imprimir "Menú\n 1. Contar número de palabras\n 2. Reemplazar una palabra por otra\n 3. Contar el número de caracteres\n 4. Volver al menú principal"
        Leer opcionst
         Si opcionst = 1:
            Llamar a la función contar_numero_palabras

        Si opcionst = 2:
            Imprimir "Ingresa la palabra a ser modificada"
            Leer palabra_mod
            Imprimir "Ingresa la palabra de reemplazo"
            Leer palabra_ree
            Llamar a la función reemplazar_palabra
    
        Si opcionst = 3:
            Llamar a la función contar_caracteres

        Si opcionst = 4:
            Regresar al menú principal

    Si opcion = 3:
        Imprimir "Por favor, ingresa el nombre del archivo .csv a procesar"
        Leer csv
        Imprimir "Menú\n 1. Mostrar las primeras 15 filas\n 2. Calcular estadísticas de una columna\n 3. Graficar una columna\n 4. Volver al menú principal"
        Leer opcionsc

        Si opcionsc = 1:
            Llamar a la función primeras_filas

        Si opcionsc = 2:
            Imprimir "Ingresa el nombre de la columna para el análisis"
            Llamar a la función estadisticas_columna

        Si opcionsc = 3:
            Imprimir "Ingresa el nombre de la columna a graficar"
            Llamar a la función graficar_columna

        Si opcionsc = 4:
            Regresar al menú principal

    Si opcion = 4:
        Terminar el programa

Imprimir "Gracias por usar este programa, ¡regresa pronto!"

Fin