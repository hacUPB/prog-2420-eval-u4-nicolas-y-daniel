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
    
    except FileNotFoundError:
        print("Error: el archivo no fue existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")