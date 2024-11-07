def estadisticas_columna(csv, nombre_columna):
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
        print("Error: el archivo no fue existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")