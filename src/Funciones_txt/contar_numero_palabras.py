def contar_numero_palabras(txt):
    try:
        # Abrir el archivo en modo lectura
        with open(txt, 'r', encoding='utf-8') as archivo:
            
            contenido = archivo.read()  # Leer todo el contenido del archivo

            # Separar el contenido en palabras usando split(), que divide por espacios en blanco
            palabras = contenido.split()
            
            # Contar la cantidad de palabras
            numero_palabras = len(palabras)
            
            # Mostrar el resultado
            print(f"El archivo '{txt}' contiene {numero_palabras} palabras.")
    
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
