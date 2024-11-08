from os import system
import matplotlib.pyplot as plt
from Listar_archivos import listar_archivos
from Funciones_txt import contar_numero_palabras
from Funciones_txt import reemplazar_palabra
from Funciones_txt import contar_caracteres
from Funciones_csv import primeras_filas
from Funciones_csv import estadisticas_columna
from Funciones_csv import graficar_columna

def main():

    while True:

        print("Menú Principal\n1. Listar archivos presentes en la ruta actual o ingresar una ruta\n2. Procesar archivo de texto (.txt)\n3. Procesar archivo separado por comas (.csv)\n4. Salir")
        opcion = input("Escriba solo el número de alguna de las opciones del menú: ")
        system("cls")

        if opcion == "1":

            # Llamar a la función para listar archivos en la ruta actual o en una ruta especificada
            
            print("¡Excelente! Vamos a listar un archivo...")
            listar_archivos()
        
        elif opcion == "2":

            # Submenú para archivos de texto

            while True:

                print("Submenú para archivos de texto (.txt)\n1. Contar número de palabras\n2. Reemplazar una palabra por otra en una posición específica\n3. Contar el número de caracteres\n4. Regresar al Menú Principal")
                opcion_txt = input("Escriba solo el número de alguna de las opciones del submenú: ")
                system("cls")

                if opcion_txt == "1":

                    print("¡Muy bien! Vamos a contar la cantidad de palabras...")
                    txt = input("Ingrese la ruta del archivo de texto: ")
                    contar_numero_palabras(txt)

                elif opcion_txt == "2":

                    print("¡Muy bien! Vamos a reemplazar una palabra...")
                    txt = input("Ingrese la ruta del archivo de texto: ")
                    palabra_a_buscar = input("Ingrese la palabra que desea modificar: ")
                    nueva_palabra = input("Ingrese la palabra por la cual se reemplazará: ")
                    try:
                        numero_ocurrencia = int(input("Ingrese el número de ocurrencia de la palabra que desea modificar: "))
                        reemplazar_palabra(txt, palabra_a_buscar, nueva_palabra, numero_ocurrencia)
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue

                elif opcion_txt == "3":

                    print("¡Muy bien! Vamos a contar los caracteres...")
                    txt = input("Ingrese la ruta del archivo de texto: ")
                    contar_caracteres(txt)

                elif opcion_txt == "4":
                    break  # Salir del submenú y regresar al menú principal

                else:
                    print("Opción no válida, intente de nuevo.")
        
        elif opcion == "3":

            # Submenú para archivos CSV
            
            while True:
            
                print("Submenú para archivos CSV (.csv)\n1. Mostrar las primeras 15 filas\n2. Calcular estadísticas de una columna\n3. Graficar una columna\n4. Regresar al Menú Principal")
                opcion_csv = input("Seleccione una opción: ")
                system("cls")

                if opcion_csv == "1":

                    print("¡Muy bien! Vamos a analizar las 15 primeras lineas...")
                    csv = input("Ingrese la ruta del archivo CSV: ")
                    primeras_filas(csv)

                elif opcion_csv == "2":

                    print("¡Muy bien! Vamos a calcular las estadisticas de una columna...")
                    csv = input("Ingrese la ruta del archivo CSV: ")
                    nombre_columna = input("Ingrese el nombre de la columna: ")
                    estadisticas_columna(csv, nombre_columna)

                elif opcion_csv == "3":

                    print("¡Muy bien! Vamos a graficar una columna...")
                    csv = input("Ingrese la ruta del archivo CSV: ")
                    nombre_columna = input("Ingrese el nombre de la columna: ")
                    graficar_columna(csv, nombre_columna)

                elif opcion_csv == "4":
                    break  # Salir del submenú y regresar al menú principal

                else:
                    print("Opción no válida, intente de nuevo.")

        elif opcion == "4":
            print("Gracias por usar este programa, ¡regresa pronto!")
            break  # Salir del programa

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()