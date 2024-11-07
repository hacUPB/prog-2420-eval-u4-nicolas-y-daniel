def contar_caracteres(txt):
    try:
        # Abrir el archivo en modo lectura
        with open(txt, 'r', encoding='utf-8') as archivo:

            contenido = archivo.read()  # Leer todo el contenido del archivo

            # Contar todos los caracteres (incluidos espacios)
            total_con_espacios = len(contenido)
            
            # Inicializar contador en cero
            total_sin_espacios = 0

            # Contar caracteres sin espacios en blanco
            for caracter in range(len(contenido)):
                if caracter != " ":
                    total_sin_espacios += 1

            # Mostrar los resultados
            print(f"El archivo '{txt}' contiene {total_con_espacios} caracteres en total (incluyendo espacios).")
            print(f"El archivo '{txt}' contiene {total_sin_espacios} caracteres en total (sin contar espacios).")
    
    except FileNotFoundError:
        print("Error: el archivo no fue existe. Por favor, revisa la ruta proporcionada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
