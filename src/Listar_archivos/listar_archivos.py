import os

def listar_archivos():
    # Pedir al usuario la ruta del directorio
    ruta = input("Ingrese la ruta del directorio (deje vacío para la ruta actual): ")
    
    # Si el usuario deja la ruta vacía, se usa la ruta actual
    if ruta.strip() == "":
        ruta = os.getcwd()  # Obtener la ruta actual
    
    # Verificar si la ruta existe y es un directorio
    if os.path.isdir(ruta):
        print(f"\nArchivos en el directorio '{ruta}':")
        
        # Listar los archivos y directorios en la ruta
        archivos = os.listdir(ruta)
        
        # Verificar si hay archivos en el directorio
        if archivos:
            for archivo in archivos:
                print(archivo)
        else:
            print("No se encontraron archivos en el directorio.")
    else:
        print("La ruta especificada no es válida.")