from guardarLeerJSON import leerJSON

def campers_inscritos():
    campers = leerJSON("campers.json")
    
    print("====== CAMPERS EN ESTADO INSCRITO ======\n")
    encontrados = False
    for camper in campers:
        if camper["estado"] == "inscrito":
            encontrados = True
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"ID: {camper['ID']}")
            print(f"Jornada: {camper['jornada']}")
            print("-" * 40)

    if not encontrados:
        print("No hay campers en estado inscrito.")
