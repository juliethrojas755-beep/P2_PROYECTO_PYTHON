import json

def leerJSON(nombreArchivo):
    try:
        with open(nombreArchivo,"r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
        
def guardarJSON(nombreArchivo, datos):
        with open(nombreArchivo,"w") as archivo:
            json.dump(datos,archivo,indent=4)

