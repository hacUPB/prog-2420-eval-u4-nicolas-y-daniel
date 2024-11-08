import matplotlib.pyplot as plt

def graficar_columna(csv, nombre_columna):
    try:

        # Abrir el archivo CSV en modo lectura
        with open(csv, 'r', encoding='utf-8') as archivo:

            # Leer la primera línea para obtener los encabezados
            encabezados = archivo.readline().strip().split(',')
            
            # Buscar el índice de la columna deseada
            if nombre_columna not in encabezados:
                print(f"La columna '{nombre_columna}' no se encontró en el archivo.")
                return
            
            indice_columna = encabezados.index(nombre_columna)
            datos_columna = []

            # Leer el archivo línea por línea y obtener los valores de la columna
            for linea in archivo:
                valores = linea.strip().split(',')
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
        print("Error: el archivo no fue existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
