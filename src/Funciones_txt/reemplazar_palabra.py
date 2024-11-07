def reemplazar_palabra(txt, palabra_a_buscar, nueva_palabra, numero_ocurrencia):
    try:
        # Abrir el archivo en modo lectura y cargar el contenido
        with open(txt, 'r', encoding='utf-8') as archivo:

            contenido = archivo.read()

        # Separar el contenido en palabras
        palabras = contenido.split()

        # Contador de ocurrencias encontradas
        ocurrencias = 0

        # Recorrer las palabras y reemplazar solo la ocurrencia específica
        for i in range(len(palabras)):
            if palabras[i] == palabra_a_buscar:
                ocurrencias += 1
                # Si se alcanza la ocurrencia deseada, se reemplaza la palabra
                if ocurrencias == numero_ocurrencia:
                    palabras[i] = nueva_palabra
                    break  # Salir del bucle después de reemplazar

        # Verificar si se encontró la ocurrencia
        if ocurrencias < numero_ocurrencia:
            print(f"La palabra '{palabra_a_buscar}' no se encontró {numero_ocurrencia} veces en el archivo.")
            return

        # Unir las palabras para reconstruir el contenido del archivo
        nuevo_contenido = ' '.join(palabras)

        # Escribir el contenido modificado de nuevo en el archivo
        with open(txt, 'w', encoding='utf-8') as archivo:
            archivo.write(nuevo_contenido)

        print(f"Se ha reemplazado la ocurrencia número {numero_ocurrencia} de '{palabra_a_buscar}' por '{nueva_palabra}' en el archivo '{txt}'.")

    except FileNotFoundError:
        print("Error: el archivo no fue existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
