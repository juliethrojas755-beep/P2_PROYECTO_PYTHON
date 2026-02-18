from guardarLeerJSON import leerJSON

def campersInscritos():
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

def campersAprobaronExamen():
    campers = leerJSON("campers.json")
    
    print("====== CAMPERS QUE APROBARON EL EXAMEN INICIAL ======")
    
    encontrados = False

    for camper in campers:
        pruebaInicial = camper.get("pruebaInicial", {})
        notaDefinitiva = pruebaInicial.get("definitiva")

        if notaDefinitiva is not None and notaDefinitiva >= 60:
            encontrados = True
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"ID: {camper['ID']}")
            print(f"Nota Definitiva: {notaDefinitiva}")
            print("-" * 40)

    if not encontrados:
        print("No hay campers que hayan aprobado el examen inicial.")
