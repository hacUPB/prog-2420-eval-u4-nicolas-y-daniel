import matplotlib.pyplot as plt

def estadisticas_columna(csv, delimitador, nombre_columna):
    try:
        # Abrir el archivo CSV en modo lectura
        with open(csv, 'r', encoding='utf-8') as archivo:

            # Leer la primera línea para obtener los encabezados
            encabezados = archivo.readline().strip().split(delimitador)
            
            # Buscar el índice de la columna deseada
            if nombre_columna not in encabezados:
                print(f"La columna '{nombre_columna}' no se encontró en el archivo.")
                return
            
            indice_columna = encabezados.index(nombre_columna)
            datos_columna = []

            # Leer el archivo línea por línea y obtener los valores de la columna
            for linea in archivo:
                valores = linea.strip().split(delimitador)
                try:
                    # Convertir el valor a un número (float) y agregarlo a la lista de datos
                    valor = float(valores[indice_columna])
                    datos_columna.append(valor)
                except ValueError:
                    # Ignorar filas que no tengan un valor numérico en la columna
                    continue

            # Calcular estadísticas si hay datos en la columna
            if datos_columna:
                total_datos = len(datos_columna)
                promedio = sum(datos_columna) / total_datos
                datos_columna.sort()  # Ordenar para calcular la mediana

                # Calcular la mediana
                if total_datos % 2 == 0:
                    mediana = (datos_columna[total_datos // 2 - 1] + datos_columna[total_datos // 2]) / 2
                else:
                    mediana = datos_columna[total_datos // 2]

                valor_max = max(datos_columna)
                valor_min = min(datos_columna)

                # Mostrar los resultados
                print(f"Estadísticas para la columna '{nombre_columna}':")
                print(f"  Número de datos: {total_datos}")
                print(f"  Promedio: {promedio}")
                print(f"  Mediana: {mediana}")
                print(f"  Valor máximo: {valor_max}")
                print(f"  Valor mínimo: {valor_min}")
            else:
                print(f"No se encontraron datos numéricos en la columna '{nombre_columna}'.")

    except FileNotFoundError:
        print("Error: el archivo no existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def graficar_columna(csv, delimitador, nombre_columna):
    try:

        # Abrir el archivo CSV en modo lectura
        with open(csv, 'r', encoding='utf-8') as archivo:

            # Leer la primera línea para obtener los encabezados
            encabezados = archivo.readline().strip().split(delimitador)
            
            # Buscar el índice de la columna deseada
            if nombre_columna not in encabezados:
                print(f"La columna '{nombre_columna}' no se encontró en el archivo.")
                return
            
            indice_columna = encabezados.index(nombre_columna)
            datos_columna = []

            # Leer el archivo línea por línea y obtener los valores de la columna
            for linea in archivo:
                valores = linea.strip().split(delimitador)
                try:
                    # Convertir el valor a un número (float) y agregarlo a la lista de datos
                    valor = float(valores[indice_columna])
                    datos_columna.append(valor)
                except ValueError:
                    # Ignorar filas que no tengan un valor numérico en la columna
                    continue

            # Verificar si hay datos en la columna para graficar
            if datos_columna:

                # Crear la gráfica
                plt.figure(figsize=(10, 5))
                plt.plot(datos_columna, marker='o', linestyle='-', color='b')
                plt.title(f"Gráfica de la columna '{nombre_columna}'")
                plt.xlabel("Índice")
                plt.ylabel(nombre_columna)
                plt.grid(True)
                plt.show()

            else:
                print(f"No se encontraron datos numéricos en la columna '{nombre_columna}'.")

    except FileNotFoundError:
        print("Error: el archivo no existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def primeras_filas(csv):
    try:
        # Abrir el archivo CSV en modo lectura
        with open(csv, 'r', encoding='utf-8') as archivo:

            # Contador de filas
            contador_filas = 0
            
            # Leer y mostrar las primeras 15 filas
            for linea in archivo:
                print(linea.strip())  # Imprimir la línea sin saltos de línea adicionales
                contador_filas += 1
                
                # Detenerse después de mostrar 15 filas
                if contador_filas == 15:
                    break

            # Indicar al usuario que el archivo tiene menos de 15 filas
            if contador_filas < 15:
                print(f"El archivo tiene menos de 15 filas. Estas han sido todas las filas encontradas en {csv}")
    
    except FileNotFoundError:
        print("Error: el archivo fue existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")