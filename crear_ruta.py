
import json

archivo= "seccionAcademica.json"

def agregar_ruta():
    try:

        with open (archivo, "r", encoding= "utf-8") as f:
            datos= json.load (f)
    except FileNotFoundError:
        datos = {}

    if not isinstance(datos, dict):
        datos = {"rutas": []}

    datos.setdefault("rutas", [])
    if not isinstance(datos["rutas"], list):
        datos["rutas"] = []

        print ("---AGREGAR RUTA----")

        nueva_ruta= input ("Escribe el nombre de la ruta: ").strip()
        if nueva_ruta in datos ["rutas"]:
            print ("Esa ruta ya existe")
            return
        
        datos["rutas"].append(nueva_ruta)

        with open (archivo, "w", encoding= "utf-8") as f:
            json.dump(datos, f, indent=4)

        print ("Ruta agregada correctamente ")
if __name__ == "__main__":
    agregar_ruta()
       







